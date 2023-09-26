import bz2

with open('data.dat', 'rb') as f_in, bz2.BZ2File('data.bz2', 'wb') as f_out:
    f_out.write(f_in.read())
