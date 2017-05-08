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