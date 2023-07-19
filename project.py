import requests
from bs4 import BeautifulSoup
import lxml

response = requests.get(url="https://news.ycombinator.com/news")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "lxml")

articles = soup.find_all(name="a",class_="storylink")
article_texts = []
article_links = []
for article_tag in articles:
    article_text = article_tag.getText()
    article_texts.append(article_text)
    article_link = article_tag.get("href")
    article_links.append(article_link)


article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name='span', class_="score")]

# print(article_texts)
# print(article_links)
print(article_upvotes)

n = max(article_upvotes)

i = article_upvotes.index(n)





