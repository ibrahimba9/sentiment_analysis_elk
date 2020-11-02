# sentiment_analysis_elk
Tweet Sentiment Analysis with ELK and Python

# Introduction
this personal project is realised to learn about sentiment analysis on tweets with Python and integrating it on an ELK (Elasticsearch - Logstash - Kibana) pipeline for automation and real time visualization.

# Requirements
you need to install and configure the following tools:
- Java 8
- Nginx
- Elasticsearch
- Kibana
- Logstash
After installation you need to configure a local Nginx server.

# Workflow
![alt text](https://github.com/ibrahimba9/sentiment_analysis_elk/blob/main/Screenshots/workflow.PNG)
1- Scraping data frow twitter
2- Analysisng sentiments with Textblob 
3- Data Engineering
4- Connecting with Elasticsearch
5- Visualizing the results on Kibana

# Logstash Configuration
In the Inuput section of the logstash file, we need to insert your twitter API credentials (consumer_key, oauth token, ...).
You need to specify the keywords related to your research. In this examples I'm collecting tweets about Tesla and Elon Musk.
In the Filter section, I am using the "prune" filter to only extract certain features. In my case i only chose to collect the ID of the tweet, The text of the Tweet and its date.
After that, I'm using the http filter to call a Python script to apply the sentiment analysis on every tweet I collect.
The Python script is returning the sentiment of the text and its score.
You can use the mutate filter to change the name of the variables.
In the Output, I'm just connecting to the elasticsearch server to send the data collected and preprocessed (the tweet and its generated sentiment).

To run this pipeline, you need to:
1- First, run the python script so that it waits for data to collect and apply the Sentiment analysis.
Command: Python predict_tweet.py
![alt text](https://github.com/ibrahimba9/sentiment_analysis_elk/blob/main/Screenshots/Screenshot%20from%202020-05-25%2003-41-54.png)
2- Run the logstash file to start the scraping and the workflow
Command: sudo path_to_file/tweet_log.conf
![alt text](https://github.com/ibrahimba9/sentiment_analysis_elk/blob/main/Screenshots/Screenshot%20from%202020-05-25%2003-33-4922222.png)

This is a representation of the stream of the collectiuon of tweet and application of the logstash pipeline.
![alt text](https://github.com/ibrahimba9/sentiment_analysis_elk/blob/main/Screenshots/Screenshot%20from%202020-05-25%2003-33-39.png)

# Visualization
You can check kibana to see the data collected on real time.
![alt text](https://github.com/ibrahimba9/sentiment_analysis_elk/blob/main/Screenshots/Screenshot%20from%202020-05-25%2003-32-06.png)
In my case I used Kibana to generate a Piechart and a Barplot to visualise the number of Positive, Negative and Neutral Sentiments of the collected tweets
![alt text](https://github.com/ibrahimba9/sentiment_analysis_elk/blob/main/Screenshots/Screenshot%20from%202020-05-25%2003-31-33.png)
