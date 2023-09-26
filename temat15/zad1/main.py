import io

def wyjscie(buffer: io.StringIO):
    print(buffer.getvalue()[:100])
