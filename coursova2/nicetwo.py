#! /usr/bin/env python
# -*- coding: utf-8 -*-
from InstagramAPI import InstagramAPI
import users_likers_adt
import simplejson
import operator
try:
    import urllib2
except:
    import urllib.request
import time
from datetime import datetime
import getpass


class RealFriends:
    """
    Gets information about all users who liked your media
    """
    def __init__(self, api):
        """
        Initiates parameters of the class
        :param api: InstagramAPI(login, password)
        """
        self.current_stats = []
        self.api = api
        self.api.login()
        self.api.getSelfUserFeed()
        self.name = InstagramAPI.LastJson['items'][0]['user']['username']

    def _get_userid(self, user):
        """
        Converts str -> int
        :param user: str, username which will become user ID
        :return: int, user ID
        """
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
        """
        Converts string time into timestamp
        :param timer: str, date which will be converted
        :return: int, timestamp
        """
        try:
            timer = time.mktime(datetime.strptime(timer, "%d/%m/%Y").timetuple())
            return timer
        except ValueError:
            return '0'

    def handmade_stats(self, user=''):
        """
        Allows you to choose any images and shows user's who liked this media
        :param user: str, username if user == '' then user = login
        :return: list of users who liked image and how many images were selected
        """
        likers = {}
        if user == '':
            user = self.name
        try:
            lik = users_likers_adt.UsersLikers(user, self.api)
        except KeyError:
            print('This account is private')
            return 0
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
                    print(' WRONG INPUT, try again or press "Enter" to finish')
                    pass
            except IndexError:
                print(' WRONG INPUT, try again or press "Enter" to finish')
                pass
        for i in lik.all_added():
            for j in lik.media_likers(i):
                if j not in likers:
                    likers[j] = 1
                else:
                    likers[j] += 1
        likers = sorted(likers.items(), key=operator.itemgetter(1), reverse=True)
        self.current_stats = [likers, len(lik.all_added()), user]
        return self.current_stats

    def likers_stats(self, user='', timer='0', last_number=0):
        """
        Allows to add a group of images simultaneously
        :param user: str, username if user == '' then user = login
        :param timer: str, min time from which images were uploaded
        :param last_number: int, max number of newest images
        :return: list of users who liked image and how many images were selected
        >>> print(likers_stats(timer='01/06/2017')
        [[(u'inst_by_ukraine', 1), (u'acleadc', 1), (u'odegda_ukr', 1)], 9]

        >>> print (likers_stats(last_number=2))
        [[(u'inst_by_ukraine', 1), (u'acleadc', 1)], 2]
        """
        likers = {}
        if user == '':
            user = self.name
        try:
            inform = users_likers_adt.UsersLikers(user, self.api)
        except KeyError:
            print('This account is private')
            return 0
        if timer != '0':
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
        self.current_stats = [likers, len(items), user]
        return self.current_stats

    def one_user_check(self, user):
        """
        Creates string out of last given results about how many images user liked
        :return: str, how many pictures user liked
        """
        if self.current_stats == []:
            return "Selected images don't have likes"
        for i in self.current_stats[0]:
            if i[0] == user:
                return 'User ' + i[0] + ' liked ' + str(int(i[1] * 100 / self.current_stats[1])) + \
                          '%(' + str(i[1]) + '/' + str(self.current_stats[1]) + ') of selected images\n'
        return "This user didn't like selected images"

    def __str__(self):
        """
        Creates string out of last given results
        :return: str, how many pictures users liked
        """
        string = ''
        if self.current_stats == []:
            return "Selected images don't have likes"
        for i in self.current_stats[0]:
            string += 'User ' + i[0] + ' liked ' + str(int(i[1] * 100 / self.current_stats[1])) +\
                      '%(' + str(i[1]) + '/' + str(self.current_stats[1]) + ') of selected images\n'
        return string

    def follow_4_follow(self):
        """
        A little function to help you to start follow those users who like you
        The list of people who like you contains only those who liked images from your last request if you
        requested self media likers. Otherwise it will follow all people who liked your media and you don't follow them
        """
        InstagramAPI.getSelfUsersFollowing()
        following = InstagramAPI.LastJson
        following = [ad['username'] for ad in following['users']]
        if self.current_stats[2] != self.name:
            sure = raw_input(' Are you sure you want to follow ALL people who liked selected images? '
                             'Print "yes" to agree or press any button for no\n ')
            if sure == 'yes':
                self.likers_stats()
        else:
            sure = raw_input(' Are you sure you want to follow all people who liked selected images? '
                             'Print "yes" to agree or press any button for no\n ')
        if sure == 'yes':
            for i in self.current_stats[0]:
                if i[0] not in following:
                    InstagramAPI.follow(self._get_userid(i[0]))


if __name__ == "__main__":
    login = raw_input("Enter login or just press 'Enter' to use admin account: ")
    if login != '':
        psw = getpass.getpass('Password: ')
    else:
        login = 'jogryn'
        psw = '511999'
    InstagramAPI = InstagramAPI(login, psw)
    a = RealFriends(InstagramAPI)
    a.likers_stats('dzwinka_stepaniuk')#last_number=2)
    print(a)
    print(a.one_user_check('bartman109'))
    print(a.one_user_check('dutefron'))
    a.handmade_stats('dzwinka_stepaniuk')
    print(a)
    a.follow_4_follow()
