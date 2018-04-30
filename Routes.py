import tornado.web
import  tornado.ioloop
import json
from MongoConnection import MongoConnection
class Login(tornado.web.RequestHandler):
    def get(self):
        self.render("login.html")

    def post(self):
        username=self.get_argument("form-username")
        password=self.get_argument("form-password")
        connection=MongoConnection()
        if(connection.checkUserNameAndPassword(username,password)):
            self.set_secure_cookie("admin",self.get_argument("form-username"))
            self.redirect("/post")
        else:
            self.redirect("/index")

class Post(tornado.web.RequestHandler):
    def get(self,post_id):
        self.render("post.html",items=MongoConnection().getArticle(post_id),)




class About(tornado.web.RequestHandler):
    def get(self):
        self.render("about.html")

class Contact(tornado.web.RequestHandler):
    def get(self):
        self.render("contact.html")

class Index(tornado.web.RequestHandler):
    def get(self):
        self.redirect("/")
