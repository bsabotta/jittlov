import subprocess
from Helpers import Helpers

print("Where do you want to create files for a new CRUD API?")

filePath = Helpers.confirm_choice("Please enter the full file path for API files: ")

confirm = Helpers.confirm_path(filePath)

if confirm:

    apiName = Helpers.confirm_choice("What is the name of the API you are making?  ")

    print("We are going to create a virtual environment for the API to run in.  Please wait...")
    subprocess.run(["python3", "-m", "venv", filePath + '/' + apiName + "_venv"])

    fullApiPath = filePath + '/' + apiName

    # Replace the placeholders in the API files with passed-in user input
    print("Updating template script file...")

    subprocess.run(["mkdir", fullApiPath])

    subprocess.run(["cp", "Helpers.py", fullApiPath + "/Helpers.py"])
    subprocess.run(["cp", "MongoHelpers.py", fullApiPath + "/MongoHelpers.py"])
    subprocess.run(["cp", "jittlov_dependencies_template.py",
                    fullApiPath + "/jittlov_dependencies.py"])
    subprocess.run(["cp", "jittlov_setup_template.py", fullApiPath + "/jittlov_setup.py"])

    Helpers.update_file(fullApiPath + "/jittlov_dependencies.py",
                        fullApiPath + "/jittlov_dependencies.py",
                        [{"search": "[apiName]_venv", "replace": apiName + "_venv"},
                         {"search": "#![filePath]/", "replace": "#!" + filePath + '/'}])

    Helpers.update_file(fullApiPath + "/jittlov_setup.py", fullApiPath + "/jittlov_setup.py",
                        [{"search": "[apiName]_venv", "replace": apiName + "_venv"},
                         {"search": "#![filePath]/", "replace": "#!" + filePath + '/'}])

    print("New wizard script file created.")

    subprocess.run(["chmod", "+x", fullApiPath + "/jittlov_dependencies.py"])
    subprocess.run(["chmod", "+x", fullApiPath + "/jittlov_setup.py"])

    print("Updated script file to execute.")

    subprocess.run([fullApiPath + "/jittlov_dependencies.py", filePath, apiName])


else:
    print("Invalid path.  Exiting CRUD API Wizard.  Thank you!")
