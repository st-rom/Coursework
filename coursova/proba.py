from instagram.client import InstagramAPI
#mport sys
#print (sys.version) #parentheses necessary in python 3.
access_token = "0ddf1441779744469cf9323c2844a8d6"
client_secret = "c3b09255b52847f3adeb9f823413ffe6"
api = InstagramAPI(access_token=access_token, client_secret=client_secret)
recent_media, next_ = api.user_recent_media(user_id="79a3467592714815b2ab038172b2d2bf", count=10)
for media in recent_media:
    print(media.caption.text)
