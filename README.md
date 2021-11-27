## Ironhack Data Analytics Bootcamp 
# Final Project - Build a Book Recommender

[Books?](images/image.jpg)

## **Goal of the project**

The objective of this project is to build a book recommender, which suggests books based on the similarity of the title and description.


## **Exploring the Data**

The data used was scraped from goodreads.com and contains 8137 books of various genres, years, length and popularity.

## **Project Content** 

The process was done in the following steps:

1.  Webscraping using BeautifulSoup
2.  General Data Cleaning
3.  Data preprocessing for the recommendation model:
    3.1 Tokenizing with NLTK
    3.2 Use sklearn CountVectorizer and cosine_similarity to receive the recommendations based on the frequency of words in the description
4.  User Input handling: Use fuzzywuzzy to assign the user input to the right title in the database
5.  Set up Streamlit for presentational purposes of the model and to include other features that can be chosen by the user


## **Special Libraries used**

- [pandas]('https://pandas.pydata.org')
- [NLTK]('https://www.nltk.org')
- [sklearn.feature_extraction]('https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html')
- fuzzywuzzy
- [Streamlit]('https://streamlit.io')

### Submitted on 27.11.2021