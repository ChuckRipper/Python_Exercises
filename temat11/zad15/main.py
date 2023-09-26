import functools

wyjscie = functools.reduce(lambda d, src: d.update(src) or d, wejscie, {})
