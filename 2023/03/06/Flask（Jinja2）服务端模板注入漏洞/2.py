num = -1
search = '__builtins__'
for c in ().__class__.__bases__[0].__subclasses__():
    num += 1
    try:
        if search in c.__init__.__globals__.keys():
            print(c, num)
    except:
        pass
