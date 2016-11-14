# -*- coding: utf-8 -*-
"""
Created on Sun Nov 06 15:19:20 2016

Mike made a small change to this file

@author: sneha
"""
import urllib2
import json
import time
import csv
import oauth2

#scrape data from yelp using API key
from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator


TOKEN = 'kG_IQ-L1nOqgBfjZPW-EvgsehH5Oggwd'
TOKEN_SECRET = 'C8vJ3qJfCvvWRbqVHvWF4ykOJYI'
CONSUMER = 'dXVZCM7svoQDVya576vXwg'
CONSUMER_SECRET = 'XGoTHgnqrOqRXnUNRsAdG6oViEk'

# This function performs a Yelp API request, taken from Yelp's python example
def api_request(url, url_params):
    """ Make a request with Yelp's API """
    consumer = oauth2.Consumer(CONSUMER, CONSUMER_SECRET)
    token = oauth2.Token(TOKEN, TOKEN_SECRET)

    oauth_request = oauth2.Request(method="GET", url=url, 
                                   parameters=url_params)
    oauth_request.update({'oauth_nonce': oauth2.generate_nonce(),
                          'oauth_timestamp': oauth2.generate_timestamp(),
                          'oauth_token': TOKEN,
                          'oauth_consumer_key': CONSUMER})

    oauth_request.sign_request(oauth2.SignatureMethod_HMAC_SHA1(), 
                               consumer, token)
    signed_url = oauth_request.to_url()

    conn = urllib2.urlopen(signed_url, None)
    try:
        response = json.loads(conn.read())
    finally:
        conn.close()
    return response

def search(term, location, limit=10):
    """ Search Yelp with a term and location """
    url = 'http://api.yelp.com/v2/search'
    url_params = {'term': term.replace(' ', '+'),
                  'location': location.replace(' ', '+'),
                  'limit': limit}
    response = api_request(url, url_params)
    bizs = response['businesses']
    return bizs

from pprint import pprint
bizs = search('', 'Raleigh, NC')
# Look at our results and the ratings
pprint([(biz['name'], biz['rating']) for biz in bizs])




consumer_key    = 'qDBPo9c_szHVrZwxzo-zDw'
consumer_secret = '4we8Jz9rq5J3j15Z5yCUqmgDJjM'
token           = 'jeRrhRey_k-emvC_VFLGrlVHrkR4P3UF'
token_secret    = 'n-7xHNCxxedmAMYZPQtnh1hd7lI'

consumer = oauth2.Consumer(consumer_key, consumer_secret)

category_filter = 'restaurants'
location = 'Chapel Hill, NC'
options =  'category_filter=%s&location=%s&sort=1' % (category_filter, location)
url = 'http://api.yelp.com/v2/search?' + options

oauth_request = oauth2.Request('GET', url, {})
oauth_request.update({'oauth_nonce'      : oauth2.generate_nonce(),
                      'oauth_timestamp'  : oauth2.generate_timestamp(),
                      'oauth_token'       : token,
                      'oauth_consumer_key': consumer_key})

token = oauth2.Token(token, token_secret)
oauth_request.sign_request(oauth2.SignatureMethod_HMAC_SHA1(), consumer, token)
signed_url = oauth_request.to_url()

print signed_url
