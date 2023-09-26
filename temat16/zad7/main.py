import zipfile

compression = zipfile.ZIP_BZIP2
with zipfile.ZipFile('data.zip', 'w', compression=compression) as z:
    for foldername, subfolders, filenames in os.walk('data'):
        for filename in filenames:
            z.write(os.path.join(foldername, filename))
