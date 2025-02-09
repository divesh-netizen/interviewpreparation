## **Day 3: Containerization & Docker - Deep Dive**  

### **📌 Goal for Today**
By the end of today, you should have a solid understanding of **Docker**, how containers work, how to build efficient Docker images, and how to use **Docker Compose** for multi-container applications.

---

## **🚀 1. What is Containerization?**  
- **Containers** allow you to package applications along with their dependencies.  
- Unlike VMs, containers share the **host OS kernel**, making them **lightweight** and **fast**.  
- Containers ensure **consistency** across different environments (dev, test, prod).  

### **🆚 Containers vs Virtual Machines (VMs)**  
| Feature | Containers | Virtual Machines |
|---------|-----------|------------------|
| Startup Time | Seconds | Minutes |
| Size | MBs | GBs |
| OS Dependency | Shares host OS kernel | Requires full OS |
| Performance | Near-native speed | Slower due to OS overhead |
| Isolation | Process-level isolation | Full OS isolation |

---

## **🔹 2. Understanding Docker Architecture**  
Docker follows a **client-server** architecture:  
1. **Docker CLI**: The command-line interface to interact with Docker.  
2. **Docker Daemon**: Runs in the background, manages containers.  
3. **Docker Images**: Blueprints for containers.  
4. **Docker Containers**: Running instances of images.  
5. **Docker Registry (Docker Hub, AWS ECR, etc.)**: Stores images.  

---

## **🛠 3. Installing Docker & Basic Commands**  
### **🔹 Installation**
- [Install Docker](https://docs.docker.com/get-docker/) for your OS.

### **🔹 Basic Docker Commands**
```bash
# Check Docker version
docker --version

# Pull an image from Docker Hub
docker pull nginx

# Run a container
docker run -d --name mynginx -p 8080:80 nginx

# List running containers
docker ps

# List all containers (including stopped ones)
docker ps -a

# Stop a container
docker stop mynginx

# Remove a container
docker rm mynginx

# Remove an image
docker rmi nginx

# View logs of a container
docker logs mynginx
```

---

## **📜 4. Writing a Dockerfile (Best Practices)**  
A **Dockerfile** is a script containing instructions for building a Docker image.

### **🔹 Example Dockerfile (FastAPI App)**
```dockerfile
# Use official Python base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy application files
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# Expose application port
EXPOSE 8000

# Run FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### **🔹 Building and Running the Image**
```bash
# Build the image
docker build -t myfastapiapp .

# Run the container
docker run -d -p 8000:8000 myfastapiapp
```

---

## **🔹 5. Docker Compose (Multi-Container Apps)**  
Docker Compose lets you define multi-container applications using a `docker-compose.yml` file.

### **🔹 Example: FastAPI + PostgreSQL**
```yaml
version: "3.8"

services:
  db:
    image: postgres:13
    container_name: postgres_db
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
      POSTGRES_DB: mydb
    ports:
      - "5432:5432"

  app:
    build: .
    container_name: fastapi_app
    depends_on:
      - db
    ports:
      - "8000:8000"
```

### **🔹 Running Docker Compose**
```bash
# Start all services
docker-compose up -d

# Stop services
docker-compose down
```

---

## **🔐 6. Docker Security Best Practices**
✅ Use **official** base images to avoid vulnerabilities.  
✅ Keep images **minimal** (e.g., use `python:3.9-slim` instead of `python:3.9`).  
✅ Never run containers as **root**.  
✅ Use **Docker secrets** for sensitive credentials.  
✅ Scan images using **Docker Scout** or **Trivy**:
```bash
docker scan myfastapiapp
```

---

# **🚀 Deep Dive into Docker Compose**  

Docker Compose is a **powerful tool** that helps manage multi-container applications. It allows you to define and run multiple interconnected services (e.g., app, database, cache) using a **single YAML configuration file**.  

---

## **📌 1. Why Use Docker Compose?**  
✅ **Easier Multi-Container Management** – Define all services in one `docker-compose.yml` file.  
✅ **Simplified Networking** – Services can communicate using container names (DNS resolution).  
✅ **Environment Variable Management** – Store and use environment variables easily.  
✅ **Volume Persistence** – Data persists even after container restarts.  
✅ **Scaling** – Scale services up/down using a single command.  

---

## **📜 2. Anatomy of a `docker-compose.yml` File**  
A `docker-compose.yml` file consists of **multiple services** (containers), each with its configuration.  

### **🔹 Basic Structure of a Docker Compose File**  
```yaml
version: "3.8"  # Define the Docker Compose version

services:
  web:          # Service Name
    image: nginx
    ports:
      - "8080:80"  # Map host port 8080 to container port 80

  db:
    image: postgres:13
    environment:
      POSTGRES_USER: myuser
      POSTGRES_PASSWORD: mypassword
      POSTGRES_DB: mydatabase
    volumes:
      - db_data:/var/lib/postgresql/data  # Data persistence

volumes:
  db_data:  # Named volume for database persistence
```

---

## **🛠 3. Running Docker Compose**
### **🔹 Step 1: Start Services**
```bash
docker-compose up -d
```
✅ **`-d` (detached mode)** runs containers in the background.  

### **🔹 Step 2: Check Running Services**
```bash
docker-compose ps
```

### **🔹 Step 3: View Logs**
```bash
docker-compose logs -f
```

### **🔹 Step 4: Stop Services**
```bash
docker-compose down
```
✅ Removes containers **but keeps volumes** (data is retained).  
✅ To remove volumes as well:  
```bash
docker-compose down -v
```

---

## **🔗 4. Inter-Service Communication**
Docker Compose allows services to communicate using their **service name** (instead of IP addresses).

### **🔹 Example: FastAPI + PostgreSQL**
```yaml
version: "3.8"

services:
  db:
    image: postgres:13
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
      POSTGRES_DB: mydb
    volumes:
      - db_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"

  app:
    build: .
    depends_on:
      - db
    environment:
      DATABASE_URL: postgresql://user:password@db:5432/mydb
    ports:
      - "8000:8000"

volumes:
  db_data:
```
### **🔹 How Services Communicate**
- The **FastAPI app** can connect to PostgreSQL using `db:5432`.  
- `DATABASE_URL` uses `db` as the hostname instead of an IP.

---

## **📂 5. Managing Environment Variables**
Instead of hardcoding environment variables inside `docker-compose.yml`, store them in a **`.env` file`**.

### **🔹 `.env` File**
```
POSTGRES_USER=user
POSTGRES_PASSWORD=password
POSTGRES_DB=mydb
```

### **🔹 Use `.env` in `docker-compose.yml`**
```yaml
version: "3.8"

services:
  db:
    image: postgres:13
    environment:
      POSTGRES_USER: ${POSTGRES_USER}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
      POSTGRES_DB: ${POSTGRES_DB}
```

### **🔹 Run Docker Compose with `.env`**
```bash
docker-compose up --env-file .env -d
```

---

## **🗃 6. Volumes & Persistent Storage**
By default, data inside a container is **lost** when the container stops. **Volumes** solve this problem.

### **🔹 Named Volumes**
```yaml
volumes:
  db_data:
```
Stored under `/var/lib/docker/volumes/`.

### **🔹 Mounting Volumes in Services**
```yaml
services:
  db:
    volumes:
      - db_data:/var/lib/postgresql/data
```
✅ Data **persists** even after `docker-compose down`.

### **🔹 Bind Mounts (Local Directory to Container)**
```yaml
services:
  app:
    volumes:
      - ./app:/usr/src/app
```
✅ Syncs local `app` directory with `/usr/src/app` inside the container.

---

## **🚀 7. Scaling Services with Docker Compose**
You can scale services **horizontally** using the `--scale` flag.

### **🔹 Scale a Service**
```bash
docker-compose up --scale web=3 -d
```
✅ Launches **3 instances** of the `web` service.  
✅ Load balancers (e.g., Nginx) can distribute traffic.

---

## **🔐 8. Security Best Practices**
✅ Use **environment variables** instead of hardcoding secrets.  
✅ Restrict container permissions using **non-root users**.  
✅ Use `network_mode: "none"` to **disable networking** when not needed.  
✅ Regularly update images (`docker-compose pull`).  

---

## **🎯 Summary**
1. **Docker Compose Basics** – Multi-container management with YAML.  
2. **Running & Stopping Services** – `up`, `down`, `logs`, `ps`.  
3. **Inter-Service Communication** – Use service names instead of IPs.  
4. **Environment Variables** – Use `.env` for security & flexibility.  
5. **Data Persistence** – Use **volumes** for databases & shared storage.  
6. **Scaling Services** – `--scale` for horizontal scaling.  
7. **Security Best Practices** – Non-root users, env vars, restricted networking.  

---

## **🔜 What’s Next?**
Tomorrow, we dive into **Infrastructure as Code (IaC)** with **Terraform**, covering AWS & Azure provisioning.

Let me know if you have any questions before we move on! 🚀
