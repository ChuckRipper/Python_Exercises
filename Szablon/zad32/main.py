from itertools import chain, combinations
wyjscie = set(map(frozenset, chain.from_iterable(combinations(wejscie, r) for r in range(len(wejscie)+1))))
