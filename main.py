from random import randint
import time

print("Raven's BlackJack game.")

#sleep()
def sleep(Time):
  Time = float(Time)
  time.sleep(Time)

#async wait()
def wait(Time):
  time.sleep(Time)

#print + wait
def print_wait(msg, Time):
  print(msg)
  wait(Time)
  
#line
def line():
  print("--------------------")

line()
sleep(.5)
replay = True
while replay == True:
  print_wait("Would you like to play a game?", .5)
  replay2 = True
  while replay2 == True:
    answer = input("Y/N \n")
    answer = answer.lower()
    if answer == "y":
      replay2 = False
    elif answer == "n":
      print("Oh well...")
      sleep(1)
    else:
      print("Haha very funny, now type Y or N")
  sleep(.75)
  print_wait("Alright!", 1)
  print_wait("Now let's start", .5)
  deck = [randint(1,11), randint(1,11)]
  botDeck = [randint(1,11), randint(1,11)]
  print_wait("This is your starting deck.", .25)
  print(deck)

  #hit_or_pass function
  def hit_or_pass():
    print_wait("Dealer: Would you like to hit or pass? hit/pass/help", .5)
    replay2 = True
    while replay2 == True:
      choice = input("")
      choice = choice.lower()
      if choice == "hit":
        randomNum = randint(1,11)
        deck.append(randomNum)
        replay2 = False
      elif choice == "help":
        sleep(1)
        print_wait("Hit will give you a card ranging from 1 to 11 \nPass will skip your turn", 1)
        print("Now try to choose hit or pass")
      elif choice == "pass":
        replay2 = False
      else:
        print("Haha.. Now choose hit or pass")

        
  hit_or_pass()

  #Check Win/Lose
  deckNum = len(deck)
  BdeckNum = len(deck)

  #Bot
  if BdeckNum == 2:
    if(botDeck[0] + botDeck[1]) == 21:
      print("Your opponent won!")
      replay = False
      break
    elif(botDeck[0] + botDeck[1]) > 21:
      print("Your opponent exploded!")
      replay = False
      break

  #Player
  if deckNum == 2:
    if(deck[0] + deck[1]) == 21:
      print("You won!")
      replay = False
      break
    elif(deck[0] + deck[1]) > 21:
      print("You exploded!")
      replay = False
      break
  elif deckNum == 3:
    if(deck[0] + deck[1] + deck[2]) == 21:
      print("You won!")
      replay = False
      break
    elif(deck[0] + deck[1] + deck[2]) > 21:
      print("You exploded!")
      replay = False
      break

  line()
  print_wait("This is your current deck", .5)
  print(deck)
  line()
  print_wait("Now is your opponents turn.", .5)

  #Bot Turn Function
  def botChoose():
    bot_total = botDeck[0] + botDeck[1]
    replay2 = True
    while replay2 == True:
      if bot_total <= 13:
        botDeck.append(randint(1,11))
        print("Your opponent decided to hit!")
        replay2 = False
      elif bot_total >=17:
        print("Your opponent passed.")
        replay2 = False

  
  botChoose()

  #Check Win/Lose
  deckNum = len(deck)
  BdeckNum = len(deck)

  #Bot
  if BdeckNum == 2:
    if(botDeck[0] + botDeck[1]) == 21:
      print("Your opponent won!")
      replay = False
      break
    elif(botDeck[0] + botDeck[1]) > 21:
      print("Your opponent exploded!")
      replay = False
      break
  elif BdeckNum == 3:
    if(botDeck[0] + botDeck[1] + botDeck[2]) == 21:
      print("Your opponent won!")
      replay = False
      break
    elif(botDeck[0] + botDeck[1] + botDeck[2]) > 21:
      print("Your opponent exploded!")
      replay = False
      break

  #Player
  if deckNum == 2:
    if(deck[0] + deck[1]) == 21:
      print("You won!")
      replay = False
      break
    elif(deck[0] + deck[1]) > 21:
      print("You exploded!")
      replay = False
      break
  elif deckNum == 3:
    if(deck[0] + deck[1] + deck[2]) == 21:
      print("You won!")
      replay = False
      break
    elif(deck[0] + deck[1] + deck[2]) > 21:
      print("You exploded!")
      replay = False
      break
  
  hit_or_pass()
  
  #Check Win/Lose
  deckNum = len(deck)
  BdeckNum = len(deck)

  #Bot
  if BdeckNum == 2:
    if(botDeck[0] + botDeck[1]) == 21:
      print("Your opponent won!")
      replay = False
      break
    elif(botDeck[0] + botDeck[1]) > 21:
      print("Your opponent exploded!")
      replay = False
      break
  elif BdeckNum == 3:
    if(botDeck[0] + botDeck[1] + botDeck[2]) == 21:
      print("Your opponent won!")
      replay = False
      break
    elif(botDeck[0] + botDeck[1] + botDeck[2]) > 21:
      print("Your opponent exploded!")
      replay = False
      break

  #Player
  if deckNum == 2:
    if(deck[0] + deck[1]) == 21:
      print("You won!")
      replay = False
      break
    elif(deck[0] + deck[1]) > 21:
      print("You exploded!")
      replay = False
      break
  elif deckNum == 3:
    if(deck[0] + deck[1] + deck[2]) == 21:
      print("You won!")
      replay = False
      break
    elif(deck[0] + deck[1] + deck[2]) > 21:
      print("You exploded!")
      replay = False
      break
  elif deckNum == 4:
    if(deck[0] + deck[1] + deck[2] + deck[3]) == 21:
      print("You won!")
      replay = False
      break
    elif(deck[0] + deck[1] + deck[2] + deck[3]) > 21:
      print("You exploded!")
      replay = False
      break 

  line()
  print_wait("This is your current deck", .5)
  print(deck)

  #Bot's Turn
  line()
  print_wait("Now is your opponents turn.", .5)
  botChoose()
  
  #Check Win/Lose
  deckNum = len(deck)
  BdeckNum = len(deck)

  #Bot
  if BdeckNum == 2:
    if(botDeck[0] + botDeck[1]) == 21:
      print("Your opponent won!")
      replay = False
      break
    elif(botDeck[0] + botDeck[1]) > 21:
      print("Your opponent exploded!")
      replay = False
      break
  elif BdeckNum == 3:
    if(botDeck[0] + botDeck[1] + botDeck[2]) == 21:
      print("Your opponent won!")
      replay = False
      break
    elif(botDeck[0] + botDeck[1] + botDeck[2]) > 21:
      print("Your opponent exploded!")
      replay = False
      break
  elif BdeckNum == 4:
    if(botDeck[0] + botDeck[1] + botDeck[2] + botDeck[3]) == 21:
      print("Your opponent won!")
      replay = False
      break
    elif(botDeck[0] + botDeck[1] + botDeck[2] + botDeck[3]) > 21:
      print("Your opponent exploded!")
      replay = False
      break

  print_wait("Now it's time to compare!", 1)
  print_wait("Let's see...", 1)
  if BdeckNum == 2:
    bot_total = botDeck[0] + botDeck[1]
  elif BdeckNum == 3:
    bot_total = botDeck[0] + botDeck[1] + botDeck[2]
  elif BdeckNum == 4:
    bot_total = botDeck[0] + botDeck[1] + botDeck[2] + botDeck[3]

  print(f"Your opponent got a total of {bot_total}")
  sleep(1)
  
  if deckNum == 2:
    user_total = deck[0] + deck[1]
  elif deckNum == 3:
    user_total = deck[0] + deck[1] + deck[2]
  elif deckNum == 4:
    user_total = deck[0] + deck[1] + deck[2] + deck[3]

  print(f"You got a total of {user_total}")
  sleep(1)

  if user_total > bot_total:
    result = 0
  elif user_total < bot_total:
    result = 1
  else:
    result = 2

  if result == 0:
    print("You won this game!")
    replay=False
    break
  elif result == 1:
    print("Your opponent won!")
    replay = False
    break
  else:
    print("It's a tie!")
    replay = False
    break






















































































































































