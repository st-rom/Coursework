
from InstagramAPI import InstagramAPI
import urllib
InstagramAPI = InstagramAPI("jogryn", "511999")
InstagramAPI.login()
InstagramAPI.timelineFeed()
video_url = InstagramAPI.LastJson['items'][5]['video_versions'][0]['url']
video_local_path = video_url.split("/")[-1]
thumbnail_url = InstagramAPI.LastJson['items'][0]['image_versions2']['candidates'][0]['url'][:-48]
thumbnail_local_path = thumbnail_url.split("/")[-1]

urllib.urlretrieve(video_url,video_local_path)
urllib.urlretrieve(thumbnail_url,thumbnail_local_path)
#1:47 13-06
user,pwd = 'jogryn', '511999'

#InstagramAPI = InstagramAPI(user, pwd)
#InstagramAPI.login() # login
print video_local_path, thumbnail_local_path, video_url, thumbnail_url
#print(InstagramAPI.changeProfilePicture(thumbnail_local_path))
#print(InstagramAPI.uploadVideo(video_local_path, thumbnail_local_path))
print(InstagramAPI.uploadPhoto(thumbnail_local_path, '#fol4fol'))
