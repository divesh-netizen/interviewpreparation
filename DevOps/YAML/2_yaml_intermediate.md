
---

# **📌 Day 2: Intermediate YAML for CI/CD**
> 🎯 **Goal:** Learn advanced YAML features like multi-line handling, references (`&` and `*`), environment variables, and apply them in real CI/CD pipeline files.

---

## **🔹 1. Multi-line Strings in YAML**
In YAML, we can store multi-line values efficiently.

### **🟢 1.1 Preserve Newlines (`|` - Literal Block Scalar)**
✔️ Keeps the **exact formatting** (includes line breaks)  
```yaml
message: |
  This is a multi-line string.
  The line breaks are preserved.
  Useful for long messages.
```
**Output:**
```
This is a multi-line string.
The line breaks are preserved.
Useful for long messages.
```

---

### **🟢 1.2 Collapse Newlines (`>` - Folded Block Scalar)**
✔️ Converts multiple lines into a **single-line string**  
```yaml
message: >
  This is a multi-line string.
  The line breaks are removed.
  Useful for log messages.
```
**Output:**
```
This is a multi-line string. The line breaks are removed. Useful for log messages.
```

---

### **🟢 1.3 Single & Double Quotes in YAML**
✔️ Use quotes when the string contains special characters (`:` `@` `#` etc.)  
```yaml
single_quote: 'This is a string with "double quotes" inside.'
double_quote: "This is a string with 'single quotes' inside."
```

✔️ **Why are quotes important?**  
If a string contains special characters like `yes`, `no`, `on`, `off`, YAML might misinterpret them as **booleans**.  
To avoid issues, **always wrap such values in quotes**:  
```yaml
value1: "yes"  # Treated as a string
value2: yes    # Treated as a boolean (true)
```

---

## **🔹 2. Using Aliases (`&`) and Anchors (`*`)**
✔️ Avoid duplication and reuse values using **anchors** and **aliases**.

📌 **Example:**
```yaml
defaults: &common_settings
  timeout: 30
  retries: 3
  log_level: debug

job1:
  <<: *common_settings
  name: "Deploy to Staging"

job2:
  <<: *common_settings
  name: "Deploy to Production"
  retries: 5  # Override a specific value
```

### **🔍 Breakdown**
✔️ `&common_settings` → Defines an **anchor** (reusable block)  
✔️ `*common_settings` → Uses an **alias** (copies the values)  
✔️ `<<: *common_settings` → Merges the **default settings** into `job1` and `job2`  
✔️ `retries: 5` → Overrides `retries` for `job2`  

---

## **🔹 3. Environment Variables in YAML (For CI/CD Pipelines)**
Most CI/CD tools allow you to use environment variables inside YAML files.

📌 **Example for GitHub Actions (`.github/workflows/deploy.yml`)**
```yaml
name: Deploy Pipeline
on: push
jobs:
  deploy:
    runs-on: ubuntu-latest
    env:
      AWS_REGION: us-east-1
      APP_ENV: production
    steps:
      - name: Print Environment Variables
        run: echo "Deploying to $AWS_REGION in $APP_ENV mode"
```

📌 **Example for Bitbucket Pipelines (`bitbucket-pipelines.yml`)**
```yaml
pipelines:
  default:
    - step:
        script:
          - echo "Deploying to $DEPLOY_ENV"
```
✔️ In Bitbucket, define **DEPLOY_ENV** under **Repository → Settings → Environment Variables.**  

---

## **🔹 4. Writing a Real CI/CD Pipeline in YAML**
Let’s build a **GitHub Actions CI/CD pipeline** (`.github/workflows/deploy.yml`) for deploying a **Node.js app**.

📌 **Example:**
```yaml
name: Node.js Deployment

on:
  push:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Code
        uses: actions/checkout@v3

      - name: Set up Node.js
        uses: actions/setup-node@v3
        with:
          node-version: 18

      - name: Install Dependencies
        run: npm install

      - name: Run Tests
        run: npm test

  deploy:
    needs: build
    runs-on: ubuntu-latest
    environment: production
    steps:
      - name: Deploy App
        run: |
          echo "Deploying to production server..."
          # SSH or AWS deployment commands go here
```
✔️ **Triggers**: Runs on `push` to `main`  
✔️ **Jobs**: `build` and `deploy`  
✔️ **`needs: build`**: Ensures `deploy` runs only after `build` succeeds  
✔️ **Environment Variables**: Used for production settings  

---

## **🔹 5. YAML Best Practices for CI/CD**
✅ **Keep it Modular** → Use anchors & aliases to avoid duplication  
✅ **Use Environment Variables** → Don’t hardcode secrets in YAML  
✅ **Validate YAML Syntax** → Use [yaml-lint](https://github.com/adrienverge/yamllint)  
✅ **Use Meaningful Job Names** → Helps in debugging CI/CD logs  
✅ **Structure YAML for Readability** → Keep related steps together  

---

## **🔹 Hands-on Challenges**
### **🚀 Task 1: Use Anchors & Aliases**
✅ Modify the GitHub Actions YAML to **reuse** a common setup block  
✅ Use an **anchor (`&`)** for `setup-node` and **alias (`*`)** in multiple places  

---

### **🚀 Task 2: Create a YAML Pipeline for Bitbucket**
✅ Write a **Bitbucket Pipelines (`bitbucket-pipelines.yml`)** file  
✅ It should:  
- Install dependencies  
- Run tests  
- Deploy using environment variables  

📌 **Example Starter:**
```yaml
pipelines:
  default:
    - step:
        name: Install & Test
        script:
          - npm install
          - npm test

    - step:
        name: Deploy
        deployment: production
        script:
          - echo "Deploying to $DEPLOY_ENV"
```

---
