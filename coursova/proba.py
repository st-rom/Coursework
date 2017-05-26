#mport sys
#import json
#import simplejson
#import _json
#print (sys.version) #parentheses necessary in python 3.
access_token = '5041771937.79a3467.7673f7a4abe049c5bbe229a4ad826316'

from instagram.client import InstagramAPI
access_token = '5041771937.79a3467.7673f7a4abe049c5bbe229a4ad826316'
client_secret = "c3b09255b52847f3adeb9f823413ffe6"
api = InstagramAPI(client_secret=client_secret, access_token=access_token)
usr = api.user_search('jogryn')
#usr = api.user_relationship('jogryn')

print usr
recent_media, next_ = api.user_recent_media(user_id="jogryn", count=10)
for media in recent_media:
   print media.caption.text

'''
api = InstagramAPI(access_token=access_token, client_secret=client_secret)
recent_media, next_ = api.user_recent_media(user_id="79a3467592714815b2ab038172b2d2bf", count=10)
for media in recent_media:
    print(media.caption.text)
'''

#api = InstagramAPI(client_id='79a3467592714815b2ab038172b2d2bf', client_secret='c3b09255b52847f3adeb9f823413ffe6', access_token=access_token)
#print(api.list_subscriptions())
#popular_media = api.media_popular(count=20)

#for media in popular_media:
#x    print media.images['standard_resolution'].url
