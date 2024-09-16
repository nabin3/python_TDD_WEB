# What is an function test?
Tests that use Selenium let us drive a real web browser, so they really let us see how the application functions 
from the user’s point of view. That’s why they’re called functional tests. This means that an FT can be a sort of specification for your application. It tends to track what you might call a User Story, and follows how the user might work with a particular feature and how the app should respond to them.
Functional Test = Acceptance Test=End-To-End Test = black box Test = closed box Test

# How to write one functional_test?
FT should have human readable story we can follow. We make it explicit using comments that accompany the test code. When creating a new FT, we can write 
the comments first, to capture the key points of the User Story. Being human-readable, you could even share them with nonprogrammers, as a way of 
 discussing the requirements and features of your app. 
    And one of the thing we often talk about is minimum viable app, what is the simplest thing we can build that is still useful?
* When our FT fails and it said AssertionError for (assert 'To-Do' in browser.title), we don't know what browser title was and the opened browser doesn't close automaticallky. Solution is
```bash
assert 'To-Do' in browser.title, f"Browser title was {browser.title}"
# Here fir st statement is checking if Assertionerror thrown, if yes then the f-string will be printed. here **,** is used between two statement to separate them from each other
``` 
 we could also use a try/finally to clean up the old firefox window.
But these sorts of problems are quite common in testing, and there are some ready-made solutions for us in the standard library’s **unittest** module.

* Tests are organised in classes, which inherit from ```unittest.TestCase```. 

* Any method whose name start with ```test_``` is a test method, and will be run by the test runner. We can have more than one test_method per class.

* ```setUp and tearDown``` are special methods, run at start and end of each test_method respectively.

* unittest provides lots of helper functions like assertIn to make
test assertions, like assertEqual, assertTrue, assertFalse, and so
on.

* self.fail just fails no matter what, producing the error message given.
We can use it as a reminder to finish the test.

* we call ```unittest.main()```, which launches the unittest test runner, which will automatically find test classes and methods in the file and run them.