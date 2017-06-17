#! /usr/bin/env python
# -*- coding: utf-8 -*-
import getpass
from InstagramAPI import InstagramAPI
from niceone import GeoFriends
from nicetwo import RealFriends

login = raw_input("Enter login or just press 'Enter' to use admin account: ")
if login != '':
    print('Do not worry, your password is safe. It is invisible right now for safety measures so keep entering it')
    psw = getpass.getpass('Password: ')
else:
    login = 'jogryn'
    psw = '511999'
InstagramAPI = InstagramAPI(login, psw)

print('Program from niceone.py GeoFriends.'
      ' \nIt checks all photos uploaded in entered period of time and finds if'
      ' somebody you might know was one of these people')
e = GeoFriends(InstagramAPI)
e.related_users('Old Town Lviv', 180)
print('People who you might know:')
print(e)
e.geo_pix('Old Town Lviv', 45)
print('All images posted in Old Town Lviv in last 45 minutes')
print(e)

print('Program from nicetwo.py RealFriends. \nFinds all users who liked selected media of entered user')
a = RealFriends(InstagramAPI)
a.likers_stats('inst_by_ukraine', timer='01/06/2017')
print('All users who liked pictures uploaded after 1st June 2017 by user "inst_by_ukraine"')
print(a)
print('How many of these photos user "jogryn" liked')
print(a.one_user_check('jogryn'))
print('Now it is time to add pictures of user "noutbukiukrayina" likers statistic to which will be shown')
a.handmade_stats('noutbukiukrayina')
print(a)
print('If you want to you can start following those who liked selected pictures\n'
      'It is useful when you check likers of your account and want to start follow people who like staff that you post')
a.follow_4_follow()
