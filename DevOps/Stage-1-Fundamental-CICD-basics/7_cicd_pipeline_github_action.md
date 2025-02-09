Great! Let's dive into **Day 7: CI/CD Pipeline Integration**—this is the final step for building a complete CI/CD pipeline that automates deployments to **AWS ECS** and **Azure App Services**. Here’s the detailed breakdown for today:

---

### **Day 7: CI/CD Pipeline with GitHub Actions**  

#### **1. Creating a GitHub Actions Workflow**  
Start by setting up the **GitHub Actions** workflow for automating the Terraform plan and apply commands.

- **Create a workflow file** in your repository: `.github/workflows/terraform.yml`.
- **Trigger the pipeline** on `push` to the `main` branch or when a pull request is made.

```yaml
name: Terraform Deploy

on:
  push:
    branches:
      - main

jobs:
  terraform:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout Code
        uses: actions/checkout@v3

      - name: Set up Terraform
        uses: hashicorp/setup-terraform@v1
        with:
          terraform_version: '1.3.7'

      - name: Terraform Init
        run: terraform init

      - name: Terraform Plan
        run: terraform plan -var-file="environments/dev/terraform.tfvars"

      - name: Terraform Apply (Manual Approval)
        if: github.ref == 'refs/heads/main'
        run: terraform apply -var-file="environments/dev/terraform.tfvars" -auto-approve
        env:
          TF_CLOUD_TOKEN: ${{ secrets.TF_CLOUD_TOKEN }}
```

---

#### **2. Integrating Terraform into CI/CD**

- **API Token**: Store the `TF_CLOUD_TOKEN` in **GitHub Secrets** for secure access.
- **Terraform Init**: Initializes Terraform, downloading the necessary providers (AWS, Azure, etc.).
- **Terraform Plan**: Generates an execution plan for the infrastructure changes.
- **Terraform Apply**: Applies the changes to your infrastructure. This step can be manual (via GitHub Actions interface) if you prefer a review step.

---

#### **3. Building & Deploying Docker Images**

For **AWS ECS** and **Azure App Services**, you need to build and push Docker images. Let’s integrate Docker into the pipeline.

- **Docker Build and Push** for AWS ECS (to ECR):
  - Use `docker build` to build your app image.
  - Use `docker push` to upload it to **AWS ECR**.

Example GitHub Actions for Docker:
```yaml
      - name: Log in to AWS ECR
        uses: aws-actions/amazon-ecr-login@v1

      - name: Build Docker Image
        run: |
          docker build -t ${{ secrets.AWS_ECR_REPO_URI }}:$GITHUB_SHA .
          docker tag ${{ secrets.AWS_ECR_REPO_URI }}:$GITHUB_SHA ${{ secrets.AWS_ECR_REPO_URI }}:latest

      - name: Push Docker Image to ECR
        run: |
          docker push ${{ secrets.AWS_ECR_REPO_URI }}:$GITHUB_SHA
          docker push ${{ secrets.AWS_ECR_REPO_URI }}:latest
```

- **Docker Build for Azure App Services**: 
  You’ll use **Azure Container Registry** (ACR) for this. You’ll build your Docker image and push it to **ACR**.

Example for Azure Container Registry:
```yaml
      - name: Log in to Azure Container Registry
        uses: azure/docker-login@v1
        with:
          login-server: ${{ secrets.ACR_LOGIN_SERVER }}
          username: ${{ secrets.ACR_USERNAME }}
          password: ${{ secrets.ACR_PASSWORD }}

      - name: Build Docker Image
        run: docker build -t ${{ secrets.ACR_NAME }}.azurecr.io/myapp:$GITHUB_SHA .

      - name: Push Docker Image to ACR
        run: docker push ${{ secrets.ACR_NAME }}.azurecr.io/myapp:$GITHUB_SHA
```

---

#### **4. Automating Deployment to AWS ECS & Azure App Services**

- **For AWS ECS**, you need to update the ECS **Task Definition** with the new Docker image, and trigger a deployment on ECS.

Here’s an example of a simple ECS deployment step:
```yaml
      - name: Update ECS Task Definition
        run: |
          ecs-cli configure --region ${{ secrets.AWS_REGION }} --access-key ${{ secrets.AWS_ACCESS_KEY_ID }} --secret-key ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          ecs-cli compose --file docker-compose.yml --project-name myapp service up

      - name: Deploy to ECS
        run: |
          ecs-cli compose --file docker-compose.yml --project-name myapp service start
```

- **For Azure App Services**, you’ll need to deploy your Docker container to **Azure App Services**.

Example Azure deployment step:
```yaml
      - name: Deploy to Azure App Service
        uses: azure/webapps-deploy@v2
        with:
          app-name: ${{ secrets.AZURE_APP_NAME }}
          images: ${{ secrets.ACR_NAME }}.azurecr.io/myapp:$GITHUB_SHA
```

---

#### **5. Final Review & Debugging Issues**

- Once the **CI/CD pipeline** runs, you should:
  - **Monitor logs** in GitHub Actions.
  - Verify if the **ECR/ACR** contains the updated Docker image.
  - Confirm the deployments to **AWS ECS** and **Azure App Services** are successful.
  - Test the FastAPI/Node.js application to ensure everything is functioning.

---

### **Wrap-up for Day 7**

By the end of **Day 7**, you should have:
- A working **CI/CD pipeline** that deploys your application to both **AWS ECS** and **Azure App Services**.
- Automated Docker builds and deployments.
- Successful **Terraform integration** into the pipeline for provisioning resources.

Let me know if you'd like to adjust the pipeline or go into deeper details for any specific part! 🚀