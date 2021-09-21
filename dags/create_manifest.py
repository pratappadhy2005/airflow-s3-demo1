import json
import os, time, datetime
S3_BUCKET_NAME="Initial Value"
def edapPolicy(**kwargs):
#Read the policy file
    directory = r'/usr/local/airflow/dags'
    for filename in os.listdir(directory):
        if filename.startswith("policy"):
            print(os.path.join(directory, filename))
            with open("/usr/local/airflow/dags/"+filename) as jsonFile:
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
                fileArray = jsonObject['fileDetails']
                ManifestFileName = jsonObject['manifestFileName']

                print(Email)
                print(Owner)
                print(fileArray)   
                print(S3_BUCKET_NAME) 
                
                finalFileName = "["
                for fileName in fileArray:
                    print(fileName)
                    #Get metadata of a file using the standard Python script
                    file = "/usr/local/airflow/dags/" + fileName

                    print(file)
                    
                    if "[" == finalFileName:
                        finalFileName = finalFileName + '"' + fileName +'"'
                    else:
                        finalFileName = finalFileName + ',"' + fileName +'"'     
                    

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
                finalFileName = finalFileName + "]"
                json_data = {
                    "fileNames": finalFileName,
                    "createdBy": Owner,
                    "updatedBy": Owner,
                    "email" : Email,
                    "createdDateTime": time.ctime(created),
                    "updatedDateTime": time.ctime(modified),
                    "searchKey": finalFileName
                }
                
                print(json_data)   

            with open('/usr/local/airflow/dags/' + ManifestFileName, 'w') as jsonFile:
                json.dump(json_data, jsonFile)
                jsonFile.close() 
                print("File has been created with the dynamic JSON data")   