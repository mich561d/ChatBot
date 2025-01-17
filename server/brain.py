import pickle
import json
import random
import datetime as dt
import tensorflow as tf
import tflearn
import numpy
from nltk.stem.lancaster import LancasterStemmer
import nltk


def downloadNLTK():
    nltk.download()
# downloadNLTK()


stemmer = LancasterStemmer()
date_format = '%Y/%m/%d-%H:%M:%S'

# Opens data file intents.json
with open('intents.json') as file:
    data = json.load(file)

try:
    with open('data.pickle', 'rb') as f:
        words, labels, training, output = pickle.load(f)
except:
    words = []
    labels = []
    docs_x = []
    docs_y = []

    # Preparing data for our model.
    for intent in data['intents']:
        for pattern in intent['patterns']:
            # Gets every word, word by word. Instead of an entire sentence
            wrds = nltk.word_tokenize(pattern)
            # Extend list since we already know it a list, instead of looping though and appending.
            words.extend(wrds)
            docs_x.append(wrds)
            docs_y.append(intent['tag'])

        # Get every tag
        if intent['tag'] not in labels:
            labels.append((intent['tag']))

    # Stems the words.        
    words = [stemmer.stem(w.lower()) for w in words if w != '?']
    # Sorts them and removes duplicates.
    words = sorted(list(set(words)))
    labels = sorted(labels)

    training = []
    output = []

    # Bag of words - one hot incoded.

    # How often a tag is represented -> one hot incoded.
    out_empty = [0 for _ in range(len(labels))]

    for x, doc in enumerate(docs_x):
        bag = []
        wrds = [stemmer.stem(w) for w in doc]

        for w in words:
            if w in wrds:
                bag.append(1)
            else:
                bag.append(0)

        output_row = out_empty[:]
        output_row[labels.index(docs_y[x])] = 1

        training.append(bag)
        output.append(output_row)

    training = numpy.array(training)
    output = numpy.array(output)

    with open('data.pickle', 'wb') as f:
        pickle.dump((words, labels, training, output), f)

# Model

# Resetting underlying data graph
tf.reset_default_graph()

net = tflearn.input_data(shape=[None, len(training[0])]) # Input data, som er længden af vores data (patterns)
net = tflearn.fully_connected(net, 8) # Hidden layer 1
net = tflearn.fully_connected(net, 8) # Hidden layer 2
net = tflearn.fully_connected(net, len(output[0]), activation='softmax') # Output layer (tags)
net = tflearn.regression(net)

model = tflearn.DNN(net) # Model wrapper that can perform classifier tasks.

# Model done

# Training the model
current_date = dt.datetime.now()
if current_date.day == 1 or 1 == 1:
    start_time = dt.datetime.now().strftime(date_format)
    model.fit(training, output, n_epoch=600, batch_size=8, show_metric=True)
    model.save('model.tflearn')
    end_time = dt.datetime.now().strftime(date_format)

    with open('.././intern/data_learning.json') as json_file:
        json_data = json.load(json_file)

    now = dt.datetime.now()
    now_year = str(now.year)
    now_month = str(now.month)
    now_day = str(now.day)
    if now_year not in json_data.keys():
        json_data[now_year] = {}
    if now_month not in json_data[now_year].keys():
        json_data[now_year][now_month] = {}
    if now_day not in json_data[now_year][now_month].keys():
        json_data[now_year][now_month][now_day] = {
            "start_time": "", "end_time": ""}

    json_data[now_year][now_month][now_day]["start_time"] = start_time
    json_data[now_year][now_month][now_day]["end_time"] = end_time

    json = json.dumps(json_data)
    f = open(".././intern/data_learning.json", "w")
    f.write(json)
    f.close()
else:
    try:
        model.load('model.tflearn')
    except:
        model.fit(training, output, n_epoch=600,
                  batch_size=8, show_metric=True)
        model.save('model.tflearn')

# Bag of words for the input from user
def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]
    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1

    return numpy.array(bag)


def chat(userInput):
    results = model.predict([bag_of_words(userInput, words)])[0]
    results_index = numpy.argmax(results)
    tag = labels[results_index]

    if results[results_index] > 0.5:
        for tg in data['intents']:
            if tg['tag'] == tag:
                responses = tg['responses']

        return random.choice(responses)
    else:
        return random.choice(data['default'])
