message = 'global'

print("=============Non-global=============")
def enclosing():
    message = 'enclosing'

    def local():
        message = 'local'

    print('enclosing mesasge:', message)
    local()
    print('enclosing mesasge:', message)

print('enclosing mesasge:', message)
enclosing()
print('enclosing mesasge:', message)


print("=============  Global  =============")
def global_enclosing():
    message = 'enclosing'

    def local():
        global message
        message = 'local'

    print('enclosing mesasge:', message)
    local()
    print('enclosing mesasge:', message)

print('enclosing mesasge:', message)
global_enclosing()
print('enclosing mesasge:', message)

print("==============Non-local=============")
def nonlocal_enclosing():
    message = 'enclosing'

    def local():
        nonlocal message
        message = 'local'

    print('enclosing mesasge:', message)
    local()
    print('enclosing mesasge:', message)

print('enclosing mesasge:', message)
nonlocal_enclosing()
print('enclosing mesasge:', message)