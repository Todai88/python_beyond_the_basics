def wrapper():

    def wrapped():
        _var = 'from local function'
        print(_var)
    return wrapped
