"""
Example on how closures and scope works.
"""
g = 'global'

def outer(p='param'):
    l = 'local'

    def inner():
        print(g, p, l)
    inner()
