A repository for my snippets from the PluralSight course with the same name


01 Organizing Larger Programs:
------
#### Overview:
Module covered the fundamentals on how to use the `sys` library
and how to set up modules.

#### General thoughts:
Interesting how a `__init__.py`-file gets run by default if the 
module (directory) it's existing in is invoked. 

This makes me believe that the python interpreter runs certain
files (with .py extension) by default **if** they 
follow some certain naming conventions.

#### Recommended project structure:

```
project_name
│── README.md
│── __main__.py    
└─── project_name
│    │── __init__.py
│    │── more_source.py
│    │── subpackage1
│    │   └───__init__.py
│    └───test
│        │   __init__.py
│        │   test_code.py
└───folder2
    │   file021.txt
    │   file022.txt
```

#### Duck tails:

One suggested solution to package(module)-handling was to use a 
sort of singleton module.

Consider a "service" that handles the registry of modules that have been loaded:

######registry.py
```
_registry = []

    def register(name):
        _registry.append(name)
    
    def registered_names():
        return iter(_registry)
```
used as such: 
######use_registry.py
```buildoutcfg
import registry

registry.register('module_name')

for name in registry.registered_names():
    print(name)
```


02 Beyond Basic Functions
---------
#### Overview:
This module covers more *advanced* topics surrounding functions.

#### General thoughts:


##### Callable instances:
Consider the class **callable.py**:
```buildoutcfg
class Callable:
    
    def __init__(self):
        self._some_data = []
        
    def __call__(self, to_append):
        self._some_data.append(to_append)
    
    def __str__(self):
        return ' '.join(self._some_data)
        
```
This class uses ```__call__``` to invoke the function without explicitly 
having to use function calls etc:

```buildoutcfg
>>> from callable import Callable
>>> callable = Callable()
>>> print(callable)

>>> callable("some string")
>>> print(callable)
some string
```
As shown in above example the class function-definition \__call\__ is called
whenever you invoke `callable("some argument")` with some argument.

----

#### Lambda functions:
This was actually quite interesting. I'd heard of Lambda functions before,
but I've never really done anything with them. They seem quite straight-
forward though.
Basically you use lambda functions as an anonymous, throwaway function.

Consider this:
```
names = ["Bethany Ditzel", "Joakim Bajoul", "Bork Borkins", "Fredrik Edlund"]

#print names sorted on the last name
print(sorted(names, key=lambda NAMES: NAMES.split()[-1]))
#print names sorted on the first name
print(sorted(names, key=lambda NAMES: NAMES.split()[0]))
```

or:

```
def adder(x):
    return lambda y: x + y
add5 = adder(5)
add5(1)
6
```

Lambda functions are great for developers to nest functions in other
functions.

In the second example we have a function `adder` that returns
the sum of x and y. However y isn't set to a value in it's
function body (x is supplied in the function's parameter).

So after the `adder` has been invoked the first time (`add5 = adder(5)`) we
can rewrite the return of the function like this:
`return lambda y: 5 + y` since y hasn't been supplied.

During this time we have also assigned the function `adder` to `add5`
so if we call `add5` with 1 (`add5(1)`) we are supplying it with a y-value.

----

#### Extended Formal Arguments Syntax:

Executing the file `extended_arguments.py` in 02/other-files we notice a few things:
1. `*args` are returned as a class tuple
2. That the class is callable. 

Knowing this it's a matter of iterating over the items in the tuple (args)
to manipulate the objects.


Here are some requirements when working with `*args` and `**kwargs`:

1. If *args is present it must precede **kwargs or a syntax error will be thrown during compilation.
     <br><br>
     &nbsp;&nbsp;&nbsp;&nbsp; __Ie. this isn't allowed:__ `def print_args(**kwargs, *args)`
2. Any arguments preceding `*args` will be considered regualr positional arguments:
     
    ```
        def print(arg1, arg2, *args):
            print(arg1)
            print(arg2)
            print(args)
            print(type(args))
      ```
      
3. Any regular positional arguments passed __AFTER__ `*args` are considered mandatory keyword arguments.
Failure to do so results in a type error:
```buildoutcfg
def print_args(arg1, arg2, *args, kwarg1, kwarg2):
    print(arg1)
    print(arg2)
    print(args)
    print(kwarg1)
    print(kwarg2)
print_args(1, 2, 3, 4, 5, kwarg1=6, kwarg2=7) # OK
print_args(1, 2, 3, 4, 5, 6, 7)               # Type error
```

4. If used `**kwargs` must be the last argument in the function, after both `*args` and any 
potential regular positional arguments:
```buildoutcfg
def print_args(arg1, arg2, *args, kwarg1, kwarg2, **kwargs):
    print(arg1)
    print(arg2)
    print(args)
    print(kwarg1)
    print(kwarg2)
    print(kwargs)
print_args(1, 2, 3, 4, 5, kwarg1=6, kwarg2=7, kwarg3=8, kwarg9=10) # OK
def print_args(arg1, arg2, *args, kwarg1, kwarg2, **kwargs, kwargs10) # invalid syntax error
```
