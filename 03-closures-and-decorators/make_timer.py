import time

def make_time():
    last_called = None

    def elapsed():
        nonlocal last_called
        now = time.time() # get current time
        if last_called is None: # checks if last_called has been set in either scope.
            last_called = now
            return None
        result = now - last_called
        last_called = now
        return result # returns the current time - the time when the function was called last.

    return elapsed #returns a a function
