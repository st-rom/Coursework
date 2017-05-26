from instagram.client import InstagramAPI
from simplejson import *
import httplib2
import json
import six


access_token = '5041771937.79a3467.7673f7a4abe049c5bbe229a4ad826316'
client_secret = "c3b09255b52847f3adeb9f823413ffe6"
user_id = "jogryn"#"79a3467592714815b2ab038172b2d2bf"
api = InstagramAPI(access_token=access_token, client_secret=client_secret)
#access_token = api.exchange_code_for_access_token('')

#print(dumps([1,2,3,{'4': 5, '6': 7}], separators=(',', ':')))
recent_media, next_ = api.user_recent_media(user_id=user_id, count=10)
for media in recent_media:
    print(media.caption.text)

