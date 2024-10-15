# Crawlers?

Crawlers are automated scripts or programs which browse the internet systematically, visiting websites and collecting information.

## Why do we use them?

- Search Engines - to make searches more fast and efficient
- Web Scraping - to collect data across the web
- Monitoring - to monitor websites, looking for any change 

## Working

- **Starting Point:** The crawler begins by visiting a set of predefined URLs, usually referred to as "seed URLs" or "starting pages."
- **Link Extraction:** It then scans the HTML content, following hyperlinks on each page to discover and visit other pages.
- **Recursion:** The crawler repeats this process recursively, visiting new pages and discovering more links.
- **Indexing:** The content of each page is processed and stored in an index, often along with metadata like the URL, timestamps, and keywords.

>> This indexing is what is done in inverted index

