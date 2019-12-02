# _____TF-IDF libraries_____
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

# _____helper Libraries_____
import pickle
import csv
import json
import timeit
import random
import re
import spacy
import os
from django.conf import settings
#import os

nlp = spacy.load('en_core_web_sm')

def clean_text(text):
    text = text.lower()
    text = re.sub(r"i'm", "i am", text)
    text = re.sub(r"he's", "he is", text)
    text = re.sub(r"she's", "she is", text)
    text = re.sub(r"that's", "that is", text)
    text = re.sub(r"what's", "what is", text)
    text = re.sub(r"where's", "where is", text)
    text = re.sub(r"\'ll", " will", text)
    text = re.sub(r"\'ve", " have", text)
    text = re.sub(r"\'re", " are", text)
    text = re.sub(r"\'d", " would", text)
    text = re.sub(r"won't", "will not", text)
    text = re.sub(r"can't", "cannot", text)
    return text

def preprocess(userQuery):
    ques = []
    temp = clean_text(userQuery.lower())
    # stop-words removal
    for token in temp.split(' '):
        t = str(token)
        if nlp.vocab[t].is_stop:
            pass
        else:
            ques.append(t)
    ques_list = ' '.join(ques)

    # lemmatization
    ques2 = []
    temp2 = nlp(ques_list)
    for token2 in temp2:
        ques2.append(token2.lemma_)
    ques_list = ' '.join(ques2)
    
    return ques_list

def talk_to_cb_primary(test_set_sentence, minimum_score , json_file_path , tfidf_vectorizer_pikle_path ,tfidf_matrix_train_pikle_path):
   
    test_set = (test_set_sentence, "")

    try:

        ##--------------to use------------------#
        print("FIRST")
        f = open(os.path.join(settings.BASE_DIR, tfidf_vectorizer_pikle_path), 'rb')
        tfidf_vectorizer = pickle.load(f)
        f.close()
        print("SECOND")

        f = open(os.path.join(settings.BASE_DIR, tfidf_matrix_train_pikle_path), 'rb')
        tfidf_matrix_train = pickle.load(f)
        f.close()
        print("THIRD")

        # ----------------------------------------#
    except:
        print("NO TRAINING")

    tfidf_matrix_test = tfidf_vectorizer.transform(test_set)

    cosine = cosine_similarity(tfidf_matrix_test, tfidf_matrix_train)

    cosine = np.delete(cosine, 0)
    max = cosine.max()
    response_index = 0
    if (max > minimum_score):
        new_max = max - 0.01
        list = np.where(cosine > new_max)
        response_index = random.choice(list[0])
    else :
        return "Apologies, I can't understand. My developers haven't trained me much! :(" , 0

    j = 0

    with open(os.path.join(settings.BASE_DIR, json_file_path), "r") as sentences_file:
        reader = json.load(sentences_file)
        for row in reader:
            j += 1  # we begin with 1 not 0 &    j is initialized by 0
            if j == response_index:
                return row["response"], max
                break







def previous_chats(query):
    minimum_score = 0.7
    file = "data.json"
    tfidf_vectorizer_pikle_path = "previous_tfidf_vectorizer.pickle"
    tfidf_matrix_train_path = "previous_tfidf_matrix_train.pickle"
    query_response, score = talk_to_cb_primary(query , minimum_score , file , tfidf_vectorizer_pikle_path , tfidf_matrix_train_path)
    return query_response

# while 1:
#     sent = input("Ask: ")
#     sent = preprocess(sent)
#     print(sent)
#     print(previous_chats(sent))

