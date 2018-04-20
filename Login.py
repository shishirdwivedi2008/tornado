import tornado.web
import  tornado.ioloop
import json

class Login(tornado.web.RequestHandler):
    def get(self):
        self.render("login.html")

    def post(self):
        username=self.get_argument("form-username")
        password=self.get_argument("form-password")
        if(username=="shishirdwivedi2008@gmail.com" and password=="shishir"):
            self.redirect("/post.html")
        else:
            self.redirect("/index.html")

class Post(tornado.web.RequestHandler):
    def get(self):
        self.render("post.html")

class About(tornado.web.RequestHandler):
    def get(self):
        self.render("about.html")

class Contact(tornado.web.RequestHandler):
    def get(self):
        self.render("contact.html")

class Index(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")
