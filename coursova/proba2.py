from instagram.client import InstagramAPI
import urllib.request
import simplejson
import httplib2
import json
import six

#from src.Instagram import Instagram
#insta = Instagram(username, password);
access_token = "5041771937.79a3467.7673f7a4abe049c5bbe229a4ad826316"
client_secret = "c3b09255b52847f3adeb9f823413ffe6"
#usernameId = "5041771937"#"79a3467592714815b2ab038172b2d2bf"
user_id = '5041771937'
user_id2 = '5513427638'
client_id = '79a3467592714815b2ab038172b2d2bf'
redirect_uri = 'http://127.0.0.1'
client_ips = '91.201.191.182'
location_id = '217022337'
media_id = 'BSkDsAZhiNN'
info = 'https://api.instagram.com/v1/users/self/?access_token=5041771937.79a3467.7673f7a4abe049c5bbe229a4ad826316'
info2 = 'https://api.instagram.com/v1/users/5513427638/?access_token=5041771937.79a3467.7673f7a4abe049c5bbe229a4ad826316'
info3 = 'https://api.instagram.com/v1/tags/streetart/media/recent?access_token=5041771937.79a3467.7673f7a4abe049c5bbe229a4ad826316'
api = InstagramAPI(access_token=access_token, client_secret=client_secret, client_id=client_id, redirect_uri=redirect_uri, client_ips=client_ips)
all_lines = []
with urllib.request.urlopen(info3) as webpage:

    for line in webpage:
        #line = line.strip()
        line = line.decode('utf-8')
        #line = dict(line)
        #line = line.split()
line = simplejson.loads(line)
print(len(line), type(line), line)
def loop_printer(ine):
    for i in ine:
        if type(i) == list:
            loop_printer(i)
        elif type(i) == dict:
            print(i)
            loop_printer(i)
        else:
            print('OLOLOLO', i)
loop_printer(line['data'])
#line = ' '.join(line['data'])
#line = simplejson.loads(line)
#print(len(line['data']), type(line['data']), line['data'])

#print(api.user_follows(user_id2))
#print(api.user_followed_by(user_id2))
print(api.user(user_id))
#print(api.user_media_feed())
#print(api.user_liked_media())
print(api.user_search('jogryn'))#works
print(api.user_relationship(user_id2))#works


print(line['data'][0]['images'])


recent_media, next_ = api.user_recent_media()
photos = []
for media in recent_media:
    photos.append('<img src="%s"/>' % media.images['thumbnail'].url)
