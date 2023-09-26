import lzma

with lzma.open('data.xz', 'rb') as f_in, open('data.dat', 'wb') as f_out:
    f_out.write(f_in.read())
