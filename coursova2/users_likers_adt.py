#! /usr/bin/env python
# -*- coding: utf-8 -*-
from InstagramAPI import InstagramAPI
import simplejson
from node import *
try:
    import urllib2
except:
    import urllib.request


class UsersLikers:
    '''
    This ADT helps to add images of the user to the node
    for more convenient usage in future
    '''
    def __init__(self, user, api):
        '''
        Initiates parameters
        :param user: str, username
        :param api: InstagramAPI(login, password)
        '''
        self.user = self._get_userid(user)
        self.api = api
        self.list_of_added = []
        self.api.login()
        self.api.getTotalUserFeed(self.user)
        dict2 = self.api.LastJson
        self.api.getUserFeed(self.user)
        dict1 = self.api.LastJson
        dicts = [dict1, dict2]
        super_dict = {}
        for d in dicts:
            for k, v in d.iteritems():  # d.items() in Python 3+
                super_dict.setdefault(k, []).append(v)
        q = super_dict['items'][0]
        w = super_dict['items'][1]
        for cl in q:
            cl.pop('organic_tracking_token', None)
        for cl in w:
            cl.pop('organic_tracking_token', None)
        if str(q) == str(w):
            e = q
        else:
            e = []
            e.extend(q)
            e.extend(w)
        super_dict['items'] = e
        self.info = super_dict['items']
        self._head = None

    def add(self, v1=0, v2=0):
        """
        Adds the value.
        If v1 = 0 and v2 ==0 adds all user's images
        :param v1: the value to be added or in case if v2 != 0 the value from which all images will be added up to v2
        :param v2: the value to which numbers will be added.
        >>> print(self.add())
        {1: [u'inst_by_ukraine'], 2: [u'acleadc'], 3: []}

        >>> print(self.add(-1))
        {3: []}

        >>> print(self.add(-3, -2))
        {1: [u'inst_by_ukraine'], 2: [u'acleadc']}
        """
        if v1 < 0:
            v1 += len(self.info) + 1
        elif v1 == 0:
            v1 = 1
            if v2 == 0:
                v2 = len(self.info)
        if v2 == 0:
            v2 = v1
        elif v2 < 0:
            v2 += len(self.info) + 1
        for value in range(v1, v2 + 1):
            if value not in self.list_of_added:
                media_id = self.info[value - 1]['id']
                self.api.getMediaLikers(media_id)
                if self._head is None:
                    self._head = Node({value: [i['username'] for i in self.api.LastJson['users']]})
                else:
                    rest = self._head
                    self._head = Node({value: [i['username'] for i in self.api.LastJson['users']]})
                    self._head.next = rest
                self.list_of_added.append(value)
            else:
                pass

    def all_added(self):
        '''
        Creates dictionary with image's numbers as keys and users who liked it as value
        :return: dict, users who liked image
        '''
        h = self._head
        dict_of_pix = {}
        while h is not None:
            dict_of_pix[int(str(h))] = h.item[int(str(h))]
            h = h.next
        return dict_of_pix

    def _get_userid(self, user):
        '''
        Converts str -> int
        :param user: str, username which will become user ID
        :return: int, user ID
        '''
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

    def media_likers(self, numb):
        '''
        Returns list of usernames of users who liked media
        :param numb: int, number of image starting from the newest uploads
        :return: list of strings
        >>> self.media_likers(4)
        [u'anticafelv', u'pappa_ronny', u'aksesuaru_pasaule']

        >>> self.media_likers(-1)
        [u'aksesuaru_pasaule']
        '''
        if numb < 0:
            media_id = self.info[len(self.info) + numb]['id']
        else:
            media_id = self.info[numb - 1]['id']
        self.api.getMediaLikers(media_id)
        us = []
        for i in self.api.LastJson['users']:
            us.append(i['username'])
        return us

    def __str__(self):
        '''
        Creates string
        :return: str, list of added images and numbers of users who liked that image
        '''
        h = self._head
        string = ''
        i = 0
        while h is not None:
            try:
                string += str(h) + ' - ' + self.info[int(str(h)) - 1]['video_versions'][0]['url'] + \
                          ': ' + str(len(h)) + ' known likes\n'
            except KeyError:
                string += str(h) + ' - ' + self.info[int(str(h)) - 1]['image_versions2']['candidates'][0]['url'] +\
                     ': ' + str(len(h)) + ' known likes\n'
            i += 1
            h = h.next
        return string

if __name__ == "__main__":
    InstagramAPI = InstagramAPI("jogryn", "511999")
    a = UsersLikers('pappa_ronny', InstagramAPI)
    #a.add(4)
    a.add(1, 2)
    #a.add(5, 6)
    #a.add(-3, -1)
    #a.add(-2)
    #a.add()
    print(a.all_added())
    print(a)
    print(a.media_likers(-2))
