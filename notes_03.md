# Testing a simple home page with unit tests:

## First Django app, and our first unit test:
Django encourages us to structure our code into apps, the point is that one project can have many apps, we can use third-party apps developed by other people or reuse our own apps from different project. 

* To start an app we dol like this ```python manage.py startapp app_name```.   This will create a folder which name will be given app name. ```python manage.py startapp lists``` have created an folder name lists.
```bash
.
├── db.sqlite3
├── functional_test.py
├── lists
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── manage.py
└── superlists
    ├── asgi.py
    ├── __init__.py
    ├── __pycache__
    │   ├── __init__.cpython-312.pyc
    │   ├── settings.cpython-312.pyc
    │   ├── urls.cpython-312.pyc
    │   └── wsgi.cpython-312.pyc
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

## Difference between functinal test and unittest:
functional tests test the application from the outside, from the user’s point of view. Unit tests test the application from the inside, from the  
programmer’s point of view. 

## Applying both functionaltest and unittesta in our TDD:
1. We will write functional test.
2. One we have functional test that fails, we will think about how to write code that can get it to pass(or at least to get past its current faliure). We now write unittests to define how we want our code to behave.
3. Once we have failing unittests, we write the smallest amount of application code we can, just enough to get unittest to pass. We may iterate between steps 2 and 3 a few times, until we think the functional test will get a little further.
4. Now we rerun our functional tests and see if they pass, or get a little further. That may prompt us to write some new unit tests, and some new code, and so on.
5. Once we’re comfortable that the core functionality works end-to-end, we can extend out to cover more permutations and edge cases, using just unit tests now.

Functional tests should help us to build an application that actually works, and guarantee we never accidentally break it. Unit tests should help us to write code that’s clean and bug free.

### FTs vs Unit Tests:
        FTs                     |         Unit Tests
One test per feature/user story | Many tests per feature.
Test from user's point of view  | Test from programmer's poin of view.
Can test the UI "really" works  | Test the internals, individual functions or classes.

## Unit Testing in Django:
We open up ```tests.py``` file located in app folder in our case lists. Here we imported ```TestCase``` from ```djando.test```. This TestCase is an augmented version of unittest with some django specific features.
    Where we run functional test explicitly, unittest we define here in ```tests.py``` will automatically run by automated test runner.
With this command ```python manage.py test```

## Django's MVC, URLs amd view functions:
Django is structured along a classic Model-View-Controller(MVC) pattern. Well, broadly.
It definitely does have models, but what Django calls views are really controllers, and the view part is actually provided by the templates,

Irrespective of any of that, as with any web server, Django’s main job is to decide what to do when a user asks for a particular URL on our site.
Django’s workflow goes something like this:

1. An HTTP request comes in for a particular URL.
2. Django uses some rules to decide which view function should deal with
the request (this is referred to as resolving the URL).
3. The view function processes the request and returns an HTTP response.

## The Unit-Test/Code Cycle:
1. In the terminal, run the unit tests and see how they fail.
2. In the editor, make a minimal code change to address the current test failure.
And repeat!
The more nervous we are about getting our code right, the smaller and more
minimal we make each code change—​the idea is to be absolutely sure that each
bit of code is justified by a test.

## Django Test Client:
* We can access the tests client via self.client, which is available on any test that uses django.test.TestCase.It provides methods like .get() which simulate a browser making http requests,and take a URL as their first parameter. We use this instead of manually creating a request object and calling the view function directly

* Django also provides some assertion helpers like assertContains that save us from having to manually extract and decode response content.

## Reading Tracebacks:
1. The first place you look is usually the error itself. Sometimes that’s
all you need to see, and it will let you identify the problem immediately.
But sometimes, it’s not quite self-evident.
2. The next thing to double-check is: which test is failing?
3. Then we look for the place in our test code that kicked off the failure.
We work our way down from the top of the traceback, looking for the
filename of the tests file, to check which test function, and what line of
code, the failure is coming from.
3. In Python 3.11 and later, you can also look out for the string of carets,
which try to tell you exactly where the exception came from.
4.  we look further down for any of our own application code which was involved with the problem.

## urls.py
* Django uses a file called urls.py to map URLs to view functions. This mapping is also called routing. There is a main urls.py for the whole site in the project folder.
* Django strips the leading slash from all urls, so "/url/path/to" becomes "url/path/to" and the base URL is just the empty string, ''.