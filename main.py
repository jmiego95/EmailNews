import requests

API_KEY = "6be7b888210e4bbf8eacafbbd33f2765"
url = "https://newsapi.org/v2/everything?q=SVB&" \
      "from=2023-02-13&sortBy=publishedAt&apiKey=" \
      "6be7b888210e4bbf8eacafbbd33f2765"

request = requests.get(url)
content = request.json()
print(content["articles"])
for article in content["articles"]:
      print(article["title"])
      print(article["description"])
