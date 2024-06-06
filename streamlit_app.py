import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import json

st.header("PROJECT - TEAM 5")

#buscar en el json el acceso/permisos que tiene la persona y mostrarlas
def read_file(file_name):
    df = pd.DataFrame()
    df = pd.read_csv(file_name)
    #columns_info = {"columns": list(df.columns)}
    #print(json.dumps(columns_info, indent=4))
    for col in df.columns:
        print(col)

netflix = "netflix.csv"
IMDB = "IMDb Top TV Series.csv"
read_file(netflix)
read_file(IMDB)

users_data  = json.load(open("users.json", "r"))
roles_data  = json.load(open("roles.json", "r"))
dd_data  = json.load(open("dd.json", "r"))

def get_info_by_name(name):
  user_record = next((user for user in users_data['users'] if user['name'] == name), None)

  if user_record:
    user_roles = user_record['roles']
    user_roles_data = roles_data.get(user_roles, {})
    user_info = {field: dd_data[field] for field in user_roles_data.get('campos', [])}
    #print(user_info)
    user_json = {
      "name": user_record['name'],
      "roles": user_roles,
      "info": user_info
    }
    return user_json
  else:
    return None

#nombre de la variable
name = st.text_input("NEW NAME")
st.write("My new name: ", name)
user_info = get_info_by_name(name)

if user_info:
     #print(user_info)
  print(json.dumps(user_info, indent=4))
else:
  print(f"No hay info de '{name}'.")

file = st.file_uploader('File uploader')
nd = pd.read_csv(file)
st.write(nd)
