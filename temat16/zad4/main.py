import tarfile

with tarfile.open('data.tar', 'w') as t:
    t.add('data/')
