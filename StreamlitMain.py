import streamlit as st
from PIL import Image
import pandas as pd

#store the dataframe to use in the same folder

st.write('# No worries. He knows what you want to read next.')

image = Image.open('image.jpeg') #save in the same folder
st.image(image, use_column_width=True)

#Inputs 
st.sidebar.header('User Input Features')
rating = st.sidebar.slider('Rating',0,3,5)
year = st.sidebar.slider('Year', 1920, 1990,2021) #lowest value, default value, highest value
pages = st.sidebar.slicer('Pages', 0,350,27500)
col1, col2 = st.columns(2)
with col1:
    #genre=st.chooseoption#####
    title = st.text_input('Title', 'Enter Title')
with col2:
    author = st.text_input('Author', 'Enter Author')
    series = st.text_input('Series','Enter Series')
    

 #store inputs in dictionary
user = pd.DataFrame({'year':year, 'author':author,'rating':rating,'series':series,'title': title}, index=[0])

st.write("The user input is:")
st.table(user)


##Move code from jupyter
#if st.button('Predict'):
   # data = pd.read_csv('bookspreprocessed', index_col=0)

    #include: if input= empty procees with model



#Predict



#Plots
#final=(prediction.Z).rest_index()
#px.pie(final, values='probability',names='species')
#st.plotly_chart()