# **🔥 Terraform Cloud Integration for Remote State & Approvals**  

Terraform Cloud provides a **fully managed remote backend** for storing Terraform state, running Terraform workflows, and enabling team collaboration.  
With Terraform Cloud, we get:  
✅ **Remote State Management** (No need for S3/DynamoDB)  
✅ **Access Controls & Team Permissions**  
✅ **Automated Terraform Runs** (Plan & Apply)  
✅ **Policy Enforcement with Sentinel**  
✅ **Approval Workflow for Manual Approvals**  

---

## **📌 Step 1: Set Up Terraform Cloud Workspace**
1. Go to **[Terraform Cloud](https://app.terraform.io/)** and sign up.  
2. Create a new **Workspace** (`dev-infra` or `prod-infra`).  
3. Choose **"Version Control Workflow"** if connecting to GitHub or GitLab.  
4. Link the repository where your Terraform code exists.  

---

## **📌 Step 2: Configure Terraform to Use Terraform Cloud**
Modify `global/backend.tf` to use Terraform Cloud instead of S3:  

```hcl
terraform {
  cloud {
    organization = "my-org"

    workspaces {
      name = "dev-infra"
    }
  }
}
```

Now, run:
```bash
terraform init
```
Terraform will **auto-connect** to Terraform Cloud and manage the state remotely.  

---

## **📌 Step 3: Secure Variables in Terraform Cloud**
- Go to **Workspace → Variables**  
- Add sensitive variables like:  
  - `AWS_ACCESS_KEY_ID`
  - `AWS_SECRET_ACCESS_KEY`
  - `TF_VAR_database_password`  
- Set these variables as **Environment Variables** to avoid hardcoding them in Terraform code.  

---

## **📌 Step 4: Enable Manual Approvals**
Terraform Cloud has **two modes**:
1. **Auto Apply Mode** (Terraform applies changes automatically).  
2. **Manual Apply Mode** (Requires approval before applying).  

For approvals:
- Go to **Workspace Settings → General**
- Change **Apply Method** to **Manual Apply**  

This means Terraform Cloud will **run `terraform plan` automatically**, but an admin must **manually approve `terraform apply`** in the UI.

---

## **📌 Step 5: Configure GitHub Actions/Jenkins for Terraform Cloud**
Modify your pipeline to work with Terraform Cloud:

### **🔹 GitHub Actions (`.github/workflows/terraform.yml`)**
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

      - name: Setup Terraform
        uses: hashicorp/setup-terraform@v1
        with:
          cli_config_credentials_token: ${{ secrets.TF_CLOUD_TOKEN }}

      - name: Terraform Init
        run: terraform init

      - name: Terraform Plan
        run: terraform plan -var-file="environments/dev/terraform.tfvars"

      - name: Terraform Apply (Requires Manual Approval)
        if: github.ref == 'refs/heads/main'
        run: terraform apply -var-file="environments/dev/terraform.tfvars" -auto-approve
```
🔹 **TF_CLOUD_TOKEN** → Store Terraform Cloud API token as a **GitHub Secret**.

---

### **🔹 Jenkins Pipeline (`Jenkinsfile`)**
```groovy
pipeline {
    agent any

    environment {
        TF_CLOUD_TOKEN = credentials('terraform-cloud-token')
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/user/repo.git'
            }
        }

        stage('Terraform Init') {
            steps {
                sh 'terraform init'
            }
        }

        stage('Terraform Plan') {
            steps {
                sh 'terraform plan -var-file="environments/dev/terraform.tfvars"'
            }
        }

        stage('Terraform Apply') {
            steps {
                input message: "Apply Terraform changes?"
                sh 'terraform apply -var-file="environments/dev/terraform.tfvars" -auto-approve'
            }
        }
    }
}
```
🔹 Store **Terraform Cloud API Token** as a **Jenkins Credential** (`terraform-cloud-token`).  

---

## **📌 Step 6: Enable Notifications (Slack, Email, Webhooks)**
Terraform Cloud can send notifications on **plan completion, apply success/failure, and manual approval requests**.  
To enable notifications:
- Go to **Workspace → Settings → Notifications**
- Choose **Slack/Webhook/Email**  
- Add the notification **URL & triggers**  

Example:  
✅ Notify Slack when Terraform Apply is **waiting for approval**  
✅ Notify Email on **successful deployment**  

---

# **🚀 Key Benefits of Terraform Cloud**
✅ **No Need for S3/DynamoDB** – Terraform Cloud manages state.  
✅ **Secure Variable Management** – Store AWS keys safely.  
✅ **Approval Workflows** – Admins must approve before deployment.  
✅ **Access Control & Role-Based Permissions**.  
✅ **Audit Logs & Collaboration** – Track changes easily.  

---