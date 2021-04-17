#![filePath]/[apiName]_venv/bin/python

import subprocess
import sys
from Helpers import Helpers
from MongoHelpers import MongoHelpers

api_path = sys.argv[1]
api_name = sys.argv[2]

fullApiPath = api_path + '/' + api_name

print("Copying API files into virtual environment.")
subprocess.run(["cp", "__init_template__.py", fullApiPath + "/__init__.py"])
subprocess.run(["cp", "MongoApi.py", fullApiPath])
subprocess.run(["cp", "MongoApiConfig.py", fullApiPath])
subprocess.run(["cp", "run_template.sh", api_path + "/run.sh"])
subprocess.run(["chmod", "+x", api_path + "/run.sh"])


print("Updating MongoApi file")
Helpers.update_file(fullApiPath + "/MongoApi.py",
                    fullApiPath + "/MongoApi.py",
                    [{"search": "[apiName]", "replace": api_name}])

print("Updating MongoApiConfig file")
databaseUrl = MongoHelpers.confirm_mongo_db()
databaseName = MongoHelpers.confirm_mongo_db_name(databaseUrl)
databaseTable = MongoHelpers.confirm_mongo_collection_name(databaseUrl, databaseName)

apiBroadcastIp = Helpers.confirm_choice("Please enter the IP for the API to broadcast: [ex: 127.0.0.1] ")
apiBroadcastHttp = input("Do you want to use HTTPS? [y/n] ")

if apiBroadcastHttp == "Y" or apiBroadcastHttp == "y":
    apiBroadcastHttp = "https://"
else:
    apiBroadcastHttp = "http://"

apiBroadcastPort = Helpers.confirm_choice("Please enter the port for the API to broadcast: ")

print("Updating __init__ file")
Helpers.update_file(fullApiPath + "/__init__.py",
                    fullApiPath + "/__init__.py",
                    [{"search": "[apiName]", "replace": api_name},
                     {"search": "[apiBroadcastHttp]", "replace": apiBroadcastHttp},
                     {"search": "[apiBroadcastIp]", "replace": apiBroadcastIp},
                     {"search": "[apiBroadcastPort]", "replace": apiBroadcastPort}])
 
Helpers.update_file(fullApiPath + "/MongoApiConfig.py",
                    fullApiPath + "/MongoApiConfig.py",
                    [{"search": "[databaseUrl]", "replace": databaseUrl},
                     {"search": "[databaseName]", "replace": databaseName},
                     {"search": "[databaseTable]", "replace": databaseTable},
                     {"search": "[apiBroadcastHttp]", "replace": apiBroadcastHttp},
                     {"search": "[apiBroadcastIp]", "replace": apiBroadcastIp},
                     {"search": "[apiBroadcastPort]", "replace": apiBroadcastPort},
                     {"search": "[apiName]", "replace": api_name}])

schemaFileContents = Helpers.get_schema_file_contents()

with open(fullApiPath + '/Schema.py', 'w') as file:
    file.write(schemaFileContents)

print("Updating run file")

Helpers.update_file(api_path + "/run.sh",
                    api_path + "/run.sh",
                    [{"search": "[apiName]", "replace": api_name},
                     {"search": "[filePath]", "replace": api_path},
                     {"search": "[apiBroadcastIp]", "replace": apiBroadcastIp},
                     {"search": "[apiBroadcastPort]", "replace": apiBroadcastPort},
                     ])

subprocess.run([api_path + "/run.sh"])
