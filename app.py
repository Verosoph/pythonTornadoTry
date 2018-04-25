import tornado.ioloop
import tornado.web

import os.path

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')
       

# This tells tornado where to find the static files
settings = dict( 
    template_path = os.path.join(os.path.dirname(__file__),"template"),
    static_path = os.path.join(os.path.dirname(__file__),"static")
)

# r"/" == root website adress
application = tornado.web.Application([
    (r"/",MainHandler)
],**settings)

#Start the server at a port
port = 8889
if __name__ == "__main__":
    print 'Server is running on port ' +str(port)
    print 'Press ctrl+c to close'
    application.listen(port)
    tornado.ioloop.IOLoop.instance().start()
