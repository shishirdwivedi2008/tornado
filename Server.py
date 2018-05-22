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
            self.redirect('http://' + self.request.host, permanent=False)
        
    def get(self):
        self.render("index1.html",items=MongoConnection().getSummary())

setting=dict({
        'debug':True,
       #'static_path':os.path.join(os.getcwd(),'static'), # Disabling it since serving content from nginx
        'template_path':os.path.join(os.getcwd(),'template'),
        'cookie_secret': b'$2b$12$.fHCIiJT8UWFS2DdvMWe6O5JqHu.MKjh.Vl8yBhwmv0to5ARqjWXa',
        'login_url': "/login",
},
)

handler=[
        (r"/",Server),(r"/login.*",Login),(r"/post/([0-9]+)",Post),(r"/about.*",About),(r"/contact.*",Contact),
    (r"/index.*",Index),(r"/post",PostWithoutParam)
 ]

application=tornado.web.Application(handler,**setting)
# Enable this piece of code when what to do HTTPS
#http_server = tornado.httpserver.HTTPServer(application,ssl_options = {
 #   "certfile": os.path.join(os.getcwd(),'host.cert'),
  #  "keyfile": os.path.join(os.getcwd(),'host.key'),
   # })

#HTTP Connection only
http_server = tornado.httpserver.HTTPServer(application)



if __name__ == '__main__':
    http_server.listen(8081)
    #application.listen(8080)
    print("Listening HTTPS on port 8081")
    tornado.ioloop.IOLoop.instance().start()
