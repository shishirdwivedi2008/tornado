import tornado.web
import tornado.ioloop
import Settings
import os
from Routes import *
from tornado.log import enable_pretty_logging
enable_pretty_logging()
from datetime import datetime


class Server(tornado.web.RequestHandler):
    def hprepare(self):
        if self.request.protocol == 'http':
            self.redirect('https://' + self.request.host, permanent=False)
        
    def get(self):
        self.render("index1.html",items=MongoConnection().getSummary())

setting=dict({
        'debug':True,
        'static_path':os.path.join(os.getcwd(),'static'),
        'template_path':os.path.join(os.getcwd(),'template'),
        'cookie_secret': b'$2b$12$.fHCIiJT8UWFS2DdvMWe6O5JqHu.MKjh.Vl8yBhwmv0to5ARqjWXa',
        'login_url': "/login",
},
)

handler=[
        (r"/",Server),(r"/login.*",Login),(r"/post/([0-9]+)",Post),(r"/about.*",About),(r"/contact.*",Contact),
    (r"/index.*",Index),(r"/post",Post)
 ]

application=tornado.web.Application(handler,**setting)

http_server = tornado.httpserver.HTTPServer(application,ssl_options = {
    "certfile": os.path.join(os.getcwd(),'host.cert'),
    "keyfile": os.path.join(os.getcwd(),'host.key'),
    })


if __name__ == '__main__':
    http_server.listen(443)
    #application.listen(8080)
    print("Listening HTTPS on port 443")
    tornado.ioloop.IOLoop.instance().start()
