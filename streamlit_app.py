import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

st.header("PROJECT - TEAM 5")

"""nombre de la variable"""
input = st.text_input("NEW NAME")
st.write("My new name: ", input)

"""buscar en el json el acceso/permisos que tiene la persona y mostrarlas"""


file = st.file_uploader('File uploader')
nd = pd.read_csv(file)
st.write(nd)
