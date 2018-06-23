# coding:utf-8
Template_Path = '/u/dwivedi/Downloads/tornado/template'
Static_Path = '/u/dwivedi/Downloads/tornado/static'

summary = """<div class="post-preview">
            <a href="post/3">
              <h2 class="post-title">
                Python basics : Strings in depth
              </h2>
              <h3 class="post-subtitle">
              </h3>
            </a>
            <p class="post-meta">Posted by
              <a href="#">Shishir</a>
              on Jun 23, 2018</p>
          </div>
          <hr>
          """

article = '''<header class="masthead" style="background-image: url('../static/img/python-logo-master.png')">
      <div class="overlay"></div>
      <div class="container">
        <div class="row">
          <div class="col-lg-8 col-md-10 mx-auto">
            <div class="post-heading">
              <h1>Python basics : Strings in depth</h1>
              <h2 class="subheading">Strings are a collection of characters. In python, just like any other data structure, a string is also an object, and comes with its whole lot of in-built properties which we can use to perform various operations.</h2>
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

            <h2 class="section-heading">Declaring a string in Python</h2>
            <p>In Python, a string is a collection of characters enclosed in a single, double or triple quotes. Here are a few examples :</p>
            <pre>
             <code>
             string_1 = "Hello World"
             string_2 = 'Hello World'
             string_3 = """Hello World""
             </code>
             </pre>
             <p>The above 3 expressions does the same job: assign “Hello World” to their respective variables. So why do we have multiple ways of representing a string? It’s simple. So here is the difference:</p>
             <p>1. A string starting with a single quote ends with a single quote. To have a single quote in between the text, it will either have to escape the single quote or start and end with double quote instead. </p>
             <p>2. A string starting with a double quote ends with a double quote. To have a double quote in between the text, it will either have to escape the double quote or start and end with single quote instead.</p>
             <p>3.Triple quotes are used to create multiple-line string.</p>
             
             <pre>
             <code>
             # check how we'll escape single quote in b/w text
             a = '\'Hi\' said aforlalgo'  # will store "'Hi' said aforlago"
             # check how we'll escape single quote in b/w text
             a = "\"Hi\" said aforalgo"  # will store '"Hi" said aforlago'
             a = """Hello World
             This is a multi-line string"""  # will store 'Hello World\nThis is a multi-line string'
             </code>
             </pre>
             <p>In-built string properties</p>
             <p><b>Concatenation :</b> To add 2 strings, you can use + operator or use the in-built add function
             <pre>
             <code>
                a = "Hello "
                b = "World"
                c = a + b  # concatenation using + operator
                d = a.__add__(b)  # concatenation using in-built function
                print c == d  # returns True
                </code>
                </pre>
            <p><b>Updating or deleting a string:</b> Strings are immutable i.e. you can’t update a string. However, you can do this:</p>
            <pre>
            <code>
                a = "Hello "
                b = "World"
                a = a + b  # a = "Hello World"
                </code>
                </pre>
                
                <p>In the above lines of code, first we assign “Hello ” to <b>a</b>, then we assign “World” to <b>b</b>, then <b>we assign the sum of a and b to a new variable named ‘a’</b>. Thus we are assigning the newly created string to the variable. Please note that strings are immutable, variables can point to whatever they want.</p>
                <p>1.Formatting a string: inserting value of variables</p>
                <p>2. <b>Length:</b> To find the number of characters in a string, you can use the in-built function len</p>
                <pre>
                <code>
                    a = "Hello World"
                    b = len(a)  # b = 11
                    </code>
                    </pre>
    <p><b>Indexing a string(accessing characters from string):</b> In Python, characters in a string are indexed and can be accessed by specifying their particular index. The indexing starts from 0. To find the index of first occurrence of any character, Python has an in-built function <b>index</b>. It raises <b>ValueError</b> if the particular character that you are looking for is not present in the string</p>
    <pre>
    <code>
        a = "Hello World"
        a.index("H")  # returns 0
        a.index("e")  # returns 1
        a.index("o")  # returns 4
        a.index("d")  # returns 10
        a.index("s")  # raises ValueError
        # You can also access characters at a particular index 
        print(a[0])  # prints H
        print(a[1])  # prints e
        print(a[10]  # prints d
        print(a[11])  # raises IndexError
        </code>
        </pre>
 <p><b>Iterating through strings:</b> Python allows you to traverse over the characters of a string</p>
 <pre>
 <code>
        my_string = "Hello World"
        for character in my_string:
            print(character)
        </code>
        </pre>
    
<p><b>Slicing:</b> To access substrings, use the square brackets for slicing along with the indices to obtain your substring. For example −</p>

    <pre>
    <code>
        my_string = "Hello World"
        hello = my_string[:5]  # saves 'Hello' to the variable hello
        </code>
        </pre>
<p><b>Finding the index of particular character:</b> Use find to get the index of first occurrence of character from the left, use find to get the index of the first occurrence of the character from the right</p>
<pre>
<code>
    my_string = "Hello World"
    my_string.find("l")  # returns 2
    # get the index of the first occurrence from the right
    my_string.rfind("l")  # returns 9
    # returns -1 if the character is not found
    my_string.find("s")  # returns -1
    </pre>
    </code>
<p><b>Convert to upper and lowercase</b></p>
<pre>
</code>
        my_string = "hello world"
        # convert all characters into uppercase
        my_string.upper()  # returns HELLO WORLD 
        # convert all characters into lowercase
        my_string.lower()  # returns hello world
        # convert string into title case
        my_string.title()  # returns Hello World
        # capitalize string
        my_string.capitalize()  # returns Hello world
</code>
</pre>

<p><b>Check if string is numeric, alpha, alphanumeric, isupper or islower:</b></p>
<pre>
<code>
    my_string = "Hello world"
    #check if all characters are alphabetic
    my_string.isaplha()  # True
    # check if all characters are alphanumeric
    my_string.isalnum()  # True
    # check if all characters are digits
    my_string.isdigit()  # False
    # check if string is in uppercase
    my_string.isupper()  # False
    # check if string is in lowercase
    my_string.islower()  # False
    </code>
    </pre>
    
    <p><b>Strip characters from the given string:</b></p>
    <pre>
    <code>
        my_string = "   hello world     "
        # normal strip (strips character from right)
        my_string.strip()  # returns '  hello world'
        my_string.lstrip()  # returns '  hello world'
        # strip characters from left
        my_string.lstrip()  # returns 'hello world     '

        # strip particular characters
        my_string = "hello!!!!"
        my_string.strip("!")  # returns 'hello'
        </code>
        </pre>
    <p><b>Check if a string starts with or ends with given string:</b></p>
    <pre>
    <code>
        my_string = "hello world"
        my_string.startswith("hello")  # returns True
        my_string.startswith("world"  # returns False
        my_string.endswith("hello")  # returns False
        my_string.endswith("world"  # returns True
        </code>
        </pre>
    <p>These are some of many in-built functions that Python come with. You can check all the functions by using the python’s help function</p>
    <pre>
    <code>
    help(str)
    </code>
    </pre>
             
      </div>
    </article>


    <hr>
'''''