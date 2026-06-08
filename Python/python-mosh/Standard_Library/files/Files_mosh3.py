from pathlib import Path
from time import ctime

path = Path("/Users/jack/Desktop/Python/Module/ecommerce")
path2 = Path("/Users/jack/Desktop/Python/Student_Table.txt")

print(ctime(path.stat().st_ctime))
print(path2.read_text())



