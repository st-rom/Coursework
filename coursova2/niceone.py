#! /usr/bin/env python
# -*- coding: utf-8 -*-
from InstagramAPI import InstagramAPI
import simplejson
try:
    import urllib2
except ImportError:
    import urllib.request
import time
from datetime import datetime
import getpass


class Instagramer:
    '''
    Finds people who took a photo near some location an past x minutes and shows
     if they have some friends in common with you
    '''
    def __init__(self, api):
        '''
        Initiates parameters of the class
        :param api: InstagramAPI(login, password)
        '''
        self.api = api
        self.api.login()
        self.last_result = ''

    def _get_userid(self, user):
        '''
        Converts str -> int
        :param user: str, username which will become user ID
        :return: int, user ID
        '''
        #print(user)
        info = 'https://www.instagram.com/' + user + '/?__a=1'
        try:
            webpage = urllib2.urlopen(info)
            for line in webpage:
                web_info = line.decode('utf-8')
            webpage.close()
        except NameError:
            with urllib.request.urlopen(info) as webpage:
                for line in webpage:
                    web_info = line.decode('utf-8')
        info = simplejson.loads(web_info)
        usernameID2 = info['user']['id']
        return usernameID2

    def _media_time(self, item, past=30):
        '''
        Compares time when picture was taken and real time and returns date string
        :param item: dict, media object which will be checked
        :param past: int, max time difference in minutes between upload time and time now
        :return: string, if image feets in time and False otherwise
        '''
        timestamp = item['device_timestamp']
        mon = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        try:
            upl_time = time.strftime("%d %b %Y %H:%M:%S GMT", time.gmtime(timestamp / 1000.0)).split(' ')  # %a
        except ValueError:
            timestamp = item['taken_at']
            upl_time = time.strftime("%d %b %Y %H:%M:%S GMT", time.gmtime(timestamp / 1000.0)).split(' ')  # %a
        if int(upl_time[2]) < 2005 or int(upl_time[2]) > 2018:
            try:
                upl_time = time.strftime('%d %b %Y %H:%M:%S GMT', time.gmtime(timestamp)).split(' ')
            except ValueError:
                timestamp = item['taken_at']
                upl_time = time.strftime('%d %b %Y %H:%M:%S GMT', time.gmtime(timestamp)).split(' ')
            if int(upl_time[2]) < 2005 or int(upl_time[2]) > 2018:
                timestamp = item['taken_at']
                upl_time = time.strftime('%d %b %Y %H:%M:%S GMT', time.gmtime(timestamp)).split(' ')
        # print upl_time
        real_time = str(datetime.utcnow())
        real_time = [real_time[8:10], mon[int(real_time[5:7]) - 1], real_time[0:4], real_time[11:19], 'GMT']
        # print real_time
        need = 0
        if upl_time[2] == real_time[2]:
            pass
        elif int(real_time[2]) - int(upl_time[2]) == 1 \
                and real_time[0:2] == ['01', 'Jan'] and upl_time[0:2] == ['31', 'Dec']:
            pass
        else:
            return False
        if upl_time[1] == real_time[1]:
            pass
        elif mon.index(real_time[1]) - mon.index(upl_time[1]) != 1 \
                and mon.index(real_time[1]) - mon.index(upl_time[1]) != -11:
            return False
        elif (real_time[0] != '01' and (upl_time[0] != '31' or upl_time[0] != '30')) \
                and (real_time[0:2] != ['01', 'Mar'] and (upl_time[0:2] != ['28', 'Feb']
                                                          or upl_time[0:2] != ['29', 'Feb'])):
            return False
        if upl_time[0] != real_time[0] and int(real_time[0]) - int(upl_time[0]) != 1 \
                and (real_time[0] != '01' and (upl_time[0] != '31' or upl_time[0] != '30')) \
                and (real_time[0:2] != ['01', 'Mar'] and (upl_time[0:2] != ['28', 'Feb']
                                                          or upl_time[0:2] != ['29', 'Feb'])):
            return False
        elif upl_time[0] == '30' and upl_time[1] != 'Apr' and upl_time[1] != 'Jun' \
                and upl_time[1] != 'Sep' and upl_time[1] != 'Nov':
            return False
        elif upl_time[0] != real_time[0]:
            need += 24
        dif = ((int(real_time[3][0:2]) + need) * 60) + int(real_time[3][3:5]) - \
              (int(upl_time[3][0:2]) * 60 + int(upl_time[3][3:5]))
        # print dif
        if abs(dif) < past:
            return ' '.join(upl_time[:-1])
        else:
            return False

    def geo_pix(self, place, past_time=30):
        """
        Returns all images and some information about them which were taken less than past_time ago
        :param place: str, place were images were taken
        :param past_time: int, max time difference in minutes between upload time and time now
        :return: list of lists, some info about image
        >>> print(self.geo_pix('Statue of Liberty'))
         [u'Statue Of Liberty, Liberty Island, New York City', '15 Jun 2017 03:52:11', u'ysabelvictoriabenitez',
          u'http://scontent-waw1-1.cdninstagram.com/t51.2885-15/e35/19122435_874202616044765_3289123171168419840_n.jpg?ig_cache_key=MTUzNzQ1MzgxMzM2Mzc0NDc4Mw%3D%3D.2&se=7'],
          [u'Liberty Island', '15 Jun 2017 02:49:45', u'sh.ocean', u'http://scontent-waw1-1.cdninstagram.com/t51.2885-15/e35/19122241_1417151758367601_7876705605497389056_n.jpg?ig_cache_key=MTUzNzQyMTM5OTAxODQ2MjYzNw%3D%3D.2&se=7'],
           [u'Liberty Island', '15 Jun 2017 01:42:43', u'guzhixuan', u'http://scontent-waw1-1.cdninstagram.com/t51.2885-15/e35/19120567_233572653812503_8067180808005222400_n.jpg?ig_cache_key=MTUzNzM4ODgzNjA1Mjk5NTcwMg%3D%3D.2&se=7']]

        >>> print(self.geo_pix('High Castle', 15))
        [u'Lviv High Castle', '15 Jun 2017 03:52:11', u'ysabelvictoriabenitez',
          u'http://scontent-waw1-1.cdninstagram.com/t51.2885-15/e35/19122435_874202616044765_3289123171168419840_n.jpg?ig_cache_key=MTUzNzQ1MzgxMzM2Mzc0NDc4Mw%3D%3D.2&se=7']]
        """
        users = []
        self.api.searchLocation(place)
        loader = ' '
        for i in self.api.LastJson['items']:
            # print('-' + i['location']['name'])
            if len(loader) < 4:
                loader += '*'
                print(loader)
            else:
                loader = ' *'
                print(loader)
            self.api.getLocationFeed(i['location']['pk'])
            for j in self.api.LastJson['items']:
                if self._media_time(j, past_time) is not False:
                    users.append([i['location']['name'], self._media_time(j, past_time), j['user']['username'],
                                  j['image_versions2']['candidates'][0]['url']])
        self.last_result = users
        return users

    def related_users(self, place, past_time=30):
        """
        Returns dictionary which contains information about
        any connections between you and people who took photos in entered place
        :param place: str, where photos were taken at
        :param past_time: int, max time difference in minutes between upload time and time now
        :return: dict, information about connections

        >>> print(related_users('Lviv Town Hall'))
        {'follows': [], 'you_follow': ['kolja_mak'], 'followed_by': ['lena200 is followed by jerony777'], 'follows_you': []}

        >>> print(related_users('Lviv Town Hall'))
        {'follows': [], 'you_follow': ['ulik_ren'], 'followed_by': [], 'follows_you': []}
        """
        common = {'you_follow': [], 'follows_you': [], 'followed_by': [], 'follows': []}
        self.api.getSelfUsersFollowing()
        s_foling = [c['username'] for c in self.api.LastJson['users']]
        self.api.getSelfUserFollowers()
        s_folers = [d['username'] for d in self.api.LastJson['users']]
        for i in self.geo_pix(place, past_time):
            if i[2] in s_folers:
                common['follows_you'].append(i[2] + ' follows you')
            if i[2] in s_foling:
                common['you_follow'].append('You follow ' + i[2])
            self.api.getUserFollowings(self._get_userid(i[2]))
            foling = [b['username'] for b in self.api.LastJson['users']]
            for j in list(set(s_foling) & set(foling) & set(s_folers)):
                if i[2] + ' follows ' + j not in common['follows']:
                    common['follows'].append(i[2] + ' follows ' + j)
            self.api.getUserFollowers(self._get_userid(i[2]))
            folers = [a['username'] for a in self.api.LastJson['users']]
            for l in list(set(s_foling) & set(folers) & set(s_folers)):
                if i[2] + ' is followed by ' + l not in common['followed_by']:
                    common['followed_by'].append(i[2] + ' is followed by ' + l)
        self.last_result = common
        return common

    def __str__(self):
        """
        Creates string out of last results that were done
        :return: str, information about last operation
        """
        string = ''
        if type(self.last_result) == dict:
            for i in self.last_result:
                if self.last_result[i] != []:
                    string += self.last_result[i] + '\n'
        elif type(self.last_result) == list:
            for i in self.last_result:
                string += 'At ' + i[1] + ' GMT user ' + i[2] + ' uploaded photo near ' + i[0] + ': ' + i[3] + '\n'
        return string


if __name__ == "__main__":
    login = raw_input("Enter login or just press 'Enter' to use admin account: ")
    if login != '':
        psw = getpass.getpass('Password: ')
    else:
        login = 'jogryn'
        psw = '511999'
    InstagramAPI = InstagramAPI(login, psw)
    e = Instagramer(InstagramAPI)
    e.related_users('Old Town Lviv', 200)
    print(e)
    e.geo_pix('Old Town Lviv', 200)
    print(e)
