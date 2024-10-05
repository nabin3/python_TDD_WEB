# common things to know:
* To check if selenium installed successfully or not we run ```python -c "from selenium import webdriver; webdriver.Firefox()"```
* Do nothing until you have a test. Follow Red, Green, Refactor.

# Useful TDD concepts:
## Regression:
When a change unexpectedly breaks some aspect of the application which used to work.

## Unexpected faliure:
When a test fails in a way we weren’t expecting.
This either means that we’ve made a mistake in our tests,
or that the tests have helped us find a regression,
and we need to fix something in our code.

## Triangulation:
Adding a test case with a new specific example for some existing code,
to justify generalising the implementation
(which may be a “cheat” until that point).

## Three strikes and refractor:
A rule of thumb for when to remove duplication from code.
When two pieces of code look very similar,
it often pays to wait until you see a third use case,
so that you’re more sure about what part of the code really is the common,
re-usable part to refactor out.

## The scratcpad ro-do list:
A place to write down things that occur to us as we’re coding,
so that we can finish up what we’re doing and come back to them later.

## If functional_test behave wired:
If something strange is going on with your FTs,it’s always worth trying to upgrade Selenium.
### Story:
I found the FTs hung when I tried to run them. It turns out that Firefox had auto-updated itself overnight,
and my versions of Selenium and Geckodriver needed upgrading too. A quick visit to the geckodriver releases page
confirmed there was a new version out.So a few downloads and upgrades were in order:
* A quick pip install --upgrade selenium first.
* Then a quick download of the new geckodriver.
* I saved a backup copy of the old one somewhere, and put the new one in its place somewhere on the PATH.
* And a quick check with geckodriver --version confirms the new one was ready to go.
The FTs were then back to running the way I expected them to.

## traling slash(/):
The convention I’m using is that URLs without a trailing slash are “action” URLs which modify the database.





