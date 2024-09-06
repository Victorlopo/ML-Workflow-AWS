import json
import boto3
import os
import base64

s3 = boto3.client('s3')

def lambda_handler(event, context):
    responses = []
    for image in event['cases']:
        key = image['s3_key']
        bucket = image['s3_bucket']
        filename = key.split('/')[-1]
        local_path = f'/tmp/{filename}'
        
        # Download the image from S3
        s3.download_file(bucket, key, local_path)
        with open(local_path, 'rb') as file:
            image_data = base64.b64encode(file.read())
            
            # Save each image
            responses.append({
                "image_data":image_data, 
                "s3_bucket":bucket,
                "s3_key":key,
                "inferences":[]
            })
            
    return {
        'statusCode': 200, 
        'body': responses
    }



import json
#import sagemaker
import base64
import boto3
#from sagemaker.serializers import IdentitySerializer
#from sagemaker.predictor import Predictor

# Fill this in with the name of your deployed model
ENDPOINT = 	'image-classification-2024-09-06-08-56-48-077'
client = boto3.client('runtime.sagemaker')

def lambda_handler(event, context):
    
    responses = []
    
    for request in event['body']:

        # Decode the image data from base64 to binary (the model needs the input in binary to make the predictions)
        image_data = base64.b64decode(request['image_data'])  
    
        # Make a prediction
        predictor = client.invoke_endpoint(
            EndpointName=ENDPOINT,
            ContentType='application/x-image',
            Body=image_data)
            
        
        
        inferences = str(predictor['Body'].read().decode('utf-8'))
        
        # Save predictions
        responses.append({
            "s3_bucket":request['s3_bucket'],
            "s3_key":request['s3_key'],
            "inferences":inferences
        })

    # We return the data back to the Step Function    
    return {
        'statusCode': 200,
        "body": responses
    }


import json


THRESHOLD = .8


def lambda_handler(event, context):
    
    confidentPredictions = True
    
    for image in event['body']:
        # Grab the inferences from the event
        inferences = json.loads(image['inferences']) 
        
        # Check if any values in our inferences are above THRESHOLD
        meets_threshold = any(prediction > THRESHOLD for prediction in inferences) 
        
        # If our threshold is met, pass our data back out of the
        # Step Function, else, end the Step Function with an error
        if meets_threshold:
            pass
        else:
            confidentPredictions=False
            
    
    return {
        'statusCode': 200,
        'confidentPredictions': confidentPredictions,
        'body': event['body']
    }
