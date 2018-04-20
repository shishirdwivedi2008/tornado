import tornado.web
import tornado.ioloop
import Settings
from Login import *
class Server(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

setting={
        'debug':True,
        'static_path':Settings.Static_Path,
        'template_path':Settings.Template_Path
}

handler=[
        (r"/",Server),(r"/login.*",Login),(r"/post.*",Post),(r"/about.*",About),(r"/contact.*",Contact),
    (r"/index.*",Index)
 ]

application=tornado.web.Application(handler,**setting)


if __name__ == '__main__':
    application.listen(8888)
    print("Listening on port 8888")
    tornado.ioloop.IOLoop.instance().start()
