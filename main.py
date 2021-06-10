import time
import random

print ()
naam = input ('Hoe heet je? ')
print ()
print ('Hello,', naam,'tijd om galgje te spelen ')
print ()

woorden = ["informatica","informatiekunde","spelletje",
"aardigheidje","scholier","fotografie","waardebepaling","specialiteit","verzekering","universiteit","heesterperk"]
galg = [
  "---------",
  "|       |",
  "|       O",
  "|       |",
  "|      -+-",
  "|       |",
  "|      / \\",
  "|",
  "|",
  "------------"
]

time.sleep(1)

print ('We gaan beginnen ...')
time.sleep(0.5)

woordkiezen = random.choice(woorden)
woord = (woordkiezen) 

guesses = ''
turns = 10
while turns > 0:

  letters_not_guesed = 0             
    toonwoord=''
    for char in woord: 
        if char in guesses:  
           toonwoord=toonwoord + (char)
        else:
           toonwoord=toonwoord + ('_') 
           letters_not_guesed += 1   
     print ('Woord:',toonwoord, '. Al gegokte letters:', guesses)      
     print ()