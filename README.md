# AWS Lambda Image Upload to S3

This project demonstrates how to upload a Base64-encoded image to an Amazon S3 bucket using AWS Lambda and API Gateway.

##  Features

- Upload images to S3 using Lambda
- Trigger via API Gateway HTTP endpoint
- Returns public S3 URL of the image

##  Technologies

- AWS Lambda
- Amazon S3
- API Gateway
- Python (boto3, base64)

##  API Request Format

**Endpoint**  
`POST https://vafawlywt9.execute-api.eu-north-1.amazonaws.com/default/uploadImageToS3`

**Header**
