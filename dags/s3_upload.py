# import requests
# import csv
# import json
import  boto3
from auth import ACCESS_KEY,SECRET_KEY
from create_manifest import *

def pushS3():
    with open("/usr/local/airflow/dags/policy.json") as jsonFile:
        jsonObject = json.load(jsonFile)
        jsonFile.close()

    # This value should be read from the create_manifest python file
    S3_BUCKET_NAME = jsonObject['vaultName']
    print(S3_BUCKET_NAME)
    ''' pushing data to S3 bucket'''
    client=boto3.client('s3',aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)

    #Start uploading the files
    client.create_bucket(Bucket=S3_BUCKET_NAME)
    with open("/usr/local/airflow/dags/unstructured.csv","rb") as f:
        client.upload_fileobj(f,S3_BUCKET_NAME,"unstructured.csv")
    with open("/usr/local/airflow/dags/policy.json","rb") as f:
        client.upload_fileobj(f,S3_BUCKET_NAME,"policy.json")
    with open("/usr/local/airflow/dags/manifest.json","rb") as f:
        client.upload_fileobj(f,S3_BUCKET_NAME,"manifest.json")
    print("Policy, Manifest and Unstructured files have been uploaded to S3")