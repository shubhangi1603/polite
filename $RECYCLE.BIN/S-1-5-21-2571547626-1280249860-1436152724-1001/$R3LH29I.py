import streamlit as st

import pandas as pd

from PIL import Image
from streamlit.proto.RootContainer_pb2 import SIDEBAR

st.title("polite")

st. image('title_image.jpg')
st.header('sentiment analysis')
st.markdown("---")
Sidebar = st.sidebar

Sidebar.header("choose your option ")
choices=['view dataset','serach tweets', 'upload image']

selOpt =Sidebar.selectbox('choose what to do?' ,choices)

x= st.slider("select a value")
st.write(x, 'squared is', x*x)

def viewDataset():
    with st.spinner("loading data...."):
        df = pd.read_csv('pokemon.csv')
        st.dataframe (df)

def getTwitterInput():
    user_input = st.text_input("enter twitter handle  or a hashtag")
    btn = st.button("serach tweets")
    
        

def saveimage():
    img_name =st.text_input("enter name of image")
    img_file =st.file_uploader("upload your image")

    if image_file:
        img = image.open(img_file)
        st.image(img)

    btn =st.button("save image")
    if btn:
        try:
            img.save("uploads/"+img_name+".png") 
            st.success("image saved")
        except:
            st.error('something went wrong')


if selOpt == choices[0]:
       viewDataset()
elif selOpt == choices[1]:
    getTwitterInput()

elif selOpt == choices[2]:

    saveimage()           
 



   











