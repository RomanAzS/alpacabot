import urllib2
import json

def wz(query):
    try:
        query = query.replace(' ', '+')
        url = "http://api.worldweatheronline.com/free/v1/weather.ashx?q=%s&format=json&num_of_days=5&fx=no&includelocation=no&key=jxxxegjtk2r2cg7wyrshbvsp" % query
        req = urllib2.Request(url)
        response = urllib2.urlopen(req)
        response = response.read()
        response = json.loads(response)
		
        data = response['data']['current_condition'][0]
		
        degC = data['temp_C']
        degF = data['temp_F']
        mbar = data['pressure']
        humi = data['humidity']
        winddir = data['winddir16Point']
        windKPH = data['windspeedKmph']
        windMPH = data['windspeedMiles']
        wzdescr = data['weatherDesc'][0]['value']
		
        place = response['data']['request'][0]['query']
        type = response['data']['request'][0]['type']
		
        kPa = mbar2kpa(mbar)
		
        info = "\002Weather in %s %s:\002 \x1fConditions:\x1f %s, %sC(%sF) \x1fWind:\x1f %s at %s kph(%s mph) \x1fHumidity:\x1f %s%% \x1fAtmospheric Pressure:\x1f %s mbar(%s kPa)" % (type, place, wzdescr, degC, degF, winddir, windKPH, windMPH, humi, mbar, kPa)
		
        return info.encode('ascii', 'ignore')
		
    except:
        return "Error: your argument is invalid."
		
def mbar2kpa(mbar):
    mbar = int(mbar)
    kpa = mbar * .1
    return str(kpa)

