🚀 Let’s dive into **Terraform Basics (AWS & Azure).**  

---

# **📌 What is Terraform?**
Terraform is an **Infrastructure as Code (IaC)** tool that allows you to **define, deploy, and manage cloud resources using code**. Instead of manually creating resources in the AWS or Azure console, you **write a configuration file** and let Terraform handle the deployment.  

✅ **Why Use Terraform?**  
- **Automates infrastructure deployment** (No more manual setup).  
- **Consistent and repeatable** (Same setup every time).  
- **Multi-cloud support** (Works for AWS, Azure, GCP, etc.).  
- **Version-controlled infrastructure** (Rollback if needed).  

---

## **🔹 How Terraform Works? (Key Concepts)**  

### **1️⃣ Terraform Configuration Files (.tf)**
- Terraform uses **`.tf` files** to define cloud resources.  
- You describe what you want (EC2, S3, VMs, etc.), and Terraform provisions them.  

### **2️⃣ Providers**
- Terraform needs a **provider** to interact with a cloud (AWS, Azure, GCP).  
- Example:  
  ```hcl
  provider "aws" {
    region = "us-east-1"
  }
  ```

### **3️⃣ Terraform State**
- Terraform keeps track of deployed resources using a **state file (`terraform.tfstate`)**.  
- **Remote State** (S3/Azure Storage) allows teams to collaborate safely.  

### **4️⃣ Modules**
- **Reusable Terraform code blocks** for organizing infrastructure.  
- Example: A module for a VPC that can be reused across environments.  

---

# **📌 Terraform Installation & Setup**  
## **✅ Install Terraform (Linux/Mac/Windows)**
Run the following command to install Terraform:  

**Linux/macOS:**  
```bash
curl -fsSL https://apt.releases.hashicorp.com/gpg | sudo apt-key add -
sudo apt-add-repository "deb [arch=amd64] https://apt.releases.hashicorp.com $(lsb_release -cs) main"
sudo apt update && sudo apt install terraform
terraform -v
```

**Windows:**  
- Download from [Terraform Official Site](https://developer.hashicorp.com/terraform/downloads).  
- Add Terraform to the system PATH.  

---

# **📌 Writing Basic Terraform Configurations**  

## **1️⃣ Deploy an EC2 Instance on AWS**
### **Step 1: Create a new Terraform Project**
```bash
mkdir terraform-aws && cd terraform-aws
touch main.tf
```

### **Step 2: Define AWS Provider (`main.tf`)**
```hcl
provider "aws" {
  region = "us-east-1"
}
```

### **Step 3: Define an EC2 Instance (`main.tf`)**
```hcl
resource "aws_instance" "my_ec2" {
  ami           = "ami-0c55b159cbfafe1f0"  # Amazon Linux 2 AMI (Update this for your region)
  instance_type = "t2.micro"

  tags = {
    Name = "TerraformInstance"
  }
}
```

### **Step 4: Initialize, Plan & Apply Terraform**
```bash
terraform init       # Initializes Terraform
terraform plan       # Shows what Terraform will create
terraform apply      # Deploys the EC2 instance
```

**✅ Terraform will create an EC2 instance.**  

---

## **2️⃣ Deploy a Virtual Machine on Azure**
### **Step 1: Define Azure Provider (`main.tf`)**
```hcl
provider "azurerm" {
  features {}
}
```

### **Step 2: Define a Virtual Machine (`main.tf`)**
```hcl
resource "azurerm_resource_group" "rg" {
  name     = "my-resource-group"
  location = "East US"
}

resource "azurerm_virtual_network" "vnet" {
  name                = "my-vnet"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  address_space       = ["10.0.0.0/16"]
}

resource "azurerm_network_interface" "nic" {
  name                = "my-nic"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name

  ip_configuration {
    name                          = "internal"
    subnet_id                     = azurerm_virtual_network.vnet.id
    private_ip_address_allocation = "Dynamic"
  }
}

resource "azurerm_linux_virtual_machine" "vm" {
  name                = "my-vm"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  size                = "Standard_B1ls"
  admin_username      = "azureuser"

  network_interface_ids = [azurerm_network_interface.nic.id]

  admin_ssh_key {
    username   = "azureuser"
    public_key = file("~/.ssh/id_rsa.pub")  # Path to your SSH key
  }

  os_disk {
    caching              = "ReadWrite"
    storage_account_type = "Standard_LRS"
  }

  source_image_reference {
    publisher = "Canonical"
    offer     = "UbuntuServer"
    sku       = "18.04-LTS"
    version   = "latest"
  }
}
```

### **Step 3: Initialize, Plan & Apply Terraform**
```bash
terraform init
terraform plan
terraform apply
```

**✅ Terraform will create an Azure VM.**  

---

## **📌 Terraform State & Remote Storage**
Terraform **stores state** in a local file (`terraform.tfstate`).  
For **team collaboration**, store it in **S3 (AWS) or Azure Storage**.

### **🔹 Storing Terraform State in AWS S3**
Modify your `main.tf`:
```hcl
terraform {
  backend "s3" {
    bucket = "my-terraform-state"
    key    = "state/terraform.tfstate"
    region = "us-east-1"
  }
}
```

### **🔹 Storing Terraform State in Azure Storage**
Modify your `main.tf`:
```hcl
terraform {
  backend "azurerm" {
    resource_group_name  = "my-resource-group"
    storage_account_name = "myterraformstate"
    container_name       = "tfstate"
    key                  = "terraform.tfstate"
  }
}
```

---

# **📌 Destroying Resources**
If you want to **delete everything Terraform created**:
```bash
terraform destroy
```

---

# **✅ Summary of Today’s Learnings**
✔ **Terraform automates cloud infrastructure provisioning.**  
✔ **Terraform configurations are written in `.tf` files.**  
✔ **Terraform uses state (`terraform.tfstate`) to track resources.**  
✔ **You deployed an EC2 instance (AWS) and VM (Azure) using Terraform.**  
✔ **Terraform state should be stored remotely for collaboration.**  

---


Here’s a **Terraform AWS Cheat Sheet** 📜🚀 with best practices, reusable patterns, and optimized configurations for **creating any AWS service efficiently.**  

---

# **🔥 Terraform AWS Cheat Sheet**
### **✅ Core Terraform Commands**
```bash
terraform init          # Initialize Terraform
terraform validate      # Validate .tf files
terraform plan          # Show execution plan
terraform apply         # Deploy infrastructure
terraform destroy       # Destroy infrastructure
terraform fmt           # Format .tf files
terraform output        # View output variables
terraform state list    # List managed resources
terraform taint <res>   # Mark resource for recreation
```

---

# **📌 Best Practices for Terraform AWS**
✅ **Use Remote State for Collaboration**
```hcl
terraform {
  backend "s3" {
    bucket         = "my-terraform-state"
    key            = "terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "terraform-lock"
  }
}
```
🔹 **DynamoDB Table for Locking** prevents conflicts.  

✅ **Use Variable Files (`variables.tf`)**  
```hcl
variable "region" {
  description = "AWS Region"
  default     = "us-east-1"
}
```
Call with:  
```bash
terraform apply -var-file="prod.tfvars"
```

✅ **Use Modules for Reusability**
```hcl
module "vpc" {
  source = "./modules/vpc"
  vpc_cidr = "10.0.0.0/16"
}
```

✅ **Tag Everything**
```hcl
tags = {
  Environment = "dev"
  ManagedBy   = "terraform"
}
```

✅ **Use IAM Roles instead of Hardcoding Credentials**
```hcl
provider "aws" {
  region = "us-east-1"
  assume_role {
    role_arn = "arn:aws:iam::123456789012:role/TerraformRole"
  }
}
```

---

# **🔹 VPC (Virtual Private Cloud)**
```hcl
resource "aws_vpc" "main" {
  cidr_block = "10.0.0.0/16"
  enable_dns_support = true
  enable_dns_hostnames = true
}
```

## **Public & Private Subnets**
```hcl
resource "aws_subnet" "public" {
  vpc_id                  = aws_vpc.main.id
  cidr_block              = "10.0.1.0/24"
  map_public_ip_on_launch = true
}

resource "aws_subnet" "private" {
  vpc_id     = aws_vpc.main.id
  cidr_block = "10.0.2.0/24"
}
```

## **Internet Gateway**
```hcl
resource "aws_internet_gateway" "gw" {
  vpc_id = aws_vpc.main.id
}
```

---

# **🔹 EC2 Instances**
```hcl
resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t3.micro"
  subnet_id     = aws_subnet.public.id

  user_data = file("bootstrap.sh")

  tags = {
    Name = "WebServer"
  }
}
```

## **Attach Security Group**
```hcl
resource "aws_security_group" "web_sg" {
  vpc_id = aws_vpc.main.id

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
```

---

# **🔹 Load Balancer (ALB)**
```hcl
resource "aws_lb" "alb" {
  name               = "my-load-balancer"
  internal           = false
  load_balancer_type = "application"
  security_groups    = [aws_security_group.web_sg.id]
  subnets           = [aws_subnet.public.id]
}
```

## **ALB Target Group**
```hcl
resource "aws_lb_target_group" "tg" {
  name     = "my-target-group"
  port     = 80
  protocol = "HTTP"
  vpc_id   = aws_vpc.main.id
}
```

---

# **🔹 S3 Bucket**
```hcl
resource "aws_s3_bucket" "my_bucket" {
  bucket = "my-unique-bucket-name"
  acl    = "private"
}
```

## **Enable Versioning**
```hcl
resource "aws_s3_bucket_versioning" "versioning" {
  bucket = aws_s3_bucket.my_bucket.id
  versioning_configuration {
    status = "Enabled"
  }
}
```

---

# **🔹 RDS Database**
```hcl
resource "aws_db_instance" "mysql" {
  allocated_storage = 20
  engine            = "mysql"
  instance_class    = "db.t3.micro"
  username         = "admin"
  password         = "mypassword"
  publicly_accessible = false
}
```

---

# **🔹 Lambda Function**
```hcl
resource "aws_lambda_function" "my_lambda" {
  function_name = "MyLambdaFunction"
  role          = aws_iam_role.lambda_exec.arn
  handler       = "index.handler"
  runtime       = "nodejs14.x"
  filename      = "lambda.zip"
}
```

## **Lambda IAM Role**
```hcl
resource "aws_iam_role" "lambda_exec" {
  name = "lambda_exec_role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action    = "sts:AssumeRole"
      Effect    = "Allow"
      Principal = { Service = "lambda.amazonaws.com" }
    }]
  })
}
```

---

# **🔹 CloudWatch Logs**
```hcl
resource "aws_cloudwatch_log_group" "log_group" {
  name = "/aws/lambda/my_lambda"
  retention_in_days = 30
}
```

---

# **🔹 CI/CD (GitHub Actions + Terraform)**
## **GitHub Actions for Terraform Deployment**
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

      - name: Terraform Init
        run: terraform init

      - name: Terraform Apply
        run: terraform apply -auto-approve
```

---

# **✅ Key Takeaways**
✔ **Use remote state with S3 + DynamoDB locking**  
✔ **Organize infrastructure using modules**  
✔ **Always use IAM roles instead of hardcoded credentials**  
✔ **Use `terraform fmt` and `terraform validate` for clean code**  
✔ **Use `terraform plan` before applying changes**  

---

Here’s a **modular Terraform structure** for managing AWS services effectively. This approach ensures **scalability, reusability, and maintainability** while following best practices.  

---

# **🌟 Modular Terraform Structure for AWS**
✅ **Organized directory structure**  
✅ **Reusability with modules**  
✅ **Separation of concerns**  
✅ **Easy environment management**  

---

## **📂 Folder Structure**
```plaintext
terraform-aws-infra/
│── modules/
│   ├── vpc/
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   ├── outputs.tf
│   ├── ec2/
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   ├── outputs.tf
│   ├── alb/
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   ├── outputs.tf
│   ├── rds/
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   ├── outputs.tf
│   ├── s3/
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   ├── outputs.tf
│
│── environments/
│   ├── dev/
│   │   ├── main.tf
│   │   ├── terraform.tfvars
│   ├── prod/
│   │   ├── main.tf
│   │   ├── terraform.tfvars
│
│── global/
│   ├── providers.tf
│   ├── backend.tf
│   ├── variables.tf
│   ├── outputs.tf
│
│── .gitignore
│── README.md
```

---

## **📌 Module: VPC**
```hcl
# modules/vpc/main.tf
resource "aws_vpc" "main" {
  cidr_block = var.vpc_cidr
  enable_dns_support = true
  enable_dns_hostnames = true

  tags = {
    Name = var.vpc_name
  }
}

output "vpc_id" {
  value = aws_vpc.main.id
}
```

**🔹 Variables:**
```hcl
# modules/vpc/variables.tf
variable "vpc_cidr" { default = "10.0.0.0/16" }
variable "vpc_name" { default = "main-vpc" }
```

---

## **📌 Module: EC2**
```hcl
# modules/ec2/main.tf
resource "aws_instance" "web" {
  ami           = var.ami_id
  instance_type = var.instance_type
  subnet_id     = var.subnet_id

  tags = {
    Name = "Web Server"
  }
}
```

**🔹 Variables:**
```hcl
# modules/ec2/variables.tf
variable "ami_id" {}
variable "instance_type" {}
variable "subnet_id" {}
```

---

## **📌 Module: Application Load Balancer**
```hcl
# modules/alb/main.tf
resource "aws_lb" "alb" {
  name               = var.alb_name
  internal           = false
  load_balancer_type = "application"
  security_groups    = var.security_groups
  subnets           = var.subnets
}

output "alb_arn" {
  value = aws_lb.alb.arn
}
```

**🔹 Variables:**
```hcl
# modules/alb/variables.tf
variable "alb_name" {}
variable "security_groups" {}
variable "subnets" {}
```

---

## **📌 Module: S3**
```hcl
# modules/s3/main.tf
resource "aws_s3_bucket" "bucket" {
  bucket = var.bucket_name
  acl    = "private"
}

output "bucket_name" {
  value = aws_s3_bucket.bucket.id
}
```

**🔹 Variables:**
```hcl
# modules/s3/variables.tf
variable "bucket_name" {}
```

---

# **📌 Environment: Dev**
```hcl
# environments/dev/main.tf
module "vpc" {
  source   = "../../modules/vpc"
  vpc_cidr = "10.0.0.0/16"
  vpc_name = "dev-vpc"
}

module "ec2" {
  source        = "../../modules/ec2"
  ami_id        = "ami-12345678"
  instance_type = "t3.micro"
  subnet_id     = module.vpc.vpc_id
}

module "alb" {
  source = "../../modules/alb"
  alb_name = "dev-alb"
  security_groups = ["sg-12345678"]
  subnets = ["subnet-12345678", "subnet-87654321"]
}
```

**🔹 Dev Variables:**
```hcl
# environments/dev/terraform.tfvars
bucket_name = "my-dev-bucket"
```

---

# **📌 Remote State Backend**
```hcl
# global/backend.tf
terraform {
  backend "s3" {
    bucket         = "my-terraform-state"
    key            = "terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "terraform-lock"
  }
}
```

---

## **✅ Deployment Steps**
1️⃣ **Initialize Terraform**
```bash
terraform init
```
2️⃣ **Validate Configuration**
```bash
terraform validate
```
3️⃣ **Plan Changes**
```bash
terraform plan -var-file="environments/dev/terraform.tfvars"
```
4️⃣ **Apply Changes**
```bash
terraform apply -var-file="environments/dev/terraform.tfvars" -auto-approve
```

---

# **🔥 Key Benefits of This Structure**
✅ **Reusability** → Each module is self-contained and can be reused across environments.  
✅ **Scalability** → Easy to add new services by adding new modules.  
✅ **Separation of Concerns** → Different teams can work on different modules independently.  
✅ **Consistency** → Standardized naming and structure.  
✅ **Version Control** → Each environment has its own state and variables.  

---
Let's integrate **Terraform deployment into a CI/CD pipeline** using **GitHub Actions** and **Jenkins**.  

---

# **🔥 CI/CD Pipeline for Terraform Deployment**
We will set up **two CI/CD pipelines**:
1. **GitHub Actions** (for teams using GitHub)
2. **Jenkins** (for teams using self-hosted Jenkins)

Each pipeline will:  
✅ **Lint & validate Terraform code**  
✅ **Run `terraform plan` to preview changes**  
✅ **Run `terraform apply` for deployment**  
✅ **Use AWS credentials securely**  
✅ **Work with multiple environments (dev/prod)**  

---

# **🚀 Option 1: GitHub Actions Pipeline**
📌 **Steps**:
1. **Triggers**: Runs on every push to `main` branch.
2. **Terraform Validation**: Checks for syntax errors.
3. **Plan & Apply**: Deploys to AWS.
4. **Store State Remotely**: Uses S3 backend.

---

## **📌 GitHub Actions Workflow (`.github/workflows/terraform.yml`)**
```yaml
name: Terraform Deploy

on:
  push:
    branches:
      - main
  pull_request:

jobs:
  terraform:
    runs-on: ubuntu-latest

    permissions:
      id-token: write
      contents: read

    steps:
      - name: Checkout Code
        uses: actions/checkout@v3

      - name: Setup Terraform
        uses: hashicorp/setup-terraform@v1

      - name: Terraform Init
        run: terraform init

      - name: Terraform Validate
        run: terraform validate

      - name: Terraform Plan
        run: terraform plan -var-file="environments/dev/terraform.tfvars"

      - name: Terraform Apply
        if: github.ref == 'refs/heads/main'
        run: terraform apply -var-file="environments/dev/terraform.tfvars" -auto-approve
```

**🔹 Secure AWS Authentication** (Use GitHub OIDC for better security):
- **IAM Role with OIDC** (instead of AWS keys).
- If needed, you can use `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` from GitHub secrets.

---

# **🚀 Option 2: Jenkins Pipeline**
📌 **Steps**:
1. **Triggered manually or on code changes**  
2. **Terraform validation & plan**  
3. **Approval before `terraform apply`**  
4. **AWS credentials managed via Jenkins secrets**  

## **📌 Jenkins Pipeline (`Jenkinsfile`)**
```groovy
pipeline {
    agent any

    environment {
        AWS_ACCESS_KEY_ID = credentials('aws-access-key')
        AWS_SECRET_ACCESS_KEY = credentials('aws-secret-key')
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

        stage('Terraform Validate') {
            steps {
                sh 'terraform validate'
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

### **🔹 Configuring Jenkins**
1. **Install Plugins**: Terraform, Pipeline, AWS Credentials.
2. **Create AWS Credentials in Jenkins**:
   - `aws-access-key`
   - `aws-secret-key`
3. **Create a Jenkins Job**:
   - Select **Pipeline**
   - Choose **Pipeline Script from SCM** (point to GitHub repo)

---

# **🚀 Key Takeaways**
✅ **GitHub Actions** → Best for GitHub-based teams (OIDC authentication for security).  
✅ **Jenkins** → Best for on-prem/self-hosted teams with manual approvals.  
✅ **Both support Terraform state locking (S3 + DynamoDB)**.  
✅ **Secure AWS authentication (GitHub OIDC or Jenkins secrets)**.  

---
