def tag(name, **kwargs):
    # >>> tag('img', src='test.jpg')
    # would give us:
    # 'img'
    # (src="test.jpg")
    # dict
    print(name)
    print(kwargs)
    print(type(kwargs)) # prints a dictionary object