import json
import base64
import boto3
import uuid

s3 = boto3.client('s3')
BUCKET_NAME = 'my-image-uploader-baba'

def lambda_handler(event, context):
    try:
        body = event['body']
        is_base64_encoded = event['isBase64Encoded']
        
        if is_base64_encoded:
            image_data = base64.b64decode(body)
        else:
            image_data = body.encode("utf-8")

        filename = f"{uuid.uuid4()}.jpg"
        
        s3.put_object(
            Bucket=BUCKET_NAME,
            Key=filename,
            Body=image_data,
            ContentType='image/jpeg'
        )
        
        image_url = f"https://{BUCKET_NAME}.s3.amazonaws.com/{filename}"
        
        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Image uploaded", "url": image_url}),
            "headers": {
                "Content-Type": "application/json"
            }
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
        