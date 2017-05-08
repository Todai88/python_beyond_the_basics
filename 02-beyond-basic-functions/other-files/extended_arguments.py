class Extended_arguments:

    def __call__(self, *args):
        print(args)
        print(type(args))

        # do some manipulation
        for item in args:
            print("I'm a {} with value {}".format(type(item)), item)


def good_practice(length, *items):
    # This is considered better practice as it gives a better error-message
    # to show the user what the issue actually is.

    # This function simply uses v as an accumulator and iterates over the tuple
    # of supplied arguments
    print("I'm good practice")
    print("First argument has type of: {}".format(type(length)))
    print("Second argument has type of: {}".format(type(items)))

    v = length
    for item in items:
        v *= item
    return v

def bad_practice(*items):
    # This is bad practice as it gies the user a bad error (stop iterator):
    # when no items have been provided. This is bad as it doesn't explain the problem.

    print("I'm bad practice...")
    i = iter(items)
    v = next(i)

    for item in i:
        v *= item
    return v


