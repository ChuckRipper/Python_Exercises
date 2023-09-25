class MetaWyjscie(type):
    def __getattr__(cls, name):
        class_name = name
        value = int("".join(filter(str.isdigit, name)))

        new_class = type(class_name, (WyjscieBase,), {})
        instance = new_class(value)
        setattr(cls, class_name, new_class)
        return new_class

class WyjscieBase:
    def __init__(self, parametr):
        self.parametr = parametr

class Wyjscie(metaclass=MetaWyjscie):
    pass
