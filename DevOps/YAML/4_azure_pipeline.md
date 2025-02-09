
### **Azure DevOps YAML Keys in Detail**
Azure DevOps pipelines are highly flexible, and you can use several keys depending on your requirements. I'll go through each key and explain its usage in different scenarios.

#### 1. **`trigger`**
Defines when the pipeline is triggered. By default, pipelines run automatically when changes are pushed to the repository, but you can control this behavior.

- **Basic Trigger Example**:
    ```yaml
    trigger:
      branches:
        include:
          - main  # Only triggers for the 'main' branch
    ```

- **Advanced Trigger Example**: You can trigger on multiple branches or even exclude some.
    ```yaml
    trigger:
      branches:
        include:
          - main
          - dev
        exclude:
          - feature/*
    ```

- **Path Trigger Example**: Trigger only when specific files or directories are changed.
    ```yaml
    trigger:
      paths:
        include:
          - 'src/**'
        exclude:
          - 'docs/**'
    ```

#### 2. **`pr` (Pull Request Trigger)**
Defines when a pull request triggers the pipeline.

- **Basic PR Trigger Example**:
    ```yaml
    pr:
      branches:
        include:
          - main
    ```

- **Advanced PR Trigger Example**: Trigger a pipeline when PRs are created for specific branches.
    ```yaml
    pr:
      branches:
        include:
          - feature/*
        exclude:
          - dev
    ```

#### 3. **`pool`**
Defines which agent pool is used to run the pipeline. You can use Microsoft-hosted agents or specify self-hosted agents.

- **Use Microsoft-Hosted Agents** (most common):
    ```yaml
    pool:
      vmImage: 'ubuntu-latest'  # You can also use 'windows-latest' or 'macos-latest'
    ```

- **Use Self-Hosted Agent**: Define a custom agent pool.
    ```yaml
    pool:
      name: 'MySelfHostedAgentPool'
    ```

#### 4. **`variables`**
Variables can be defined globally or per job. You can use them in multiple places within the pipeline.

- **Basic Variable Example**:
    ```yaml
    variables:
      myVar: 'Hello World'
    ```

- **Using Variables in Steps**:
    ```yaml
    steps:
      - script: echo $(myVar)
    ```

- **Environment Variables in Pipeline**:
    ```yaml
    variables:
      SYSTEM_ACCESSTOKEN: $(System.AccessToken)
    ```

#### 5. **`jobs`**
Defines the set of jobs that the pipeline will run. Jobs can run sequentially or in parallel.

- **Single Job Example**:
    ```yaml
    jobs:
      - job: Build
        steps:
          - script: echo "Building project..."
    ```

- **Multiple Jobs Example**: Jobs can be run in parallel.
    ```yaml
    jobs:
      - job: Build
        steps:
          - script: echo "Building project..."

      - job: Test
        steps:
          - script: echo "Running tests..."
    ```

- **Job Dependencies**: Define that a job depends on the completion of another job.
    ```yaml
    jobs:
      - job: Build
        steps:
          - script: echo "Building project..."

      - job: Deploy
        dependsOn: Build
        steps:
          - script: echo "Deploying project..."
    ```

#### 6. **`steps`**
Defines a list of tasks or scripts that the pipeline will execute. This is where most of the pipeline's actions (build, test, deploy) occur.

- **Script Example**:
    ```yaml
    steps:
      - script: echo "Hello, World!"
    ```

- **Using Tasks**: Tasks are reusable pipeline steps. Azure DevOps has built-in tasks for common operations like `npm install`, `docker build`, `Azure App Service Deploy`, etc.
    ```yaml
    steps:
      - task: Docker@2
        inputs:
          containerRegistry: '$(dockerRegistryServiceConnection)'
          repository: 'my-image'
          command: 'buildAndPush'
          Dockerfile: '**/Dockerfile'
          tags: 'latest'
    ```

#### 7. **`checkout`**
Controls whether or not to check out source code. By default, this is automatically set, but you can disable it if needed.

- **Disable Checkout**: Useful if you don’t need to check out the source code (e.g., for testing with pre-built containers).
    ```yaml
    steps:
      - checkout: none
    ```

- **Checkout with Specific Submodules**: If you have submodules in your repository, you can specify their behavior.
    ```yaml
    steps:
      - checkout: self
        submodules: true
    ```

#### 8. **`container`**
Run your pipeline inside a Docker container. This is useful when you want the pipeline steps to run inside a pre-configured Docker image.

- **Basic Example**:
    ```yaml
    jobs:
      - job: Build
        container: 'node:14'
        steps:
          - script: npm install
    ```

#### 9. **`resources`**
Defines external resources such as repositories, pipelines, or containers that the pipeline uses.

- **Repository Resource**:
    ```yaml
    resources:
      repositories:
        - repository: MyRepo
          type: git
          name: 'my-project'
          ref: refs/heads/main
    ```

- **Pipeline Resource**: Use another pipeline’s artifacts.
    ```yaml
    resources:
      pipelines:
        - pipeline: another-pipeline
          source: 'AnotherPipeline'
          trigger:
            branches:
              include:
                - main
    ```

#### 10. **`condition`**
Allows you to set conditional execution for a step, job, or stage. For example, you can only run a job if a previous job succeeded.

- **Run a Step Based on Success of Previous Step**:
    ```yaml
    steps:
      - script: echo "Building project..."
        displayName: 'Build Project'

      - script: echo "Deploying project..."
        condition: succeeded()  # This will only run if the previous step succeeded
    ```

#### 11. **`timeoutInMinutes`**
Sets a maximum time for the pipeline, job, or step. After this time, the pipeline will be canceled.

- **Timeout Example**:
    ```yaml
    jobs:
      - job: Build
        timeoutInMinutes: 60
        steps:
          - script: echo "Building project..."
    ```

#### 12. **`cache`**
Caches dependencies to speed up pipeline runs. For example, you can cache Python dependencies or Node.js packages.

- **Cache Node.js Dependencies**:
    ```yaml
    steps:
      - task: Cache@2
        inputs:
          key: 'npm | "$(Agent.OS)" | package-lock.json'
          restoreKeys: |
            npm | "$(Agent.OS)"
          path: $(NPM_CACHE)
      - script: npm install
        displayName: 'Install dependencies'
    ```

#### 13. **`artifacts`**
Defines where to publish and download build artifacts.

- **Publish Artifact Example**:
    ```yaml
    steps:
      - task: PublishBuildArtifacts@1
        inputs:
          PathtoPublish: '$(Build.ArtifactStagingDirectory)'
          ArtifactName: 'drop'
          publishLocation: 'Container'
    ```

---

### **How to Use These Keys in Different Scenarios**
1. **CI/CD for FastAPI Project (Example)**: 
    - **Triggers**: Automatically triggers on changes to the `main` branch (or `dev` for feature development).
    - **Steps**: Use **tasks** like `Docker@2` to build and push images, then deploy to an Azure Web App with `AzureWebAppContainer@1`.
    - **Jobs**: Split jobs for building, testing, and deploying.

2. **Running Tests in Parallel**:
    - Create multiple jobs for different test environments or configurations, like running unit tests and integration tests in parallel.

3. **Using Containers for Consistent Environments**:
    - Use the **`container`** key to specify a Docker image for running tests or building code.

4. **Handle Failures**:
    - Use **`condition`** to handle when a job should run based on the success or failure of previous jobs.

---


### **🔹 Commonly Used Keys in `azure-pipelines.yml`**

Before we get to the full example, let me give you a brief overview of the common Azure DevOps YAML keys:

1. **`trigger`**: Defines which branches trigger the pipeline.
2. **`pool`**: Defines the agent pool to run the pipeline.
3. **`steps`**: A list of tasks to perform during the pipeline execution.
4. **`variables`**: Used to define variables used throughout the pipeline.
5. **`jobs`**: Defines individual jobs that run in parallel or sequentially.
6. **`checkout`**: Controls whether to check out source code for the pipeline.
7. **`task`**: Refers to tasks you want to execute, such as installing dependencies, running tests, or deploying to an environment.

---

### **Sample FastAPI Project Structure**
We'll use a **FastAPI** application for this example. Here's how the project structure might look:

```
fastapi-azure-project/
├── azure-pipelines.yml       # Azure DevOps Pipeline File
├── app/
│   ├── main.py               # FastAPI App Entry Point
│   ├── requirements.txt      # Python Dependencies
├── Dockerfile                # Dockerfile to containerize FastAPI app
├── .env                      # Environment Variables (optional)
└── README.md
```

### **1. FastAPI App (`app/main.py`)**
This is a simple **FastAPI** application that we will be deploying.

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI!"}
```

### **2. `requirements.txt`**
This file lists the dependencies that our FastAPI app needs to run.

```text
fastapi==0.95.0
uvicorn[gunicorn]==0.21.1
```

### **3. `Dockerfile`**
A Dockerfile to containerize the FastAPI application.

```Dockerfile
# Use the official Python image from Docker Hub
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the FastAPI app code into the container
COPY ./app /app

# Expose the port the app will run on
EXPOSE 8000

# Command to run the FastAPI app with Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

### **4. `azure-pipelines.yml`**
This is the **Azure DevOps pipeline YAML file**. It automates the process of building and deploying the FastAPI app using Docker.

```yaml
trigger:
  branches:
    include:
      - main  # The pipeline will trigger on changes to the 'main' branch

pool:
  vmImage: 'ubuntu-latest'  # Using Ubuntu-based agents

variables:
  imageName: 'fastapi-app'  # Define the image name

jobs:
- job: BuildAndDeploy
  displayName: 'Build and Deploy FastAPI App'
  steps:
  - task: UsePythonVersion@0
    inputs:
      versionSpec: '3.x'  # Use the latest Python version
      addToPath: true

  - task: Checkout@1
    displayName: 'Checkout Repository'

  - script: |
      python -m pip install --upgrade pip
      pip install -r app/requirements.txt  # Install dependencies
    displayName: 'Install Dependencies'

  - task: Docker@2
    inputs:
      containerRegistry: '<yourContainerRegistryServiceConnection>'  # Azure Container Registry service connection
      repository: 'fastapi-app'  # The name of the image in the registry
      command: 'buildAndPush'
      Dockerfile: '**/Dockerfile'  # Path to the Dockerfile
      tags: 'latest'  # Tag the Docker image as 'latest'
    displayName: 'Build and Push Docker Image'

  - task: AzureWebAppContainer@1
    inputs:
      azureSubscription: '<yourAzureSubscription>'  # Azure Subscription for deployment
      appName: '<yourAppName>'  # Azure Web App name
      imageName: 'fastapi-app:latest'  # The image we just pushed
    displayName: 'Deploy FastAPI to Azure Web App'
```

---

### **Explanation of `azure-pipelines.yml`**

1. **Trigger**:
    - The pipeline will automatically run on changes to the **`main`** branch.

2. **Pool**:
    - We’re using **`ubuntu-latest`** as the agent pool to run the pipeline on an Ubuntu-based VM.

3. **Variables**:
    - `imageName`: Defines the **Docker image** name for the FastAPI app.

4. **Steps**:
    - **UsePythonVersion@0**: Sets up Python and ensures the latest version is used.
    - **Checkout@1**: Checks out the source code from the repository.
    - **Install Dependencies**: Installs Python dependencies from the `requirements.txt` file.
    - **Docker@2**: Builds the Docker image and pushes it to the **Azure Container Registry**.
    - **AzureWebAppContainer@1**: Deploys the Docker image to an **Azure Web App**.

---

### **5. How to Set Up Azure DevOps Pipeline**

- **Create an Azure DevOps project** if you don’t have one already.
- **Connect your repository** (GitHub, Azure Repos, etc.).
- **Create a pipeline** and link the `azure-pipelines.yml` file.
- For the Docker task to work, you need to configure:
    - **Azure Container Registry** service connection.
    - **Azure Web App** and its corresponding service connection (to deploy the image).

---

### **6. Running the Project Locally with Docker**

If you want to test the Docker setup locally before deploying to Azure, you can do so with the following commands:

1. **Build the Docker image**:
   ```bash
   docker build -t fastapi-app .
   ```

2. **Run the Docker container**:
   ```bash
   docker run -d -p 8000:8000 fastapi-app
   ```

3. Visit [http://localhost:8000](http://localhost:8000) to see the FastAPI app in action.

---

### **7. Summary of Azure DevOps YAML Pipeline Steps**
| **Step**                        | **Description** |
|----------------------------------|-----------------|
| `trigger`                        | Defines which branches trigger the pipeline. |
| `pool`                           | Defines the VM image used for the pipeline. |
| `variables`                      | Declares variables like `imageName`. |
| `UsePythonVersion@0`             | Installs Python on the agent. |
| `Checkout@1`                     | Checks out the code from the repository. |
| `Install Dependencies`           | Installs the Python dependencies. |
| `Docker@2`                       | Builds and pushes the Docker image to Azure Container Registry. |
| `AzureWebAppContainer@1`         | Deploys the Docker image to Azure Web App. |

---

Now you're all set to run this **FastAPI app** with a fully automated CI/CD pipeline in Azure DevOps!