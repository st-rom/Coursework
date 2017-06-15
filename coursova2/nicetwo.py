#! /usr/bin/env python
# -*- coding: utf-8 -*-
from InstagramAPI import InstagramAPI
import users_likers_adt
import simplejson
import operator
try:
    import urllib2
except ImportError:
    import urllib.request
import time
from datetime import datetime
import getpass


class RealFriends:
    def __init__(self, api):
        self.current_stats = []
        self.api = api
        self.api.login()
        self.api.getSelfUserFeed()
        self.name = InstagramAPI.LastJson['items'][0]['user']['username']

    def _get_userid(self, user):
        info = 'https://www.instagram.com/' + user + '/?__a=1'
        try:
            webpage = urllib2.urlopen(info)
            for line in webpage:
                web_info = line.decode('utf-8')
            webpage.close()
        except:
            with urllib.request.urlopen(info) as webpage:
                for line in webpage:
                    web_info = line.decode('utf-8')
        info = simplejson.loads(web_info)
        usernameID2 = info['user']['id']
        return usernameID2

    def _time_converter(self, timer):
        try:
            timer = time.mktime(datetime.strptime(timer, "%d/%m/%Y").timetuple())
            return timer
        except ValueError:
            return '0'

    def handmade_stats(self):
        likers = {}
        lik = users_likers_adt.UsersLikers(self.name, self.api)
        inp = ' '
        while inp != '':
            inp = raw_input(' Enter the number of image you want to add(from newest to oldest) '
                            '\n or enter two numbers divided  by space to add all images in '
                            'that range(for example: "3 7").\n Press "Enter" to finish\n ')
            try:
                if inp == '':
                    break
                elif len(inp.split(' ')) == 2:
                    lik.add(int(inp.split(' ')[0]), int(inp.split(' ')[-1]))
                elif inp.isdigit():
                    lik.add(int(inp))
                else:
                    print(' Wrong input, try again or press "Enter" to finish')
                    pass
            except IndexError:
                print(' Wrong input, try again or press "Enter" to finish')
                pass
        for i in lik.all_added():
            for j in lik.media_likers(i):
                if j not in likers:
                    likers[j] = 1
                else:
                    likers[j] += 1
        likers = sorted(likers.items(), key=operator.itemgetter(1), reverse=True)
        self.current_stats = [likers, len(lik.all_added())]
        return self.current_stats

    def likers_stats(self, timer='0', last_number=0):
        likers = {}
        inform = users_likers_adt.UsersLikers(self.name, self.api)
        if timer != '0':
            InstagramAPI.getTotalSelfUserFeed()
            items = [t + 1 for t in range(len(inform.info))
                     if self._time_converter(timer) < inform.info[t]['taken_at']]
        elif last_number != 0:
            inform.add(1, last_number)
            items = inform.all_added()
        else:
            inform.add()
            items = inform.all_added()
        for i in items:
            for j in inform.media_likers(i):
                if j not in likers:
                    likers[j] = 1
                else:
                    likers[j] += 1
        likers = sorted(likers.items(), key=operator.itemgetter(1), reverse=True)
        self.current_stats = [likers, len(items)]
        return self.current_stats

    def __str__(self):
        string = ''
        for i in self.current_stats[0]:
            string += 'User ' + i[0] + ' liked ' + str(int(i[1] * 100 / self.current_stats[1])) +\
                      '%(' + str(i[1]) + ') of selected images\n'
        return string

    def follow_4_follow(self):
        InstagramAPI.getSelfUserFollowers()
        followers = InstagramAPI.LastJson
        InstagramAPI.getSelfUsersFollowing()
        following = InstagramAPI.LastJson
        following = [ad['username'] for ad in following['users']]
        for i in followers['users']:
            if i['username'] not in following:
                InstagramAPI.follow(self._get_userid(i['username']))

if __name__ == "__main__":
    login = raw_input("Enter login or just press 'Enter' to use admin account: ")
    if login != '':
        psw = getpass.getpass('Password: ')
    else:
        login = 'jogryn'
        psw = '511999'
    InstagramAPI = InstagramAPI(login, psw)
    a = RealFriends(InstagramAPI)
    a.likers_stats('01/06/2017')
    print(a)
    a.handmade_stats()
    print(a)
