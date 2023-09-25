class OgraniczonaLista(list):
    def append(self, item):
        if len(self) < 30:
            super().append(item)
