import io

def wyjscie(buffer: io.StringIO):
    return buffer.getvalue().count('\n') + 1
