# **Scenario: Deploying a FastAPI App Using Docker Compose with Load Balancer on Multiple EC2 Instances**  

## **📌 Goal**  
Deploy a **FastAPI application** across multiple EC2 instances using **Docker Compose** and an **Application Load Balancer (ALB)**. The goal is to:  
✅ **Run multiple instances** of the FastAPI app.  
✅ **Distribute traffic** using a Load Balancer.  
✅ **Ensure scalability** by adding/removing EC2 instances dynamically.  

---

## **🚀 High-Level Architecture**  
1️⃣ **EC2 Auto Scaling Group** – Ensures instances scale up/down automatically.  
2️⃣ **Application Load Balancer (ALB)** – Distributes traffic to multiple EC2 instances.  
3️⃣ **Docker Compose** – Runs the FastAPI app + database on each instance.  
4️⃣ **Amazon RDS (PostgreSQL)** – A managed database instance (instead of running PostgreSQL on each EC2).  
5️⃣ **Terraform (Optional)** – Automates infrastructure provisioning.  

---

## **🛠 1. How Docker Compose Works in This Setup**  
Since **Docker Compose is designed for a single host**, it does **not handle multi-instance deployments** natively. However, we can:  
✅ **Use Docker Compose for service orchestration** within **each EC2 instance**.  
✅ **Deploy the same stack** (FastAPI + dependencies) on multiple EC2 instances.  
✅ **Use an ALB** to route traffic between EC2 instances.  

💡 **Key Considerations**  
- **Each EC2 instance runs an independent FastAPI app** (Dockerized).  
- **The Load Balancer distributes traffic** across instances.  
- **Database is external** (RDS PostgreSQL) to maintain data consistency.  

---

## **🔗 2. Step-by-Step Deployment Plan**  

### **📌 Step 1: Infrastructure Setup (AWS Components)**
1️⃣ **Create an Application Load Balancer (ALB)**  
- Target group to forward traffic to EC2 instances.  
- Health checks to ensure only healthy instances receive traffic.  

2️⃣ **Launch EC2 Instances in an Auto Scaling Group**  
- Define a **Launch Template** to spin up instances automatically.  
- User Data script ensures that Docker & Docker Compose are installed.  

3️⃣ **Use an RDS PostgreSQL Database**  
- RDS ensures **data consistency** across multiple instances.  

---

### **📌 Step 2: Docker Compose Setup on EC2**  

#### **🔹 `docker-compose.yml` (FastAPI App with External RDS Database)**
```yaml
version: "3.8"

services:
  app:
    image: my-fastapi-app:latest  # Pre-built Docker image
    container_name: fastapi_app
    environment:
      DATABASE_URL: postgresql://user:password@rds-instance-endpoint:5432/mydb
    ports:
      - "8000:8000"
    restart: always
```
✅ **RDS as External DB** – The FastAPI app connects to an external RDS instance instead of running PostgreSQL locally.  
✅ **Container Restarts Automatically** – Ensures uptime even if the container crashes.  

---

### **📌 Step 3: Automating Deployment on EC2**  

#### **🔹 User Data Script (Bootstrapping EC2)**
When new EC2 instances launch, we need them to:  
1. Install Docker & Docker Compose.  
2. Pull the latest FastAPI image from a container registry.  
3. Run `docker-compose up -d` automatically.  

**User Data Script (EC2 Launch Template)**  
```bash
#!/bin/bash
# Install Docker
apt update && apt install -y docker.io
systemctl start docker && systemctl enable docker

# Install Docker Compose
curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose

# Login to ECR (if using AWS ECR)
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin <AWS_ACCOUNT_ID>.dkr.ecr.us-east-1.amazonaws.com

# Pull latest image & start app
docker pull my-fastapi-app:latest
docker-compose up -d
```
✅ **Runs on every new EC2 instance** in the Auto Scaling Group.  
✅ **Pulls the latest Docker image** from ECR/Docker Hub.  
✅ **Runs the FastAPI app automatically.**  

---

### **📌 Step 4: Load Balancer Configuration**  

1️⃣ **Create an Application Load Balancer (ALB)**  
- **Target Group** → Attach EC2 instances (Port **8000**)  
- **Health Check** → Ensure FastAPI is healthy (`/docs` or `/health`)  
- **Listener Rule** → Forward HTTP requests to the target group  

2️⃣ **Test the Load Balancer**  
- Get the **ALB DNS Name** from AWS Console  
- Access the FastAPI app:  
  ```bash
  curl http://<ALB-DNS-NAME>:8000/docs
  ```
- The ALB will distribute traffic to **available EC2 instances** running the FastAPI app.  

---

### **📌 Step 5: Auto Scaling**
✅ If traffic increases, AWS **Auto Scaling Group** launches **new EC2 instances**, and the **ALB** routes traffic automatically.  
✅ If traffic decreases, AWS **terminates extra instances** to save costs.  
✅ New instances **bootstrap themselves using the User Data script** (Docker Compose is automatically executed).  

---

## **📜 Final Flow Diagram**
```
         ┌─────────── AWS Load Balancer ────────────┐
         │                                          │
 ┌───────▼─────────┐                    ┌─────────▼───────┐
 │ EC2 Instance 1  │                    │ EC2 Instance 2  │
 │ (Docker Compose)│                    │ (Docker Compose)│
 │ FastAPI App     │                    │ FastAPI App     │
 │ on Port 8000    │                    │ on Port 8000    │
 └─────────────────┘                    └─────────────────┘
         │                                          │
         └────────────────┬────────────────────────┘
                          │
               ┌──────────▼──────────┐
               │   AWS RDS (PostgreSQL) │
               │   Shared Database     │
               └──────────────────────┘
```

---

## **🔑 Key Takeaways**
✅ **Docker Compose runs independently on each EC2 instance** (not across multiple instances).  
✅ **Load Balancer distributes traffic to multiple EC2 instances** running the FastAPI app.  
✅ **Auto Scaling Group launches/terminates EC2 instances dynamically** based on demand.  
✅ **RDS provides a shared database** to avoid data inconsistency.  
✅ **User Data ensures new instances bootstrap automatically** with Docker Compose.  

---

# **How Do New EC2 Instances Bootstrap Themselves with User Data?**  

When an **Auto Scaling Group (ASG)** launches new EC2 instances, they need to:  
1️⃣ Install required software (**Docker, Docker Compose**).  
2️⃣ Download and start the **FastAPI application** using `docker-compose up -d`.  
3️⃣ Register themselves with the **Load Balancer (ALB)** so they can receive traffic.  

---

## **📌 What Triggers a New EC2 Instance Creation?**
- **Auto Scaling Group (ASG) Policy:** If CPU usage exceeds 70%, ASG **automatically launches** a new EC2 instance.  
- **Manual Scaling:** You can manually increase the number of instances.  
- **Instance Failure:** If an instance crashes, ASG replaces it.  

---

## **📌 Who Executes the User Data Script?**
- **Amazon EC2 automatically runs the user data script** when a new instance starts.  
- This script is stored in the **Launch Template** used by the ASG.  
- It ensures that every new EC2 instance is **configured the same way** (Docker installed, app running, etc.).  

---

## **📜 How Does It Work? (Step-by-Step Flow)**
### **Step 1: Auto Scaling Group Decides to Launch a New Instance**
- If load increases (e.g., **CPU > 70%**), AWS triggers the launch of a **new EC2 instance**.  
- The **Launch Template** specifies how instances should be configured.  

### **Step 2: EC2 Instance Starts & Executes the User Data Script**
- AWS **automatically runs the script ONCE** when the instance boots.  
- The script is stored inside the instance metadata (`/var/lib/cloud/instance/user-data.txt`).  
- **This script does the following:**  
  1. Installs **Docker** and **Docker Compose**.  
  2. Pulls the **latest FastAPI image** from Docker Hub or AWS ECR.  
  3. Runs `docker-compose up -d` to start the FastAPI app.  

### **Step 3: EC2 Instance Registers with Load Balancer**
- The **Application Load Balancer (ALB)** periodically checks the health of instances.  
- When an instance is **ready** (i.e., FastAPI responds to health checks), ALB starts routing traffic to it.  

---

## **🔗 Detailed Example: User Data Script**
```bash
#!/bin/bash
# Update system and install required packages
apt update && apt install -y docker.io

# Start Docker service
systemctl start docker && systemctl enable docker

# Install Docker Compose
curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose

# Login to ECR (If pulling from AWS Elastic Container Registry)
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin <AWS_ACCOUNT_ID>.dkr.ecr.us-east-1.amazonaws.com

# Pull the latest FastAPI image (from Docker Hub or ECR)
docker pull my-fastapi-app:latest

# Create a docker-compose.yml file (or download it)
cat <<EOF > docker-compose.yml
version: "3.8"
services:
  app:
    image: my-fastapi-app:latest
    environment:
      DATABASE_URL: postgresql://user:password@rds-instance-endpoint:5432/mydb
    ports:
      - "8000:8000"
    restart: always
EOF

# Start the application using Docker Compose
docker-compose up -d
```
✅ **This script ensures** that every new instance is **ready to serve requests automatically** when launched.  

---

## **🔄 How Does Scaling Work in Real Time?**
### **✅ Example Scenario**
- You start with **2 EC2 instances** behind the ALB.  
- A **traffic spike** occurs (many users hitting the API).  
- **CPU usage crosses 70%** → Auto Scaling triggers the launch of **one more instance**.  
- A **new EC2 instance boots up** and runs the **User Data script**:
  1. Installs Docker + Docker Compose.
  2. Pulls the FastAPI image and starts the container.
  3. ALB detects the instance as **healthy** and starts sending traffic to it.
- Now, **3 instances** are handling requests, reducing CPU load.  

### **❌ What If Load Decreases?**
- If traffic **drops**, ASG **terminates** excess instances.  
- Docker Compose stops running on those instances.  
- The **remaining instances continue handling traffic**.  

---

## **📜 High-Level Flow Diagram**
```
         ┌────────── AWS Load Balancer (ALB) ───────────┐
         │                                              │
 ┌───────▼───────────┐                       ┌────────▼────────┐
 │ EC2 Instance (1)  │                       │ EC2 Instance (2) │
 │ - User Data Runs  │  <------ Scaling Up-- │ - User Data Runs │
 │ - Docker Compose  │                       │ - Docker Compose │
 └───────────────────┘                       └──────────────────┘
         │                                              │
         └───────────────┬────────────────────────────┘
                         ▼
                  ┌─────────────┐
                  │ AWS Auto Scaling Group │
                  └─────────────┘
                         ▼
              ┌──────────────────────┐
              │ CloudWatch Metrics   │
              │ (Triggers Scaling)   │
              └──────────────────────┘
```

---

## **🔑 Key Takeaways**
✅ **EC2 automatically runs the User Data script on boot** (configures Docker, starts app).  
✅ **Docker Compose runs independently inside each EC2 instance** (not across multiple instances).  
✅ **Auto Scaling Group (ASG) dynamically adds/removes instances** based on load.  
✅ **Application Load Balancer (ALB) routes traffic only to healthy instances**.  
✅ **If an instance fails, ASG replaces it, and the new instance auto-configures itself using User Data.**  
