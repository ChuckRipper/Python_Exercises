import tarfile

with tarfile.open('data.tar.bz2', 'w:bz2') as t:
    t.add('data/')
