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
    def __init__(self, api):
        #self.login = login
        #self.psw = psw
        #InstagramAPI = InstagramAPI(login, psw)
        self.api = api
        self.api.login()

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

    def _media_time(self, item, past=30):
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
        #real_time = time.strftime('%d %b %Y %H:%M:%S GMT', time.gmtime(item['taken_at'])).split(' ')
        #dif2 = ((int(real_time[3][0:2]) + need) * 60) + int(real_time[3][3:5]) - \
        #      (int(upl_time[3][0:2]) * 60 + int(upl_time[3][3:5]))
        #print(dif2, upl_time, time.strftime('%d %b %Y %H:%M:%S GMT', time.gmtime(item['taken_at'])).split(' '))
        if abs(dif) < past:
            return ' '.join(upl_time[:-1])
        else:
            return False

    def geo_pix(self, place, past_time=30):
        users = []
        self.api.searchLocation(place)
        for i in self.api.LastJson['items']:
            print('-' + i['location']['name'])
            self.api.getLocationFeed(i['location']['pk'])
            for j in self.api.LastJson['items']:
                if self._media_time(j, past_time) is not False:
                    users.append([i['location']['name'], self._media_time(j, past_time), j['user']['username'],
                                  j['image_versions2']['candidates'][0]['url']])
        return users

    def related_users(self, place, past_time=30):
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
        return common


if __name__ == "__main__":
    login = raw_input("Enter login or just press 'Enter' to use admin account: ")
    if login != '':
        psw = getpass.getpass('Password: ')
    else:
        login = 'jogryn'
        psw = '511999'
    InstagramAPI = InstagramAPI(login, psw)
    e = Instagramer(InstagramAPI)
    print(e.related_users('Lviv Old Town', 200))
    print(e.geo_pix('Lviv Old Town', 200))



'''
InstagramAPI.tagFeed("dzvinka_if")
items = InstagramAPI.LastJson["items"]
count = 0
c2 = 0
for photo in items:
    c2 += 1
    InstagramAPI.getMediaLikers(photo["id"])
    for userLiker in InstagramAPI.LastJson["users"]:
        count += 1
        if userLiker["username"] == 'jogryn':
            print (userLiker["username"], photo['id'], count, c2, 'JOOOOOOOOOOOO')
            break
        print (userLiker["username"], photo['id'], count, c2)
'''
'''
#Get everybody who liked
InstagramAPI.getMediaLikers(media_id['items'][0]["id"])
c = 0
for userLiker in InstagramAPI.LastJson["users"]:
    c += 1
    print (userLiker["username"], c)
'''
