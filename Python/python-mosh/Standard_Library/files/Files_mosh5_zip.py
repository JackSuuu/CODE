from pathlib import Path
from zipfile import ZipFile

# how to create a zip file
with ZipFile("files.zip", "w") as zip:
    for path in Path("Emails").rglob("*.*"):
        zip.write(path)

# how to read the information in a zip file
with ZipFile("files.zip") as zip:
    print(zip.namelist())
    info = zip.getinfo("...")
    print(info.file_size)
    print(info.compress_size)
    zip.extractall("directry")