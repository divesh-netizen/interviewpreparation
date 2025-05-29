### Summary
---

#### **🌍 EC2 Overview**  
- Virtual servers in the cloud.  
- Pay-as-you-go pricing.  
- Flexible configurations (CPU, RAM, Storage, OS).  

---

#### **🖥️ EC2 Instance Types**  
| Category | Series | Use Case |
|----------|--------|----------|
| General Purpose | T, M | Web servers, small apps |
| Compute Optimized | C | Gaming, HPC, media processing |
| Memory Optimized | R, X | Databases, caching, analytics |
| Storage Optimized | I, D | Big data, log processing |
| GPU Instances | G, P | AI, ML, video rendering |

---

#### **💰 Pricing Models**  
| Type | Description | Best For |
|------|------------|----------|
| **On-Demand** | Pay per second/minute | Short-term workloads |
| **Reserved** | 1 or 3-year commitment | Long-term, steady apps |
| **Spot** | Up to 90% discount, can be interrupted | Batch jobs, testing |
| **Dedicated** | Full physical server | Compliance needs |

---

#### **🔒 Security & Networking**  
- **Security Groups** → Instance-level firewall.  
- **Network ACLs (NACLs)** → Subnet-level firewall.  
- **Elastic IP (EIP)** → Static public IP.  
- **VPC (Virtual Private Cloud)** → Isolated cloud network.  

---

#### **📦 EC2 Storage Options**  
| Type | Persistent? | Use Case |
|------|------------|----------|
| **EBS (Elastic Block Store)** | ✅ Yes | Boot volumes, databases |
| **Instance Store** | ❌ No | Temporary storage |
| **EFS (Elastic File System)** | ✅ Yes | Shared storage across instances |

---

#### **⚖️ Load Balancing & Scaling**  
- **Auto Scaling** → Adds/removes instances based on demand.  
- **Elastic Load Balancer (ELB)** → Distributes traffic across multiple instances.  

---

### **🛠️ Backup & Recovery**  
- **EBS Snapshots** → Backup of disk volumes.  
- **AMIs (Amazon Machine Images)** → Pre-configured instance templates.  

---

### **🔹 Amazon EC2 Q&A**

#### **Basic Concepts**
1️⃣ **Q:** What is Amazon EC2?  
   **A:** Amazon Elastic Compute Cloud (EC2) is a cloud service that provides scalable virtual machines (instances) to run applications.

2️⃣ **Q:** What are the different EC2 instance types?  
   **A:**  
   - **General Purpose (T, M series)** – Balanced CPU and memory.  
   - **Compute Optimized (C series)** – More CPU power, good for high-performance tasks.  
   - **Memory Optimized (R, X series)** – More RAM, good for databases.  
   - **Storage Optimized (I, D series)** – High disk performance for big data.  
   - **GPU Instances (G, P series)** – Designed for machine learning and graphics processing.

3️⃣ **Q:** What are the different pricing models for EC2?  
   **A:**  
   - **On-Demand** – Pay per second/minute, flexible.  
   - **Reserved Instances** – 1 or 3-year commitment, cheaper.  
   - **Spot Instances** – Discounted but can be interrupted.  
   - **Dedicated Hosts** – Physical servers for compliance needs.  

4️⃣ **Q:** What is an AMI (Amazon Machine Image)?  
   **A:** An AMI is a pre-configured template that contains an operating system and software needed to launch EC2 instances.

---

#### **Security & Networking**
5️⃣ **Q:** What is a Security Group in EC2?  
   **A:** A security group acts as a virtual firewall that controls inbound and outbound traffic to EC2 instances.

6️⃣ **Q:** What is the difference between Security Groups and NACLs?  
   **A:**  
   - **Security Groups** work at the instance level and are stateful (if you allow inbound traffic, the response is automatically allowed).  
   - **Network ACLs (NACLs)** work at the subnet level and are stateless (you must allow both inbound and outbound traffic separately).  

7️⃣ **Q:** What is an Elastic IP (EIP)?  
   **A:** A static public IP address that remains the same even if you stop/start an instance.

8️⃣ **Q:** What is an Elastic Load Balancer (ELB)?  
   **A:** A service that distributes incoming traffic across multiple EC2 instances to improve performance and availability.

---

#### **Storage & Backups**
9️⃣ **Q:** What is the difference between EBS and Instance Store?  
   **A:**  
   - **EBS (Elastic Block Store)** – Persistent storage that remains even if the instance stops.  
   - **Instance Store** – Temporary storage that is lost when the instance stops.  

🔟 **Q:** How do you back up an EC2 instance?  
   **A:** By creating **EBS snapshots**, which store a point-in-time backup of your EBS volume.

---

### **1️⃣ EC2 Basics**  
1️⃣ **Q:** What are the key benefits of using EC2?  
   **A:**  
   - Scalability – Easily scale up/down instances.  
   - Flexibility – Choose instance types, OS, and configurations.  
   - Pay-as-you-go – No upfront costs, pay only for what you use.  
   - Integration – Works with other AWS services like S3, RDS, and VPC.  

2️⃣ **Q:** What operating systems are supported by EC2?  
   **A:**  
   - Windows  
   - Linux (Amazon Linux, Ubuntu, CentOS, Red Hat, etc.)  
   - MacOS (for Apple-specific workloads)  

3️⃣ **Q:** What is a Key Pair in EC2?  
   **A:** A key pair (private & public key) is used for secure SSH access to an EC2 instance.  

---

### **2️⃣ EC2 Instance Lifecycle & States**  
4️⃣ **Q:** What are the different EC2 instance states?  
   **A:**  
   - **Pending** – Instance is launching.  
   - **Running** – Instance is active and being used.  
   - **Stopping** – Instance is shutting down.  
   - **Stopped** – Instance is off but can be restarted.  
   - **Terminated** – Instance is deleted and cannot be recovered.  

5️⃣ **Q:** What happens when you stop an EC2 instance?  
   **A:** The instance shuts down, and you stop being charged for compute, but the **EBS volume remains attached** (unless you chose "delete on termination").  

6️⃣ **Q:** What happens when you terminate an EC2 instance?  
   **A:** The instance is permanently deleted, and **all attached storage is lost unless manually backed up**.  

---

### **3️⃣ EC2 Pricing Models (More Details)**  
7️⃣ **Q:** When should you use On-Demand instances?  
   **A:** For short-term, unpredictable workloads where you don’t want long-term commitments.  

8️⃣ **Q:** When should you use Reserved Instances?  
   **A:** For applications with **steady workloads** where you can commit for **1 or 3 years** to get discounts (up to 72% cheaper than On-Demand).  

9️⃣ **Q:** What are Spot Instances, and why are they cheap?  
   **A:**  
   - Spot Instances are unused EC2 capacity that AWS sells at a **discount (up to 90%)**.  
   - They **can be interrupted** if AWS needs the capacity.  
   - Ideal for **batch processing, testing, or workloads that can handle interruptions**.  

🔟 **Q:** What is a Dedicated Host?  
   **A:** A physical EC2 server fully dedicated to you. Used for **compliance needs** or when you need to bring your own licenses (BYOL).  

---

### **4️⃣ EC2 Instance Types (More Details)**  
1️⃣1️⃣ **Q:** What are the General Purpose EC2 instance types?  
   **A:** **T, M series** – Balanced compute, memory, and networking. Used for web apps, databases, and general workloads.  

1️⃣2️⃣ **Q:** What are Compute-Optimized instances used for?  
   **A:** **C series** – High CPU power, used for gaming servers, scientific modeling, and high-performance computing (HPC).  

1️⃣3️⃣ **Q:** What are Memory-Optimized instances used for?  
   **A:** **R, X series** – Large RAM capacity, ideal for databases, caching, and in-memory analytics.  

1️⃣4️⃣ **Q:** What are Storage-Optimized instances used for?  
   **A:** **I, D series** – High disk performance, used for big data, log processing, and analytics.  

1️⃣5️⃣ **Q:** What are GPU-based instances used for?  
   **A:** **G, P series** – Designed for machine learning, AI, deep learning, and graphics rendering.  

---

### **5️⃣ EC2 Networking & Connectivity**  
1️⃣6️⃣ **Q:** What is a Public vs. Private IP in EC2?  
   **A:**  
   - **Public IP** – Used for internet access; changes if the instance stops/restarts.  
   - **Private IP** – Used for internal communication; remains fixed in the VPC.  

1️⃣7️⃣ **Q:** What is an Elastic IP (EIP)?  
   **A:** A **static public IP** that you can assign to an instance, ensuring it doesn’t change even if the instance stops/restarts.  

1️⃣8️⃣ **Q:** What are Security Groups?  
   **A:**  
   - Act as **firewalls** for EC2 instances.  
   - Control **inbound and outbound traffic**.  
   - **Stateful** – If you allow incoming traffic, the response is automatically allowed.  

1️⃣9️⃣ **Q:** What is the difference between Security Groups and Network ACLs?  
   **A:**  
   - **Security Groups** – Instance-level firewall (Stateful).  
   - **Network ACLs (NACLs)** – Subnet-level firewall (Stateless).  

2️⃣0️⃣ **Q:** What is a VPC, and why is it important for EC2?  
   **A:** A **Virtual Private Cloud (VPC)** is a **private network** where EC2 instances run. It provides security, isolation, and networking control.  

---

### **6️⃣ EC2 Storage: EBS vs. Instance Store**  
2️⃣1️⃣ **Q:** What is Amazon EBS?  
   **A:** Amazon **Elastic Block Store (EBS)** is persistent storage that remains even after an EC2 instance stops.  

2️⃣2️⃣ **Q:** What are the different types of EBS volumes?  
   **A:**  
   - **General Purpose SSD (gp3, gp2)** – Standard for most workloads.  
   - **Provisioned IOPS SSD (io1, io2)** – High-performance applications.  
   - **Cold HDD (sc1)** – Low-cost storage for backups.  

2️⃣3️⃣ **Q:** What is the difference between EBS and Instance Store?  
   **A:**  
   - **EBS** – Persistent, remains even after instance stops.  
   - **Instance Store** – Temporary, deleted when the instance stops.  

---

### **7️⃣ EC2 Scaling & Load Balancing**  
2️⃣4️⃣ **Q:** What is Auto Scaling?  
   **A:** Automatically adds/removes EC2 instances based on traffic demand.  

2️⃣5️⃣ **Q:** What is an Elastic Load Balancer (ELB)?  
   **A:** A service that distributes traffic across multiple EC2 instances to improve availability.  

2️⃣6️⃣ **Q:** What are the different types of ELBs?  
   **A:**  
   - **Application Load Balancer (ALB)** – Works at Layer 7 (HTTP/HTTPS).  
   - **Network Load Balancer (NLB)** – Works at Layer 4 (TCP/UDP).  
   - **Classic Load Balancer (CLB)** – Older version, supports basic routing.  

---

### **8️⃣ EC2 Backup & Recovery**  
2️⃣7️⃣ **Q:** What is an AMI (Amazon Machine Image)?  
   **A:** A pre-configured template containing OS, software, and settings to launch EC2 instances.  

2️⃣8️⃣ **Q:** What is an EBS Snapshot?  
   **A:** A **point-in-time backup** of an EBS volume that can be used to restore data.  

2️⃣9️⃣ **Q:** How do you back up an entire EC2 instance?  
   **A:** By creating an **AMI** (which includes OS, software, and configurations) or taking **EBS snapshots**.  

---
