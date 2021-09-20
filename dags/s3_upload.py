# import requests
# import csv
# import json
import  boto3
from auth import ACCESS_KEY,SECRET_KEY
from create_manifest import *

def pushS3():
    directory = r'/usr/local/airflow/dags'
    for filename in os.listdir(directory):
        if filename.startswith("policy"):
            print(os.path.join(directory, filename))
            with open("/usr/local/airflow/dags/"+filename) as jsonFile:
                jsonObject = json.load(jsonFile)
                jsonFile.close()

                UnstructuredFileName = jsonObject['fileName']
                ManifestFileName = jsonObject['manifestFileName']
                ManifestVaultName = jsonObject['manifestValutName']
                S3_BUCKET_NAME = jsonObject['vaultName']
                #PolicyFileName = jsonObject['vaultName']

                # This value should be read from the create_manifest python file
                # Upload Manifest files
                ''' pushing data to S3 bucket'''
                client=boto3.client('s3',aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)

                #Start uploading the manifest files
                client.create_bucket(Bucket=ManifestVaultName)
                with open("/usr/local/airflow/dags/"+ManifestFileName,"rb") as f:
                    client.upload_fileobj(f,ManifestVaultName,ManifestFileName)
                print("Manifest files have been uploaded to S3")

                # Upload policy and unstructured files
                client.create_bucket(Bucket=S3_BUCKET_NAME)
                with open("/usr/local/airflow/dags/"+UnstructuredFileName,"rb") as f:
                    client.upload_fileobj(f,S3_BUCKET_NAME,UnstructuredFileName)
                with open("/usr/local/airflow/dags/"+filename,"rb") as f:
                    client.upload_fileobj(f,S3_BUCKET_NAME,filename)
                print("Policy and unstructured files have been uploaded to S3")