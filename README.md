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


