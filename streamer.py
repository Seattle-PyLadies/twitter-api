from slistener import SListener
import time, tweepy, sys, oauth2 as oauth

## OAuth with Tweepy
consumerToken = your_token 
consumerSecret = your_secret 
accessToken = access_token 
accessTokenSecret = token_secret 

auth = tweepy.auth.OAuthHandler(consumerToken, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)

def main():

    # Inside of 'track' add keywords of interest
    track = ['Seattle', 'Python']
 
    listen = SListener(api, 'twitterDump')
    stream = tweepy.Stream(auth, listen)

    print "Streaming started..."

    try: 
        stream.filter(track = track)
    except:
        print "error!"
        stream.disconnect()

if __name__ == '__main__':
    main()
