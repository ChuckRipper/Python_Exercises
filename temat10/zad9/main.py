class Wyjscie:
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        instance.__dict__ = {}  # to prevents inherited attributes from parent
        return instance