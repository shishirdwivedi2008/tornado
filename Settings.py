#coding:utf-8
Template_Path='/u/dwivedi/Downloads/tornado/template'
Static_Path='/u/dwivedi/Downloads/tornado/static'

summary="""<div class="post-preview">
            <a href="post/2">
              <h2 class="post-title">
                Building RESTful APIs with Tornado
              </h2>
              <h3 class="post-subtitle">
                The Tornado Web framework makes it easy to write RESTful APIs in Python. How easy? Have a look
              </h3>
            </a>
            <p class="post-meta">Posted by
              <a href="#">Shishir</a>
              on April 30, 2018</p>
          </div>
          <hr>
          """


article='''<header class="masthead" style="background-image: url('../static/img/tornado.png')">
      <div class="overlay"></div>
      <div class="container">
        <div class="row">
          <div class="col-lg-8 col-md-10 mx-auto">
            <div class="post-heading">
              <h1>Building RESTful APIs with Tornado</h1>
              <h2 class="subheading">The Tornado Web framework makes it easy to write RESTful APIs in Python. How easy? Have a look</h2>
              <span class="meta">Posted by
                <a href="#">Shishir</a>
                on August 30, 2018</span>
            </div>
          </div>
        </div>
      </div>
    </header>

    <!-- Post Content -->
    <article>
      <div class="container">
        <div class="row">
          <div class="col-lg-8 col-md-10 mx-auto">
            
           <p>Tornado is a Python Web framework and asynchronous networking library that provides excellent scalability due to its non-blocking network I/O. It also greatly facilitates building a RESTful API quickly. These features are central to Tornado, as it is the open-source version of FriendFeed's Web server. A few weeks ago, Tornado 3.  was released, and it introduced many improvements. In this article, I show how to build a RESTful API with the latest Tornado Web framework and I illustrate how to take advantage of its asynchronous features</p>
           
            
            <h2 class="section-heading">Mapping URL Patterns to Request Handlers</h2>
            
            <p>To get going, download the latest stable version and perform a manual installation or execute an automatic installation with <code>pip</code> by running <code>pip install tornado</code>.</p>
            <p>To build a RESTful API with Tornado, it is necessary to map URL patterns to your subclasses of <code>tornado.web.RequestHandler</code>, which override the methods to handle HTTP requests to the URL. For example, if you want to handle an HTTP GET request with a synchronous operation, you must create a new subclass of <code>tornado.web.RequestHandler</code> and define the <code>get()</code> method. Then, you map the URL pattern in <code>tornado.web.Application</code>.</p>
            <p>Listing One shows a very simple RESTful API that declares two subclasses of <code>tornado.web.RequestHandler</code> that define the get method: <code>VersionHandler</code> and <code>GetGameByIdHandler</code>.</p>
            
            <p><pre>
            <code>
            from datetime import date
            import tornado.escape
            import tornado.ioloop
            import tornado.web
 
            class VersionHandler(tornado.web.RequestHandler):
                def get(self):
                response = { 'version': '3.5.1',
                     'last_build':  date.today().isoformat() }
                self.write(response)
 
            class GetGameByIdHandler(tornado.web.RequestHandler):
                    def get(self, id):
                    response = { 'id': int(id),
                     'name': 'Crazy Game',
                     'release_date': date.today().isoformat() }
                    self.write(response)
 
            application = tornado.web.Application([
            (r"/getgamebyid/([0-9]+)", GetGameByIdHandler),
            (r"/version", VersionHandler)
            ])
 
        if __name__ == "__main__":
            application.listen(8888)
            tornado.ioloop.IOLoop.instance().start()
    </code>
    
    </pre>
    <p>The code is easy to understand. It creates an instance of <code>tornado.web.Application</code> named 
    application with the collection of request handlers that make up the Web application. 
    The code passes a list of tuples to the Application constructor. The list is composed of a regular expression (regexp)
     and a <code>tornado.web.RequestHandler</code> subclass (request_class). 
     The application.listen method builds an HTTP server for the application with the defined rules on the specified port. 
     In this case, the code uses the default 8888 port. Then, the call to <code>tornado.ioloop.IOLoop.instance().start()</code>
      starts the server created with application.listen.</p>
      
      <p>When the Web application receives a request, Tornado iterates over that list and creates an instance of the first 
      <code>tornado.web.RequestHandler</code> subclass whose associated regular expression matches the request path, and then calls the <code>head()</code>, <code>get()</code>, <code>post()</code>, <code>delete()</code>,
       <code>patch()</code>, <code>put()</code> or <code>options()</code> method with the corresponding parameters for the new instance based on the HTTP request</p>
       <p>The simplest case is the <code>VersionHandler.get</code> method, which just receives self as a parameter because the URL pattern doesn't include any parameter. The method creates a response dictionary, 
       then calls the <code>self.write</code> method with response as a parameter. The <code>self.write</code> method writes the received chunk to the output buffer. 
       Because the chunk (response) is a dictionary, <code>self.write</code> writes it as JSON and sets the <code>Content-Type</code> of the response to <code>application/json</code>. The following lines show the example response for GET <code>http://localhost:8888/version</code> and the response headers:</p>
       
       <p>
       <pre>
       <code>
       {"last_build": "2018-04-30", "version": "3.5.1"
        Date: Mon, 30 April 2018 19:45:04 GMT
        Etag: "d733ae69693feb59f735e29bc6b93770afe1684f"
        Content-Type: application/json; charset=UTF-8
        Server: TornadoServer/3.1
        Content-Length: 48</p>

       </code>
       
       </pre>
       
       <p>If you want to send the data with a different Content-Type, you can call the <code>self.set_header</code> with "Content-Type" 
       as the response header name and the desired value for it. You have to call <code>self.set_header</code> after calling <code>self.write</code>
     It sets the Content-Type to text/plain instead of the default application/json in a new version of the <code>VersionHandler</code> class. Tornado encodes all header values as UTF-8.</p>
     
     <p>
     <pre>
     <code>
     class VersionHandler(tornado.web.RequestHandler):
        def get(self):
            self.write("Version: 3.5.1. Last build: " + date.today().isoformat())
            self.set_header("Content-Type", "text/plain")

     </code>
     </pre>
     </p>
       
    <p>
    The following lines show the example response for GET http://localhost:8888/version and the response headers with the new version of the VersionHandler class:
    </p>
    <p>
    <pre>
    <code>
    Server: TornadoServer/3.1
    Content-Type: text/plain
    Etag: "c305b564aa650a7d5ae34901e278664d2dc81f37"
    Content-Length: 38
    Date: Mon, 30 April 2018 02:50:48 GMT

    </code>
    </pre>
    </p>
    
       <p>The <code>GetGameByIdHandler.get</code> method receives two parameters: self and id. The method creates a response
        dictionary that includes the integer value received for the id parameter, then calls the <code>self.write</code> 
        method with response as a parameter. The sample doesn't include any validation for the id parameter in order to keep the code as simple as possible, as I'm focused on the way in which the get method works. 
        I assume you already know how to perform validations in Python. The following lines show the example response for GET <code>http://localhost:8888/getgamebyid/500</code> and the response headers:
        </p>
        <p>
        <pre>
        <code>
        {"release_date": "2018-04-30", "id": 500, "name": "Crazy Game"}
 
        Content-Length: 63
        Server: TornadoServer/3.1
        Content-Type: application/json; charset=UTF-8
        Etag: "489191987742a29dd10c9c8e90c085bd07a22f0e"
        Date: Mon, 30 April 2018 03:17:34 GMT

        </code>
        </pre>
        </p>
        <p>
        If you need to access additional request parameters such as the headers and body data, 
        you can access them through self.request. This variable is a <code>tornado.httpserver.HTTPRequest</code> instance that provides
         all the information about the HTTP request.
         The HTTPRequest class is defined in <code>httpserver.py</code>
        </p>

          </div>
        </div>
      </div>
    </article>

    <hr>
'''''