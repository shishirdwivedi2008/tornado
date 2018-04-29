Template_Path='/u/dwivedi/Downloads/tornado/template'
Static_Path='/u/dwivedi/Downloads/tornado/static'

summary="""<div class="post-preview">
            <a href="post/1">
              <h2 class="post-title">
                How to start working with Lambda Expressions in Java
              </h2>
            </a>
            <p class="post-meta">Posted by
              <a href="#">Shishir</a>
              on April 27, 2018</p>
          </div>
          <hr>
          """


article='''<header class="masthead" style="background-image: url('../static/img/lambda.jpg')">
      <div class="overlay"></div>
      <div class="container">
        <div class="row">
          <div class="col-lg-8 col-md-10 mx-auto">
            <div class="post-heading">
              <h1>How to start working with Lambda Expressions in Java</h1>
              <h2 class="subheading"></h2>
              <span class="meta">Posted by
                <a href="#">Shishir</a>
                on August 27, 2018</span>
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
            
           <p>Before Lambda expressions support was added by JDK 8, I’d only used examples of them in languages like C# and C++.</p>
            <p>Once this feature was added to Java, I started looking into them a bit closer.</p>
            <p>The addition of lambda expressions adds syntax elements that increase the expressive power of Java. In this article, I want to focus on foundational concepts you need to get familiar with so you can start adding lambda expressions to your code today.</p>
            
            
            <h2 class="section-heading">Quick Introduction</h2>
            
            <p>Lambda expressions take advantage of parallel process capabilities of multi-core environments as seen with the support of pipeline operations on data in the Stream API.</p>
            <p>They are anonymous methods (methods without names) used to implement a method defined by a functional interface. It’s important know what a functional interface is before getting your hands dirty with lambda expressions.</p>
            <h2 class="section-heading">Functional interface</h2>
            </p>A functional interface is an interface that contains one and only one abstract method.</p>
            <p>If you take a look at the definition of the Java standard <b>Runnable interface</b>, you will notice how it falls into the definition of functional interface because it only defines one method: <code>run()</code>.</p>
            <p>In the code sample below, the method computeName is implicitly abstract and is the only method defined, making MyName a functional interface.</p>
            <p><pre>interface MyName{
            String computeName(String str);
            }</pre>
            </p>
            
            <h2 class="section-heading">The Arrow Operator</h2>
            <p>Lambda expressions introduce the new arrow operator <code>-> </code>into Java. It divides the lambda expressions in two parts:</p>
            <p><pre>(n) -> n*n</pre></p>
            
            <p>The left side specifies the parameters required by the expression, which could also be empty if no parameters are required.</p>
            <p>The right side is the lambda body which specifies the actions of the lambda expression. It might be helpful to think about this operator as “becomes”. For example, “n becomes n*n”, or “n becomes n squared”.</p>
            <p>With functional interface and arrow operator concepts in mind, you can put together a simple lambda expression:</p>
            <p>
            <pre>interface NumericTest {
	                boolean computeTest(int n); 
                }
                public static void main(String args[]) {
	                NumericTest isEven = (n) -> (n % 2) == 0;
	                NumericTest isNegative = (n) -> (n < 0);

	                // Output: false
	                System.out.println(isEven.computeTest(5));

	                // Output: true
	                System.out.println(isNegative.computeTest(-5));
                }
                </pre>
                </p>
            <p>
            <pre>
                     interface MyGreeting {
	                    String processName(String str);
                }

            public static void main(String args[]) {
	            MyGreeting morningGreeting = (str) -> "Good Morning " + str + "!";
	            MyGreeting eveningGreeting = (str) -> "Good Evening " + str + "!";
  
  	            // Output: Good Morning Luis! 
	            System.out.println(morningGreeting.processName("Luis"));
	
	            // Output: Good Evening Jessica!
	            System.out.println(eveningGreeting.processName("Jessica"));	
            }
</pre>
</p>

<p>
The variables <code>morningGreeting</code> and <code>eveningGreeting</code>, lines 6 and 7 in the sample above, make a reference to MyGreeting interface and define different greeting expressions.

When writing a lambda expression, it is also possible to explicitly specify the type of the parameter in the expression like this:

</p>
<p>
<pre>
        interface MyString {
	        String myStringFunction(String str);
        }

        public static void main (String args[]) {
	        // Block lambda to reverse string
	        MyString reverseStr = (str) -> {
		    String result = "";
		
		    for(int i = str.length()-1; i >= 0; i--)
			    result += str.charAt(i);
		
		    return result;
	    };

	        // Output: omeD adbmaL
	        System.out.println(reverseStr.myStringFunction("Lambda Demo")); 
        }
</pre>
</p>

<h2 class="section-heading">Block Lambda Expression</h2>
<p>So far, I have covered samples of single expression lambdas. There is another type of expression used when the code on the right side of the arrow operator contains more than one statement known as block lambdas:<p>
<p> <pre>interface MyString {
	String myStringFunction(String str);
}

public static void main (String args[]) {
	// Block lambda to reverse string
	MyString reverseStr = (str) -> {
		String result = "";
		
		for(int i = str.length()-1; i >= 0; i--)
			result += str.charAt(i);
		
		return result;
	};

	// Output: omeD adbmaL
	System.out.println(reverseStr.myStringFunction("Lambda Demo")); 
}
</pre></p>

          <h2 class="section-heading">Generic Functional Interfaces</h2>   
          <p>A lambda expression cannot be generic. But the functional interface associated with a lambda expression can. It is possible to write one generic interface and handle different return types like this</p>
          <p>
          <pre>
          interface MyGeneric {
	T compute(T t);
}

public static void main(String args[]){

	// String version of MyGenericInteface
	MyGeneric<String> reverse = (str) -> {
		String result = "";
		
		for(int i = str.length()-1; i >= 0; i--)
			result += str.charAt(i);
		
		return result;
	};

	// Integer version of MyGeneric
	MyGeneric<Integer> factorial = (Integer i) -> {
		int result = 1;
		int n = 5;
		
		for(int i=1; i <= n; i++)
			result = i * result;
		
		return result;
	};

	// Output: omeD adbmaL
	System.out.println(reverse.compute("Lambda Demo")); 

	// Output: 120
	System.out.println(factorial.compute(5)); 

}
</pre>
</p>
  
  <h2 class="section-heading">Lambda Expressions as arguments</h2>
  <p>One common use of lambdas is to pass them as arguments.</p>
  <p>They can be used in any piece of code that provides a target type. I find this exciting, as it lets me pass executable code as arguments to methods.</p>
  <p>To pass lambda expressions as parameters, just make sure the functional interface type is compatible with the required parameter.</p>
  <p>
  <pre>
  interface MyString {
	String myStringFunction(String str);
}

public static String reverseStr(MyString reverse, String str){
  return reverse.myStringFunction(str);
}

public static void main (String args[]) {
	// Block lambda to reverse string
	MyString reverse = (str) -> {
		String result = "";
		
		for(int i = str.length()-1; i >= 0; i--)
			result += str.charAt(i);
		
		return result;
	};

	// Output: omeD adbmaL
	System.out.println(reverseStr(reverse, "Lambda Demo")); 
}

</pre>
</p>

<p>These concepts will give you a good foundation to start working with lambda expressions. Take a look at your code and see where you can increase the expressive power of Java.</p>
            
            

          </div>
        </div>
      </div>
    </article>

    <hr>
'''