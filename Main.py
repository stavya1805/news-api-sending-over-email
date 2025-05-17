import requests
from send_email import send_email

api_key = "5098df43930442a8b8019a2e3f52c822"
topic = "tesla"

url = ("https://newsapi.org/v2/everything?"
       f"q={topic}&"
       "sortBy=publishedAt&"
       "apiKey=890603a55bfa47048e4490069ebee18c&"
       "language=en")

request = requests.get(url)
content = request.json()
body =  "Subject : Today's News\n\n"
for article in content["articles"][:19]:
    if article["description"] is not None:
      body = (body + article["title"] + "\n" +
              article["description"] + "\n" +
              article["url"] + 2 * "\n")

body = body.encode("utf-8")
send_email(body)



