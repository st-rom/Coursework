from InstagramAPI import InstagramAPI
import urllib
#import proba
#username2 = input('Enter username: ')
#info = 'https://www.instagram.com/' + username2 + '/?__a=1'
InstagramAPI = InstagramAPI("jogryn", "511999")
InstagramAPI.login() # login
InstagramAPI.getTimeline()
thumbnail_url = InstagramAPI.LastJson['items'][0]['image_versions2']['candidates'][0]['url'][:-48]
thumbnail_local_path = thumbnail_url.split("/")[-1]
urllib.urlretrieve(thumbnail_url,thumbnail_local_path)
print(InstagramAPI.uploadPhoto(thumbnail_local_path, '#fol4fol'))
