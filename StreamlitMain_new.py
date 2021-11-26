import streamlit as st
from PIL import Image
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import linear_kernel
import Functions_Books as funct
from fuzzywuzzy import process

#1. Header
st.write('# No worries. He knows what you want to read next.')
image = Image.open('images\image.jpeg') #save in the same folder
st.image(image, use_column_width=True)

title_user = st.text_input('Please enter a title', '')
#recommendation =''
#df1 = 'Default'

#1. User input 
st.sidebar.header('User Input Features')
with st.form(key ='Form1'): 
    with st.sidebar:
        #author = st.text_input('Author', '')  
        no_ratings =st.slider('Popularity: Minimum No of total Ratings',0,1000000,0)        #no ratings = st.number_input('Maximum number of tweets', 100)
        rating =st.slider('Rating',0.0,5.0,(0.0,5.0)) 
        pages = st.number_input('Maximum number of pages', 0)
        #unique_genres = sorted(df1.genres.unique()) #data=loadeddata, column genres
        #genres = st.sidebar.multiselect('Genres',unique_genres, unique_genres)
        #Vorher explode, dann in Model
        submitted1 = st.form_submit_button(label = 'Apply selection')


if submitted1:
    dfo=pd.read_csv('DataFinal\DataPreprocessed.csv',index_col=0)
    #reset index
    dfo.reset_index(drop=True, inplace=True)
    dfo['average_rating']=dfo['average_rating'].round(2)
    #1. Check user input: rating
    min_rating = rating[0]
    max_rating = rating[1]
    st.write('min_rating=',min_rating,'max_rating=',max_rating)
    #df = df1[df1['average_rating'].between(min_rating, max_rating)]
    #2. Check user input: page number
    if isinstance(pages, int) is True: #pages True,av_rating=True immer, no_ratings True/False
        df = dfo[dfo['pages']<=int(pages)]
        df2 = df[df['average_rating'].between(min_rating, max_rating)]
        if isinstance(no_ratings, int) is True:
            df1 = df2[df2['total_number_ratings']>=int(no_ratings)]
        else:
            df1=df2.copy() 
            st.write(df1)   
    else: #Pages False(nicht gefiltert),av_rating True immer, rating True/False
        df3 = dfo[dfo['average_rating'].between(min_rating, max_rating)]
        if isinstance(no_ratings, int) is True:
            df1 = df3[df3['total_number_ratings']>=int(no_ratings)]
        else:
            df1=df3.copy()
    st.write(df1)   
    

if st.button('Predict'):
    try:
        df1.reset_index(drop=True, inplace=True)
        recommendation = funct.give_recommendationComplete(title_user,df1)
        st.write(recommendation, 2)
    except:
        df1=pd.read_csv('DataFinal\DataPreprocessed.csv',index_col=0) #or feature output df, either filtered or original
        #reset index
        df1.reset_index(drop=True, inplace=True)
        recommendation1 = funct.give_recommendationComplete(title_user, df1)
        st.write(recommendation1[0],1)
        st.write(recommendation1[1])
        st.write(recommendation1[2])
        st.write(recommendation1[3])
        st.write(recommendation1[4])
        st.write(recommendation1[5])
        st.write(recommendation1[6])


        



 #Still to do: 
 #include: if input= empty procees with model + link of book cover 
 #  #feature_author = functionFuzzyAuthor(author)
    #Function includes search similarity in column Author
#year = st.sidebar.slider('Year', 1920, 1990,2021) #lowest value, default value, highest value
#authors = st.text_input('Authors', '')#