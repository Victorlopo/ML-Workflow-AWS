# ML-Workflow-AWS

## Context
In this project, a classifier for three of the classes present in the CIFAR-100 dataset was developed using Amazon SageMaker. The project covers all stages from ETL processes, model creation, and deployment, to monitoring and automating tasks with AWS Lambda and Step Functions.

## Load S3
The processed data, including both the training and test datasets, are stored in Amazon S3. This setup facilitates easy access and scalability for training and evaluating the machine learning models. The S3 buckets are structured to ensure separation of training and test data, supporting systematic model training and evaluation.
