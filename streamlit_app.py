import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

st.header("PROJECT - TEAM 5")
"""
# Welcome to Streamlit!
Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:.
If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).
In the meantime, below is an example of what you can do with just a few lines of code:
"""
"""
Cachar lo que meta en un input text
nombre de la variable
"""
input = st.text_input("NEW VALUE")
st.write("My new value: ", input)



file = st.file_uploader('File uploader')
nd = pd.read_csv(file)
st.write(nd)
