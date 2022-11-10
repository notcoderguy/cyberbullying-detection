import pickle
import re
import pandas as pd
import string
import emoji
from contractions import contractions_dict

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
nltk.download('omw-1.4')
nltk.download('wordnet')
nltk.download('punkt')
nltk.download('stopwords')

# convert to lower case
def text_lower(text):
    text = text.str.lower()
    return text

# expand contractions
def text_decontraction(text):
    expanded_words = []   
    for word in text.split():
        if word in contractions_dict:
            expanded_words.append(contractions_dict[word])
        else:
            expanded_words.append(word)
    text = " ".join(expanded_words)

    text = re.sub(r"can\'t", "can not", text)
    text = re.sub(r"n\'t", " not", text)
    text = re.sub(r"\'re", " are", text)
    text = re.sub(r"\'s", " is", text)
    text = re.sub(r"\'d", " would", text)
    text = re.sub(r"\'ll", " will", text)
    text = re.sub(r"\'t", " not", text)
    text = re.sub(r"\'ve", " have", text)
    text = re.sub(r"\'m", " am", text)
    return text

# remove emojis
def clean_emoji(text):
    text = emoji.replace_emoji(text, replace='')
    return text

def clean_entities(text):
    STOPWORDS = set(stopwords.words('english'))
    text = text.replace('\r', '').replace('\n', ' ').lower()
    text = re.sub(r"(?:\@|https?\://)\S+", "", text)
    text = re.sub(r'[^\x00-\x7f]',r'', text)
    banned_list= string.punctuation
    table = str.maketrans('', '', banned_list)
    text = text.translate(table)
    text = [word for word in text.split() if word not in STOPWORDS]
    text = ' '.join(text)
    text =' '.join(word for word in text.split() if len(word) < 14)
    return text

# remove hashtags
def clean_hashtags(text):
    mod_text = " ".join(word.strip() for word in re.split('#(?!(?:hashtag)\b)[\w-]+(?=(?:\s+#[\w-]+)*\s*$)', text))
    cleaned_text = " ".join(word.strip() for word in re.split('#|_', mod_text))
    return cleaned_text

# remove multiple spaces
def clean_space(text):
    re.sub("\s\s+" , " ", text)
    return text

# remove repeated words
def clean_repeated_words(text):
    re.sub(r'(.)1+', r'1', text)
    return text

# remove numbers
def clean_numbers(text):
    re.sub('[0-9]+', '', text)
    return text

# tokenize
def text_tokenize(text):
    tokenizer = RegexpTokenizer('\w+')
    text = text.apply(lambda x: tokenizer.tokenize(x))
    return text

# Stemming
def text_stemming(text):
    st = nltk.PorterStemmer()
    text = [st.stem(word) for word in text]
    return text

# Lemmatization
def text_lemmatize(text):
    lm = nltk.WordNetLemmatizer()
    text = [lm.lemmatize(word) for word in text]
    return text

def preprocees(text):    
    text = text_lower(text)
    text = text.apply(lambda x: text_decontraction(x))
    text = text.apply(lambda x: clean_emoji(x))
    text = text.apply(lambda x: clean_entities(x))
    text = text.apply(lambda x: clean_hashtags(x))
    text = text.apply(lambda x: clean_space(x))
    text = text.apply(lambda x: clean_repeated_words(x))
    text = text.apply(lambda x: clean_numbers(x))
    text = text_tokenize(text)
    text = text.apply(lambda x: text_stemming(x))
    text = text.apply(lambda x: text_lemmatize(x))
    text = text.apply(lambda x: " ".join(x))
    return text

def text_vectoriser(text):
    text = pd.Series(text)
    text = preprocees(text)
    text = [text[0],]
    vectorizer = pickle.load(open("data/vectorizer.pkl", "rb"))
    vector = vectorizer.transform(text)

    return vector

def analysis(text, model):
    with open("data/" + model + "_clf.pkl", "rb") as f:
        load_model = pickle.load(f)
    prediction = load_model.predict(text)
    return prediction

def response_gen(prediction):
    if prediction == "age":
        return {"status": 1, "message": "Cyberbullying on basis of age is detected.", "label": "age"}
    elif prediction == "ethnicity":
        return {"status": 1, "message": "Cyberbullying on basis of ethnicity is detected.", "label": "ethnicity"}
    elif prediction == "gender":
        return {"status": 1, "message": "Cyberbullying on basis of gender is detected.", "label": "gender"}
    elif prediction == "religion":
        return {"status": 1, "message": "Cyberbullying on basis of religion is detected.", "label": "religion"}
    elif prediction == "not_cyberbullying":
        return {"status": 0, "message": "No Cyberbullying case is detected.", "label": "not_cyberbullying"}