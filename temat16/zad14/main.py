import gzip

with gzip.open('data.gz', 'rb') as f_in, open('data.dat', 'wb') as f_out:
    f_out.writelines(f_in)
