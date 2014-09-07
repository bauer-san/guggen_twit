#-------------------------------------------------------------------------------
# Name:        guggen_twit_stream.py
# Purpose:     Parse the twitter stream and display relevant tweets to Guggen hat
#
# Author:      Geoff
#
# Created:     06/09/2014
# Copyright:   (c) Geoff 2014
# Licence:     free, as in fish
#-------------------------------------------------------------------------------

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import twittercreds

##CONSUMER_KEY = moved_to_twittercreds
##CONSUMER_SECRET = moved_to_twittercreds
##ACCESS_KEY = moved_to_twittercreds
##ACCESS_SECRET = moved_to_twittercreds

class MyListener(StreamListener):
    """ A listener handles tweets are the received from the stream.
    """
    def on_data(self, data):
        print data
        tweet_text = json.loads(data)['text']
        print tweet_text[tweet_text.find('#hat')+5:len(tweet_text)]

        return True

    def on_connect(self):
        print 'Connection SUCCESSFUL'
        return

##    def on_direct_message(self, data):
##        print 'DM'
##        print data
##        tweet_text = json.loads(data)['text']
##        print tweet_text[tweet_text.find('#hat')+5:len(tweet_text)]
##
##        return True

    def on_error(self, status):
        print status

if __name__ == '__main__':
    listen = MyListener()
    auth = OAuthHandler(twittercreds.CONSUMER_KEY, twittercreds.CONSUMER_SECRET)
    auth.set_access_token(twittercreds.ACCESS_KEY, twittercreds.ACCESS_SECRET)

    stream = Stream(auth, listen)
    stream.filter(track=['bauer_san #hat'])
