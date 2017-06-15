from InstagramAPI import InstagramAPI
import simplejson
from node import *
try:
    import urllib2
except:
    import urllib.request





class UsersLikers:
    def __init__(self, user, api):
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
        :param v1: the value to be added.
        :param v2: the value to be added.
        """
        if v1 < 0:
            v1 += len(self.info) + 1
        elif v1 == 0:
            v1 = 1
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
        h = self._head
        dict_of_pix = {}
        while h is not None:
            dict_of_pix[int(str(h))] = h.item[int(str(h))]
            h = h.next
        return dict_of_pix

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

    def media_likers(self, numb):
        media_id = self.info[numb - 1]['id']
        self.api.getMediaLikers(media_id)
        us = []
        for i in self.api.LastJson['users']:
            us.append(i['username'])
        return us

    def __str__(self):
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
        print(self.info)
        return string

if __name__ == "__main__":
    InstagramAPI = InstagramAPI("pappa_ronny", "511999")
    a = UsersLikers('jogryn', InstagramAPI)
    a.add(4)
    a.add(1)
    a.add(5, 6)
    a.add(-3, -1)
    a.add(-2)
    a.add()
    print(a.all_added())
    print(a)
    print(a.media_likers(11))
