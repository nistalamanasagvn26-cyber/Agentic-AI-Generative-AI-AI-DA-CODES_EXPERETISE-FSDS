import pandas as pd
import numpy as np
import streamlit as st
st.title('My First Streamlit App Created by mr.senapathi')
st.write('welcome! calculate the square of the number')
st.header('select a number')
number=st.slider('pick a number',0,100,25)
st.subheader('Result')
sq_number=number*number
st.write(f'The Square of **{number}** is {sq_number}')



