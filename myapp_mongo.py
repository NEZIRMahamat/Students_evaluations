import certifi
import pymongo
import qrcode
from pymongo import MongoClient
import streamlit as st


st.title("Evaluation de compétence !")
st.sidebar.button("Activer")
st.sidebar.write("Bienvenue Nezir")

db_uri = "mongodb+srv://nezir:DBnezir%23%23@cluster0.cs5k6gu.mongodb.net/test"

client = MongoClient(db_uri, tlsCAFile=certifi.where())
### Syntaxe : Client["BaseDeDonnées"]["Collections"] ou Client.BaseDeDonnées.Collections

data_base = client.students
studenst_evaluations = data_base.students_evaluations


#db.list_collection_names()
print("insert")
#data_base.list_collection_names()

#studenst_evaluations.insert_many([{"note": 10, "level": "B3"}, {"note":14, "level": "M1"}])
#print(studenst_evaluations.find({"note": 10}))

#print(type(studenst_evaluations))


client.close()