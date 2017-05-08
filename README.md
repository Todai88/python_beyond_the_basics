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
----

#### Forwarding arguments

Short module.
Covers how to use unpacked collections as arguments. 

See 02/forwarding_arguments.py:

```buildoutcfg
## this is a good implementation of a function as it soaks up any potential trailing arguments

def color(red, green, blue, **kwargs):
    print("r=", red)
    print("g=", green)
    print("b=", blue)
    print(kwargs)
    
def test(arg1 , arg2, *args):
    print(arg1)
    print(arg2)
    print(args)
    
t = (11, 12, 13, 14, 15, 16)
k = {'red': 20, 'green': 30, 'blue': 40, 'alpha': 50, 'beta': 60}

test(*t) # star unpacks the collection into positional arguments
print("first finished!")
color(**k) # double start unpacks the collection into a dictionary with named arguments
```

----

#### Duck Tail: Transposing Tables

This was fucking awesome!

So in the previous module I learnt how to unpack collections. This module ties it up well.

Consider these two lists:
```buildoutcfg
first  = [1, 2, 3]
second = [4, 5, 6]
```
Using `zip` we can zip the two lists together:
```buildoutcfg
(1, 4)
(2, 5)
(3, 6)
```
Zip can also handle multiple series:
```buildoutcfg
third = [7, 8, 9]
zip(first, second, third)
(1, 4, 7)
(2, 5, 8)
(3, 6, 9)
```
If we then create a list of the three lists `col = [first, second, third]` we would end up with
something quite clumpy. Consider printing that:
```
for item in zip(col[0], col[1], col[2]:
    print(item)
```
It simply looks quite clumpsy... But what if we implement the unpacking we learned earlier?
```buildoutcfg
for item in zip(*col):
    print(item)
```
Or if we create our own datastructure (primitive, I know..):
```buildoutcfg
placeholder = list(zip(*col))
print(placeholder)
```

Both work fine and looks a lot more refined.

This technique is called transpositioning and basically transposes rows into columns:
```buildoutcfg
first  = [1, 2, 3]
second = [4, 5, 6]
third  = [7, 8, 9]
col = [first, second, third]

# col = [[1, 2, 3,], 
#        [4, 5, 6], 
#        [7, 8, 9]]

transposed = list(zip(col))

# transposed = [(1, 4, 7),
#               (2, 5, 8),
#               (3, 6, 9)]
```

----

<br>

03 - Closures and decorators
----

#### 01: Local functions:

A named function like `def sort(list):` will create a reference to a memory address every 
time it is executed.

__LEGB__ rule: Local, Enclosing, Global, Built-in.
```buildoutcfg
"""
Global scope
"""
PI = TAU / 2

def func(x):
    """
    Enclosing scope
    """
    def local_func(n):
        """
        Local scope
        """
        a = 'hello'
        return a + n
    y = 2
    return x + y
```

How are local functions useful?

Useful for specialized, one-off functions like sorting-key functions.
They also aid in code organization and readability.
Similar to lambdas, but more general (may contain multiple expressions and statements)

#### Returning Functions From Functions:
Remember how we mentioned that a local function has a reference to its memory address?
Because of that we can return a local function from its wrapping function much in
the same way we can return any other datatype.

#### Closures and Nested Scopes:

This was really interesting as is showed how closures work.

Consider this code:
```buildoutcfg
def enclosing():
    x = 'closed'
    def local_func():
        print(x)
    return local_func
```
We know that `local_func()` can access `x` in its scope because of the LEGB rule. 
But how?
Imagine we had imported `enclosing()` and are running a python shell:
 ```buildoutcfg
>>> lf = enclosing()
>>> lf() 
closed over
>>> lf.__closeure__
(<cell at 0x10ea95cc8: str object at 0x10eac19f0>,)
```
After calling __closure__ on the `enclosing()` object we can see that it shows us the memory allocation
of a string object inside of its scope, `x`.


#### Function factories

Really interesting too!

Remember the LEGB rule. And look at this code:
```buildoutcfg
def raise_to(exp):
    def raise_to_exp(x):
        return pow(x, exp)
    return raise_to_exp
```
We already know that we can return functions in functions. But what we migth not know
is that a returned function that has been instantiated by a parameter of its
wrapping function still keeps that parameter in memory.

In the case of the code above we can see that `raise_to_exp` returns the POW of 
two items, `x` and `exp`. `exp` was the argument of its wrapping function `raise_to_exp`.
Because of that `raise_to_exp` has access to a reference to that argument's memory allocation.

So if we imagine we have imported `raise_to_exp` and run a shell:

```buildoutcfg
>>> squared = raise_to(2)
```
then square will basically be: 
```buildoutcfg
def raise_to_exp(x):
    return pow(x, 2)
```
So if we call square with:
```buildoutcfg
>>> squared(3)
9
>>> sqiared(2)
4
```
If we created a new reference to `raise_to`:
```buildoutcfg
>>> cubed = raise_to(3)
```
Then cubed would be a reference to the memory allocation of:
```buildoutcfg
def raise_to_exp(x):
    return pow(x, 3)
```
And run it like:
```buildoutcfg
>>> cubed(3)
27
```

So basically what has happend is that you create two different variables
that hold a reference to two separate instances of the function `raise_to_exp(x)`,
each with its own individual reference to the argument `exp` too. 

These references are saved in your RAM.