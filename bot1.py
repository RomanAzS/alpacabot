from twisted.words.protocols import irc
from twisted.internet import reactor, protocol
from twisted.python import log
from string import Template
from bs import insults, azi_insults, philosophies
from fibo import fib2
from wiki import wiki 
from notes import notes 
from rules import rulesOfTheInternet as rules
from convert import convert 
from dict import dictionary as dict
from tz import tz 
from wz import wz 
from prefixes import whattodo
#from botlast import makelist, append, last
import bs
import re
import time, sys
import urllib2
import random

class Bot(irc.IRCClient):
    """ IRC bot"""
    nickname = "alpacabot" # Nickname of the bot
    realname = "Hamster Bot" # Real name field, can contain spaces
    username = "HamsterBot" # Username/Ident
    chanlist = ["#TheGrammarNaziBoners", "#LGBTeens", "#programming", "#nu", "#SHARKY'sDrugDen", "#justchat"]
    azi = ["hamster", "hammy", "azi", "legolas", "smeagol", "dinoshi", "faramir", "thranduil", "sharky", "kojiro"]
    opers = ["hamster", "hammy", "azi", "legolas", "smeagol", "dinoshi", "neoinr", "neoite", "ritsuka", "kvasir"]
    opersh = ["hamster@haters.gon.hate","hamster@alpa.ca",  "azi@haters.gon.hate", "Azi@F2D81641.F516A8C9.8D5014A8.IP".lower(), "robin@n0.ms", "kvasir@i.am.loveless",  "andrew@i.am.loveless", "zero-one@netadmin.localhost", "joey@goes.rawr", "me@it.wasnt.me", "lion@goes.rawr", "azi@alpaca"]
    count = 0
    quotlist = []
    
    
    def connectionMade(self): # What happens when bot first connects
        irc.IRCClient.connectionMade(self)
        print("[connected at %s]" % time.asctime(time.localtime(time.time())))

    def connectionLost(self, reason): # What happens when bot loses connection
        irc.IRCClient.connectionLost(self, reason)
        print("[disconnected at %s]" % time.asctime(time.localtime	(time.time())))

    def signedOn(self): # What happens when bot has connected
        p = open("botpass.txt")
        self.password = p.read()
        p.close()
        self.msg("NickServ", "identify HamsterBot %s" % self.password) # Basic Nickserv identify
#        if self.nickname != "HamsterBot":
 #           self.msg("NickServ", "ghost HamsterBot swagonball")
  #          time.sleep(5)
   #         self.setNick("HamsterBot")
    #        self.msg("NickServ", "identify swagonball")
        self.join("#TheGrammarNaziBoners") #connect to channel
        self.join("#dino")

    def joined(self, channel): # What happens when bot joins a channel
        print("[I have joined %s]" % channel)
#        makelist(channel)
#	self.me("#LGBTeens", "dinosaurs")

    def privmsg(self, user, channel, msg): # What happens when bot gets a message
        self.count = self.count + 1
        swag = user.split('!')
        user = user.split('!', 1)[0] # Turn user!ident@host into nickname
        print("%s:<%s> %s" % (channel, user, msg)) # Show the message in console
        capsIntact = msg
        if channel == self.nickname: # Check if it's a private message
            pm = 1 
        else:
            pm = 0
#            append(channel, user, msg)
            
        msg = msg.lower()
        if swag[1].lower() in self.opersh or channel.lower() == "#dino": # if the user is in the oper list
            admin = 1 
        else: 
            admin = 0
        
        if channel == "#thegrammarnaziboners":
            tstchan = 1
        else:
            tstchan = 0
            
        insult_ = True
        fibo_ = True
        choose_ = True
        dict_ = True
        wiki_ = True
        tz_ = True
        wz_ = True
        rule_ = True
        convert_ = True
        flist = {'insult': insult_, 'fibo': fibo_, 'choose': choose_, 'dict': dict_, 'wiki': wiki_, 'wz': wz_,  'tz': tz_, 'rule': rule_, 'convert': convert_}

        
        if msg.startswith("~die"): 
            try:
                if admin == 1:                    
                    if user.lower() in self.azi:
                        print "Killed by %s" % user
                        reactor.stop()
                    else:
                        self.notice(user, "Not amused")
                        print("%s attempted to kill me!")
            except:
                self.notice(user, "You are not authorized to perform this command.")
                print("%s attempted to kill me!" % user)
        elif msg.startswith("~set ") and swag.lower() == "hamster@alpa.ca":
#            self.sendLine("MODE %s +B %s" % (self.nickname, self.nickname))
            self.mode(self.nickname, True, 'B', limit=None, user=self.nickname, mask=None)
        elif msg.startswith("~stop") and admin == 1:
            self.quit()
        elif msg.startswith("~id") and (admin == 1 or user.lower == "Kojiro"):
            self.msg("Nickserv", "identify hamsterbot %s" % self.password)
        elif msg.startswith("~ghost ") and admin == 1:
            msg = msg.split()
            self.msg("Nickserv", "ghost %s swagonball" % msg[1])
        elif msg.startswith("~donut") and admin == 1:
            msg = msg.split(' ') 
            try:
                if msg[1].isdigit(): #hopefully if i use a number it'll join that chan
                    i = int(msg[1]) 
                    chan = self.chanlist[i]
                    self.join(chan) #why doesnt this work nvm it does
                elif msg[1] == "joinall" or msg[1] == "all":
                    for item in self.chanlist:
                         self.join(item)
                else:
                    self.join(msg[1])
            except:
                if admin != 1:
                    self.notice(user, "You are not authorized to perform this command.")
                else:
                    self.say(channel, "-_-")
        elif msg.startswith("~bye"): 
            try:
                if admin == 1:
                    self.part(channel)
            except:
                self.notice(user, "You are not authorized to perform 	this command.")
                print("%s attempted to use command ~bye." % user)
        elif msg.startswith("~nick"): 
            try:
                if admin == 1:
                    msg = msg.split(' ')
                    self.setNick(msg[1])
            except:
                self.notice(user, "You are not authorized to perform this command.")
                print("%s tried to change my nick" % user)
        elif msg.startswith("~toggle ") and admin == 1:
            msg = msg.split()
            if len(msg) == 3:
                if flist.has_key(msg[1]):
                    funct = msg[1].strip()
                    if msg[2].strip() == "on" or msg[2] == '1':
                        flist[funct] = True
                    elif msg[2].strip() == 'off' or msg[2] == '0':
                        flist[funct] = False             
                    elif msg[2] == 'not':
                        flist[funct] = not flist[funct]
                    else:
                        self.notice(user, "Values accepted: on/off or 1/0")
                else:
                    self.notice(user, "No function found with that name or function may not be switched on/off")
            elif len(msg) == 2:
                if msg[1] == 'help':
                    self.notice(user, "The following functions may be switched on/off: insult, choose, convert, dict, fibo, rule, tz, wz, wiki")
                elif msg[1] == 'is_on':
                    is_on = []
                    for key, value in flist.iteritems():                    
                        if value == True:
                            is_on.append(key)
                    self.notice(user, "The following functions are on: %r" % is_on)
            else:
                self.notice(user, "Toggle takes 2 arguments. Do ~toggle help for functions that may be toggled on/off")
                
        elif msg.startswith("~say ") and admin == 1:
            msg = msg[5:]
            self.say(channel, msg)
        elif msg.startswith("~note ") and (swag[1].lower()=="hamster@alpa.ca"):
            msg = msg[6:]
#           bs.notes(str(msg))
            self.notice(user, notes(str(msg)))
        elif msg.startswith(":prefixes "):
            msg = msg[10:]
            self.say(channel, whattodo(msg, user))
            
        elif msg.startswith(".insult ") and insult_ == True:
            msg = msg.split(' ')
            #nick = msg[1]                
            try:
                if msg[1].lower() in self.azi:
                    self.say(channel, random.choice(azi_insults))
                elif msg[1].lower() == "?roulette":
                    self.say(channel, "%s, %s" % (user, random.choice(insults)))
                else:
                    insult = "%s, %s" % (msg[1], random.choice(insults))
                    self.say(channel, insult)
            except IndexError:
                self.say(channel, random.choice(insults))
        elif msg.startswith(".inslut") and flist['insult'] == True:
            msg = msg.split(' ')
            insult = "%s, %s" % (user, random.choice(insults))
            self.say(channel, insult)
        elif msg.startswith(".halp") or msg.startswith(".help"):
            try:
                if admin == 1:
                    self.notice(user, "Commands: .help, .insult <user>, .fibo, .convert <conversion> <numbers>, .gay, .rule <1-47>, .choose <option1, option2,...>, .dict <query>")
                    self.notice(user, "Restricted commands: ~die, ~bye, ~donut <channel>, ~nick <newnick>")
            except:
                    self.notice(user, "Commands: .help, .about, .insult <user>, .fibo, .convert <conversion> <numbers>")
#       elif msg.startswith("~~"):
#           msg = msg.strip("~~")
#           exec(msg)
        elif msg.startswith(".choose ") and flist['choose'] == True:
            msg = msg[8:]
#           re.sub("or*", '', msg)
            
            msg = msg.split(",")
            msg = random.choice(msg)
            words = msg.split(' ')
            if words[0] == 'or' and len(words) > 1:
                msg = msg.replace('or ','')
            self.msg(channel, "%s: %s" % (user, msg.strip()))
#        elif msg.startswith(".last"):
#            msg = msg[5:]
#            list = last(channel, msg)
#            for item in list:
#                self.msg(user, item)
        elif msg.startswith(".wiki ") and flist['wiki'] == True: #broken wikipedia feature
            msg = msg[6:]
            msg = msg.replace(' ', '_')
            self.msg(channel, str(wiki(str(msg))))
        elif msg.startswith(".dict ") and flist['dict'] == True: #dictionary feature
 #           msg = capsIntact
            msg = msg[6:]
            self.msg(channel, dict(msg))
        elif msg.startswith(".tz ") and flist['tz'] == True: #timezone feature
            msg = msg[4:]
            self.msg(channel, tz(msg))
        elif msg.startswith(".wz ") and flist['wz'] == True: #weatherbot feature
            msg = msg[4:]
            self.msg(channel, wz(msg))
        elif msg.startswith(".gay"):
            self.msg(channel, "%s: http://blog.okcupid.com/index.php/gay-sex-vs-straight-sex" % user)
        elif msg.startswith(".rule ") and flist['rule'] == True:
            msg = msg.split()
            self.msg(channel, rules((msg[1].strip())))
        elif msg.startswith(".fibo") and flist['fibo'] == True: 
            msg = msg.split(' ')
            num = msg[1]
            i = fib2(int(num))
            self.msg(channel, str(i))
        elif msg.startswith(".convert") and flist['convert'] == True: 
            msg = msg.split(' ')
            if convert(msg).startswith('S') or convert(msg).startswith('N'):
                if '::' in convert(msg):
                    resp = convert(msg).split('::')
                    self.notice(user, resp[0])
                    self.notice(user, resp[1])
                else:
                    self.notice(user, convert(msg))
            elif pm == 1:
                self.notice(user, convert(msg))
            else:
                self.msg(channel, convert(msg))

    def action(self, user, channel, msg): #What happens with a /me
        user = user.split('!', 1)[0] # Turn user!ident@host into nickname
        print("%s:* %s %s" % (channel, user, msg))

    def alterCollidedNick(self, nickname) : #Changes nick if nick is taken
        return nickname + "_not" + str(random.randint(1,1337))

#    def quit(self, message)
        



class BotFactory(protocol.ClientFactory): #Making an instance of the bot

    def __init__(self): #Welcome message
        print "HamsterBot!"

    def buildProtocol(self, addr):
        p = Bot()
        p.factory = self
        return p

    def clientConnectionLost(self, connector, reason):
        """reconnect if disconnected"""
        connector.connect()

    def clientConnectionFailed(self, connector, reason):
        print "Connection failed: ", reason
        reactor.stop()


if __name__ == '__main__':

    # create factory protocol and application
    f = BotFactory()

    # connect factory to this host and port
    reactor.connectTCP("irc.awfulnet.org", 6667, f)

    # run bot
    reactor.run()

