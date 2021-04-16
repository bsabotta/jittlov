import os


class Helpers:

    @staticmethod
    def update_file(sent_file_path, output_file_path, find_replace_list):
        with open(sent_file_path, 'r') as file:
            file_data = file.read()

            for current in find_replace_list:
                search_string = current['search']
                replace_string = current['replace']

                file_data = file_data.replace(search_string, replace_string)

        with open(output_file_path, 'w') as file:
            file.write(file_data)

    @staticmethod
    def confirm_choice(question_text):
        while True:
            return_value = input(question_text)
            confirm = input("You entered: " + return_value + ".  Is that correct [y/n]  ")
            if confirm == 'Y' or confirm == 'y':
                return return_value

    @staticmethod
    def get_schema_file_contents():
        schema_file_contents = "from marshmallow import Schema, fields\n\n"
        schema_file_contents = schema_file_contents + "class ModelSchema(Schema):\n"

        # Add the schema by looping until the user wants to stop
        while True:
            confirm = input("Do you want to add a field to the schema? [y/n]: ")
            if confirm != 'y' and confirm != 'Y':
                break
            else:
                field_name = input("Please enter the Name of the field: ")
                field_type = input(
                    "Please enter the type of the field (1 = String, 2 = Number, 3 = Boolean, 4 = DateTime): ")

                if field_type == "1":
                    field_type = "Str"
                    default = "None"
                elif field_type == "2":
                    field_type = "Number"
                    default = "0"
                elif field_type == "3":
                    field_type = "Bool"
                    default = "False"
                elif field_type == "4":
                    field_type = "DateTime"
                    default = "None"
                else:
                    print("Bad data entered.  Schema not written.")
                    break

                schema_file_contents = schema_file_contents + "    " + field_name + " = fields."
                schema_file_contents = schema_file_contents + field_type + "(default=" + default + ")\n"

        return schema_file_contents

    @staticmethod
    def does_directory_exist(path):
        return os.path.isdir(path)

    @staticmethod
    def confirm_path(path):
        return_value = False
        exists = Helpers.does_directory_exist(path)
        if not exists:
            confirm = input("This file path does not exist.  Do you want to create it? [y/n] ")
            if confirm == 'y' or confirm == 'Y':
                os.mkdir(path)
                print(path + " successfully created.")
                return_value = True
            else:
                return return_value
        else:
            return_value = True
        return return_value
