import urllib2
import re
import json

# this is a time zone function
# input should be between 1-3 paramters seperated by commas, 
# concatenated into one string before being passed to function
# query in format city+city,state,country
def tz(query):
    try:
        query = query.replace(' ', '+')
        url = "http://api.worldweatheronline.com/free/v1/tz.ashx?q=%s&format=json&key=jxxxegjtk2r2cg7wyrshbvsp" % query
        req = urllib2.Request(url)
        response = urllib2.urlopen(req)
        response = response.read()
        response = json.loads(response)
	

        data = response['data']['request'][0] #figure this out; i wanna use json
        timeData = response['data']['time_zone'][0]
	
        place = data['query']
        type = data['type']
        offset = timeData['utcOffset']
        time = timeData['localtime']
	
        if not offset.startswith('-'):
            offset = "+%s" % offset
        else:
            offset = offset
	
        info = "\002Time in %s %s\002: %s, UTC %s" % (type, place, time, offset)
    
        return info.encode('ascii', 'ignore')
    
    except:
        return "Error: your argument is invalid."