def egzekutor(*args, **kwargs):
    for func in args:
        for k, v in kwargs.items():
            print(func(k, v))
