import os
import boto3

def get_rds_iam_token():
    """
    Generates an RDS IAM authentication token.
    Uses environment variables for AWS credentials if present.
    """
    host = os.getenv("RDS_HOST", "database-1-instance-1.c3qms0w66h02.ap-south-1.rds.amazonaws.com")
    port = int(os.getenv("RDS_PORT", 5432))
    user = os.getenv("RDS_USER", "postgres")
    region = os.getenv("RDS_REGION", "ap-south-1")

    # Access Keys from environment
    aws_access_key = os.getenv("AWS_ACCESS_KEY_ID")
    aws_secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")

    client = boto3.client(
        'rds', 
        region_name=region,
        aws_access_key_id=aws_access_key,
        aws_secret_access_key=aws_secret_key,
    )

    # Generate token
    token = client.generate_db_auth_token(
        DBHostname=host,
        Port=port,
        DBUsername=user,
        Region=region
    )
    return token
