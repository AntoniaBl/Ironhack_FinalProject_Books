import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from fuzzywuzzy import process
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer





#Clean Data

#Replace Value in Columns
def replace_in_column(df, column,find,replace_by):
    for df.rows in df[column]:
        df[column] = df[column].str.replace(find,replace_by)

#Replace nall with mean in column
def fillup_mean(column):
    column_mean = df1[column].mean()
    df1[column] = df[column].fillna(column_mean)

#Replace nall with median in column
def fillup_median(column):
    column_median = df1[column].median()
    df1[column] = df[column].fillna(column_median)

#Give year
def yearinrows(df,column):
    for df.rows in df[column]:
        df[column] = df[column].year

#Convert data types

def convert_data_types(df,convertto, incolumns=[]):
    for column in incolumns:
        if convertto == "object":
            df[column]=df[column].astype('object')
        elif convertto == "date":
            df[column]=pd.to_datetime(df[column])
        elif convertto == "number":
            df[column]=pd.to_numeric(df[column])

# Word Embedding, Tokenizing with NLTK 
def return_Serieslowercase(df,column):
    df[column]=df[column].str.lower()

def remove_stopwords(text):
    #print(text)
    text = str(text).split()
    stops = set(stopwords.words("english"))
    text = [w for w in text if not w in stops]
    text = " ".join(text)
    return text

def remove_nonAscii(s):
    return "".join(i for i in s if  ord(i)<128)

def remove_punctuation(text):
    tokenizer = RegexpTokenizer(r'\w+')
    text = tokenizer.tokenize(text)
    text = " ".join(text)
    return text

# Data Preprocessing

def combine_features(data):
    features=[]
    for i in range(0, data.shape[0]):
        features.append( data['title_tokenized'][i] + ' ' + data['desccription_tokenized'][i] + ' ' + data['series_tokenized'][i])
    return features

#Model

#UserInput other title recommendations
def suggestions_other_title(title_user):
    choices = df1['title'] 
    # Get a list of matches ordered by score, default limit to 5
    rec = process.extract(title_user, choices)
    print('This exact title was not found in the database. Did you mean one of these?')
    for i in rec:
        print(i[0])

#Assume book title if fuzzy ratio is above 95
def assume_book_title(title_user):
    choices = df1['title'] 
    # Get a list of matches ordered by score, default limit to 5
    rec = process.extract(title_user, choices)
    lst=[]
    for i in rec:
        lst.append(i[1])
        #print(i[1])
        if lst[0]>95:
            title_user=i[0]#list.sort(key=lst, reverse=True)
            print('I did not find an exact match in the database. I assume you mean the book: ' + title_user)
            give_5bookrecommendationsCount(title_user)
            break
        else:
            error
    

#Book Recommendations based on Wordcount

def give_5bookrecommendationsCount(title_user):
    #1.Step - convert the description from combined_features to a matrix of word counts
    cm = CountVectorizer().fit_transform(df1['combined_features'])
    #2.Get the cosine_simmilarity from the count matrix
    cs = cosine_similarity(cm)
    #Get index of title of user input
    indices = df1[df1.title == title_user].index.values[0]
    #Create a list of tuples in the form (index,similarity)
    scores = list(enumerate(cs[indices]))
    # Sort the list of similar books in descending order
    sorted_score = sorted(scores, key=lambda x:x[1], reverse=True)
    sorted_score = sorted_score[1:]
    # Create a loop to print the first 5 books from the sorted list
    j=0
    print('The 5 most recommended books to '+title_user+' are:\n')
    for item in sorted_score:
        book_title = df1[df1.index == item[0]]['title'].values[0]
        print(j+1, book_title)
        j=j+1
        if j >=5:
            break

#Complete suggestion function -combines the 3 functions above
def give_recommendationComplete(title_user):
    try:
        give_5bookrecommendationsCount(title_user)
    except:
        try:
            assume_book_title(title_user)
        except:
            suggestions_other_title(title_user)       






