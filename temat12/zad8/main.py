import statistics
import math

print(statistics.mean(wejscie))
print(math.exp(sum(map(math.log, wejscie)) / len(wejscie)))
print(len(wejscie) / sum(1/x for x in wejscie))
