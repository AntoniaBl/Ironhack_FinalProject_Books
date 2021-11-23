import streamlit as st
from PIL import Image
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
#from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
from sklearn.metrics.pairwise import linear_kernel
import Functions_Books as funct
from fuzzywuzzy import process

#1. Header
st.write('# No worries. He knows what you want to read next.')
image = Image.open('image.jpeg') #save in the same folder
st.image(image, use_column_width=True)

title_user = st.text_input('Please enter a title', '')
recommendation =''


#2. Define Model Functions:
def suggestions_other_title(title_user):
    choices = df1['title'] 
    # Get a list of matches ordered by score, default limit to 5
    rec = process.extract(title_user, choices)
    str1=''
    #print()
    for i in rec:
        str1 +=(i[0])
    suggestions = str("This exact title was not found in the database. Did you mean one of these?\n"+str(str1)+"\n")
    return suggestions

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
    #print('The 5 most recommended books to '+title_user+' are:\n')
    str2=''
    for item in sorted_score:
        book_title = df1[df1.index == item[0]]['title'].values[0]
        str2+=(str(j+1)+' ' + book_title + "\n")
        #print(j+1, book_title)
        j=j+1
        if j >=5:
            return 'The 5 most recommended books to '+str(title_user)+' are:\n' + str(str2)
#For Genre,Author:After explode do list and append only if title is not yet in list, if len(list) = 5 dann return
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
            return 'I did not find an exact match in the database. I assume you mean the book: ' + title_user +give_5bookrecommendationsCount(title_user)
        else:
            error


def give_recommendationComplete(title_user):
    try:
        #print(1)
        a = give_5bookrecommendationsCount(title_user)
        if a:
            return a
    except:
        try:
            #print(2)
            b = assume_book_title(title_user)
            if b:
                return b 
        except:
            #print(3)
            c= suggestions_other_title(title_user) 
            if c:
                return c       
    

#3. Gice and Print recommendations
if st.button('Predict'):
    df1=pd.read_csv('DataFinal\DataPreprocessed.csv',index_col=0) #or feature output df, either filtered or original
    #reset index
    df1.reset_index(drop=True, inplace=True)
    recommendation = give_recommendationComplete(title_user)
       
st.write(recommendation)
 #include: if input= empty procees with model + link of book cover  + new lines


#4. Feature inputs Average_rating, total_ratings, pages
st.sidebar.header('User Input Features')
with st.form(key ='Form1'): # if still needed, else do st.sidebar everywhere
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
    if isinstance(pages, int) is True: #pages True,av_rating=True immer, no_ratinsg True/False
        df = dfo[dfo['pages']<=int(pages)]
        df2 = df[df['average_rating'].between(min_rating, max_rating)]
        if isinstance(no_ratings, int) is True:
            df1 = df2[df2['total_number_ratings']>=int(no_ratings)]
        else:
            df1=df2.copy()    
    else: #Pages False(nicht gefiltert),av_rating True immer, rating True/False
        df3 = dfo[dfo['average_rating'].between(min_rating, max_rating)]
        if isinstance(no_ratings, int) is True:
            df1 = df3[df3['total_number_ratings']>=int(no_ratings)]
        else:
            df1=df3.copy()

    st.write(df) 












 #   feature_author = functionFuzzyAuthor(author)
    #Function includes search similarity in column Author




#year = st.sidebar.slider('Year', 1920, 1990,2021) #lowest value, default value, highest value
#authors = st.text_input('Authors', '')












#Plots
#final=(prediction.Z).rest_index()
#px.pie(final, values='probability',names='species')
#st.plotly_chart()