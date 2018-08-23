# coding:utf-8
Template_Path = '/u/dwivedi/Downloads/tornado/template'
Static_Path = '/u/dwivedi/Downloads/tornado/static'

summary = """<div class="post-preview">
            <a href="post/5">
              <h2 class="post-title">
               Learning Tree Data Structure(DFS)
              </h2>
              <h3 class="post-subtitle">
              The DFS algorithm is a recursive algorithm that uses the idea of backtracking. It involves exhaustive searches of all the nodes by going ahead, if possible, else by backtracking
              </h3>
            </a>
            <p class="post-meta">Posted by
              <a href="/about">Shishir</a>
              on Aug 23, 2018</p>
          </div>
          <hr>
          """

article = '''<header class="masthead" style="background-image: url('../static/img/DFS.jpeg')">
      <div class="overlay"></div>
      <div class="container">
        <div class="row">
          <div class="col-lg-8 col-md-10 mx-auto">
            <div class="post-heading">
              <h1>Learning Tree Data Structure(DFS)</h1>
              <span class="meta">Posted by
                <a href="/about">Shishir</a>
                on Jun 23, 2018</span>
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
          <h2 class="section-heading">DFS — Depth-First Search</h2>
          <p>DFS explores a path all the way to a leaf before backtracking and exploring another path. Let’s see an example of this type of traversal.</p>
          <a href="#">
              <img class="img-fluid" src="../static/img/DFS.jpeg" alt="">
            
          </a>
          <p>So the result of this algorithm will be: 1–2–3–4–5–6–7. Why?</p>
          <p>
          <ul><li>We start with the root (1). Print it.</li>
          <li>Go to the left child (2). Print it.</li>
          <li>Go to the left child (3). Print it. (This node doesn’t have any children)</li>
          <li>Backtrack and go the right child (4). Print it. (This node doesn’t have any children)</li>
          <li>Backtrack to the root node and go the right child (5). Print it.</li>
          <li>Go to the left child (6). Print it. (This node doesn’t have any children)</li>
          <li>Backtrack and go the right child (7). Print it. (This node doesn’t have any children)</li>
          <li>Done.</li>
</ul></p>
<p>This is what we call <b>DFS</b> algorithm. Going deep to the leaf and backtrack.</p>

<p>Now that we are familiar with this traversal algorithm, we will understand 3 types of DFS: <code>pre-order</code>, <code>in-order</code>, and <code>post-order</code></p>
<p>
<ul>
<li><p><code>Pre-order</code>: This is exactly what we did above. Print the current node’s value. Go to the left child and print it. Backtrack. Go to the right child and print it</p>
    <pre>
    <code>
               def pre_order(self):
                  print(self.value)

                  if self.left_child:
                    self.left_child.pre_order()

                  if self.right_child:
                      self.right_child.pre_order()

                      </code>
                      </pre>



</li>
<li><p><code>In-order</code>: We go way down to the left child and print it first. Backtrack and print it. And go way down to the right child and print it.</p>
    <a href="#">
              <img class="img-fluid" src="../static/img/Inorder.jpeg" alt="">
            
          </a>
    <p>So the result of the in order algorithm (for this tree example) will be: 3–2–4–1–6–5–7. The left first, the middle second, and the right last.</p>
    <pre>
    <code>
        def in_order(self):
          if self.left_child:
              self.left_child.in_order()

          print(self.value)

        if self.right_child:
            self.right_child.in_order()
            </code>
            </pre>
  <p> 1.Go to the left child and print it. If, and only if, it has a left child.</p>
  <p>2.Print node‘s value</p>
  <p>3.Go to the right child and print it. If, and only if, it has a right child.</p>
  </li>

  <li><p><code>Post-order</code>: We go way down to the left child and print it first. Backtrack. Go way down to the right child. Print it second. Backtrack and print it.</p>
   <a href="#">
              <img class="img-fluid" src="../static/img/Inorder.jpeg" alt="">
            
          </a>
        <p>So the result of the post order algorithm (for this tree example) will be: 3–4–2–6–7–5–1. The left first, the right second, and the middle</p>
        <pre>
        <code>
              def post_order(self):
                if self.left_child:
                  self.left_child.post_order()

                if self.right_child:
                  self.right_child.post_order()

                print(self.value)
                </code>
                </pre>
    <p>1.Go to the left child and print it. If, and only if, it has a left child.</p>
    <p>2.Go to the right child and print it. If, and only if, it has a right child.</p>
    <p>3.Print node‘s value</p>

</li>

</ul>
</p>
         

    
      </div>
    </article>


    <hr>
'''''