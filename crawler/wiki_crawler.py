# This crawler is to fetch wikipedia fetaured articles
# The fetched articles data is to be stored seperately as different files in the data folder
import requests, json
from bs4 import BeautifulSoup

url_wiki = "https://en.wikipedia.org"
url_feat_articles = "https://en.wikipedia.org/wiki/Wikipedia:Featured_articles"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}
# headers to mimic the actions of a browser

# Starting menu
print("Select any one option from below: ")
print("1. To update the featured articles database.")
print("2. To proceed with the present featured articles database locally")

user_input = int(input("Enter your choice"))

if user_input == 1:
  feat_page = requests.get(url_feat_articles, headers=headers)
  status_code = feat_page.status_code

  # Error management for status codes
  if status_code == 200:
    print("Connected to featured articles page...")
  else:
    print(f"HTTP Response Code:{status_code}")

  # A prompt for user
  print("Creating a list of articles to visit...")

  feat_page_data = BeautifulSoup(feat_page.text, "html.parser")
  # print(feat_page_data.prettify()) # To look for classes or ids to be selected

  # On reviewing the output html code what we can see is the info about the article like its url and title is in span tag
  # <span class="featured_article_metadata has_been_on_main_page">

  # Grabbing all these span tags
  feat_articles = feat_page_data.find_all('span', class_='featured_article_metadata has_been_on_main_page')

  # Creating a list of dictionaries containing article title and link
  articles = []
  for i in feat_articles:
    articles.append(
      {
        "title": i.a.text,
        "link": url_wiki + i.a["href"]
      }
    )

  # Saving this list in the data folder named featured articles
  with open("./crawler/data/featured_articles.json", "w") as feat_articles_json:
    json.dump(articles, feat_articles_json, indent=4)

  # User promt informing the completion of list
  print("List Generated...")
  print(f"Total articles found: {len(articles)}")

elif user_input == 2:
  pass

else:
  print("Please choose from available choices...")
  print("Exiting...")