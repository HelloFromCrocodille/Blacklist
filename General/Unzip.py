import zipfile

def Unzip(filename):
    file_zip = zipfile.ZipFile(filename, 'r')
    file_zip.extractall()
    file_zip.close()