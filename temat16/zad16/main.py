import tarfile

with tarfile.open('data.tar.gz', 'w:gz') as t:
    t.add('data/')
