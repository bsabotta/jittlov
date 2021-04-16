from pymongo import MongoClient
from bson.objectid import ObjectId

from [apiName].MongoApiConfig import MongoApiConfig


class MongoApi:
    def __init__(self):
        self.client = MongoClient(MongoApiConfig.mongo_url())
        database = MongoApiConfig.mongo_database()
        collection = MongoApiConfig.mongo_collection()

        cursor = self.client[database]
        self.collection = cursor[collection]

    def read(self):
        documents = self.collection.find()
        output = [{item: data[item] for item in data if item != '_id'} for data in documents]
        return output

    def read_by_id(self, data):
        print(data)
        documents = self.collection.find({"_id": ObjectId(data)})
        output = [{item: data[item] for item in data if item != '_id'} for data in documents]
        return output

    def write(self, data):
        new_document = data
        response = self.collection.insert_one(new_document)
        output = {'Status': 'Successfully Inserted', 'Document_ID': str(response.inserted_id)}
        return output

    def update(self, obj_id, data):
        updated_data = {"$set": data}
        response = self.collection.update_one({"_id": ObjectId(obj_id)}, updated_data)
        output = {'Status': 'Successfully Updated' if response.modified_count > 0 else "Nothing was updated."}
        return output

    def delete(self, data):
        response = self.collection.delete_one({"_id": ObjectId(data)})
        output = {'Status': 'Successfully Deleted' if response.deleted_count > 0 else "Document not found."}
        return output
