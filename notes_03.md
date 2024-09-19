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