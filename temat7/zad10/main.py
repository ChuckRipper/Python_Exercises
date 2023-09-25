import time

def czas():
    t = time.time()
    while True:
        yield time.time() - t
        t = time.time()
