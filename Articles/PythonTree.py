# coding:utf-8
Template_Path = '/u/dwivedi/Downloads/tornado/template'
Static_Path = '/u/dwivedi/Downloads/tornado/static'

summary = """<div class="post-preview">
            <a href="post/4">
              <h2 class="post-title">
               Learning Tree Data Structure(Basics)
              </h2>
              <h3 class="post-subtitle">
              </h3>
            </a>
            <p class="post-meta">Posted by
              <a href="#">Shishir</a>
              on Aug 22, 2018</p>
          </div>
          <hr>
          """

article = '''<header class="masthead" style="background-image: url('../static/img/TreeDataStructure.jpeg')">
      <div class="overlay"></div>
      <div class="container">
        <div class="row">
          <div class="col-lg-8 col-md-10 mx-auto">
            <div class="post-heading">
              <h1>Learning Tree Data Structure(Basics)</h1>
              <span class="meta">Posted by
                <a href="#">Shishir</a>
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
          <p>When we first start learning to code, it’s common to learn arrays as the “main data structure”. Eventually, we learn hash table too. If you are pursuing a Computer Science degree, you have a Data Structure class, and you also learn Linked Lists, Queues, and Stacks. Those data structures are all called “linear” data structures because they all have a logical start and a logical end.

When we start learning trees and graphs, it gets really confusing. We don’t store data in a linear way. Both data structures have a specific way to store data.

This post is an attempt to we better understand the Tree Data Structure and clarify any doubts about it. We will learn about what is a tree, examples of it, its terminology, how it works, and a technical implementation (a.k.a code!)

Let’s start this learning journey! :)</p>

 <h2 class="section-heading">Definition</h2>
 <p>As we said early when we start programming, it is common to understand better the linear data structures than data structures like trees and graphs.

Trees are well known as a non-linear Data Structure. It doesn’t store data in a linear way. It organizes data in a hierarchical way.</p>

  <h2 class="section-heading">Let’s dive in real life examples</h2>
  <p>What do I mean about hierarchical way? Imagine a family tree with all generation relationship: grandparents, parents, children, siblings, etc. We commonly organize it in a hierarchical way</p>
  <a href="#">
              <img class="img-fluid" src="../static/img/MyFamilyTree.jpeg" alt="">
  </a>
  This is my Tree Family. Tossico, Akikazu, Hitomi and Takemi are all my grandparents. Toshiaki and Juliana are my parents. TK, Yuji, Bruno and Kaio are the children of my parents (Me and my brothers, duh!)

Company hierarchy is another example.

<a href="#">
              <img class="img-fluid" src="../static/img/CompanyTree.jpeg" alt="">
  </a>
<p>If you are a web developer, you probably understand how the DOM (Document Object Model) works. It works as a tree.</p>

<a href="#">
              <img class="img-fluid" src="../static/img/DOM.jpeg" alt="">
  </a>
  <p>The html tag has all other tags. So we have a head tag and a body tag. Those tags contains specific elements. The head tag has meta and title tags. And the body tag has all elements that show in the UI like h1, a, li, etc.</p>

  <h2 class="section-heading">A technical definition and its terminology</h2>
  <p>So a Tree is a collection of entities called node connected by edges. Each node contains a value or data and it can also have a child node (or not).


The first node of the tree is called the root. If this root node is connected by another node, the root is a parent node and the connected node is a child.</p>
<a href="#">
              <img class="img-fluid" src="../static/img/RootNode.jpeg" alt="">
  </a>
  <p> Tree nodes are all connected by links called edges. It’s an important part of trees, because it’s how we manage relationship between nodes.</p>

  <a href="#">
              <img class="img-fluid" src="../static/img/Edges.jpeg" alt="">
  </a>
  <p>Leafs are the “last nodes" from the tree. Or nodes without children. Like real trees. We have the root, branches, and finally the leafs.</p>

    <a href="#">
              <img class="img-fluid" src="../static/img/Leaf.jpeg" alt="">
  </a>        
  
  <p>Other important concepts to understand are height and depth.

The height of a tree is the length of the longest path to a leaf.

The depth of a node is the length of the path to its root</p>
 <a href="#">
              <img class="img-fluid" src="../static/img/HeightTree.jpeg" alt="">
  </a>
    
  <h2 class="section-heading">Binary Tree</h2>
  <p>Now we will discuss a specific type of tree. We call it Binary Tree.</p>
  <blockquote class="blockquote">“In computer science, a binary tree is a tree data structure in which each node has at most two children, which are referred to as the left child and the right child.” </blockquote>
  <p>So let’s see an example of Binary Tree.</p>

  <h2 class="section-heading">Binary Tree: Coding Mode On</h2>
  <p>The first thing we need to have in mind when implement a Binary Tree is: it is a collection of nodes, and each node has three attributes: value, left_child, and right_child.

How do we implement a simple Binary Tree initializing with these three properties? Let’s see.</p>
<pre>
<code> 
    class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None
  </code>
  </pre>
  <p>So here it is. Our Binary Tree class. When we instantiate an object, we pass the value (the node‘s data) as a parameter. And look at the left_child and the right_child. Both are set to None. Why? Because when we create our node, it doesn’t have any children. We just have the node data.

Testing it:</p>
<pre>
<code>
        tree = BinaryTree('a')
        print(tree.value) # a
        print(tree.left_child) # None
        print(tree.right_child) # None
        </code>
        </pre>
  <p>That’s it. We can pass the string “a“ as the value to our Binary Tree node. If we print the value, left_child, and right_child, we can see the values.

Let’s go to the insertion part! What do we need to do here? We will implement a method to insert a new node to the right and to the left. What’s the rule?</p>
<p>
<ul>
 <li>Current node doesn’t have a left child, we just create a new node and set it to the current node’s left_child.</li>
 <li>If it does have the left child, we create a new node and put it in the current left child‘s place. Allocate this left child node to the new node‘s left child</li>
 </ul>
 </p>
 <p>Should we draw it? :)</p>

  <a href="#">
              <img class="img-fluid" src="../static/img/DrawTree.jpeg" alt="">
            
  </a>
  <p>Let’s see the code.</p>
  <pre>
  <code>
            def insert_left(self, value):
              if self.left_child == None:
                self.left_child = BinaryTree(value)
            else:
              new_node = BinaryTree(value)
              new_node.left_child = self.left_child
              self.left_child = new_node

    </code>
    </pre>
    <p>Again, if the current node doesn’t have a left child, we just create a new node and set it to the current node’s left_child. Else we create a new node and put it in the current left child‘s place. Allocate this left child node to the new node‘s left child.</p>
    <p>And we do the same thing to to insert a right child node.</p>
    <pre>
    <code>
            def insert_right(self, value):
              if self.right_child == None:
              self.right_child = BinaryTree(value)
              else:
                new_node = BinaryTree(value)
                new_node.right_child = self.right_child
                self.right_child = new_node

                </code>
                </pre>
      
     <a href="#">
              <img class="img-fluid" src="../static/img/LeftRight.jpeg" alt="">
            
  </a>
  
  <p>
  <ul>
  <li>So here the a node will be the root of our binary Tree.</li>
  <li>a left child is b node.</li>
  <li>a right child is c node.</li>
  <li>b right child is d node (b node doesn’t have a left child).</li>
  <li>c left child is e node.</li>
  <li>c right child is f node.</li>
  <li>Both e and f nodes don’t have children.</li>
  </ul>
  </p>
  <p>So here it is:</p>
  <pre>
  <code>
              a_node = BinaryTree('a')
              a_node.insert_left('b')
              a_node.insert_right('c')

              b_node = a_node.left_child
              b_node.insert_right('d')

              c_node = a_node.right_child
              c_node.insert_left('e')
              c_node.insert_right('f')

              d_node = b_node.right_child
              e_node = c_node.left_child
              f_node = c_node.right_child

              print(a_node.value) # a
              print(b_node.value) # b
              print(c_node.value) # c
              print(d_node.value) # d
              print(e_node.value) # e
              print(f_node.value) # f
</code>
</pre>

    
      </div>
    </article>


    <hr>
'''''