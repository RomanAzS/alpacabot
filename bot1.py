from twisted.words.protocols import irc
from twisted.internet import reactor, protocol
from twisted.python import log
from string import Template
from bs import insults, azi_insults, philosophies
from fibo import fib2
from wiki import wiki as wiki
from notes import notes as notes
from rules import rulesOfTheInternet as rules
from convert import convert as convert
from dict import dictionary as dict
from tz import tz 
from wz import wz
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
    chanlist = ["#TheGrammarNaziBoners", "#LGBTeens", "#Programming"]
    azi = ["hamster", "hammy", "azi", "legolas", "smeagol", "dinoshi", "faramir", "thranduil", "sharky"]
    opers = ["hamster", "hammy", "azi", "legolas", "smeagol", "dinoshi", "neoinr", "neoite", "ritsuka", "kvasir"]
    opersh = ["hamster@haters.gon.hate","hamster@alpa.ca",  "azi@haters.gon.hate", "Azi@F2D81641.F516A8C9.8D5014A8.IP".lower(), "robin@n0.ms", "kvasir@i.am.loveless",  "andrew@i.am.loveless", "zero-one@netadmin.localhost", "joey@goes.rawr", "me@it.wasnt.me"]
    count = 0
    quotlist = []
    
    def connectionMade(self): # What happens when bot first connects
        irc.IRCClient.connectionMade(self)
        print("[connected at %s]" % time.asctime(time.localtime(time.time())))

    def connectionLost(self, reason): # What happens when bot loses connection
        irc.IRCClient.connectionLost(self, reason)
        print("[disconnected at %s]" % time.asctime(time.localtime(time.time())))

    def signedOn(self): # What happens when bot has connected
        self.msg("NickServ", "identify HamsterBot swagonball") # Basic Nickserv identify
#        if self.nickname != "HamsterBot":
 #           self.msg("NickServ", "ghost HamsterBot swagonball")
  #          time.sleep(5)
   #         self.setNick("HamsterBot")
    #        self.msg("NickServ", "identify swagonball")
        self.join("#TheGrammarNaziBoners", "#Programming") #connect to channel
	self.join("#dino")

    def joined(self, channel): # What happens when bot joins a channel
        print("[I have joined %s]" % channel)
#	self.me("#LGBTeens", "dinosaurs")

    def privmsg(self, user, channel, msg): # What happens when bot gets a message
        self.count = self.count + 1
        swag = user.split('!')
        user = user.split('!', 1)[0] # Turn user!ident@host into nickname
        print("%s:<%s> %s" % (channel, user, msg)) # Show the message in console
        capsIntact = msg
        msg = msg.lower()
        if swag[1].lower() in self.opersh or (channel.lower() == "#dino" or channel.lower() == "dino"): # if the user is in the oper list
            admin = 1 
        else: 
            admin = 0
        if channel == self.nickname: # Check if it's a private message
            pm = 1 
        else:
            pm = 0
        
        if msg.startswith("~die"): # and admin == 1:
            #message = "", user, "killed me"
            #self.quit(message = "ded")
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
                else:
                    self.join(msg[1])
            except:
                if admin != 1:
                    self.notice(user, "You are not authorized to perform this command.")
                else:
                    self.say(channel, "-_-")
        elif msg.startswith("~bye"): # and admin == 1:
            try:
                if admin == 1:
                    self.part(channel)
            except:
                self.notice(user, "You are not authorized to perform this command.")
                print("%s attempted to use command ~bye." % user)
        elif msg.startswith("~nick"): # and admin == 1:
            try:
                if admin == 1:
                    msg = msg.split(' ')
                    self.setNick(msg[1])
            except:
                self.notice(user, "You are not authorized to perform this command.")
                print("%s tried to change my nick" % user)
        elif msg.startswith("~say ") and admin == 1:
            msg = msg[5:]
            self.say(channel, msg)
        elif msg.startswith("~note ") and (swag[1].lower()=="hamster@alpa.ca"):
            msg = msg[6:]
#           bs.notes(str(msg))
            self.notice(user, notes(str(msg)))
        elif msg.startswith(".insult"):
            msg = msg.split(' ')
            #nick = msg[1]                
            try:
                if msg[1].lower() in self.azi:
                    self.say(channel, random.choice(azi_insults))
                elif msg[1].lower() == "?roulette":
                    self.say(channel, "%s %s" % (user, random.choice(insults)))
                else:
                    insult = "%s %s" % (msg[1], random.choice(insults))
                    self.say(channel, insult)
            except IndexError:
                self.say(channel, random.choice(insults))
        elif msg.startswith(".inslut"):
            msg = msg.split(' ')
            insult = "%s %s" % (user, random.choice(insults))
            self.say(channel, insult)
        elif msg.startswith(".halp") or msg.startswith(".help"):
            try:
                if admin == 1:
                    self.notice(user, "Commands: .help, .insult <user>, .fibo, .convert <conversion> <numbers>, .gay, .rule <1-47>, .choose <option1, option2,...>, .dict <query>")
                    self.notice(user, "Restricted commands: ~die, ~bye, ~donut <channel>, ~nick <newnick>")
            except:
                    self.notice(user, "Commands: .help, .about, .insult <user>, .fibo, .convert <conversion> <numbers>")
        elif msg.startswith("~~"):
            msg = msg.strip("~~")
            exec(msg)
        elif msg.startswith(".choose "):
            msg = msg[8:]
            re.sub("or*", '', msg)
            msg = msg.split(",")
            self.msg(channel, "%s: %s" % (user, random.choice(msg).strip()))
        elif msg.startswith(".wiki "): #broken wikipedia feature
            msg = msg[6:]
            msg = msg.replace(' ', '_')
            self.msg(channel, str(wiki(str(msg))))
        elif msg.startswith(".dict "): #dictionary feature
 #           msg = capsIntact
            msg = msg[6:]
            self.msg(channel, dict(msg))
        elif msg.startswith(".tz "): #timezone feature
            msg = msg[4:]
            self.msg(channel, tz(msg))
        elif msg.startswith(".wz "): #weatherbot feature
            msg = msg[4:]
            self.msg(channel, wz(msg))
        elif msg.startswith(".gay"):
            self.msg(channel, "%s: http://blog.okcupid.com/index.php/gay-sex-vs-straight-sex" % user)
        elif msg.startswith(".rule "):
            msg = msg.split()
            self.msg(channel, rules((msg[1].strip())))
        elif msg.startswith(".fibo"):
            msg = msg.split(' ')
            num = msg[1]
            i = fib2(int(num))
            self.msg(channel, str(i))
        elif msg.startswith(".convert"):
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
        user = user.split('!', 1)[1] # Turn user!ident@host into nickname
        print("%s:*%s %s" % (channel, user, msg))

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

