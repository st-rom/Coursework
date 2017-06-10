#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Use text editor to edit the script and type in valid Instagram username/password
import urllib.request
from InstagramAPI import InstagramAPI
import simplejson

#username2 = input('Enter username: ')
#info = 'https://www.instagram.com/' + username2 + '/?__a=1'
InstagramAPI = InstagramAPI("pappa_ronny", "511999")
InstagramAPI.login() # login
info = 'https://www.instagram.com/pooordude/?__a=1'
with urllib.request.urlopen(info) as webpage:
    for line in webpage:
        web_info = line.decode('utf-8')
info = simplejson.loads(web_info)
usernameID2 = info['user']['id']
print(usernameID2)
InstagramAPI.getTotalUserFeed(usernameID2)
media_id = InstagramAPI.LastJson # last response JSON
print(len(media_id['items']))
print((media_id['items'][0]))
#print((media_id['items'][0]))
for i in media_id['items'][0]:
    print(i)
print((media_id['items'][0]['caption']))
print(len(media_id['items'][0]['usertags']['in']))
#InstagramAPI.like(media_id["items"][0]["pk"]) # like first media
#print(InstagramAPI.getUserFollowers(media_id["items"][0]["user"]["pk"])) # get first media owner followers
'''
#For 'ok' status
InstagramAPI.getTotalUserFeed(usernameID2)
for i in InstagramAPI.LastJson['items']:
    InstagramAPI.getMediaLikers(i['pk'])
    print(InstagramAPI.LastJson['status'])
print('WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW')
'''
InstagramAPI.getMediaLikers(media_id['items'][0]["id"])
c = 0
print(len(InstagramAPI.LastJson))
print(InstagramAPI.LastJson)

for i in InstagramAPI.LastJson:
    print(i)

#for userLiker in InstagramAPI.LastJson["users"]:
#    c += 1
#    print(userLiker["username"], userLiker, c)
