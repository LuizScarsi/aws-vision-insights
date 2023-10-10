import json
from services.s3 import create_presigned_url
from services.rekognition import ImageAnalyser, ResponseFormatter
from utils.util import format_time

def handle_v2_description(event, context):
    """
    Example route to demonstrate a lambda function for the v2 description
    :return: JSON with statusCode and body with a message
    """

    body = {
        "message": "VISION api version 1."
    }

    response = {"statusCode": 200, "body": json.dumps(body)}
    return response

def handle_v2_vision(event, context):
    try:
        request_body = json.loads(event['body'])
        request_image_name = request_body['image_name']
        request_bucket_name = request_body['bucket_name']

        presigned_url = create_presigned_url(request_bucket_name, request_image_name)
        formatted_time = format_time()
        rekognition_response = ImageAnalyser.detect_faces(request_bucket_name, request_image_name)
        formatted_rekognition_response = ResponseFormatter.format_faces(rekognition_response)

        body = {
            "url_to_image": presigned_url,
            "created_image": formatted_time,
            "faces": formatted_rekognition_response,
        }

        response = {"statusCode": 200, "body": json.dumps(body, indent=4)}
        print(body) # Print the response to the Cloudwatch logs

    except Exception as exceptError:
        
        response = {"statusCode": 500, "body": json.dumps(str(exceptError))}

    return response