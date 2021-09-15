import json
import os, time, datetime
S3_BUCKET_NAME="Initial Value"
def edapPolicy():
#Read the policy file
    with open("/usr/local/airflow/dags/policy.json") as jsonFile:
        jsonObject = json.load(jsonFile)
        jsonFile.close()

    Email = jsonObject['email']
    Owner = jsonObject['owner']
    ApplicationId = jsonObject['applicationId']
    BusinessUnitName = jsonObject['businessUnitName']
    RetentionPolicy = jsonObject['retentionPolicy']
    S3_BUCKET_NAME = jsonObject['vaultName']
    MoveToArchive = jsonObject['moveToArchive']
    MoveToDeepArchive = jsonObject['moveToDeepArchive']
    FileName = jsonObject['fileName']

    print(Email)
    print(Owner)
    print(FileName)   
    print(S3_BUCKET_NAME) 

#Get metadata of a file using the standard Python script
    file = "/usr/local/airflow/dags/unstructured.csv"

    print(file)

    print("Modified")
    print(os.stat(file)[-2])
    print(os.stat(file).st_mtime)
    print(os.path.getmtime(file))

    print()

    print("Created")
    print(os.stat(file)[-1])
    print(os.stat(file).st_ctime)
    print(os.path.getctime(file))

    print()

    modified = os.path.getmtime(file)
    print("Date modified: "+time.ctime(modified))
    print("Date modified:",datetime.datetime.fromtimestamp(modified))
    year,month,day,hour,minute,second=time.localtime(modified)[:-3]
    print("Date modified: %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))

    print()

    created = os.path.getctime(file)
    print("Date created: "+time.ctime(created))
    print("Date created:",datetime.datetime.fromtimestamp(created))
    year,month,day,hour,minute,second=time.localtime(created)[:-3]
    print("Date created: %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))

#Create Manifest file by reading the JSON policy and unstructured file.
    json_data = {
        "fileName": FileName,
        "createdBy": Owner,
        "updatedBy": Owner,
        "createdDateTime": time.ctime(created),
        "updatedDateTime": time.ctime(modified),
        "searchKey": FileName
    }
    
    print(json_data)   

    with open('/usr/local/airflow/dags/manifest.json', 'w') as jsonFile:
        json.dump(json_data, jsonFile)
        jsonFile.close() 
        print("File has been created with the dynamic JSON data")   