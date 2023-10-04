import boto3

rekognition_client = boto3.client('rekognition')

class ImageAnalyser:
    def detect_labels(bucket_name, image_name):
        """ Recieves an bucket and an image from the bucket and returns the labels and the confidence of the labels.

        :param bucketName: string
        :param imageName: string
        :return: JSON with the response from Rekognition
        """

        try:
            response = rekognition_client.detect_labels(
                Image={
                    'S3Object': {
                        'Bucket': bucket_name,
                        'Name': image_name
                    }
                },
                MaxLabels=10,
                MinConfidence=80
            )

        except Exception as except_error:
            return except_error
        
        return response
    
    def detect_faces(bucket_name, image_name):
        """ Recieves an bucket and an image from the bucket and returns the labels and the confidence of the labels.

        :param bucketName: string
        :param imageName: string
        :return: JSON with the response from Rekognition
        """

        try:
            response = rekognition_client.detect_faces(
                Image={
                    'S3Object': {
                        'Bucket': bucket_name,
                        'Name': image_name
                    }
                },
                Attributes=[
                    'ALL',
                ]
            )

        except Exception as except_error:
            return except_error
        
        return response
    
class ResponseFormatter:
    def format_labels(rekognition_response):
        """ Recieves the response from Rekognition and formats it to a more readable format.

        :param rekognition_response: JSON
        :return: JSON with the formatted response from Rekognition
        """

        formatted_labels = []
        for label in rekognition_response['Labels']:
            formatted_labels.append({
                'Name': label['Name'],
                'Confidence': label['Confidence']
            })

        return formatted_labels
    
    def format_faces(rekognition_response):
        """ Receives the response from Rekognition and formats it to the desired format.

        :param rekognitionResponse: JSON
        :return: JSON with the formatted response from Rekognition
        """
        formatted_faces = []
        face_details = rekognition_response.get('FaceDetails', [])

        if not face_details:
            formatted_face = {
                "position": {
                    "Height": None,
                    "Left": None,
                    "Top": None,
                    "Width": None,
                },
                "classified_emotion": None,
                "classified_emotion_confidence": None,
            }

            formatted_faces.append(formatted_face)

        else:
            for face in face_details:
                formatted_face = {
                    "position": {
                        "Height": face['BoundingBox']['Height'],
                        "Left": face['BoundingBox']['Left'],
                        "Top": face['BoundingBox']['Top'],
                        "Width": face['BoundingBox']['Width'],
                    },
                    "classified_emotion": face['Emotions'][0]['Type'],
                    "classified_emotion_confidence": face['Emotions'][0]['Confidence'],
                }

                formatted_faces.append(formatted_face)

        return formatted_faces