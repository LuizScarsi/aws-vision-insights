import json

def health(event, context):
    """
    Initial basic route to check if the lambda function is running
    :return: JSON with statusCode and body with message
    """

    body = {
        "message": "Go Serverless v3.0! Your function executed successfully!",
        "input": event,
    }

    response = {"statusCode": 200, "body": json.dumps(body)}
    return response