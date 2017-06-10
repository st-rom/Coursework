from InstagramAPI import InstagramAPI
import simplejson
try:
    import urllib2
except:
    import urllib.request
import time

InstagramAPI = InstagramAPI("jogryn", "511999")
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
        InstagramAPI.getTotalUserFeed(get_userid(user))
        comment_id = InstagramAPI.LastJson['items'][0]['comments'][-1]['pk']
        #print('yes')
        time.sleep(8)
        InstagramAPI.unlike(media_id)
        InstagramAPI.deleteComment(media_id, comment_id)
        #print('oh')
        time.sleep(8)

#for i in InstagramAPI.LastJson['items'][0]:
#    print i
def geo_feed():
    print(InstagramAPI.searchLocation('\xd0\x92\xd0\xb8\xd1\x81\xd0\xbe\xd0\xba\xd0\xb8\xd0\xb9 \xd0\xb7\xd0\xb0\xd0\xbc\xd0\xbe\xd0\xba \xd0\x9b\xd1\x8c\xd0\xb2\xd1\x96\xd0\xb2'))
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
print(InstagramAPI.
print(InstagramAPI.LastJson)
