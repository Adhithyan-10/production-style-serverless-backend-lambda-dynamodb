# Architecture Folder

This folder contains the architecture diagrams used in this project.

The diagrams explain how the serverless backend system is designed using AWS services such as API Gateway, AWS Lambda, DynamoDB, CloudWatch, and SNS.

---

# Architecture Diagram

[View Full Architecture Diagram](./Archh1.png)

![Architecture Diagram](./Archh1.png)

---

# Architecture Overview

This project follows a production-style serverless backend architecture.

## Request Flow

```text
Frontend/User Request
        ↓
Amazon API Gateway
        ↓
AWS Lambda Function (Python CRUD Logic)
        ↓
Amazon DynamoDB
```

---

# Components Used

## Amazon API Gateway

Acts as the API routing layer.

Responsible for:

* Receiving HTTP requests
* Managing REST API endpoints
* Routing requests to Lambda
* Handling API-level security and authorization

Example endpoints:

* POST /users
* GET /users
* PUT /users/{id}
* DELETE /users/{id}

---

## AWS Lambda

Acts as the serverless backend compute layer.

Responsible for:

* Executing CRUD operations
* Processing API requests
* Interacting with DynamoDB
* Returning API responses

The backend logic is implemented using Python and Boto3.

---

## Amazon DynamoDB

Acts as the NoSQL database layer.

Responsible for:

* Storing user records
* Managing structured NoSQL data
* Supporting scalable serverless storage

---

## Amazon CloudWatch

Used for:

* Lambda execution logs
* Monitoring
* Metrics collection
* Debugging and troubleshooting

CloudWatch automatically stores Lambda execution logs during function execution.

---

## Amazon SNS

Used as a monitoring and notification layer.

Can be integrated with CloudWatch alarms to:

* Send alerts on failures
* Notify about high error rates
* Monitor serverless application health

---

# CRUD Workflow

The architecture supports full CRUD operations.

## Create

Insert new user data into DynamoDB.

## Read

Retrieve user records from DynamoDB.

## Update

Modify existing user information.

## Delete

Remove user records from DynamoDB.

---

# Purpose of This Architecture

The goal of this architecture is to demonstrate:

* Serverless backend development
* API-driven application design
* AWS Lambda integration
* DynamoDB CRUD workflows
* Cloud-native architecture concepts
* Monitoring and observability basics

---

# Learning Outcome

This architecture helped in understanding:

* Difference between traditional and serverless backend systems
* API Gateway request routing
* Lambda-based backend execution
* NoSQL database integration
* AWS monitoring flow using CloudWatch and SNS
* Production-style serverless design patterns
# Architecture Folder

This folder contains the architecture diagrams used in this project.

The diagrams explain how the serverless backend system is designed using AWS services such as API Gateway, AWS Lambda, DynamoDB, CloudWatch, and SNS.

---

# Architecture Diagram

[View Full Architecture Diagram](./Archh1.png)

![Architecture Diagram](./Archh1.png)

---

# Architecture Overview

This project follows a production-style serverless backend architecture.

## Request Flow

```text
Frontend/User Request
        ↓
Amazon API Gateway
        ↓
AWS Lambda Function (Python CRUD Logic)
        ↓
Amazon DynamoDB
```

---

# Components Used

## Amazon API Gateway

Acts as the API routing layer.

Responsible for:

* Receiving HTTP requests
* Managing REST API endpoints
* Routing requests to Lambda
* Handling API-level security and authorization

Example endpoints:

* POST /users
* GET /users
* PUT /users/{id}
* DELETE /users/{id}

---

## AWS Lambda

Acts as the serverless backend compute layer.

Responsible for:

* Executing CRUD operations
* Processing API requests
* Interacting with DynamoDB
* Returning API responses

The backend logic is implemented using Python and Boto3.

---

## Amazon DynamoDB

Acts as the NoSQL database layer.

Responsible for:

* Storing user records
* Managing structured NoSQL data
* Supporting scalable serverless storage

---

## Amazon CloudWatch

Used for:

* Lambda execution logs
* Monitoring
* Metrics collection
* Debugging and troubleshooting

CloudWatch automatically stores Lambda execution logs during function execution.

---

## Amazon SNS

Used as a monitoring and notification layer.

Can be integrated with CloudWatch alarms to:

* Send alerts on failures
* Notify about high error rates
* Monitor serverless application health

---

# CRUD Workflow

The architecture supports full CRUD operations.

## Create

Insert new user data into DynamoDB.

## Read

Retrieve user records from DynamoDB.

## Update

Modify existing user information.

## Delete

Remove user records from DynamoDB.

---

# Purpose of This Architecture

The goal of this architecture is to demonstrate:

* Serverless backend development
* API-driven application design
* AWS Lambda integration
* DynamoDB CRUD workflows
* Cloud-native architecture concepts
* Monitoring and observability basics

---

# Learning Outcome

This architecture helped in understanding:

* Difference between traditional and serverless backend systems
* API Gateway request routing
* Lambda-based backend execution
* NoSQL database integration
* AWS monitoring flow using CloudWatch and SNS
* Production-style serverless design patterns
