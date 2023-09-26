import zipfile

with zipfile.ZipFile('data.zip', 'w') as z:
    for foldername, subfolders, filenames in os.walk('data'):
        for filename in filenames:
            z.write(os.path.join(foldername, filename))
