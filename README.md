# ML-Workflow-AWS

## Context
In this project, a classifier for three of the classes present in the CIFAR-100 dataset was developed using Amazon SageMaker. The project covers all stages from ETL processes, model creation, and deployment, to monitoring and automating tasks with AWS Lambda and Step Functions.

## Load data to S3
The processed data, including both the training and test datasets, are stored in Amazon S3. This setup facilitates easy access and scalability for training and evaluating the machine learning models. The S3 buckets are structured to ensure separation of training and test data, supporting systematic model training and evaluation.

## Model Training with Amazon SageMaker
This section outlines the initialization and configuration of an estimator for training an image classification model using Amazon SageMaker. The process begins by retrieving the URI of the SageMaker container for image classification algorithms, ensuring the latest version of the algorithm is utilized. This container provides the necessary environment for running the image classification model.

A SageMaker Estimator object is defined, specifying the container URI, the IAM role, the count and type of compute instances for training, and the S3 output location where the resulting model artifacts will be stored. This setup is crucial for configuring the training environment with adequate resources and access policies.

Furthermore, specific hyperparameters for the model training are set, such as the image shape (defining the number of channels and image dimensions), the number of classes to predict, and the total number of training samples.

The input data for the model is organized into four specific channels—training data, validation data, and their respective image lists—and hosted on S3. The `TrainingInput` is used to specify the paths and content types of these data, facilitating SageMaker's access and loading of the data during training.

Finally, the training process is initiated by calling the `fit` method of the model with the prepared input data. This process will train the model using the specified data and automatically save the trained model artifacts in the previously defined S3 location, enabling subsequent deployment and evaluation.

## Model Deployment and Inference

### Model Monitor Configuration

Before deploying the model, we set up Amazon SageMaker's Model Monitor to track the deployment's performance. This involves capturing the input and output data for each prediction, which allows us to analyze the model's behavior over time. Data is captured at a rate of 100%, ensuring all inference data is logged, and stored in the specified S3 bucket under `Project_2_Extended/data_capture`.

### Model Deployment

The model is deployed on an `ml.m5.xlarge` instance. This instance type is chosen for its balance of compute, memory, and networking capabilities, suitable for most general-purpose workloads.
