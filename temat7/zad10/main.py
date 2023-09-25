import time

# Wariant #1
# def czas():
#     t = time.time()
#     while True:
#         yield time.time() - t
#         t = time.time()

# Wariant #2
def czas():
    prev_time = time.time()
    while True:
        cur_time = time.time()
        yield cur_time - prev_time
        prev_time = cur_time

# Wariant #3
# def czas():
#     start = time.time()
#     while True:
#         yield time.time() - start
#         start = time.time()
