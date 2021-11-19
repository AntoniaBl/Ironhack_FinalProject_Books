import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from sklearn.model_selection import train_test_split
import statsmodels.api as sm
from statsmodels.formula.api import ols
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer



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

# 



