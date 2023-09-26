import os

wyjscie = sorted([item for item in os.listdir(wejscie) if os.path.isdir(os.path.join(wejscie, item))])
