from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError
from Helpers import Helpers


class MongoHelpers:

    @staticmethod
    def validate_mongo_db(database_url):
        return_value = False
        try:
            client = MongoClient(database_url, serverSelectionTimeoutMS=1)
            client.server_info()
            return_value = True
        except (ServerSelectionTimeoutError, ValueError):
            print("The Mongo Database at path '" + database_url + "' could not be reached.")

        return return_value

    @staticmethod
    def confirm_mongo_db():
        while True:
            database_url = Helpers.confirm_choice("Please enter the URL for the Mongo database: [ex: 'mongodb://'] ")
            confirm = MongoHelpers.validate_mongo_db(database_url)
            if confirm:
                return database_url

    @staticmethod
    def validate_mongo_db_name(database_url, database_name):
        return_value = False
        client = MongoClient(database_url, serverSelectionTimeoutMS=1)
        db_names = client.list_database_names()

        confirm_message = "The database name '" + database_name
        if database_name in db_names:
            confirm_message = confirm_message + "' already exists.  Would you like to use it? [y/n] "
        else:
            confirm_message = confirm_message + "' does not exist.  Would you like to create it? [y/n] "

        confirm = input(confirm_message)

        if confirm == 'Y' or confirm == 'y':
            return_value = True

        return return_value

    @staticmethod
    def confirm_mongo_db_name(database_url):
        while True:
            database_name = Helpers.confirm_choice("Please enter the name of the database: ")
            confirm = MongoHelpers.validate_mongo_db_name(database_url, database_name)
            if confirm:
                return database_name

    @staticmethod
    def validate_mongo_collection_name(database_url, database_name, collection_name):
        return_value = False
        client = MongoClient(database_url, serverSelectionTimeoutMS=1)
        db_names = client.list_database_names()
        confirm_message = "The collection name '" + collection_name
        value_set = False

        if database_name in db_names:

            db = client[database_name]

            collection_names = db.list_collection_names()

            if collection_name in collection_names:
                confirm_message = confirm_message + "' already exists.  Would you like to use it? [y/n] "
                value_set = True

        if not value_set:
            confirm_message = confirm_message + "' does not exist.  Would you like to create it? [y/n] "

        confirm = input(confirm_message)

        if confirm == 'Y' or confirm == 'y':
            return_value = True

        return return_value

    @staticmethod
    def confirm_mongo_collection_name(database_url, database_name):
        while True:
            collection_name = Helpers.confirm_choice("Please enter the name of the collection: ")
            confirm = MongoHelpers.validate_mongo_collection_name(database_url, database_name, collection_name)
            if confirm:
                return collection_name
