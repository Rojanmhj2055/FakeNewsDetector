import pandas as pd 

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np
import pickle
import re
import random

# model = keras.models.load_model("./models/model.h5")
with open('./models/tokenizer.pickle','rb') as handle:
    tokenizer = pickle.load(handle)

model = keras.models.load_model("./models")

label=["its true","true","thumbs up","fake news","seriously","your liar"]

##this function removes unncessary puntuatuons and space,tabs and 
## othe characteers 
def normalize(i):
  normalized =[]
  i= i.lower()
  i=re.sub('https?://\S+|www\. \S+',"",i)
  i = re.sub('\\W', ' ', i)
  i = re.sub('\n', '', i)
  i = re.sub(' +', ' ', i)
  i = re.sub('^ ', '', i)
  i = re.sub(' $', '', i)
  normalized.append(i)
  return normalized

def get_prediction(mynews):
    if mynews:
        temp = normalize(mynews)
        seq = tokenizer.texts_to_sequences(temp)
        padded_seq = pad_sequences(seq,maxlen=1000,padding='post',truncating='post')
        pred = np.argmax(model.predict(padded_seq))
        if pred == 0:
            mylabel = label[random.randint(0,2)]
        else:
            mylabel = label[random.randint(3,5)]
        return mylabel

# def get_prediction(mynews):
#     if mynews:
#      temp=normalize(mynews)
#      seq = tokenizer.texts_to_sequences(temp)
#      print(seq)
#      padded_seq = pad_sequences(seq,maxlen=1000,padding='post',truncating='post')
#      pred = np.argmax(model.predict(padded_seq)
#      return pred