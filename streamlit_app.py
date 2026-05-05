# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
"""
import streamlit as st
import pandas as pd
#import matplotlib.pyplot as plt
import numpy as np

st.title('My First App')
st.write('This app performs data analysis')

value=st.slider('choose value',0,100,50)
st.write('You chose: ',value)

name=st.text_input('Plz enter your name: ')
st.write('Your name is: ',name)

if st.button('click'):
    st.write('button was clicked')
    
data=pd.DataFrame({'A':[1,2,3,4],'B':[4,5,6,7]})

st.dataframe(data)

number=st.selectbox('choose a number',[1,2,3,4])

st.write('you chose',number)

a=st.number_input('plz enter a number')
st.write('the number is ',a)


st.sidebar.title('Datasets')

#x=np.linspace(-np.pi,np.pi,100)
#y=np.cos(x)

#fig,ax=plt.subplots()

#ax.plot(x,y)

#st.pyplot(fig)


    
    
    
    
    
    
    
    
    