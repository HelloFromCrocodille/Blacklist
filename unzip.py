import zipfile

def unzip(filename, new_name=None):
    file_zip = zipfile.ZipFile(filename, 'r')
    file_zip.extractall()
    file_zip.close()