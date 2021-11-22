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

#store the dataframe to use in the same folder

st.write('# No worries. He knows what you want to read next.')

image = Image.open('image.jpeg') #save in the same folder
st.image(image, use_column_width=True)

#Inputs 
st.sidebar.header('User Input Features')
#no_ratings =st.sidebar.slider('Sum of Ratings',0,0,6000000)
#rating = st.sidebar.slider('Rating',0,3,5)
#year = st.sidebar.slider('Year', 1920, 1990,2021) #lowest value, default value, highest value
#pages = st.sidebar.slicer('Pages', 0,350,27500) #select only maximum pages

#unique_genres = sorted(data.genres.unique()) #data=loadeddata, column genres
#genres = st.sidebar.multiselect('Genres',unique_genres, unique_genres)

col1, col2 = st.columns(2)
with col1:
    #genre=st.chooseoption#####
    title_user = st.text_input('Title', 'Enter Title')
#with col2:
    #author = st.text_input('Author', 'Enter Author')
    #series = st.text_input('Series','Enter Series')
    

 #store inputs in dictionary

#user = pd.DataFrame({'sum of ratings': no_ratings, 'year':year,'rating':rating,'pages':pages}) #'author':author,series':series,'title': title_user}, index=[0])

#st.write("The user input is:")
#st.table(user)

#Define Model Functions:
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
    


recommendation =0
if st.button('Predict'):
    df1=pd.read_csv('DataFinal\DataPreprocessed.csv',index_col=0)
    #reset index
    df1.reset_index(drop=True, inplace=True)
    recommendation = give_recommendationComplete(title_user)


#Print recommendations

st.write(recommendation)

    #include: if input= empty procees with model


#Predict



#Plots
#final=(prediction.Z).rest_index()
#px.pie(final, values='probability',names='species')
#st.plotly_chart()