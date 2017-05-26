from client import InstagramAPI

access_token = "5041771937.79a3467.7673f7a4abe049c5bbe229a4ad826316"
client_secret = "c3b09255b52847f3adeb9f823413ffe6"
user_id = "5041771937"#"79a3467592714815b2ab038172b2d2bf"
api = InstagramAPI(access_token = access_token, client_secret = client_secret)
#recent_media, next_ = api.user_recent_media(user_id=user_id, count=10)
#for media in recent_media:
#    print(media.caption.text)
#print(api.user(user_id))
#print(api.list_subscriptions())

#print(api.user_followed_by(user_id))
print ()
