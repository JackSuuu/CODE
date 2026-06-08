# paths
from pathlib import Path
path = Path("/Users/jack/Desktop/Python/Module/ecommerce")

# path.exists()
# path.mkdir()
# path.rmdir()
# path.rename()

paths = [p for p in path.iterdir() if p.is_dir()]
py_files = [p for p in path.rglob("*py")]  # * means all the file, rglob method returns generator object
print(paths)
print(py_files)
print(path.stat())
