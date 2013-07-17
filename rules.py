import random

def rulesOfTheInternet(msg):
    target = open("rules.txt")
    targ = target.read()
    targ.close()
    ruleslist = targ.split("\n")
    if msg.isdigit() == True:
        msg = int(msg)
        if msg >= 0 and msg <= 100:
            return ruleslist[msg-1]
        else:
            return "Your argument is invalid."
    elif msg == "random" or msg == "rand" or msg == "r":
        return random.choice(ruleslist)
    else:
        return "Your argument is invalid."