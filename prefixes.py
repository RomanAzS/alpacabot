def whattodo(msg, user):
    msgsplt = msg.split(' ')
    target = open("prefix.txt", 'a+')
    lines = target.readlines()
    if msgsplt[0] == 'all':
        return allprefixes(lines)
    elif msgsplt[0] == "help":
            return "Add your bot's prefixes with ':prefixes add <botname> <prefixes>'. Please seperate multiple prefixes with a space. Look for prefixes & bots with ':prefixes bots' and ':prefixes prefix'."

    else:
        msg = msg.split()
        # del msg[0]
        # del msg[0]
        
        if msgsplt[0] == "add": 
            del msg[0]
            del msg[0]
            return addprefix(msgsplt[1], msg, user, target, lines)
    #        target.write("%s\t%s\t%s" % (prefix, bot, user))
    #        return "Added"
        elif msgsplt[0] == "prefix" or msgsplt[0] == "prefixes":
            if len(msgsplt) > 1: 
                return searchprefix(lines, msgsplt[1], target)
            else:
                return allprefixes(lines, target)
        elif msgsplt[0] == "bots" or msgsplt[0] == "bot":
            if len(msgsplt) > 1:
                return searchbots(lines, msgsplt[1], target)
            else:
                return allbots(lines, target)
            
            
def addprefix(bot, prefix, user, target, lines):
    for item in prefix:
        adding = "%s\t%s\t%s\n" % (item, bot, user)
        if adding in lines:
            target.close()
            return "Prefix %s for %s has already been added by %s" % (item, bot, user)
        else:
            target.write(adding)
    target.close()
    return "Added"
    
def searchprefix(lines, query, target):
 #   if len(query) == 1:
        swag = []
        for line in lines:
            if line.startswith(query):
                swag.append(line.split("\t"))
        output = "The following bots have the prefix %s: " % query
        if len(swag) == 0:
            output = "No bots were found with that prefix."
        else:
            for item in swag:
                output = ('%s %s' %(output, item[1]))
        return output
        target.close()
    
def searchbots(lines, query, target):
    target.close()
    prefixes = []
    for item in lines:
        items = item.split("\t")
        if query == items[1]:
            prefixes.append(items[0])
    if len(prefixes) == 0:
        output = "No bots found."
    else:
        output = "%s has the following prefix(es): " % query
        for item in prefixes:
            output = ('%s %s' %(output, item[0]))
    return output
    
def allprefixes(lines, target):
    target.close()
    prefixes = []
    for item in lines:
        items = item.split("\t")
        if items[0] not in prefixes:
            prefixes.append(items[0])
    return "The following prefixes are in use: %s" % ' '.join(prefixes) + ". Do ':prefixes prefix <prefix>' to see which bots have that prefix."
    
def allbots(lines, target):
    target.close()
    bots = []
    for item in lines: 
        items = item.split("\t")
        if items[1] not in bots:
            bots.append(items[1])
    return "The following bots have prefixes in prefixbot: %s" % ', '.join(bots) + ". Do ':prefixes bots <botname>' to see the prefixes entered for a bot."
    