import urllib2
import re

def wiki(msg):
    msg = str(msg)
    req = urllib2.Request("http://en.wikipedia.org/w/index.php?action=render&title=%s"  %  msg)
    req.add_header("User-agent", "Mozilla 5.10")
    response = urllib2.urlopen(req)
    response = response.read()
    response = response.split("<p>")
    res = response[1].split("p>")
    
    
    if "may refer to:" in res[0] or "can refer to:" in res[0] or "may also refer to:" in res[0]:
        res = res[0]
        res = re.sub("<.*?>", '', res)
        return "%s http://en.wikipedia.org/wiki/%s" % (res.strip("/<"), msg)
    else:
        while "<tr>" in response[1]:
            del response[1]
        while "td>" in response[1]:
            del response[1]
        while "<li>" in response[1]:
            del response[1]
        response = response[1]
        response = re.sub("<.*?>", '', response)
        response = re.sub("\[\d?\]", '', response) 
#        response = response.split('.') 
#        response = re.split("[A-Z][A-Za-z0-9\"\[\]\'\(\);,:&\s]+ *?[\.!?]", response) # broke it
        d = re.findall(".+?(?<!Dr|Mr|Jr|Sr| \w|\.\w)[.!?]\s", response)
#        response = re.split("[.!?] ", response)
        print d
        try:
            length = len(d[0]) + len(d[1])
            if (length) >= 450:
                resp = d[0].strip()
            else:
                
                resp = "%s %s" %(d[0].strip(), d[1].strip())
        except:
            resp = d[0].strip()
        return resp.strip()
