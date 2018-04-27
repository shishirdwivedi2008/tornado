from apt_pkg import init
from pymongo import MongoClient
import pymongo
import cgi
import bcrypt
import base64

class MongoConnection:
    salt = b'$2b$12$.fHCIiJT8UWFS2DdvMWe6O'
    client=None
    def __init__(self):
        self.client=MongoClient('mongodb://localhost:27017/')
        
    def checkUserNameAndPassword(self,username,password):
        store=[]
        userHash = bcrypt.hashpw(username.encode("utf-8"), self.salt)
        pwdHash = bcrypt.hashpw(password.encode("utf-8"), self.salt)
        db=self.client.user
        data=db.user.find({'user':username})
        if(data.count()==0):
            return False
        for document in data:
            if(document['userhash']==userHash and document['password']==pwdHash):
                return True
            else:
                return False

    def createUser(self,username,password):
        userHash = bcrypt.hashpw(username.encode("utf-8"), self.salt)
        pwdHash = bcrypt.hashpw(password.encode("utf-8"), self.salt)
        db = self.client.user;
        db = self.client.user;
        user = {"user": username, "userhash": userHash, "password": pwdHash, "role": "admin"}
        db.user.insert_one(user).inserted_id

    def getSummary(self):
        summary = []
        db = self.client.summary;
        data = db.summary.find().sort('post_id', pymongo.DESCENDING).limit(3)
        for document in data:
            summary.append(base64.b64decode(document['summary']))

        return summary


    def getArticle(self,id ):
        article_data=[]
        db=self.client.article
        data=db.article.find({'post_id':id})
        for document in data:
             article_data.append(base64.b64decode(document['article']))

        return article_data



if __name__ == '__main__':
    con=MongoConnection()
    print(con.getArticle(1))         

                               

