class MyMetaclass(type):
    """A metaclass"""
    def __new__(mcs, name, bases, dict):
        print("Class {} is created".format(name))
        return type.__new__(mcs, name, bases, dict)
