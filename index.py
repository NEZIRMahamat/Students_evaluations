import mysql.connector
import streamlit as st
import pandas as pd

@st.cache
def load():
   
    data = pd.read_json('quiz-1.json')
    return data


st.title("Evaluation de niveau de Compétence")

data_pd = load()
st.write(data_pd)

db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="22Nz4767ab",
    database="demo"
)

cursor = db.cursor()
db.autocommit = True

#Insertion des données dans la Base des données

def insert_data(cursor, note, level_course):
    query_insert = """INSERT INTO students_evaluations(note, level_course) VALUES(%s, %s)"""
    cursor.execute(query_insert, (note, level_course))

#print all rows on the table   
def fetch_from_data_base(cursor, callback, MAX_LINE=20):
    query_select = "SELECT id, note, level_course FROM students_evaluations"
    cursor.execute(query_select)
    while True:
        results = cursor.fetchmany(MAX_LINE)
        if not results:
            break 
        for line in results:
            callback(line)

def delete_table(cursor, id):
    query_delete = "DELETE FROM students_evaluations WHERE id=%s"
    cursor.execute(query_delete, id)


#delete_table(cursor, ("12",))
#insert_data(cursor, 11, "B3")
fetch_from_data_base(cursor, print)


db.close()



