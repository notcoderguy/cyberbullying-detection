import pickle
from fastapi import FastAPI
from pydantic import BaseModel

from functions import *
import pickle
import re
import string
import emoji
from contractions import contractions_dict

import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem import SnowballStemmer
from nltk.tokenize import RegexpTokenizer
nltk.download('stopwords')

app = FastAPI()

class TextData(BaseModel):
    text: str

@app.get("/")
async def root():
    return {
        "message": "Welcome to Cyberbullying Detection API.",
        "author": "Vasu Grover",
        "co-author": "Zubin Singh",
        "contributors": "Ishan Chopra, Shubham Singh",
        "version": "1.0.0",
        "documentation": "http://localhost:8000/redoc"
        }

@app.post("/predict/svm")
async def predict_svm(data: TextData):
    # Analyse the text
    label = analysis(text_vectoriser([data.text]), "svm")
    result = label_encoder(label[0])
    return result

@app.post("/predict/nb")
async def predict_nb(data: TextData):
    # Analyse the text
    label = analysis(text_vectoriser([data.text]), "nb")
    result = label_encoder(label[0])
    return result

@app.post("/predict/knn")
async def predict_knn(data: TextData):
    # Analyse the text
    label = analysis(text_vectoriser([data.text]), "knn")
    result = label_encoder(label[0])
    return result

@app.post("/predict/rf")
async def predict_rf(data: TextData):
    # Analyse the text
    label = analysis(text_vectoriser([data.text]), "rf")
    result = label_encoder(label[0])
    return result
