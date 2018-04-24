from apt_pkg import init
from pymongo import MongoClient

import bcrypt

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



if __name__ == '__main__':
    con=MongoConnection()
    con.checkUserNameAndPassword("SomeRandomCookieSecret","djkd")



