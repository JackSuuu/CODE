# paths
from pathlib import Path

# Path("/usr/local/bin")
# Path()
# Path("ecommerce/__init__.py")
# Path() / 'ecommerce' / '__init__.py'
# Path.home()

path = Path("ecommerce/__init__.py")
path.exists()
path.is_file()
path.is_dir()
print(path.name)
print(path.stem)
print(path.suffix)
print(path.parent)
path = path.with_suffix(".txt")
print(path.absolute())
print(path)