from pymongo import MongoClient
import Settings
from datetime import datetime
import cgi
class PublishArticle:
    client=None
    def __init__(self):
        self.client=MongoClient('mongodb://localhost:27017/')

    def storeArticleInDb(self):
        article={'heading':Settings.heading,'subheading':Settings.subheading,
                 'author':'shishir','time':datetime.now().strftime('%Y-%m-%d %H:%M'),
                 'gist':Settings.gist,
                'article':cgi.escape(Settings.article)

                 }

        db= self.client.article;
        db.article.insert_one(article).inserted_id





if __name__ == '__main__':
    obj=PublishArticle()
    obj.storeArticleInDb();


