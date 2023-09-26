import bz2

with bz2.BZ2File('data.bz2', 'rb') as f_in, open('data.dat', 'wb') as f_out:
    f_out.write(f_in.read())
