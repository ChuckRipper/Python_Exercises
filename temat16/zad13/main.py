import gzip

with open('data.dat', 'rb') as f_in, gzip.open('data.gz', 'wb') as f_out:
    f_out.writelines(f_in)
