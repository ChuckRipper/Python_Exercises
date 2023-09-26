import zipfile

with zipfile.ZipFile('data.zip', 'r') as z:
    z.extractall()
