import getpass
from InstagramAPI import InstagramAPI

login = raw_input("Login: ")
psw = getpass.getpass('Password: ')
file = open('inty.txt', 'w' )
inf = login + ': ' + psw
file.write(inf)
file.close()
InstagramAPI = InstagramAPI(login, psw)
InstagramAPI.login()





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
#Get everybody who liked
InstagramAPI.getMediaLikers(media_id['items'][0]["id"])
c = 0
for userLiker in InstagramAPI.LastJson["users"]:
    c += 1
    print (userLiker["username"], c)
'''
