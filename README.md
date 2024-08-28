# Search-Engine
Implementing a search engine that answers queries on Wikipedia articles.
Our corpus (document collection) is Wikipedia articles. 
To simplify our work and focus on the core algorithms, we won’t write the crawler to get the articles from Wikipedia. 
We will use a prebuilt file which contains approximately 50,000 articles

Link to that prebuilt file: []()

The way we are going to build this is in 3 parts:

- Create Index: Building the index of our search engine.
- Query Index: Answering search queries on the index that we built.
- Ranking: Ranking the search results of query index.

# Parsing the documents

While parsing our document we will do the following things:
1) **Concatenate** the title and the text of the page.
2) **Lowercase** all words.
3) **Get all tokens**, where a token is a string of alphanumeric characters terminated by a non-alphanumeric character. The alphanumeric characters are defined to be [a-z0-9]. So, the tokens for the word ‘apple+orange’ would be ‘apple’ and ‘orange’.
4) **Filter out** all the tokens that are in the **stop words** list, such as ‘a’, ‘an’, ‘the’.
5) **Stem each token** using to finally obtain the stream of terms. Porter Stemmer removes common endings from words. For example the stemmed version of the words fish, fishes, fishing, fisher, fished are all fish.

# Inverted Index

## What is it and how is it used in Search Engines2?

Inverted Index a key data structure used in search engines. 
It maps each word in a set of documents to the list of documents (and positions) where it appears. 
In a search engine, it's used to quickly find all documents that contain a given word, making searches fast and efficient. 
Instead of scanning every document, the engine looks up the word in the index and retrieves the relevant documents directly.

# Building the Inverted Index

## What will our inverted index store?

For Example: Consider we have these documents\
Document 1: web retrieval web search information\
Document 2: search engine web ranking\
Document 3: web search course information search\

Now the postings list for the term ‘web’ is `[ [1, [0, 2]], [2, [2]], [3, [1]] ]`. 
Meaning, the term ‘web’ appears in document 1 in positions 0 and 2 (we start counting positions from 0), document 2 position 2, and document 3 position 1.

### What is this posting list?

The postings list of a term is a list of lists, where each list corresponds to a specific document. 
So, there is a list for every document that the term appears in.
Each of this list contains the document id and the places of occurence of a word.

## The Process



