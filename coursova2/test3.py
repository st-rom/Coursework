import urllib2
import simplejson
info = 'https://www.instagram.com/jogryn/?__a=1'
webpage = urllib2.urlopen(info)
for line in webpage:
    web_info = line.encode('cp1251').decode('utf-8')
webpage.close()
print(web_info)
info = simplejson.loads(web_info)
print(info)
print(info['user']['biography'])