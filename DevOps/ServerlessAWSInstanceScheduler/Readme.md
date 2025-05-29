**AWS Management Console-based Deployment Guide** for **Serverless AWS EC2 Instance Scheduler**.

---

# **🚀 Deployment Guide (AWS Console)**
This guide will walk you through deploying:
✅ **Flask API using AWS Lambda & API Gateway**  
✅ **EC2 Scheduler using AWS Lambda & DynamoDB**  
✅ **EventBridge Rule to trigger the Lambda function**  

---

## **🛠 Step 1: Set Up AWS Lambda for EC2 Scheduling**
1️⃣ **Login to AWS Console** → **Go to Lambda** ([AWS Lambda](https://console.aws.amazon.com/lambda))  
2️⃣ **Create a new Lambda function**  
   - **Function name:** `ec2_instance_scheduler`
   - **Runtime:** `Python 3.8`
   - **Permissions:** Create a new IAM role with **EC2 Full Access, DynamoDB Access & EventBridge Invocation**
   - **Click "Create function"**  
3️⃣ **Upload Code**  
   - In **Function Code**, select **Upload a .zip file** and upload your `lambda_function.zip`
   - **Handler:** `lambda_function.lambda_handler`
   - Click **Deploy**

---

## **🛠 Step 2: Set Up DynamoDB Table**
1️⃣ **Go to AWS Console** → **DynamoDB** ([AWS DynamoDB](https://console.aws.amazon.com/dynamodb))  
2️⃣ **Create Table**  
   - **Table name:** `ec2_scheduler`
   - **Primary key:** `instance_id` (String)
   - Click **Create Table**

---

## **🛠 Step 3: Create EventBridge Rule**
1️⃣ **Go to AWS Console** → **EventBridge** ([AWS EventBridge](https://console.aws.amazon.com/events))  
2️⃣ **Create Rule**  
   - **Name:** `every-5-minutes`
   - **Event Pattern:** `Schedule` → `rate(5 minutes)`
   - **Target:** Select **AWS Lambda** → Choose `ec2_instance_scheduler`
   - Click **Create**

---

## **🛠 Step 4: Deploy Flask API via AWS Lambda**
1️⃣ **Go to AWS Console** → **Lambda**  
2️⃣ **Create a new Lambda function**  
   - **Function Name:** `ec2_scheduler_api`
   - **Runtime:** `Python 3.8`
   - **Upload Flask API Code (flask_app.zip)**
   - **Handler:** `app.lambda_handler`
   - Click **Deploy**  
3️⃣ **Enable API Gateway**
   - Scroll to **API Gateway**
   - Select **Create an API**
   - Choose **REST API**
   - Click **Deploy API**
   - Note the **Invoke URL** (e.g., `https://your-api-id.execute-api.us-east-1.amazonaws.com/prod`)

---

## **🛠 Step 5: Test the API**
1️⃣ **Create a Schedule**  
   - Open **Postman** or **curl**
   - Send a **POST request** to:
     ```
     https://your-api-id.execute-api.us-east-1.amazonaws.com/prod/schedule
     ```
   - With JSON body:
     ```json
     {
       "instance_id": "i-0abcd1234efgh5678",
       "schedule": {
         "monday": "start:08:00, stop:18:00",
         "saturday": "stop"
       }
     }
     ```

2️⃣ **Fetch a Schedule**
   - **GET request** to:
     ```
     https://your-api-id.execute-api.us-east-1.amazonaws.com/prod/schedule/i-0abcd1234efgh5678
     ```

3️⃣ **Delete a Schedule**
   - **DELETE request** to:
     ```
     https://your-api-id.execute-api.us-east-1.amazonaws.com/prod/schedule/i-0abcd1234efgh5678
     ```

---