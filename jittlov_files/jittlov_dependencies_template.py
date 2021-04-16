#![filePath]/[apiName]_venv/bin/python

import subprocess
import sys

apiPath = sys.argv[1]
apiName = sys.argv[2]

fullApiPath = apiPath + '/' + apiName

print("Installing flask and its dependencies.  Please wait...")
subprocess.check_call([sys.executable, "-m", "pip", "install", "flask"])
subprocess.check_call([sys.executable, "-m", "pip", "install", "pymongo"])
subprocess.check_call([sys.executable, "-m", "pip", "install", "apispec"])
subprocess.check_call([sys.executable, "-m", "pip", "install", "marshmallow"])
subprocess.check_call([sys.executable, "-m", "pip", "install", "flask_apispec"])
subprocess.check_call([sys.executable, "-m", "pip", "install", "flask_restful"])

subprocess.run([fullApiPath + "/jittlov_setup.py", apiPath, apiName])
