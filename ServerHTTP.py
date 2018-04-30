import tornado.web
import tornado.ioloop


class Main(tornado.web.RequestHandler):
    def get(self):
        self.redirect("https://34.217.175.167:8888")


handler=[
    (r"/",Main)
]

application=tornado.web.Application(handler)

if __name__ == '__main__':
    application.listen(8080)
    print("Listening HTTP server at 8080")
    tornado.ioloop.IOLoop.instance().start()
    