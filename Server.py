import tornado.web
import tornado.ioloop
import Settings
import os
from Login import *

class Server(tornado.web.RequestHandler):
    def prepare(self):
        if self.request.protocol == 'http':
            self.redirect('https://' + self.request.host, permanent=False)
        
    def get(self):
        self.render("index.html")

setting=dict({
        'debug':True,
        'static_path':os.path.join(os.getcwd(),'static'),
        'template_path':os.path.join(os.getcwd(),'template')
},
    
)

handler=[
        (r"/",Server),(r"/login.*",Login),(r"/post.*",Post),(r"/about.*",About),(r"/contact.*",Contact),
    (r"/index.*",Index)
 ]

application=tornado.web.Application(handler,**setting)

http_server = tornado.httpserver.HTTPServer(application,ssl_options = {
    "certfile": os.path.join(os.getcwd(),'host.cert'),
    "keyfile": os.path.join(os.getcwd(),'host.key'),
    })


if __name__ == '__main__':
    http_server.listen(8888)
    #application.listen(8080)
    print("Listening HTTPS on port 8888")
    tornado.ioloop.IOLoop.instance().start()
