import json

def edapPolicy():
    with open("/usr/local/airflow/dags/policy.json") as jsonFile:
        jsonObject = json.load(jsonFile)
        jsonFile.close()

    Email = jsonObject['email']
    Name = jsonObject['name']
    FileName = jsonObject['fileName']

    print(Email)
    print(Name)
    print(FileName)   

    json_data = {
        "product":"Python book",
        "overall":"4.0",
        "text":"Nice book"
    }

    with open('/usr/local/airflow/dags/manifest.json', 'w') as jsonFile:
        json.dump(json_data, jsonFile)
        jsonFile.close() 
        print("File has been created with the JSON data")   