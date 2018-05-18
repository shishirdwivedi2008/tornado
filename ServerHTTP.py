import tornado.web
import tornado.ioloop


class Main(tornado.web.RequestHandler):
    def get(self):
        self.redirect("https://AforAlgo.com/")


handler=[
    (r"/",Main)
]

application=tornado.web.Application(handler)

if __name__ == '__main__':
    application.listen(80)
    print("Listening HTTP server at 8080")
    tornado.ioloop.IOLoop.instance().start()
    