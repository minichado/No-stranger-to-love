import signal
import logging
import time



NG= "Never gonna"
V1 = (
	"We're no strangers to love",
	"You know the rules and so do I",
	"A full commitment's what I'm thinking of",
	"You wouldn't get this from any other guy"
	)
Inter1 = (
	"I just want to tell you how I'm feeling",
	"Gotta make you understand"
	)
Chorus = (
	"give you up",
	"let you down ",
	"run around and desert you",
	"make you cry",
	"say goodbye",
	"tell a lie and hurt you"
	)
V2 = (
	"We've known each other for so long",
	"Your heart's been aching but you're too shy to say it",
	"Inside we both know what's been going on",
	"We know the game and we're gonna play it"
	)
Inter2 = (
	"And if you ask me how I'm feeling",
	"Don't tell me you're too blind to see"
	)
Varlist=(
	V1,Inter1,Chorus,V2,Inter2,Chorus,Chorus,V2,Inter1,Chorus	)
	
def chorus(chorus):

#chorus works, woo!
	i = 0
	while i < len(chorus):
		print(NG,chorus[i])
		if (i==2):
			time.sleep(3)
		elif (i==5): 
			time.sleep(3)
		else: 
			time.sleep(1.5)
		i+=1		
def verse(lyrics):
	i = 0
	while i < len(lyrics):
		print (lyrics[i])
		time.sleep(3)
		i+=1		
def Song(wtf):
	i=0
	while i<len(wtf):
		if (wtf[i]==Chorus):
			chorus(wtf[i])
		else:
			verse(wtf[i])
		print("\n")
		i+=1


Song(Varlist)
		
		
	