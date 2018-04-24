from pymongo import MongoClient

class MongoConnection:
    def getConnection(self):
        client = MongoClient('mongodb://localhost:27017/')
        db = client.test_database
        print(db)


