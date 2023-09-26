import tarfile

with tarfile.open('data.tar.xz', 'w:xz') as t:
    t.add('data/')
