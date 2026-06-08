import json
from pathlib import Path

# how to write json file using python
movies = [
    {"id": 1, "tittle": "Terminator", "year": 1989},
    {"id": 2, "tittle": "Kindergarten Cop", "year": 1993},
]

data = json.dumps(movies)
Path("movies.json").write_text(data)

# how to read data from json file using python
data = Path("movies.json").read_text()
movies = json.loads(data)
print(movies[0]["tittle"])
