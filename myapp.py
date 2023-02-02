import streamlit as st
from pymongo import MongoClient

st.write("Hello Everyone !")
st.sidebar.button("Activer")
st.sidebar.write("Bienvenue Nezir")

db_uri = "mongodb+srv://nezir:DBnezir%23%23@cluster0.cs5k6gu.mongodb.net/test"

client = MongoClient(db_uri)
print(client)