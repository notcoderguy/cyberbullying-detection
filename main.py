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
        "authors": [
                        "Vasu Grover [RA1911003030248]", 
                        "Ishan Chopra [RA1911003030261]", 
                        "Zubin Singh [RA1911003030299]", 
                        "Shubham Singh [RA1911003030300]"
                    ],
        "version": "1.0.0",
        "documentation": "http://localhost:8000/redoc",
        "github": "https://github.com/notcoderguy/cyberbullying-detection-api"
        }

@app.post("/analyse/svm")
async def analyse_svm(data: TextData):
    # Analyse the text
    label = analysis(text_vectoriser([data.text]), "svm")
    result = response_gen(label[0])
    return result

@app.post("/analyse/nb")
async def analyse_nb(data: TextData):
    # Analyse the text
    label = analysis(text_vectoriser([data.text]), "nb")
    result = response_gen(label[0])
    return result

@app.post("/analyse/knn")
async def analyse_knn(data: TextData):
    # Analyse the text
    label = analysis(text_vectoriser([data.text]), "knn")
    result = response_gen(label[0])
    return result

@app.post("/analyse/rf")
async def analyse_rf(data: TextData):
    # Analyse the text
    label = analysis(text_vectoriser([data.text]), "rf")
    result = response_gen(label[0])
    return result
