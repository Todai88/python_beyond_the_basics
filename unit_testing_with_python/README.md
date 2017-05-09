A repository for my progress through the intermediate course with the same name.

01: Unit Testing With Python - Basic Example Using UnitTest
-----

#### Arrange:
Set up the object to be teted & collaborators. This can either be done
in your `setup` function, or in the test case itself. Use common sense and refactor 
when possible.

#### Act:
Exercise functionality on the object. This would be the function body __after__
you have setup the object you are acting on and __before__ the unit test's assertions.

#### Assert:
Make claims about the object & its collaborators.
As a general rule of thumb you should do one assert per test since one failure 
in a test might make the entire test fail rather than displaying the underlying
successes that might occur later in the function body.

It should, however, be noted that the __assert__ should test what has been done
in the __act__. So if you have this code:

```buildoutcfg
def test_phonebook_adds_names_and_numbers(self):
    # Arrange handled in setup
    self.phonebook.add("Sue", "12345") # Act
    
    self.assertIn("Sue", phonebook.get_names())
    self.assertIn("12345", phonebook.get_numbers())
```

This would be a correct test-case as we are testing the functionality of the
test's __act__. 


#### Clean up:
Release resources, restore to original state. Usually done in the `teardown` method. Not really
necessary for a pure test.


02: Why and When Should You Write Unit Tests?
----
#### Module Outline -> Documenting the Units

Unit Tests work as an executable documentation of what your unit does.
Preferably it should be created in collaboration with other roles in the company or team;
business analysts, QA-testers, other developers or UX developers might have their own
specific requirements or concerns that may need to be implemented.

Sticking to TDD through a project also ensures that a module that has been tested will function
in a way that sticks to your requirements. So before adding new implementation to a module
you run the tests on the module, then you start implementing tests for the new unit and finally
you implement the code for the module. That way you can ensure that you have a good coverage 
when the new code has been implemented. Obviously you run a test over the full function afterwards
too.

#### Designing the Units

Another reason to implement unit tests during your the development is that it helps with design.

Preferably you want a finished architecture that is loosely coupled, meaning that the units
are independently testable. 
It also helps designing the interface of the code you are implementing as you primarily will be
testing the interface of the implementation (you separate your concerns; interface and implementation).

#### Limitations of Unit Testing:

It won't find all errors: Unit Testing will not guarantee that you have 100% correct code.
It doesn't (generally) test security or performance.


#### Testing Last:

Pro: Get code into production early.

Cons: Risks discoevering testability problems and bugs late in the process,

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;you might rush or skip designing tests all together.

#### Testing First:
Building up a testable interface before you start developing and developing
automated tests before actually getting on with the development iteself.

Pro: Makes it less likely that you find your code having bugs during development. The test cases help
you identify what you are building before you are building it.

Cons: You might risk having to rework, refactor tests / code. It might make your code design the
tests instead of the intended other way around.

#### Test Driven Development (TDD):

You let your test code and development code merge. An iterative and incremental approach.

Instead of developing either of the two parts of your development (code and tests) separately
they are handled as one and the same. You might start with a basic test that 
tests your constructor and then you take it from there.