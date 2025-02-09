# **📌 Commonly Used Keys in `docker-compose.yml` & Their Usage**  
> 🎯 **Goal:** Understand the most frequently used **Docker Compose YAML keys** and how they are used.  

---

## **🔹 1. `version`**
Defines the **Docker Compose file format** version.  
```yaml
version: '3.8'
```
✔️ Recommended: Always use the **latest version** (`3.8` or later).  

---

## **🔹 2. `services`**
Defines all containers in the **Docker Compose project**.  
```yaml
services:
  app:
    image: node:18
```
✔️ Each service represents **one container**.  

---

## **🔹 3. `image`**
Specifies the **Docker image** to use.  
```yaml
    image: nginx:latest
```
✔️ Uses **pre-built** images from Docker Hub or private registry.  

---

## **🔹 4. `build`**
Used to **build an image** from a `Dockerfile`.  
```yaml
    build: .
```
✔️ Looks for `Dockerfile` in the current directory.  
✔️ Can specify a different `Dockerfile`:
```yaml
    build:
      context: .
      dockerfile: Dockerfile.dev
```

---

## **🔹 5. `container_name`**
Sets a custom **name for the container**.  
```yaml
    container_name: my-app
```
✔️ Helps in identifying the container easily.  

---

## **🔹 6. `ports`**
Maps **host ports** to **container ports**.  
```yaml
    ports:
      - "8080:80"
```
✔️ **Format:** `host:container`  
✔️ Exposes **port 80 in the container** as **8080 on the host**.  

---

## **🔹 7. `environment`**
Passes **environment variables** to the container.  
```yaml
    environment:
      - NODE_ENV=production
      - DATABASE_URL=mysql://user:pass@db:3306/app
```
✔️ Can also use `.env` file:  
```yaml
    env_file:
      - .env
```

---

## **🔹 8. `volumes`**
Mounts host directories/files into the container.  
```yaml
    volumes:
      - ./data:/var/lib/mysql
```
✔️ **Persistent storage** for databases & logs.  

---

## **🔹 9. `depends_on`**
Ensures one service **starts before another**.  
```yaml
    depends_on:
      - db
```
✔️ The `app` service **waits for** `db` to start **but doesn't check readiness**.  

---

## **🔹 10. `restart`**
Defines **restart policy** for containers.  
```yaml
    restart: always
```
✔️ **Options:**
- `no` → Never restart (default).  
- `always` → Always restart.  
- `on-failure` → Restart only if the container **fails**.  
- `unless-stopped` → Restart unless **manually stopped**.  

---

## **🔹 11. `command`**
Overrides the **default command** in the image.  
```yaml
    command: ["npm", "start"]
```
✔️ Runs `npm start` instead of the default entrypoint.  

---

## **🔹 12. `entrypoint`**
Overrides the **entrypoint script**.  
```yaml
    entrypoint: ["python", "app.py"]
```
✔️ Used when replacing the container’s default entrypoint.  

---

## **🔹 13. `healthcheck`**
Defines a **health check** for the container.  
```yaml
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:80"]
      interval: 30s
      timeout: 10s
      retries: 3
```
✔️ Ensures the container is **healthy** before use.  

---

## **🔹 14. `networks`**
Defines **custom networks** for communication.  
```yaml
    networks:
      - my_network
```
✔️ Prevents containers from using the **default network**.  

**Define a network:**
```yaml
networks:
  my_network:
    driver: bridge
```

---

## **🔹 15. `extra_hosts`**
Adds **custom host-to-IP mappings** (like `/etc/hosts`).  
```yaml
    extra_hosts:
      - "local.dev:192.168.1.100"
```
✔️ Useful when a container needs to reach an **internal service**.  

---

## **🔹 16. `ulimits`**
Sets **container resource limits** (like open files).  
```yaml
    ulimits:
      nofile:
        soft: 1024
        hard: 2048
```
✔️ Prevents resource overuse by setting **limits**.  

---

## **🔹 17. `secrets`**
Passes **sensitive data** securely.  
```yaml
    secrets:
      - db_password
```
✔️ **Define secrets in a separate file**:
```yaml
secrets:
  db_password:
    file: ./db_password.txt
```

---

## **🔹 18. `logging`**
Configures **logging drivers** for the container.  
```yaml
    logging:
      driver: json-file
      options:
        max-size: "10m"
        max-file: "3"
```
✔️ **Limits log size** and prevents disk space issues.  

---

## **🔹 19. `cap_add` & `cap_drop`**
Gives or removes **Linux capabilities**.  
```yaml
    cap_add:
      - NET_ADMIN
    cap_drop:
      - MKNOD
```
✔️ Useful for security hardening.  

---

## **🔹 20. `read_only`**
Makes the container’s filesystem **read-only**.  
```yaml
    read_only: true
```
✔️ Improves **security** by preventing modifications.  

---

## **🚀 Full Example: `docker-compose.yml`**
```yaml
version: '3.8'

services:
  app:
    image: node:18
    container_name: my-app
    build: .
    ports:
      - "3000:3000"
    environment:
      - NODE_ENV=production
      - DATABASE_URL=mysql://user:pass@db:3306/app
    volumes:
      - .:/app
    depends_on:
      - db
    restart: always
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:3000"]
      interval: 30s
      timeout: 10s
      retries: 3

  db:
    image: mysql:8
    container_name: my-db
    environment:
      - MYSQL_ROOT_PASSWORD=rootpass
      - MYSQL_DATABASE=mydb
    volumes:
      - db_data:/var/lib/mysql
    restart: unless-stopped

volumes:
  db_data:
```
---

## **🔹 Summary**
| **Key**           | **Usage** |
|-------------------|----------|
| `version`        | Defines the Docker Compose version. |
| `services`       | Defines all containers in the project. |
| `image`          | Specifies a Docker image to use. |
| `build`          | Builds an image from a Dockerfile. |
| `container_name` | Sets a custom name for the container. |
| `ports`          | Maps host ports to container ports. |
| `environment`    | Passes environment variables. |
| `volumes`        | Mounts host directories/files into the container. |
| `depends_on`     | Ensures one service starts before another. |
| `restart`        | Defines restart policies. |
| `command`        | Overrides the default command. |
| `entrypoint`     | Overrides the entrypoint script. |
| `healthcheck`    | Defines a health check. |
| `networks`       | Creates a custom network. |
| `extra_hosts`    | Adds custom host-to-IP mappings. |
| `ulimits`        | Sets resource limits. |
| `secrets`        | Passes sensitive data securely. |
| `logging`        | Configures logging drivers. |
| `cap_add`        | Adds Linux capabilities. |
| `cap_drop`       | Removes Linux capabilities. |
| `read_only`      | Makes the container filesystem read-only. |

---

### **Dummy Project Structure**
Let's assume this is a **Node.js application** with a MySQL database. The project structure could look like this:

```
my-docker-project/
├── docker-compose.yml
├── Dockerfile
├── app/
│   ├── index.js
│   └── package.json
├── .env
├── db_data/               # Docker volume (will be created by Docker)
└── README.md
```

### **1. `docker-compose.yml`**
The `docker-compose.yml` file orchestrates both the **Node.js app** and the **MySQL database**.

```yaml
version: '3.8'

services:
  app:
    container_name: node-app
    build: ./app
    image: node-app:latest
    ports:
      - "3000:3000"
    environment:
      - NODE_ENV=production
      - DATABASE_URL=mysql://user:pass@db:3306/mydb
    volumes:
      - ./app:/usr/src/app
    depends_on:
      - db
    restart: always
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:3000"]
      interval: 30s
      timeout: 10s
      retries: 3
    networks:
      - app_network

  db:
    container_name: mysql-db
    image: mysql:8
    environment:
      - MYSQL_ROOT_PASSWORD=rootpass
      - MYSQL_DATABASE=mydb
    volumes:
      - db_data:/var/lib/mysql
    restart: unless-stopped
    networks:
      - app_network

volumes:
  db_data:

networks:
  app_network:
    driver: bridge
```

### **Explanation of `docker-compose.yml`**
- **Node.js App (`app`)**:  
    - **Build context** is set to `./app`, where the `Dockerfile` exists.  
    - It listens on **port 3000** and is connected to a **MySQL container** through the `DATABASE_URL` environment variable.  
    - **Health check** ensures that the service is **ready** before requests are sent.  
    - The app will always **restart** unless manually stopped (`restart: always`).
    - Uses a custom **network** called `app_network`.

- **MySQL (`db`)**:  
    - Uses the official **MySQL 8** image.  
    - Defines **root password** and **database name** using environment variables.  
    - **Data persistence** is achieved with the `db_data` volume, ensuring the database is not lost when the container stops.
    - It uses the same custom **network** `app_network`.

---

### **2. Project Files Inside the `app/` Directory**
Now, let's create a **basic Node.js application** that connects to the MySQL database.

#### **app/package.json**
```json
{
  "name": "node-app",
  "version": "1.0.0",
  "main": "index.js",
  "scripts": {
    "start": "node index.js"
  },
  "dependencies": {
    "express": "^4.17.1",
    "mysql2": "^2.2.5"
  }
}
```

#### **app/index.js**
This file will set up a simple **Express server** that connects to the **MySQL database**.

```js
const express = require('express');
const mysql = require('mysql2');

const app = express();
const port = 3000;

const connection = mysql.createConnection({
  host: 'db',  // Refers to the MySQL container's service name
  user: 'user',
  password: 'pass',
  database: 'mydb'
});

connection.connect((err) => {
  if (err) {
    console.error('Error connecting to DB:', err);
    process.exit(1);
  }
  console.log('Connected to the database');
});

app.get('/', (req, res) => {
  res.send('Hello World from Node.js with MySQL!');
});

app.listen(port, () => {
  console.log(`Server is running at http://localhost:${port}`);
});
```

#### **app/Dockerfile**
This is the **Dockerfile** that will build the image for the Node.js app.

```Dockerfile
# Use the official Node.js image from Docker Hub
FROM node:18

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy package.json and install dependencies
COPY package*.json ./
RUN npm install

# Copy the rest of the application code
COPY . .

# Expose the port the app will run on
EXPOSE 3000

# Command to run the app
CMD ["node", "index.js"]
```

---

### **3. `.env` (Environment Variables)**  
This file is used to store **environment variables** securely. It won't be directly referenced in `docker-compose.yml` (as we passed them inline), but it’s useful if you need to scale the project or manage sensitive data more securely.

```env
NODE_ENV=production
DATABASE_URL=mysql://user:pass@db:3306/mydb
```

This file would typically be **loaded** in the app by a `.env` parsing library like `dotenv`. However, in this example, we’ve used inline environment variables in `docker-compose.yml`.

---

### **4. Final Notes**
1. **Directory Mounting** (`volumes` in `docker-compose.yml`): The `./app:/usr/src/app` volume mounts the local `app/` directory into the container, allowing you to make changes locally and see them reflected immediately in the container.  
2. **Custom Networks**: The `app_network` allows the two services (Node.js and MySQL) to communicate with each other using the service names (`db` in this case).  
3. **Health Checks**: The Node.js app has a health check defined to ensure it’s ready to handle requests after starting up. This can help other services or orchestration platforms know when the app is fully up.

---

### **How to Run This Project:**
1. Navigate to the project directory (`my-docker-project/`).
2. Build and start the services using Docker Compose:
   ```bash
   docker-compose up --build
   ```
3. Once the services start, visit [http://localhost:3000](http://localhost:3000) to see the "Hello World" message.

This structure demonstrates a simple **full-stack application** with Docker Compose for **container orchestration**. The Node.js app connects to MySQL, and Docker Compose handles service definitions and their dependencies.
