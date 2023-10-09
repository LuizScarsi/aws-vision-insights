import json
from services.s3 import create_presigned_url
from services.rekognition import ImageAnalyser, ResponseFormatter
from utils.util import format_time

def handle_v1_description(event, context):
    """
    Example route to demonstrate a lambda function for the v1 description.
    :return: JSON with statusCode and body with message
    """

    body = {
        "message": "VISION api version 1."
    }

    response = {"statusCode": 200, "body": json.dumps(body)}
    return response

def handle_v1_vision(event, context):
    """
    Function that recieves a bucket and an image from the bucket
    and returns the labels and the confidence of the labels

    :return:
        :statusCode: 200 if everything went well
                     500 if something went wrong
        :body: JSON with the formatted response from Rekognition
    """
    try:
        request_body = json.loads(event['body'])
        request_image_name = request_body['image_name']
        request_bucket_name = request_body['bucket_name']

        presigned_url = create_presigned_url(request_bucket_name, request_image_name)
        formatted_time = format_time()
        rekognition_response = ImageAnalyser.detect_labels(request_bucket_name, request_image_name)
        formatted_rekognition_response = ResponseFormatter.format_labels(rekognition_response)

        body = {
            "url_to_image": presigned_url,
            "created_image": formatted_time,
            "Labels": formatted_rekognition_response,
        }

        response = {"statusCode": 200, "body": json.dumps(body, indent=4)}
        print(body) # Print the response to the CloudWatch logs

    except Exception as except_error:
        response = {"statusCode": 500, "body": str(except_error)}
        
    return response