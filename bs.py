import random
import re
import urllib2
insults = [ "oh my sweet christ, if you don't shut your mouth, I will shut it for you with my man meat.",
"just how fucking foolish are you, anyway? Your stupidity is simply amazing. ",
"every time you open your mouth, some idiot starts talking",
"from the moment I first saw you i knew I wanted to spend the rest of my life avoiding",
"some people bring happiness wherever they go. you bring happiness whenever you go",
"you're a person of rare intellience. it\'s rare when you show any",
"i'd like to see things from your point of view, but I can't seem to get my head that far up your ass",

"bathe thyself, thou malevolent flap-mouthed garbage. ",
"I'm not saying you're a skank, but if your messy cleft palate had a password, it would be '12345.'",
"wow, you are pretty. Just kidding, you're a shit-breathing bitch. "
"I know you're an insignificant prick and all, but holy sweet christ, eat a bag of dicks.",
"your mother smells like a goat and your father loves it",
"It looks like your face caught on fire and someone tried to put it out with a hammer.",
"I love what you've done with your hair. How do you get it to come out of the nostrils like that?",
"I heard you took an IQ test and they said your results were negative.",
"I don't exactly hate you, but if you were on fire and I had water, I'd drink it.",
"I wanted to dress as you for Halloween, but I couldn't fit seven dicks into my mouth.",
"I would have been your father but the dog beat me up the stairs.",
"your birth certificate is a letter of apology from the condom company.",
"I look into your eyes and get the feeling someone else is driving. ",
"I hear you are very kind to animals, so please give that face back to the gorilla",
"You're so ugly they push your face into dough to make gorilla cookies",
"I don't want to have to explain to your uncle that you can't go to the dinner party because you got caught trying to convince little boys you're santa again. ",
## I want this one to be rarer than the other ones
#"u are 1 fukin cheeky kunt mate i swear i am goin 2 wreck u i swear on my mums life and i no u are scared lil bitch gettin your mates to send me messages saying dont meet up coz u r sum big bastard with muscles lol fukin sad mate really sad jus shows what a scared lil gay boy u are and whats all this crap ur mates sendin me about sum bodybuildin website that 1 of your faverite places to look at men u lil fukin gay boy fone me if u got da b",
"Know why you have fleas? Because you're a anal-dwelling cunt.",
"you're so ugly that when your mama dropped you off at school she got a fine for littering.",
"we all sprang from apes, but you just didn't spring far enough.",
"your head is so big you have to step into your shirts",
"your asinine simian countenance alludes that your fetid stench has anulled the anthropoid ape species diversity."]

azi_insults = [#"%s is sexy"
#,"i could not insult %s, how dare you!"
#,"%s has lots of swag"
"u mad bro?"
,"nu"]

philosophies = ["Swiggity swagginses whats in the bagginses"
,"Winter is coming"
,"derriere", "paynus", "dinosaurs"
#,"azi is sexy"
,"you so full of shit you close your mouth and let your ass talk \t --lil wayne"
,"Lololol I don't know that"
,"What are you smoking"
#,"peanuts to the elephant"
,"cheese. i hate cheese"
,"doughnuts" ,"butterflies", "43"
,"Shoot for the stars; that way if you miss you're stuck in outer space with no oxygen and your suffering will end sooner."
]

# wikipedia function for bot

# all other functions are out of here, only keeping conversions


# conversions. just putting them in here to clean up the bot code

