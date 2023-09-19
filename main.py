from fastapi import FastAPI
from pydantic import BaseModel

from functions import *

app = FastAPI()

class TextData(BaseModel):
    text: str

@app.get("/")
async def root():
    return {
        "message": "Welcome to Cyberbullying Detection API.",
        "authors": [
                        "Vasu Grover [NotCoderGuy]",
                    ],
        "version": "1.0.0",
        "github": "https://github.com/notcoderguy/cyberbullyingDetectionAPI"
        }

@app.post("/analyse")
async def analyse_svm(data: TextData):
    # Analyse the text
    label = analysis(text_vectoriser([data.text]), "svm")
    print(label)
    result = response_gen(label[0])
    return result
