"""
Remember that a decorator requires a callable and returns a callable
In this case we are using the class function __call__ to return a 
reference to a local function called wrapper.

Wrapper returns the calling function (the one using decorator)
and prints its arguments if the instance variable _enabled is True.
"""


class Trace:

    def __init__(self):
        self._enabled = True

    def __call__(self, f):
        """
        @param f: the (callable) function we want to return
        @return: 
        """
        def wrap(*args, **kwargs):
            if self._enabled:
                print("Calling {}".format(f))
            return f(*args, **kwargs)
        return wrap

