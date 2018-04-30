from pymongo import MongoClient
import pymongo
import Settings
import html
from datetime import datetime
import base64
class PublishArticle:
    client=None
    def __init__(self):
        self.client=MongoClient('mongodb://localhost:27017/')

    def storeSummaryInDb(self):
        summary_data={'summary':base64.b64encode(Settings.summary.encode("utf-8")),'post_id':int(self.getPostId()+1)}
        db= self.client.summary;
        db.summary.insert_one(summary_data).inserted_id


    def getPostId(self):
        db=self.client.summary;
        data=db.summary.find().sort('post_id',pymongo.DESCENDING).limit(1)
        for document in data:
            return document['post_id']

    def storeArticleInDb(self):
        article_data={'post_id':int(self.getPostId()+1),'article':base64.b64encode(Settings.article.encode("utf-8"))}
        db=self.client.article
        db.article.insert_one(article_data).inserted_id





if __name__ == '__main__':
    obj=PublishArticle()
    #obj.storeSummaryInDb();
    obj.storeArticleInDb()
    print(obj.getPostId())


