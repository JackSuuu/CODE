import requests
from bs4 import BeautifulSoup

response = requests.get("https://papers.gceguide.com/A%20Levels/")
soup = BeautifulSoup(response.text, "html.parser")

subject = soup.select(".name")
print(subject.get("href", 0))

