# Source Code Folder

This folder contains the backend source code used in the project.

The backend logic is implemented using AWS Lambda, Python, and Boto3 to perform CRUD operations on Amazon DynamoDB.

---

# Included Files

## lambda_function.py

This file contains the AWS Lambda function responsible for:

* Processing API requests
* Executing CRUD operations
* Connecting with DynamoDB
* Managing backend business logic
* Returning API responses

---

# Backend Workflow

The serverless backend follows this workflow:

```text
Client Request
      ↓
API Gateway
      ↓
AWS Lambda Function
      ↓
DynamoDB Operations
```

---

# CRUD Operations

The backend architecture supports:

## Create

Insert new user data into DynamoDB.

## Read

Retrieve user records from DynamoDB.

## Update

Modify existing user data.

## Delete

Remove user records from DynamoDB.

---

# Technologies Used

* Python
* AWS Lambda
* Boto3
* Amazon DynamoDB
* API Gateway

---

# Purpose of This Folder

This folder demonstrates:

* Serverless backend development
* Python-based cloud automation
* DynamoDB integration
* API-driven backend architecture
* CRUD workflow implementation

---

# Learning Outcome

Through this implementation, the following concepts were understood:

* Lambda function development
* Backend request handling
* CRUD-based NoSQL operations
* Boto3 integration
* Serverless application workflow
* API-driven architecture design
