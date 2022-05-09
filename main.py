from fastapi import FastAPI,Request
from dotenv import load_dotenv
from deta import Deta
import os
load_dotenv()

app=FastAPI()
deta=Deta(os.environ.get('DETAKEY'))
db=deta.Base('notes')

@app.get('/')
def index():
    return {"message":"This is the index page of the notes API"}

@app.get('/getnotes')
async def getNotes():
    respose={}
    allnotes=db.fetch()
    for item in allnotes.items:
        respose[item["key"]]=item["note"]
    return respose

@app.post('/addnote/{id}/{note}')
async def addNote(id:str,note:str):
    db.insert({"note":note},id)
    print(f"Note inserted with id: {id}")
    return {"message":"note added!"}


@app.delete('/deletenote/{id}')
async def deleteNote(id:str):
    db.delete(id)
    return {"message":f"note with id {id} deleted"}

@app.put('/updatenote/{id}/{note}')
async def updateNote(id:str,note:str):
    db.put({"note":note},id)
    return {"message":f"note with id {id} updated"}



