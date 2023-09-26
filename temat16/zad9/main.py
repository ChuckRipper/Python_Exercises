import lzma

with open('data.dat', 'rb') as f_in, lzma.open('data.xz', 'wb') as f_out:
    f_out.write(f_in.read())
