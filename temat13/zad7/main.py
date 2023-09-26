class Wektor:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __getitem__(self, key):
        if key == "x":
            return self.x
        elif key == "y":
            return self.y
        raise KeyError(f"Nieznany klucz: {key}")
