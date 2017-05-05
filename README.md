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