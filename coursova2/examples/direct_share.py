from InstagramAPI import InstagramAPI
user,pwd = 'jogryn', '111111'                        
InstagramAPI = InstagramAPI(user,pwd)       
InstagramAPI.login()                       
mediaId='1469246128528859784_1520706701'   
recipients = []                            
InstagramAPI.direct_share(mediaId, recipients,text='aquest es es darrer')
