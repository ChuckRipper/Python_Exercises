import json

class Wyjscie(Wejscie):
    
    def to_json(self):
        return json.dumps(self.__dict__)
    
    @classmethod
    def from_json(cls, json_str):
        data = json.loads(json_str)
        obj = cls()
        for key, value in data.items():
            if not callable(value):
                setattr(obj, key, value)
        return obj
