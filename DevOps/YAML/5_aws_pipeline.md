Let's dive into **AWS CodePipeline** and understand its YAML configuration by exploring its common keys and usage in CI/CD pipelines. We'll cover:

1. **Common AWS CodePipeline Keys**
2. **Example Pipeline for a Simple Node.js Application**
3. **Example Pipeline for a Dockerized FastAPI Application**
4. **Explanation of Each Key and Its Use**

---

### **AWS CodePipeline YAML Configuration Keys**

AWS CodePipeline YAML configuration is quite similar to other CI/CD tools, but it also integrates tightly with AWS services like **CodeCommit**, **S3**, **ECR**, **Lambda**, and **CloudFormation**. Below are the most commonly used keys in AWS CodePipeline YAML files:

1. **`version`**: Specifies the version of the pipeline definition syntax.
2. **`resources`**: Defines the source repositories or artifacts that the pipeline interacts with.
3. **`stages`**: Defines a set of stages to be run, such as build, deploy, and test.
4. **`actions`**: Defines the actions within each stage, such as build or deploy tasks.
5. **`outputArtifacts`**: Defines the artifacts produced by the action to be used in the next stage.
6. **`inputArtifacts`**: Defines the input artifacts for a stage, referencing the output of previous stages.
7. **`artifactStore`**: Defines where the output artifacts are stored (typically an S3 bucket).
8. **`roleArn`**: Specifies an IAM role that grants permissions to AWS CodePipeline to execute actions.

---

### **1. AWS CodePipeline YAML for Node.js App**

In this example, we have a **Node.js application** that is stored in **AWS CodeCommit** and we’ll be using **AWS CodeBuild** to build it and **AWS Elastic Beanstalk** for deployment.

#### **Project Structure for Node.js App**:
```
nodejs-app/
├── codepipeline.yml             # AWS CodePipeline YAML file
├── app/
│   ├── index.js                 # Node.js App Entry Point
│   ├── package.json             # NPM dependencies
└── Dockerfile                   # Dockerfile (optional)
```

#### **`codepipeline.yml` Example for Node.js App**:
```yaml
version: '1'
resources:
  - name: NodeJsSource
    type: AWS::CodeCommit::Repository
    properties:
      RepositoryName: nodejs-app-repo
      BranchName: main

artifactStore:
  type: S3
  location: 'codepipeline-artifact-store'

stages:
  - name: Source
    actions:
      - name: SourceAction
        actionTypeId:
          category: Source
          owner: AWS
          provider: CodeCommit
          version: '1'
        outputArtifacts:
          - name: SourceOutput
        configuration:
          RepositoryName: nodejs-app-repo
          BranchName: main
        runOrder: 1

  - name: Build
    actions:
      - name: BuildAction
        actionTypeId:
          category: Build
          owner: AWS
          provider: CodeBuild
          version: '1'
        inputArtifacts:
          - name: SourceOutput
        outputArtifacts:
          - name: BuildOutput
        configuration:
          ProjectName: NodeJsBuildProject
        runOrder: 1

  - name: Deploy
    actions:
      - name: DeployAction
        actionTypeId:
          category: Deploy
          owner: AWS
          provider: ElasticBeanstalk
          version: '1'
        inputArtifacts:
          - name: BuildOutput
        configuration:
          ApplicationName: NodeJsApp
          EnvironmentName: NodeJsAppEnv
        runOrder: 1
```

### **Explanation of the Keys Used in the Node.js Pipeline**:

1. **`version`**: 
   - Specifies the pipeline configuration version. In this case, it's `1`.
   
2. **`resources`**:
   - The `resources` section specifies the source repository, which in this case is **CodeCommit**. The pipeline will monitor the **`main`** branch of the `nodejs-app-repo`.
   
3. **`artifactStore`**:
   - This key defines where the artifacts generated during the pipeline will be stored. We use **S3** as the artifact store.

4. **`stages`**:
   - Defines the stages that run sequentially. In our case, we have three stages: **Source**, **Build**, and **Deploy**.

5. **`actions`**:
   - Each stage contains one or more actions that will be executed in that stage. Actions are tasks like source code retrieval, building, or deploying.
   
   - **`Source Action`**: Retrieves the source code from **CodeCommit**.
     - `category: Source`: Specifies that this is a source action.
     - `outputArtifacts`: Defines the output artifact that will be passed to the next stage.
   
   - **`Build Action`**: Executes **AWS CodeBuild** to build the application. 
     - `inputArtifacts`: Refers to the output artifact from the previous stage (SourceOutput).
     - `outputArtifacts`: Defines the artifact that will be passed to the next stage (BuildOutput).

   - **`Deploy Action`**: Deploys the application using **Elastic Beanstalk**. 
     - `inputArtifacts`: Refers to the output artifact from the Build stage (BuildOutput).

6. **`runOrder`**:
   - Specifies the order in which the actions are executed. By default, it is `1`, but you can specify different values to control the execution order.

---

### **2. AWS CodePipeline YAML for Dockerized FastAPI App**

Next, let’s look at how you would define a pipeline for a **Dockerized FastAPI app** using **AWS CodePipeline**, **AWS CodeBuild**, and **Amazon Elastic Container Registry (ECR)** for Docker image storage, and **Amazon ECS** for deployment.

#### **Project Structure for FastAPI App**:
```
fastapi-docker-app/
├── codepipeline.yml               # AWS CodePipeline YAML file
├── app/
│   ├── main.py                    # FastAPI App Entry Point
│   ├── requirements.txt           # Python dependencies
├── Dockerfile                     # Dockerfile for containerizing FastAPI app
└── .env                           # Environment variables (optional)
```

#### **`codepipeline.yml` Example for Dockerized FastAPI App**:
```yaml
version: '1'
resources:
  - name: FastAPIAppSource
    type: AWS::CodeCommit::Repository
    properties:
      RepositoryName: fastapi-app-repo
      BranchName: main

artifactStore:
  type: S3
  location: 'codepipeline-artifact-store'

stages:
  - name: Source
    actions:
      - name: SourceAction
        actionTypeId:
          category: Source
          owner: AWS
          provider: CodeCommit
          version: '1'
        outputArtifacts:
          - name: SourceOutput
        configuration:
          RepositoryName: fastapi-app-repo
          BranchName: main
        runOrder: 1

  - name: Build
    actions:
      - name: DockerBuildAction
        actionTypeId:
          category: Build
          owner: AWS
          provider: CodeBuild
          version: '1'
        inputArtifacts:
          - name: SourceOutput
        outputArtifacts:
          - name: BuildOutput
        configuration:
          ProjectName: FastAPIAppDockerBuild
        runOrder: 1

  - name: PushToECR
    actions:
      - name: PushDockerImageAction
        actionTypeId:
          category: Deploy
          owner: AWS
          provider: ECR
          version: '1'
        inputArtifacts:
          - name: BuildOutput
        configuration:
          RepositoryName: fastapi-app-repository
          ImageTag: latest
        runOrder: 1

  - name: Deploy
    actions:
      - name: ECSDeployAction
        actionTypeId:
          category: Deploy
          owner: AWS
          provider: ECS
          version: '1'
        inputArtifacts:
          - name: BuildOutput
        configuration:
          ClusterName: fastapi-app-cluster
          ServiceName: fastapi-app-service
        runOrder: 1
```

### **Explanation of the Keys Used in the Dockerized FastAPI Pipeline**:

1. **`resources`**:
   - Specifies the source repository (**CodeCommit**) where the FastAPI application’s code is stored.

2. **`artifactStore`**:
   - Artifacts (like Docker images and build outputs) will be stored in **S3**.

3. **`stages`**:
   - **Source**: The first stage, where the code is pulled from **CodeCommit**.
   - **Build**: The second stage, where the code is built into a Docker image using **CodeBuild**.
   - **PushToECR**: Pushes the Docker image to **ECR**.
   - **Deploy**: Deploys the Docker image from **ECR** to an **ECS Cluster**.

4. **`actions`**:
   - **SourceAction**: Pulls code from the **CodeCommit** repository.
   - **DockerBuildAction**: Builds the Docker image using **CodeBuild**.
   - **PushDockerImageAction**: Pushes the image to **ECR**.
   - **ECSDeployAction**: Deploys the image to **Amazon ECS**.

5. **`runOrder`**:
   - Specifies the order of actions in each stage, ensuring actions run sequentially.

---

### **Summary of AWS CodePipeline Keys**:

| **Key**             | **Description**                                                |
|---------------------|----------------------------------------------------------------|
| `version`           | Defines the version of the pipeline.                          |
| `resources`         | Specifies the source repositories or external resources.      |
| `artifactStore`     | Where the pipeline stores artifacts (usually S3).             |
| `stages`            | A sequence of stages in the pipeline (e.g., Build, Deploy).   |
| `actions`           | Defines actions within each stage (e.g., build, test, deploy).|
| `outputArtifacts`   | Artifacts produced by actions, used in the next stage.        |
| `inputArtifacts`    | Artifacts passed into an action from previous stages.         |
| `artifactStore`     | Specifies where the output artifacts will be stored.          |
| `roleArn`           | IAM role that allows AWS CodePipeline to execute the actions.|

---
