from flask import Flask, jsonify, render_template, redirect, url_for, request
from elasticsearch import Elasticsearch
from textblob import Blobber
from textblob.sentiments import NaiveBayesAnalyzer
from nltk.corpus import movie_reviews
import re
import json

app = Flask(__name__)

es = Elasticsearch([{"host": "localhost", "port": 9200}])

@app.route('/predict', methods=['POST', 'GET'])
def predict_a_tweet():
    data = request.args.to_dict()
    tweet_content = data['submit']
    cleaned_tweet = clean_text(tweet_content)
    positive_likelyhood = text_blob(cleaned_tweet).sentiment.p_pos
    if 0.45 <= positive_likelyhood <= 0.55:
        return jsonify(sentiment="neutral", score=positive_likelyhood)
    if positive_likelyhood > 0.60:
        return jsonify(sentiment="positive", score=positive_likelyhood)
    else:
        return jsonify(sentiment="negative", score=positive_likelyhood)

def clean_text(tweet_to_clean):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet_to_clean).split())

if __name__ == '__main__':
    text_blob = Blobber(analyzer=NaiveBayesAnalyzer())
    app.run(host='0.0.0.0', debug=True)
