# Project Overview

## Project Title

Production-Style Serverless Backend using AWS Lambda & DynamoDB

---

# Introduction

This project demonstrates a serverless backend architecture built using AWS Lambda, API Gateway, DynamoDB, and Python.

The backend is designed to support CRUD operations while following modern cloud-native architecture principles.

Instead of running backend code on continuously running servers, the application uses AWS Lambda functions that execute only when triggered through API requests.

---

# Architecture Workflow

```text id="n4ykq0"
Frontend/User Request
        ↓
Amazon API Gateway
        ↓
AWS Lambda Function
        ↓
Amazon DynamoDB
```

---

# AWS Services Used

## Amazon API Gateway

Used for:

* API routing
* HTTP endpoint management
* Request handling
* Secure API access

---

## AWS Lambda

Used for:

* Backend compute
* CRUD logic execution
* Serverless request processing

---

## Amazon DynamoDB

Used for:

* NoSQL data storage
* User record management
* Scalable backend database operations

---

## Amazon CloudWatch

Used for:

* Lambda logs
* Monitoring
* Debugging

---

## Amazon SNS

Used for:

* Monitoring alerts
* Notification integration
* Observability workflow understanding

---

# CRUD Operations Supported

## Create

Insert user data into DynamoDB.

## Read

Retrieve stored user records.

## Update

Modify existing user information.

## Delete

Remove user records from the database.

---

# Backend Design

The architecture uses a single Lambda function for handling all CRUD operations.

API Gateway forwards requests to Lambda, and the Lambda function separates operations internally using HTTP methods such as:

```text id="h7v59m"
POST
GET
PUT
DELETE
```

---

# Goal of the Project

The primary goal of this project was to understand:

* Serverless backend architecture
* API Gateway routing
* Lambda execution workflow
* DynamoDB integration
* CRUD operations in AWS
* Event-driven backend systems

This project is part of a long-term AWS Cloud and DevOps project-based learning journey.
