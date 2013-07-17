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
    if "may refer to" in res[0]:
        res = res[0]
        res = re.sub("<.*?>", '', res)
        return "%s http://en.wikipedia.org/wiki/%s" % (res.strip("/<"), msg)
    else:
        while "<tr>" in response[1]:
            del response[1]
        response = response[1]
        response = re.sub("<.*?>", '', response)
        response = re.sub("\[\d?\]", '', response)
#        response = response.split('.')
        response = re.split("[A-Z][^\.!?] *?[\.!?]", response)
        print(str(response))
        if (len(response[0]) + len(response[1])) >= 450:
            resp = response[0]
        else:
            resp = "%s.%s." %(response[0], response[1])
        return resp.strip()
