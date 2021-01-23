from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

soup = BeautifulSoup(response.text, "html.parser")
articles = soup.find_all(name="a", class_="storylink")
articles_text = []
articles_link = []
for article_tag in articles:
    text = article_tag.getText()
    articles_text.append(text)
    link = article_tag.get("href")
    articles_link.append(link)


article_upvotes = [int(upvote.getText().split()[0]) for upvote in soup.find_all(name="span", class_="score")]

# print(articles_text)
# print(articles_link)
# print(article_upvotes)
max_upvote = max(article_upvotes)
max_upvote_index = article_upvotes.index(max_upvote)


print(articles_text[max_upvote_index])
print(articles_link[max_upvote_index])




# with open("website.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.title)
# # print(soup.title.string)
# # print(soup.prettify())
# # print(soup.a)
#
# # all anchor tags
# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)
#
# # text in anchor tag
# for tag in all_anchor_tags:
#     print(tag.getText())
#
# # get attributes
# for tag in all_anchor_tags:
#     print(tag.get("href"))
#
# # get a particular tag with id
# name = soup.find(name="h1", id="name")
# print(name)
#
# # get a particular tag with class
# heading = soup.find(name="h3", class_="heading")
# print(heading)
#
# # with selector
# name = soup.select_one(selector="#name")
# print(name)