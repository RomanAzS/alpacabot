import urllib2
import json
import re

def dictionary(msg):
    msg = str(msg)
    msg = msg.replace(' ', '+')
    try:
        msg.split()
        req = urllib2.Request("http://www.google.com/dictionary/json?callback=dict_api.callbacks.id100&sl=en&tl=en&restrict=pr%%2Cde&client=te&q=%s" % msg)
        response = urllib2.urlopen(req)
        response = response.read()[25:-10].replace("\\x", "\\u00")
        data = json.loads(response)
		
        partOfSpeech = [i["terms"][0]["labels"] for i in data["primaries"]][0][0]
        partOfSpeech = partOfSpeech["text"]
		
        word = [[[d["text"] for d in i["terms"]] for i in data ["primaries"]]][0][0][0]
	
        data = [[[n["text"] for n in d["terms"]] for d in i["entries"]] for i in data["primaries"]]#[0][1][0]

#        longerThan = False
		
        
		
        # try:   
            # entry1 = data[0][1][0]
            # if len(entry1) < 420:
                # try:
                    # entry2 = data[0][2][0] 
                    # entry1 = "[1]%s. [2]%s" % (entry1, entry2)
                    # if len(entry1) < 420:
                        # try:
                            # entry3 = data[0][3][0]	
                            # lenght = len(entry3) + len(entry1)
                            # if lenght < 420:
                                # entry1 = "%s. [3]%s" % (entry1, entry3)
                            
                        # except:
                            # pass
                # except:
                    # pass
        # except:
            # entry1 = data[0][0][0]
			
        # try:
            # entry = data[0][1][0]
            # if len(entry) > 420:
                # entry1 = entry
            # else:
                # try:
                    # entry2 = data[0][2][0]
                    # entry1 = "[1]%s. [2]%s" % (entry1, entry2)
                    # if len(entry1) > 420:
                        # entry1 = entry1
                    # else:
                        # try:
                            # entry3 = data[0][3][0]
                            # entry1 = "%s. [3]%s" % (entry1, entry3)
                            # if len(entry1) > 420:
                                # entry = entry
			
        try:
            entry1 = data[0][1][0]
            try:
                entry2 = data[0][2][0]
                entryTestLen = len(entry1) + len(entry2)
                if entryTestLen > 420:
                    entry1 = entry1
                else:
                    entry1 = "[1]%s. [2]%s" % (entry1, entry2)
                    try:
                        entry3 = data[0][3][0]
                        entryTestLen = len(entry1) + len(entry3)
                        if entryTestLen > 420:
                            entry1 = entry1
                        else:
                            entry1 = "%s. [3]%s" % (entry1, entry3)
                    except:
                        pass
            except:
                pass
        except IndexError:
            entry1 = data[0][0][0]
			
        # try:
            # ea = []
            # for n,entry in enumerate(data[0][1:]):
                # if n > 2 or len('. '.join(ea)) > 420:
                     # break
                # ea.append("[%s]%s"%(n,entry[0]))
            # entry = '. '.join(ea)
        # except IndexError:
            # entry = data[0][0][0] 
			
### note: try \x1f for u-line
        
        relatedWord = data[0][0][0]
     
	
        definition = "\002%s\002: %s. %s." % (word, partOfSpeech, entry1)
	
        definition = re.sub("<.*?>", '', definition)
	
        return definition.encode('ascii', 'ignore')

    except:
        return "Error: your argument is invalid."