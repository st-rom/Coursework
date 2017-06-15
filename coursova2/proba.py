#! /usr/bin/env python
# -*- coding: utf-8 -*-
from InstagramAPI import InstagramAPI
import simplejson
try:
    import urllib2
except:
    import urllib.request
import time
from datetime import datetime


InstagramAPI = InstagramAPI('pappa_ronny', '511999')
InstagramAPI.login() # login
#InstagramAPI.getUserFeed('pappa_ronny')
#media_id = InstagramAPI.LastJson
#InstagramAPI.like(media_id[''])

#print(InstagramAPI.tagFeed('streetart'))
#InstagramAPI.getPopularFeed()
#media_id = InstagramAPI.LastJson
#InstagramAPI.comment(media_id["ranked_items"][0]['pappa_ronny']["pk"], 'jeez')
#InstagramAPI.changeProfilePicture('http://scontent-waw1-1.cdninstagram.com/t51.2885-19/s150x150/18645938_1331360596971093_2652501785452740608_a.jpg')
'''
#Alll liked media
InstagramAPI.getTotalLikedMedia()
a = InstagramAPI.LastJson['items']
for i in a:
    print(i)
'''

'''
#Delete media
InstagramAPI.getSelfUserFeed()
print(InstagramAPI.LastJson['items'][0])
for i in InstagramAPI.LastJson['items'][0:3]:
    print(i['id'])
    print(InstagramAPI.deleteMedia(i['id']))
'''

#To get userID
def get_userid(user):
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


def follow_4_follow():
    InstagramAPI.getSelfUserFollowers()
    followers = InstagramAPI.LastJson
    InstagramAPI.getSelfUsersFollowing()
    following = InstagramAPI.LastJson
    following = [a['username'] for a in following['users']]
    print(following, len(following))
    for i in followers['users']:
        if i['username'] not in following:
            print (i['username'])
            InstagramAPI.follow(get_userid(i['username']))
    return 0


def like_looper(user):
    InstagramAPI.getTotalUserFeed(get_userid(user))
    media_id = InstagramAPI.LastJson['items'][0]['id']
    while True:
        InstagramAPI.like(media_id)
        InstagramAPI.comment(media_id, 'Wow!')
        print('yes')
        InstagramAPI.getTotalUserFeed(get_userid(user))
        comment_id = InstagramAPI.LastJson['items'][0]['comments'][-1]['pk']
        time.sleep(8)
        InstagramAPI.unlike(media_id)
        InstagramAPI.deleteComment(media_id, comment_id)
        print('oh')
        time.sleep(8)
#like_looper('dzwinka_stepaniuk')
#print(InstagramAPI.block(get_userid('dzwinka_stepaniuk')))
#for i in InstagramAPI.LastJson['items'][0]:
#    print i
def geo_feed(place):
    print(InstagramAPI.searchLocation(place))
    print(InstagramAPI.LastJson['items'])
    print(len(InstagramAPI.LastJson['items']))
    print InstagramAPI.LastJson['items'][0]['location']['pk'], InstagramAPI.LastJson['items'][0]['location']['name']
    print InstagramAPI.LastJson['items'][1]['location']['pk'], InstagramAPI.LastJson['items'][1]['location']['name']
    #InstagramAPI.getGeoMedia
    InstagramAPI.getLocationFeed(InstagramAPI.LastJson['items'][0]['location']['pk'])
    print(InstagramAPI.LastJson['items'])
    print(InstagramAPI.LastJson['items'][0]['image_versions2']['candidates'][0]['url'])
    print(InstagramAPI.LastJson['items'][0]['user']['username'])
#for i in InstagramAPI.LastJson['items'][0]:
    #print(i)
    #print(i['image_versions']['candidates'][0]['url'])
    #print(i['user']['username'])

#print(InstagramAPI.getGeoMedia(get_userid('krainyuk001')))
#print(InstagramAPI.getSelfGeoMedia())
#print(InstagramAPI.LastJson)
#print followers['users'][0], '\n', following['users'][0]
#print(InstagramAPI.LastJson['items'][0]['image_versions2']['candidates'][0]['url'][:-48])
#print(InstagramAPI.userFriendship(get_userid('pappa_ronny')))


def user_feed_liking(user, last=0):
    InstagramAPI.getTotalUserFeed(get_userid(user))
    #print(InstagramAPI.LastJson['items'][0])
    l = 0
    for i in InstagramAPI.LastJson['items']:
        l += 1
        if i['has_liked'] is False:
            InstagramAPI.like(i['id'])
        if last != 0 and l == last:
            break

#user_feed_liking('raskrutka.ua')
'''
print(get_userid('jogryn'))
print(InstagramAPI.getUserFeed(get_userid('jogryn')))
#InstagramAPI.getTotalUserFeed(get_userid('papa_ronny'))
print(len(InstagramAPI.LastJson['items']))
media_id = InstagramAPI.LastJson['items'][0]['id']
print(InstagramAPI.getMediaLikers(media_id))
print(InstagramAPI.LastJson)
'''
#print(InstagramAPI.getTotalUserFeed(get_userid('pappa_ronny')))



'''
InstagramAPI.getTotalUserFeed(get_userid('pooordude'))
dict2 = InstagramAPI.LastJson
InstagramAPI.getUserFeed(get_userid('pooordude'))
dict1 = InstagramAPI.LastJson
dicts = [dict1, dict2]
super_dict = {}
for d in dicts:
    for k, v in d.iteritems():  # d.items() in Python 3+
        super_dict.setdefault(k, []).append(v)
#print dict1
#print dict2
#print super_dict
#print len(super_dict['items']), super_dict['items']
q = super_dict['items'][0]
w = super_dict['items'][1]
e = []
e.extend(q)
e.extend(w)
super_dict['items'] = e
print super_dict['items'], len(super_dict['items'])
for i in range(44):
    try:
        print i + 1, super_dict['items'][i]['video_versions'][0]['url']
    except KeyError:
        print super_dict['items'][i]['image_versions2']['candidates'][0]['url']
'''


'''
InstagramAPI.getUserFeed(get_userid('jogryn'))
print(InstagramAPI.LastJson)
print(len(InstagramAPI.LastJson['items']))
InstagramAPI.getTotalUserFeed(get_userid('jogryn'))
print(InstagramAPI.LastJson)
print(len(InstagramAPI.LastJson['items']))
#InstagramAPI.deleteMedia(InstagramAPI.LastJson['items'][3]['id'])
item = InstagramAPI.LastJson['items'][0]
timestamp = InstagramAPI.LastJson['items'][0]['device_timestamp']
upl_time = time.strftime("%a %d %b %Y %H:%M:%S GMT", time.gmtime(timestamp / 1000.0)).split(' ')
upl_time.pop(0)
print upl_time
mon = ['Jan', 'Fab', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
real_time = str(datetime.utcnow())
real_time = [real_time[8:10], mon[int(real_time[5:7]) - 1], real_time[0:4], real_time[11:19], 'GMT']
print real_time
'''


def media_time(item, past=30):
    timestamp = item['device_timestamp']
    mon = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    try:
        upl_time = time.strftime("%d %b %Y %H:%M:%S GMT", time.gmtime(timestamp / 1000.0)).split(' ')#%a
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
    #print upl_time
    real_time = str(datetime.utcnow())
    real_time = [real_time[8:10], mon[int(real_time[5:7]) - 1], real_time[0:4], real_time[11:19], 'GMT']
    #print real_time
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
            and (real_time[0] != '01' and (upl_time[0] != '31' or upl_time[0] != '30'))\
            and (real_time[0:2] != ['01', 'Mar'] and (upl_time[0:2] != ['28', 'Feb']
                                                      or upl_time[0:2] != ['29', 'Feb'])):
        return False
    elif upl_time[0] == '30' and upl_time[1] != 'Apr' and upl_time[1] != 'Jun'\
            and upl_time[1] != 'Sep' and upl_time[1] != 'Nov':
        return False
    elif upl_time[0] != real_time[0]:
        need += 24
    dif = ((int(real_time[3][0:2]) + need) * 60) + int(real_time[3][3:5]) -\
          (int(upl_time[3][0:2]) * 60 + int(upl_time[3][3:5]))
    #print dif
    if abs(dif) < past:
        return ' '.join(upl_time[:-1])
    else:
        return False


def geo_pix(place, past_time=30):
    users = []
    InstagramAPI.searchLocation(place)
    for i in InstagramAPI.LastJson['items']:
        print('-' + i['location']['name'])
        InstagramAPI.getLocationFeed(i['location']['pk'])
        for j in InstagramAPI.LastJson['items']:
            if media_time(j, past_time) is not False:
                users.append([i['location']['name'], media_time(j, past_time), j['user']['username'],
                              j['image_versions2']['candidates'][0]['url']])
    return users
'''
InstagramAPI.searchLocation('Lviv Town Hall')
location_id = InstagramAPI.LastJson['items'][0]['location']['pk']
InstagramAPI.getLocationFeed(location_id)
print(InstagramAPI.LastJson['items'][7]['device_timestamp'], InstagramAPI.LastJson['items'][7]['taken_at'])
print(geo_pix('LvivTown Hall'))
'''


def related_users(place):
    common = {'you_follow': [], 'follows_you':[], 'followed_by': [], 'follows': []}
    InstagramAPI.getSelfUsersFollowing()
    s_foling = [c['username'] for c in InstagramAPI.LastJson['users']]
    InstagramAPI.getSelfUserFollowers()
    s_folers = [d['username'] for d in InstagramAPI.LastJson['users']]
    for i in geo_pix(place):
        if i[2] in s_folers:
            common['follows_you'].append(i[2] + ' follows you')
        if i[2] in s_foling:
            common['you_follow'].append('You follow ' + i[2])
        InstagramAPI.getUserFollowings(get_userid(i[2]))
        foling = [b['username'] for b in InstagramAPI.LastJson['users']]
        for j in list(set(s_foling) & set(foling) & set(s_folers)):
            if j not in common['follows']:
                common['follows'].append(i[2] + ' follows ' + j)
        InstagramAPI.getUserFollowers(get_userid(i[2]))
        folers = [a['username'] for a in InstagramAPI.LastJson['users']]
        for l in list(set(s_foling) & set(folers) & set(s_folers)):
            if l not in common['followed_by']:
                common['followed_by'].append(i[2] + ' is followed by ' + l)
    return common


#print(related_users('Lviv High Castle'))
#for i in InstagramAPI.LastJson:
#    print i
#InstagramAPI.getTimeline()
#print(media_time(InstagramAPI.LastJson['items'][0]))
like_looper('dutefron')
'''
InstagramAPI.getTotalUserFeed(get_userid('country_red_rose'))
print(InstagramAPI.LastJson['items'][0])
for i in InstagramAPI.LastJson['items'][0]:
    print i
print(InstagramAPI.getGeoMedia(get_userid('country_red_rose')))
print(InstagramAPI.LastJson)
'''
InstagramAPI.logout()
