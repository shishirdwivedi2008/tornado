#coding:utf-8
Template_Path='/u/dwivedi/Downloads/tornado/template'
Static_Path='/u/dwivedi/Downloads/tornado/static'

summary="""<div class="post-preview">
            <a href="post/2">
              <h2 class="post-title">
                Nginx Tutorial #1: Basic Concepts
              </h2>
              <h3 class="post-subtitle">
            
              </h3>
            </a>
            <p class="post-meta">Posted by
              <a href="#">Shishir</a>
              on May 21, 2018</p>
          </div>
          <hr>
          """


article='''<header class="masthead" style="background-image: url('../static/img/nginx.png')">
      <div class="overlay"></div>
      <div class="container">
        <div class="row">
          <div class="col-lg-8 col-md-10 mx-auto">
            <div class="post-heading">
              <h1>Nginx Tutorial #1: Basic Concepts</h1>
              <h2 class="subheading"></h2>
              <span class="meta">Posted by
                <a href="#">Shishir</a>
                on May 21, 2018</span>
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
            <p>Nginx was originally created as a web server to solve the C10k problem. And as a web server, it can serve your data with blazing speed. But Nginx is so much more than just a web server. You can use it as a reverse proxy, making an easy integration with slower upstream servers (like Unicorn, or Puma). You can distribute your traffic properly (load balancer), stream media, resize your images on the fly, cache content, and much more.

The basic nginx architecture consists of a master process and its workers. The master is supposed to read the configuration file and maintain worker processes, while workers do the actual processing of requests.</p>
            
           
            <h2 class="section-heading">Base commands</h2>
            <p>To start nginx, you simply type:</p>
            <pre><code>[sudo] nginx</code></pre>
            <p>While your nginx instance is running, you can manage it, by sending proper signals:</p>
            <pre><code>[sudo] nginx -s signal</code></pre>
            <p>Available signals:</p>
            <ul>
            <li><code>stop</code>: fast shutdown</li>
            <li><code>quit</code>: graceful shutdown (wait for workers to finish their processes)</li>
            <li><code>reload</code>: reload the configuration file</li>
            <li><code>open</code>: reopening the log files</li>
            </ul>

             <h2 class="section-heading">Directive and Context</h2>
             <p>By default, the nginx configuration file can be found in:</p>
             <ul>
             <li><code>/etc/nginx/nginx.conf,</code></li>
             <li><code>/usr/local/etc/nginx/nginx.conf</code></li>
             <li><code>/usr/local/nginx/conf/nginx.conf</code></li>
             </ul>
             <p>This file consists of:</p>
             <ul>
             <li>directive: the option that contains of name and parameters, it should end with a semicolon</li>
            
             <pre><code>gzip on;</code></pre>
             <li>context: the section where you can declare directives (similar to scope in programming languages)</li>


            <pre><code>worker_processes 2; # directive in global context

                http {              # http context
                    gzip on;        # directive in http context

                    server {          # server context
                        listen 80;      # directive in server context
                        }
                    }
            </code></pre>


              </ul>


        <h2 class="section-heading">Directive types</h2>
        <p>You have to care when using the same directive in multiple contexts, as the inheritance model differs for different directives. There are 3 types of directives, each with its own inheritance model.</p>
        <h2 class="section-heading">Normal</h2>
        <p>It has one value per context. Also, it can be defined only once in the context. Subcontexts can override the parent directive, but this override will be valid only in given subcontext.</p>
        <pre>
        <code>
        gzip on;
        gzip off; # illegal to have 2 normal directives in same context

        server {
        location /downloads {
        gzip off;
        }

        location /assets {
        # gzip is on here
        }
    }
</code></pre>

<h2 class="section-heading">Array</h2>
<p>Adding multiple directives in the same context will add to the values, instead of overwriting them altogether. Defining a directive in a subcontext will override ALL parent values in the given subcontext.

</p>

<pre><code>
error_log /var/log/nginx/error.log;
error_log /var/log/nginx/error_notive.log notice;
error_log /var/log/nginx/error_debug.log debug;

server {
  location /downloads {
    # this will override all the parent directives
    error_log /var/log/nginx/error_downloads.log;
  }
}
</code></pre>

<h2 class="section-heading">Action Directive</h2>
<p>Actions are directives that change things. Their inheritance behaviour will depend on the module.

For example, in the case of the <code>rewrite</code> directive, every matching one will be executed:</p>
<pre><code>
server {
  rewrite ^ /foobar;

  location /foobar {
    rewrite ^ /foo;
    rewrite ^ /bar;
  }
}
</code></pre>
<p>If the user tries to fetch <code>/sample</code>:</p>
<ul>
<li>the server rewrite is executed, rewriting from <code>/sample</code>, to <code>/foobar</code></li>
<li>the location <code>/foobar</code> is matched</li>
<li>the first location rewrite is executed, rewriting from <code>/foobar</code>, to <code>/foo</code></li>
<li>the second location rewrite is executed, rewriting from <code>/foo</code>, to <code>/bar</code></li>
</ul>
<p>his is the different behaviour than the <code>return</code> directive provides:</p>

<pre><code>
server {
  location / {
    return 200;
    return 404;
  }
}
</code></pre>
<p>In the above case, the <code>200</code> status is returned immediately.</p>
<h2 class="section-heading">Processing requests</h2>
<p>Inside nginx, you can specify multiple virtual servers, each described by a <code>server { }</code> context.</p>
<pre><code>

server {
  listen      *:80 default_server;
  server_name aforalgo.co;

  return 200 "Hello from aforalgo.co";
}

server {
  listen      *:80;
  server_name foo.co;

  return 200 "Hello from foo.co";
}

server {
  listen      *:81;
  server_name bar.co;

  return 200 "Hello from bar.co";
}
</code></pre>
<p>This will give nginx some insights on how to handle incoming requests. Nginx will first check the <code>listen</code> directive to test which virtual server is listening on the given IP:port combination. Then, the value from <code>server_name</code> directive is tested against the <code>Host</code> header, which stores domain name of the server.</p>
<p>Nginx will choose the virtual server in the following order:</p>
<ul>
<li>1.Server listing on IP:port, with a matching <code>server_name</code> directive</li>
<l1>2.Server listing on IP:port, with <code>default_server</code> flag</li>
<li>3.Server listing on IP:port, first one defined</li>
<li>4.If there are no matches, refuse the connection.</li>
</ul>
<p>In the example above, this will mean:</p>
<pre><code>
    Request to foo.co:80     => "Hello from foo.co"
    Request to www.foo.co:80 => "Hello from aforalgo.co"
    Request to bar.co:80     => "Hello from aforalgo.co"
    Request to bar.co:81     => "Hello from bar.co"
    Request to foo.co:81     => "Hello from bar.co"
    </code></pre>

<h2 class="section-heading">The <code>server_name</code> directive</h2>
<p>The <code>server_name</code> directive accepts multiple values. It also handles wildcard matching and regular expressions.</p>

<pre><code>
    server_name aforalgo.co www.aforalgo.co; # exact match
    server_name *.aforalgo.co;              # wildcard matching
    server_name aforalgo.*;                 # wildcard matching
    server_name  ~^[0-9]*\.aforalgo\.co$;   # regexp matching
</code></pre>
<p>When there is ambiguity, nginx uses the following order:</p>
<ul>
<li>1.Exact name</li>
<l1>2.Longest wildcard name starting with an asterisk, e.g. “*.example.org”</li>
<l1>3.Longest wildcard name ending with an asterisk, e.g. “mail.*”</li>
<li>4.First matching regular expression (in the order of appearance in the configuration file)</li>
</ul>
<p>Nginx will store 3 hash tables: exact names, wildcards starting with an asterisk, and wildcards ending with an asterisk. If the result is not in any of the tables, regular expressions will be tested sequentially.</p>
<p>It is worth keeping in mind that</p>
<p><pre><code>server_name .aforalgo.co;</code></pre></p>
<p>is an abbreviation of:</p>
<p><pre><code>server_name  aforalgo.co  www.aforalgo.co  *.aforalgo.co;</code></pre></p>

<p>With one difference: .aforalgo.co is stored in the second table, which means that it is a bit slower than explicit declaration.</p>

<p> I will talk more about <code>listen, root,location </code>directive in upcoming tutorial. Keep Reading</p>

      </div>
    </article>


    <hr>
'''''