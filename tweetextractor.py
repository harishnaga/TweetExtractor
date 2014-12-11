from tweepy.streaming import StreamListener # Importing stream listener from tweepy library 
from tweepy import OAuthHandler #Import OAuthHandler from tweepy library
from tweepy import Stream # Import Strem from tweepy library
import json #Importing JSON Library
import codecs #Importing codecs library 
import tweepy #importing tweepy library
import csv # importing csv library for csv file operations


# Go to http://apps.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key=""  #Consumer key which we get when we register for twitter app on apps.twitter.com
consumer_secret=""

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token=""
access_token_secret=""

class StdOutListener(StreamListener):
    """ A listener handles tweets are the received from the stream.
    This is a basic listener that just prints received tweets to stdout.

    """
    def on_data(self, data):
        csvFile = open('heartdisease1.csv', 'ab') #creating a csv file were streaming tweets are stored and opening in binary because when u write data into csv file it wont appened tweets leaving empty line between each tweet. 
        csvWriter = csv.writer(csvFile)
        j = json.loads(data) # Loads the json data and creates a dictonary of it
        text = j['text']
        rcount = j['retweet_count']
        timecreated = j['created_at']
        lang = j['lang']
        location = j['geo']
        
        csvWriter.writerow([text.encode('utf-8'),rcount,timecreated,lang,location])
        return True
 
        
    def on_error(self, status):
        print status

if __name__ == '__main__':
    
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    stream = Stream(auth, l)
    stream.filter(track=['#HeartDisease']) #Can use desired #tag to get data related to it.
