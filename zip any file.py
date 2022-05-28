import zipfile

with zipfile.ZipFile('filename.zip', 'w') as zip:
     zip.write('filename.py')
