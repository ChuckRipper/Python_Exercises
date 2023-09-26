import zipfile

with zipfile.ZipFile('data.zip', 'w') as z:
    z.write('data.dat')
