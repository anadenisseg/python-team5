import json
import pandas as pd
import streamlit as st
import altair as alt
import numpy as np

def load_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)
    
def print_and_write(msg):
    print(msg)
    st.write(msg)

def get_valid_name(name):
    for name_ in users['users']:
        if name_['username'].lower() == name.lower():
            return name_
    else:
        print_and_write('Invalid Name: Please provide a name inside the database')

def get_user_access(name):
    return get_valid_name(name)['access']

def get_user_role(name):
    return get_valid_name(name)['role']

def get_user_dds(name):
    return get_valid_name(name)['DDs']

def get_dds(name):
    return dd

def get_user_info(name):
    user_info = {}

    access = get_user_access(name)
    role = get_user_role(name)
    dds = get_user_dds(name)

    tag = get_user_tag(name)
    des = get_user_des(name)

    user_info['name']   = name
    user_info['access'] = access
    user_info['role']   = role
    user_info['dd']     = des

    return json.dumps(user_info, indent=4)

def get_user_tag(name):
    user = get_valid_name(name)
    role = user['role']

    for each in roles['roles']:
        if each['role'] == role:
            tag = each['tag']
            return tag

def get_user_des(name):
    dds_obj = get_dds(name)
    user_tag = get_user_tag(name)
    result = {}
    for each in dds_obj:
        result[each] = dds_obj[each][user_tag]
    return result


# Carga de datos
users = load_json('users.json')
roles = load_json('roles.json')
dd    = load_json('dd.json')
df_netflix = pd.read_csv(r'netflix.csv')
df_imdb = pd.read_csv(r'IMDb Top TV Series.csv')

try:
    st.header("PROJECT - TEAM 5")
    name = st.text_input("INSERT NEW NAME")
    st.write("MY NAME IS: ", name)

    user_info_st = get_user_info(name)
    ddd          = get_user_dds(name)
    desc         = get_user_des(name)

    net_nick_col_names  = []
    imdb_nick_col_names = []
    net_gold_col_names  = []
    imdb_gold_col_names = []

    for each in ddd:
        for file in desc[each]:
            if 'netflix' in file['DBD'].lower():
                net_nick_col_names.append(file['nickname'])
                net_gold_col_names.append(file['golden_name'].lower())

            elif 'imdb'  in file['DBD'].lower():
                imdb_nick_col_names.append(file['nickname'])
                imdb_gold_col_names.append(file['golden_name'])

    df_netflix = df_netflix.rename(columns=dict(zip(net_gold_col_names, net_nick_col_names)))
    st.write("Netflix Access:")
    st.write(df_netflix[net_nick_col_names])

    df_imdb = df_imdb.rename(columns=dict(zip(imdb_gold_col_names, imdb_nick_col_names)))
    st.write("IMDBs Access:")
    st.write(df_imdb[imdb_nick_col_names])

except:
    if name is not None and name != "":
        st.write(f"NO INFORMATION OF NAME '{name}'.")
