# This is the file that implements a flask server to do inferences. It's the file that you will modify to
# implement the scoring for your own algorithm.

import os
import json
from sklearn.externals import joblib
import flask

import urllib.request
import bs4 as bs  
import re  
import nltk
from gensim.models import Word2Vec


#Define the path
prefix = '/opt/ml/'
model_path = os.path.join(prefix, 'model')

# Load the model components

model=joblib.load(os.path.join(model_path, 'model.bin'))

# The flask app for serving predictions
app = flask.Flask(__name__)
@app.route('/ping', methods=['GET'])
def ping():
    # Check if the classifier was loaded correctly
    try:
        model
        status = 200
    except:
        status = 400
    return flask.Response(response= json.dumps(' '), status=status, mimetype='application/json' )

@app.route('/invocations', methods=['POST'])
def transformation():
    # Get input JSON data and convert it to a DF
    input_json = flask.request.get_json()
    input_json = json.dumps(input_json['input'])


    new_model = Word2Vec.load(os.path.join(model_path, 'model.bin'))
    print(new_model)


    sim_words = new_model.wv.most_similar('intelligence')  

    # Transform predictions to JSON
    result = {'output': []}

    result['output'] = sim_words
    result = json.dumps(result)
    return flask.Response(response=result, status=200, mimetype='application/json')

