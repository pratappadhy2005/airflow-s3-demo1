import json
import  boto3
import os, time, datetime

def validateJSON(**kwargs):
    directory = r'/usr/local/airflow/dags'
    for filename in os.listdir(directory):
        if filename.startswith("policy"):
            print(os.path.join(directory, filename))
            with open("/usr/local/airflow/dags/"+filename) as jsonFile:
                try:
                    print('Validating policy file with name : '+filename)
                    jsonObject = json.load(jsonFile)
                    jsonFile.close()
                    print('Validation passed for policy file with name : '+filename)
                except ValueError as err:
                    print('Validation failed for policy file with name : '+filename)
                    return False
    return True