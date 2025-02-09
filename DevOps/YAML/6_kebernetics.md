
---

## **Kubernetes Command Reference and Practical Examples**

### **Kubernetes Common Commands**

Here’s a list of the most commonly used `kubectl` commands in Kubernetes for managing pods, deployments, and services, along with explanations and practical examples:

---

### **1. Creating Resources from YAML Files**

- **Command**:
  ```bash
  kubectl create -f <Name-of-.yml-file>
  ```
  - **Explanation**: This command is used to create Kubernetes resources (such as pods, deployments, services, etc.) from a specified YAML file.
  - **Example**:
    ```bash
    kubectl create -f deployment.yaml
    ```

---

### **2. Getting Information About Pods**

- **Command**:
  ```bash
  kubectl get pods
  ```
  - **Explanation**: This command lists all the pods running in the current namespace.
  - **Example**:
    ```bash
    kubectl get pods
    ```

- **Command**:
  ```bash
  kubectl describe pod <pod-name>
  ```
  - **Explanation**: This command provides detailed information about a specific pod, including events, container status, and resource usage.
  - **Example**:
    ```bash
    kubectl describe pod nginx-12345
    ```

---

### **3. Node Information**

- **Command**:
  ```bash
  kubectl get nodes -o wide
  ```
  - **Explanation**: This command lists the nodes in your Kubernetes cluster along with additional details like OS and architecture.
  - **Example**:
    ```bash
    kubectl get nodes -o wide
    ```

---

### **4. Working with ReplicaSets**

- **Command**:
  ```bash
  kubectl get replicaset
  ```
  - **Explanation**: This command lists all ReplicaSets in the current namespace.
  - **Example**:
    ```bash
    kubectl get replicaset
    ```

- **Command**:
  ```bash
  kubectl scale --replicas=<num> replicaset <replica-set-name>
  ```
  - **Explanation**: This command scales a ReplicaSet to a desired number of replicas. It does not affect the pod definitions.
  - **Example**:
    ```bash
    kubectl scale --replicas=5 replicaset myapp-replicaset
    ```

- **Command**:
  ```bash
  kubectl replace -f <replicaset-definition>.yaml
  ```
  - **Explanation**: This command replaces an existing ReplicaSet with a new definition, allowing you to update the ReplicaSet configuration.
  - **Example**:
    ```bash
    kubectl replace -f replicaset-definition.yaml
    ```

- **Command**:
  ```bash
  kubectl edit replicaset <replica-set-name>
  ```
  - **Explanation**: Opens the ReplicaSet in the default editor for modifications.
  - **Example**:
    ```bash
    kubectl edit replicaset myapp-replicaset
    ```

---

### **5. Deployment Management**

- **Command**:
  ```bash
  kubectl apply -f <deployment-definition>.yaml
  ```
  - **Explanation**: This command applies the changes to an existing deployment, updating it to the new configuration in the YAML file.
  - **Example**:
    ```bash
    kubectl apply -f my-deployment.yaml
    ```

- **Command**:
  ```bash
  kubectl set image deployment/<app-deployment> <container-name>=<new-image>
  ```
  - **Explanation**: This command updates the container image used in a deployment.
  - **Example**:
    ```bash
    kubectl set image deployment/my-deployment nginx=nginx:v2
    ```

- **Command**:
  ```bash
  kubectl rollout status deployment/<deployment-name>
  ```
  - **Explanation**: Displays the status of a deployment rollout.
  - **Example**:
    ```bash
    kubectl rollout status deployment/my-deployment
    ```

- **Command**:
  ```bash
  kubectl rollout history deployment/<deployment-name>
  ```
  - **Explanation**: Shows the history of the deployments and rollouts for a given deployment.
  - **Example**:
    ```bash
    kubectl rollout history deployment/my-deployment
    ```

- **Command**:
  ```bash
  kubectl rollout undo deployment/<deployment-name>
  ```
  - **Explanation**: Reverts the deployment to the previous version.
  - **Example**:
    ```bash
    kubectl rollout undo deployment/my-deployment
    ```

---

### **6. Service Management**

- **Command**:
  ```bash
  kubectl get services
  ```
  - **Explanation**: This command lists all services running in the current namespace.
  - **Example**:
    ```bash
    kubectl get services
    ```

- **Command**:
  ```bash
  kubectl describe service <service-name>
  ```
  - **Explanation**: This command provides detailed information about a specific service, including endpoints and port mappings.
  - **Example**:
    ```bash
    kubectl describe service my-service
    ```

---

### **7. Deleting Pods and Resources**

- **Command**:
  ```bash
  kubectl delete pod <pod-name>
  ```
  - **Explanation**: Deletes a pod by its name.
  - **Example**:
    ```bash
    kubectl delete pod nginx-12345
    ```

---

### **8. Creating Pods from a YAML Manifest**

#### **Task**: Create a New Pod with the Nginx Image
- **Command**:
  ```bash
  kubectl run nginx --image=nginx
  ```
  - **Explanation**: This command creates a pod named `nginx` using the `nginx` image.

#### **Task**: Create a New Pod Named Redis with a Custom Image
- **Solution**:
  - First, create a manifest for the pod using `kubectl run` with the `--dry-run` option.
  - **Command**:
    ```bash
    kubectl run redis --image=redis123 --dry-run=client -o yaml > redis-definition.yaml
    ```
  - Then, create the pod using the manifest file:
    ```bash
    kubectl create -f redis-definition.yaml
    ```

  - Finally, verify the pod creation:
    ```bash
    kubectl get pods
    ```

---

### **9. Practical Use Case: Scaling Pods and ReplicaSets**

#### **Task**: Scaling a ReplicaSet
- **Scenario**: Suppose you have a ReplicaSet defined and you need to scale it from 3 replicas to 6 replicas.
- **Command**:
  ```bash
  kubectl scale --replicas=6 replicaset myapp-replicaset
  ```
- **Note**: This command will only scale the ReplicaSet, but the number of pods won’t change until the scaling operation is completed.

#### **Task**: Rolling Back a Deployment
- **Command**:
  ```bash
  kubectl rollout undo deployment/my-deployment
  ```
  - **Explanation**: This will roll back the deployment to the previous stable version.

---

### **Summary of Key Kubernetes Commands**
- **kubectl create -f <file>.yaml**: Creates resources from a YAML file.
- **kubectl get <resource>**: Lists the resources (e.g., `kubectl get pods`).
- **kubectl describe <resource> <name>**: Describes a specific resource in detail.
- **kubectl apply -f <file>.yaml**: Applies changes to existing resources.
- **kubectl scale --replicas=<num> <resource>**: Scales resources like ReplicaSets or Deployments.
- **kubectl set image deployment/<deployment-name> <container-name>=<new-image>**: Updates container image in a deployment.
- **kubectl rollout status <resource>**: Displays the rollout status of deployments.
- **kubectl delete <resource> <name>**: Deletes a resource.

---

### **Conclusion**
This document provided a detailed list of the most commonly used Kubernetes commands with explanations, examples, and practical use cases. These commands will help you efficiently manage pods, deployments, services, and replica sets in Kubernetes environments.