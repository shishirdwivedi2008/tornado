import tornado.web
import  tornado.ioloop
import json

class Login(tornado.web.RequestHandler):
    def get(self):
        self.render("login.html")

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
