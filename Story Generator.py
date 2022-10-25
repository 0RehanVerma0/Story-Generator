from ast import Import
from random import Random


import random
When=["A long time ago","Way Back in the 80s " , "Once upon a time","A Thousand Years ago!","Yesterday","on September 1st"]
Who=["a wolf","a Musician","a frog","A sniper","my cat","The Garbage man"]
name=["the alpha","Michael Jackson","Gamabunta","daniel","jasmine","Suresh"]
Went=["Woods","concert","river","Colombia","outside","Landfill site"] 
Happened=["Won a battle","Performed for his fans","Fought for Frog rights","To participate in the 2nd Worldwar","Went missing","was Fired"]
Residance=["WallStreet","Bungalow","River of Frogs","small Village","Cathouse","Big Town"]

print(random.choice(When) + ' , ' + random.choice(Who) + ' that lived in ' + random.choice(Residance) + ', went to the ' + random.choice(Went) + ' and ' + random.choice(Happened))