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

  if letters_not_guesed == 0:
        print ()
        print ('...')

        time.sleep(1)        
        print ('Hoera,', naam, 'Je hebt gewonnen')

        break  
  print

  time.sleep(1)   
  guess = input ('Raad een letter: ') 
  guesses += guess 

  if guess not in woord:
      turns -= 1
      galgregel=turns
      nr_of_to_print_lines=(10-turns)
      while nr_of_to_print_lines>0:
        print (galg[galgregel])
        galgregel +=1 
        nr_of_to_print_lines -=1
        print ("")

      x = guess.isalpha()
      if x is False:
        print("")
        print("Je hebt iets anders ingevuld dan een letter, strafpunt voor het invullen van een letter terwijl je een woord moet raden!")
      

        print ('Jammer, fout ...')
        print (naam, 'je hebt nog', + turns, 'levens')

        if turns == 0: 
          print ()
          print ('...')
          time.sleep(1)
          print ('Jammer', naam, 'je hebt verloren, het woord was:', woord)






     
     
     
     
     
     
     
  