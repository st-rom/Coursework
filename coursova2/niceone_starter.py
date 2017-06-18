#! /usr/bin/env python
# -*- coding: utf-8 -*-
import getpass
from InstagramAPI import InstagramAPI
from niceone import GeoFriends

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
gf = GeoFriends(InstagramAPI)
cont = ''
while cont != 'no':
    what_to_do = raw_input('If you want to check the location for friends who might be there print "1",'
                           '\nelse if you just want to see pictures from that place print "2" ')
    if what_to_do == '1':
        place = raw_input('Enter the name of place you want to check for friends: ')
        time = raw_input('If you want to get this information for different period of time than last 30 minutes'
                         'enter number of last minutes you want to see pictures for instead'
                         ' else just press "Enter" ')
        if time != '':
            gf.related_users(place, int(time))
            print(gf)
        elif time.isdigit() is False:
            print('Wrong input, try again')
        else:
            gf.related_users(place)
            print(gf)
    elif what_to_do == '2':
        place = raw_input('Enter the name of place you want to check for uploads: ')
        time = raw_input('If you want to get this information for different period of time than last 30 minutes'
                         'enter number of last minutes you want to see pictures for instead'
                         ' else just press "Enter" ')
        if time != '':
            gf.geo_pix(place, int(time))
            print(gf)
        elif time.isdigit() is False:
            print('Wrong input, try again')
        else:
            gf.geo_pix(place)
            print(gf)
    cont = raw_input('If you want to try again press any key. \nTo end this program print "no" ')
