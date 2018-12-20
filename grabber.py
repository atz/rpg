tool = ["hammer","screwdriver","fork","dagger","bungie-chord","slime"]

def grabber(test):
  index = 0
  for each in test:
    while index < 4:
      print "You have a " + test[index]
      index += 1
    
print grabber(tool)

answer = raw_input("I have a few wares. Odds and ends really. What are you interested in?")

def selector(choice):
  if choice == "hammer":
   return "You have chosen wisely"
  elif choice == "screwdriver":
   return "You have made a grave mistake, beggar."
  elif choice == "fork":
   return "The weapon of the obese. Godspeed you on your path to the grave."
  else:
   return "Disaster"
   
print selector(answer)

def user(choice):
  if answer == "hammer":
    pass
  elif answer == "slime":
    return "Are you... R..."
    pass
  else: 
    print "Begone fool."
    exit()
    

print user(answer)

playername = raw_input("Who are you who has chosen so wisely?") 
   
def game(inp):
  if playername == "Ralph":
    return "Good God. It... It is you. We... We are freed. I die in the arms of relief, after all these years."
    
  ans = raw_input("Well, " + playername + " it's been some time I've waited for you. What say you to a little game? Yea, or nay?")
    
  if ans == "Yea" or ans == "yea":
    return "let's get started."
  elif ans == "Nay" or ans == "nay":
    return "You aren't " + playername + ", begone devil."
    grabber(test)
  else:
    print "If only God were watching. He could make your tongue smooth in your head."
    exit()
    grabber(test)
print game(user)

def quest(hero):

  from random import randint
  import re
  enemies = ["goblins", "white men", "the unendurable passage of time", "The Monarch"]
  hp = 10
  st = 10
  att = 10
  weapon = answer
  
  print "You seem healthy enough. %s hitpoints, %d, stamina, %r, attacking skillz. " % (hp, st, att)
  print "And besides, you've got that " + weapon + " too boot."
  print enemies
  enemy_for_quest = raw_input("Which of those riles your bones?")
  if enemy_for_quest == "The Monarch":
    print "You must train. Take up thy " + weapon + " and steel yourself before me, here."
    health = randint(2,5)
    strike = 0
    Wizard_spectre = health
    print "Aileriun Cromsta, Cromsta - neigoon!"
    print "[a loud bang, and a ethereal image of a stag with blood dripping form it's eyes, stands before you. Confused a moment, its focus lands quickly on you. It bares jagged teeth.]"
    action = raw_input() 
    if action == "":
      print "You fool! Failed to act! [your flesh becomes like water and falls from your bones.]"
      exit()
    elif action ==re.compile("..."):
      strike += randint(2,4)
    if strike >= Wizard_spectre:
      print "[The Stag shatters into facets which fall to the floor and become sand on impact.]"
      print "You'll save us all. Dark times call for dark heros."
    else: 
      print "Again, you fool!! Before it's too late!"
    Wizard_spectre -= strike
         

print quest(playername)

