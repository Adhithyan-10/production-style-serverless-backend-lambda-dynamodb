# Challenges Faced

During the implementation of this project, several issues and learning challenges were encountered.

---

# 1. IAM Permission Errors

Initially, the Lambda function could not access the DynamoDB table due to missing permissions.

## Resolution

Attached the required DynamoDB access policy to the Lambda execution role.

---

# 2. DynamoDB Table Name Mismatch

Incorrect table names inside the Lambda code caused backend execution failures.

## Resolution

Verified the exact DynamoDB table name and updated the Lambda code accordingly.

---

# 3. Understanding API Gateway Workflow

Understanding how API Gateway routes requests to Lambda required additional experimentation and learning.

## Resolution

Studied the request flow between API Gateway, Lambda, and DynamoDB to understand serverless API architecture.

---

# 4. CRUD Routing Logic

Initially, there was confusion regarding how a single Lambda function handles multiple CRUD operations.

## Resolution

Understood that API Gateway forwards requests to Lambda, and Lambda separates CRUD operations internally using HTTP methods.

---

# 5. Lambda Testing & Debugging

Understanding Lambda test events and debugging serverless backend responses took time during implementation.

## Resolution

Used Lambda execution logs and test responses to validate backend functionality.

---

# Key Takeaway

These challenges helped improve understanding of:

* Serverless debugging
* AWS permissions management
* API-driven backend workflows
* Lambda execution logic
* DynamoDB integration
* Cloud-native architecture design
