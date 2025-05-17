import requests
from send_email import send_email

api_key = "5098df43930442a8b8019a2e3f52c822"

url = ("https://newsapi.org/v2/everything?q=tesla&sortBy=publishedAt&"
       "apiKey=890603a55bfa47048e4490069ebee18c")

request = requests.get(url)
content = request.json()
body = ""
for article in content["articles"]:
    if article["description"] is not None:
      body = body + article["title"] + "\n" + article["description"] + 2*"\n"
body = body.encode("utf-8")
send_email(body)



