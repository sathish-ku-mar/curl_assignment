from pymongo import MongoClient


class MongoAPI:
    def __init__(self, data):
        self.client = MongoClient("mongodb://localhost:27017/")

        database = data['database']
        collection = data['collection']
        cursor = self.client[database]
        self.collection = cursor[collection]
        self.data = data

    def read_all(self):
        """
        To get all documents
        :return: The collection data
        """
        documents = list(self.collection.find())
        output = {'msg': 'Success', 'data': documents}
        return output

    def read_one(self, data):
        """
        To get one document
        :param data: Get the filter condition
        :return: The queryset response
        """
        response = self.collection.find_one(data)
        output = {'msg': 'Success' if response else "Nothing was there.", 'data': response}
        return output

    def write(self, data):
        """
        To create the document
        :param data: Get the data to store
        :return: The queryset response
        """
        response = self.collection.insert_one(data)
        output = {'msg': 'Successfully Inserted',
                  'Document_ID': str(response.inserted_id)}
        return output

    def update(self, data):
        """
        To update the document
        :param data: Get the data to update
        :return: The queryset response
        """
        filt = data['Filter']
        updated_data = {"$set": data['DataToBeUpdated']}
        response = self.collection.update_one(filt, updated_data)
        output = {'msg': 'Successfully Updated' if response.modified_count > 0 else "Nothing was updated."}
        return output

    def delete(self, data):
        """
        To delete the document
        :param data: Get the filter condition
        :return: The queryset response
        """
        response = self.collection.delete_one(data)
        output = {'msg': 'Successfully Deleted' if response.deleted_count > 0 else "Document not found."}
        return output


if __name__ == '__main__':
    data = {
        "database": "CurlDB",
        "collection": "ticker",
    }
    mongo_obj = MongoAPI(data)
