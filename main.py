import streamlit as st
import os
from PIL import Image
from helper import *
st.title('fashion recommender system')

def save_uploaded_file(uploaded_file):
    try:
        with open(os.path.join('uploaded',uploaded_file.name),'wb') as f:
            f.write(uploaded_file.getbuffer())
        return 1    
    except:
        return 0        

uploaded_file = st.file_uploader("Upload Image")
if uploaded_file is not None:
    if save_uploaded_file(uploaded_file):
        # display the file
        display_image = Image.open(uploaded_file)
        st.image(display_image)
        indices = recommend(os.path.join('uploaded',uploaded_file.name))
        st.text('Recommended Products')
        os.remove('uploaded/'+uploaded_file.name)
        col1, col2, col3, col4,col5 = st.beta_columns(5)
        try:
            with col1:
                st.image('images/'+images_name[indices[0][1]])
        except:
            pass
        try:
            with col2:
                st.image('images/'+images_name[indices[0][2]])
        except:
            pass
        try:
            with col3:
                st.image('images/'+images_name[indices[0][3]])
        except:
            pass
        try:
            with col4:
                st.image('images/'+images_name[indices[0][4]])
        except:
            pass
        try:
            with col5:
                st.image('images/'+images_name[indices[0][5]])        
        except:
            pass                
        #file has uploaded
        
    else:
        pass    
