#! /usr/bin/env python
# -*- coding: utf-8 -*-
import getpass
from InstagramAPI import InstagramAPI
from nicetwo import RealFriends

login = raw_input("Enter login or just press 'Enter' to use admin account: ")
if login != '':
    print('Do not worry, your password is safe. It is invisible right now for safety measures so keep entering it')
    psw = getpass.getpass('Password: ')
else:
    login = 'jogryn'
    psw = '511999'
InstagramAPI = InstagramAPI(login, psw)

f = RealFriends(InstagramAPI)
print('Program from nicetwo.py RealFriends. \nFinds all users who liked selected media of entered user')
cont = ''
while cont != 'no':
    err = False
    user = raw_input('Enter the name of the user whose account likers you want to check'
                     '\nor just press "Enter" to check account with which you have logged in ')
    how = raw_input('If you want to check likers of all pictures of selected user press "Enter"\n'
                    'else if you want to add pictures that were uploaded later than some date enter that date like in '
                    'example: "01/06/2017"\nelse if you want to add some chosen pictures by yourself print "1" ')
    if how == '':
        f.likers_stats(user)
    elif '/' in how:
        f.likers_stats(user, timer=how)
    elif how == '1':
        f.handmade_stats(user)
    else:
        err = True
        print('Wrong input, try again')
    if err is False:
        numb = raw_input('Now you can see statistic of all users who liked selected media '
                         'or see it for selected users\nPrint "s" to select users or press "Enter" to see all likers ')
        if numb == '':
            print(f)
        elif numb == 's':
            stop = ' '
            while stop != '':
                if stop != ' ':
                    one_u = stop
                else:
                    one_u = raw_input("Enter user's login ")
                print(f.one_user_check(one_u))
                stop = raw_input('If you want to see statistic for another user enter his login'
                                 ' or press "Enter" to end this ')
        else:
            err = True
            print('Wrong input, try again')
    if err is False and (user == login or user == ''):
        fol = raw_input('Now you can start follow some people who liked your selected images.'
                        '\nEnter min percentage of pictures user had to like for you to start following him '
                        'or just enter his login\n'
                        'If you do not want to do this just press "Enter" ')
        if fol.isdigit() is False:
            en = ' '
            while en != '':
                if en != ' ':
                    fol = en
                f.follow_4_follow(user=fol)
                en = raw_input('If you want to follow another user enter his login else press "Enter" ')
        elif fol.isdigit():
            f.follow_4_follow(fol)
    cont = raw_input('If you want to try this program again press any key. \nTo end this program print "no" ')
