import requests
from send_email import send_email

topic = "SVB"
API_KEY = "6be7b888210e4bbf8eacafbbd33f2765"
url = f"https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "from=2023-02-13&sortBy=publishedAt&" \
      "pageSize=10" \
      "&language=en" \
      "&apiKey=6be7b888210e4bbf8eacafbbd33f2765"

request = requests.get(url)
content = request.json()

body = ""
for article in content["articles"]:
      if article['title'] is not None:
            body = body + article["title"] + \
                   "\n" + article["description"] + \
                   "\n" + article["url"] + \
                   2*"\n"

body = body.encode("utf-8")
send_email(message=body)