from pathlib import Path
from time import ctime
import shutil

source = Path("/Users/jack/Desktop/Python/record.txt")
target = Path("/Users/jack/Desktop/Python/Student_Table.txt")

shutil.copy(source, target)
