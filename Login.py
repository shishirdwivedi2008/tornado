import tornado.web
import  tornado.ioloop
import json

class Login(tornado.web.RequestHandler):
    def get(self):
        self.render("login.html")