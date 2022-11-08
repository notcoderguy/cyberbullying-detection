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
    # Load the model
    with open("data/svm_clf.pkl", "rb") as f:
        model = pickle.load(f)
    # Make a prediction
    text = text_cleaner(data.text)
    text = text_vectoriser([text])
    prediction = model.predict(text)
    return {"prediction": prediction[0]}

@app.post("/predict/nb")
async def predict_nb(data: TextData):
    # Load the model
    with open("data/nb_clf.pkl", "rb") as f:
        model = pickle.load(f)
    # Make a prediction
    text = text_vectoriser([data.text])
    prediction = model.predict(text)
    return {"prediction": prediction[0]}

@app.post("/predict/knn")
async def predict_knn(data: TextData):
    # Load the model
    with open("data/knn_clf.pkl", "rb") as f:
        model = pickle.load(f)
    # Make a prediction
    text = text_cleaner(data.text)
    text = text_vectoriser([text])
    prediction = model.predict(text)
    return {"prediction": prediction[0]}

@app.post("/predict/rf")
async def predict_rf(data: TextData):
    # Load the model
    with open("data/rf_clf.pkl", "rb") as f:
        model = pickle.load(f)
    # Make a prediction
    text = text_cleaner(data.text)
    text = text_vectoriser([text])
    prediction = model.predict(text)
    return {"prediction": prediction[0]}

