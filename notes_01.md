* Start a django project like this example: ```django-admin startproject superlists .```, that ```.``` is very omportant to put. If the dot(.) ommited
 then two nested folder named as the project name(here superlists) will be created and that is bad.
 * The file structure can llok like this:
 ```bash
 web_site/
├── db.sqlite3
├── functional_test.py
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
* The superlists folder here is intended for stuff that applies to whole project. Like ```settings.py```, this file is used to store global configuration information for the site.

* Very important file is ```manage.py```, it's django's swiss army knife and one thing it can do is run a development server: ```python mange.py runserver``` and in another shell runn ```python functional_test.py``` to run the test.