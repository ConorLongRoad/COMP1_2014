# Skeleton Program code for the AQA COMP1 Summer 2014 examination
# this code should be used in conjunction with the Preliminary Material
# written by the AQA Programmer Team
# developed in the Python 3.2 programming environment
# version 2 edited 06/03/2014

import pdb
import random
import datetime

NO_OF_RECENT_SCORES = 3

class TCard():
  def __init__(self):
    self.Suit = 0
    self.Rank = 0

class TRecentScore():
  def __init__(self):
    self.Name = ''
    self.Score = 0
    self.Date = ""

Deck = [None]
RecentScores = [None]
Choice = ''

def GetRank(RankNo):
  Rank = ''
  if RankNo == 1:
    Rank = 'Ace'
  elif RankNo == 2:
    Rank = 'Two'
  elif RankNo == 3:
    Rank = 'Three'
  elif RankNo == 4:
    Rank = 'Four'
  elif RankNo == 5:
    Rank = 'Five'
  elif RankNo == 6:
    Rank = 'Six'
  elif RankNo == 7:
    Rank = 'Seven'
  elif RankNo == 8:
    Rank = 'Eight'
  elif RankNo == 9:
    Rank = 'Nine'
  elif RankNo == 10:
    Rank = 'Ten'
  elif RankNo == 11:
    Rank = 'Jack'
  elif RankNo == 12:
    Rank = 'Queen'
  elif RankNo == 13:
    Rank = 'King'
  return Rank

def GetSuit(SuitNo):
  Suit = ''
  if SuitNo == 1:
    Suit = 'Clubs'
  elif SuitNo == 2:
    Suit = 'Diamonds'
  elif SuitNo == 3:
    Suit = 'Hearts'
  elif SuitNo == 4:
    Suit = 'Spades'
  return Suit

def DisplayMenu():
  print()
  print('MAIN MENU')
  print()
  print('1. Play game (with shuffle)')
  print('2. Play game (without shuffle)')
  print('3. Display recent scores')
  print('4. Reset recent scores')
  print("5. Options")
  print()
  print('Select an option from the menu (or enter q to quit): ', end='')

def GetMenuChoice():
  Choice = input()
  print()
  return Choice.capitalize()

def LoadDeck(Deck):
  CurrentFile = open('deck.txt', 'r')
  Count = 1
  while True:
    LineFromFile = CurrentFile.readline()
    if not LineFromFile:
      CurrentFile.close()
      break
    Deck[Count].Suit = int(LineFromFile)
    LineFromFile = CurrentFile.readline()
    Deck[Count].Rank = int(LineFromFile)
    Count = Count + 1
 
def ShuffleDeck(Deck):
  SwapSpace = TCard()
  NoOfSwaps = 1000
  for NoOfSwapsMadeSoFar in range(1, NoOfSwaps + 1):
    Position1 = random.randint(1, 52)
    Position2 = random.randint(1, 52)
    SwapSpace.Rank = Deck[Position1].Rank
    SwapSpace.Suit = Deck[Position1].Suit
    Deck[Position1].Rank = Deck[Position2].Rank
    Deck[Position1].Suit = Deck[Position2].Suit
    Deck[Position2].Rank = SwapSpace.Rank
    Deck[Position2].Suit = SwapSpace.Suit

def DisplayCard(ThisCard):
  print()
  print('Card is the', GetRank(ThisCard.Rank), 'of', GetSuit(ThisCard.Suit))
  print()

def GetCard(ThisCard, Deck, NoOfCardsTurnedOver):
  ThisCard.Rank = Deck[1].Rank
  ThisCard.Suit = Deck[1].Suit
  for Count in range(1, 52 - NoOfCardsTurnedOver):
    Deck[Count].Rank = Deck[Count + 1].Rank
    Deck[Count].Suit = Deck[Count + 1].Suit
  Deck[52 - NoOfCardsTurnedOver].Suit = 0
  Deck[52 - NoOfCardsTurnedOver].Rank = 0

def IsNextCardHigher(LastCard, NextCard):
  Higher = False
  if NextCard.Rank > LastCard.Rank:
    Higher = True
  return Higher

def GetPlayerName():
  print()
  Good = False
  pdb.set_trace()
  while not Good:
    PlayerName = input('Please enter your name: ')
    Good = PlayerName.isalpha()
  print()
  return PlayerName

def GetChoiceFromUser():
  Choice = input('Do you think the next card will be higher than the last card (enter y or n)? ')
  return Choice.capitalize()

def DisplayEndOfGameMessage(Score):
  print()
  print('GAME OVER!')
  print('Your score was', Score)
  if Score == 51:
    print('WOW! You completed a perfect game.')
  print()

def DisplayCorrectGuessMessage(Score):
  print()
  print('Well done! You guessed correctly.')
  print('Your score is now ', Score, '.', sep='')
  print()

def ResetRecentScores(RecentScores):
  for Count in range(1, NO_OF_RECENT_SCORES + 1):
    RecentScores[Count].Name = ''
    RecentScores[Count].Score = 0

def DisplayRecentScores(RecentScores):
  print()
  print('Recent Scores: ')
  print()
  print("Name:           Score:            Date:")
  for Count in range(1, NO_OF_RECENT_SCORES + 1):
    print("{0:10} {1:>10} {2:>17}".format(RecentScores[Count].Name, RecentScores[Count].Score, RecentScores[Count].Date))
  print()
  print('Press the Enter key to return to the main menu')
  input()
  print()

def GetCurrentDate():
  DateNow = datetime.datetime.now()
  Current_Day = DateNow.day
  Current_Month = DateNow.month
  Current_Year = DateNow.year
  Current_Time = "{0}/{1}/{2}".format(Current_Day, Current_Month, Current_Year)
  return Current_Time

def UpdateRecentScores(RecentScores, Score, Date):
  PlayerName = GetPlayerName()
  FoundSpace = False
  Count = 1
  while (not FoundSpace) and (Count <= NO_OF_RECENT_SCORES):
    if RecentScores[Count].Name == '':
      FoundSpace = True
    else:
      Count = Count + 1
  if not FoundSpace:
    for Count in range(1, NO_OF_RECENT_SCORES):
      RecentScores[Count].Name = RecentScores[Count + 1].Name
      RecentScores[Count].Score = RecentScores[Count + 1].Score
      RecentScores[Count].Date = RecentScores[Count + 1].Date
    Count = NO_OF_RECENT_SCORES
  RecentScores[Count].Name = PlayerName
  RecentScores[Count].Score = Score
  RecentScores[Count].Date = Date

def DisplayOptions():
  print()
  print("Here are the options: ")
  print()
  print("1. Set Ace to High or Low")
  print("2. ")
  print("3. ")
  print()

def GetOptionChoice():
  Number = False
  print("Please enter the option that you'd like to enter (1-5): ")
  while not Number:
    Option = int(input())
    if Option > 0 and Option < 5:
      return Option

def SetOptionChoice(Option):
  if Option == 1:
    SetAceHighOrLow()

def SetAceHighOrLow():
  Done = False
  print()
  print("Please enter whether you'd like to have the ace be (H)igh or (L)ow: ")
  while not Done:
    Choice = input()
    if Choice.capitalize() == "H" or Choice.capitalize() == "High":
      return "H"
    elif Choice.capitalize() == "L" or Choice.captialize() == "Low":
      return "L"
    else:
      print("That is not a valid entry. Please try again")
  
def PlayGame(Deck, RecentScores):
  LastCard = TCard()
  NextCard = TCard()
  GameOver = False
  GetCard(LastCard, Deck, 0)
  DisplayCard(LastCard)
  NoOfCardsTurnedOver = 1
  while (NoOfCardsTurnedOver < 52) and (not GameOver):
    GetCard(NextCard, Deck, NoOfCardsTurnedOver)
    Choice = ''
    while (Choice != 'Y') and (Choice != "Yes") and (Choice != 'N') and (Choice != "No"):
      Choice = GetChoiceFromUser()
    if Choice == "Y" or Choice == "Yes":
      Choice = True
    if Choice == "N" or Choice == "No":
      Choice = False
    DisplayCard(NextCard)
    NoOfCardsTurnedOver = NoOfCardsTurnedOver + 1
    Higher = IsNextCardHigher(LastCard, NextCard)
    if (Higher and Choice == True) or (not Higher and Choice == False):
      DisplayCorrectGuessMessage(NoOfCardsTurnedOver - 1)
      LastCard.Rank = NextCard.Rank
      LastCard.Suit = NextCard.Suit
    else:
      GameOver = True
  if GameOver:
    DisplayEndOfGameMessage(NoOfCardsTurnedOver - 2)
    Display = input("Would you like your score to be on the leaderboard (y)? ")
    if Display.capitalize() == "Y" or Display.capitalize() == "Yes":
      Date = GetCurrentDate()
      UpdateRecentScores(RecentScores, NoOfCardsTurnedOver - 2, Date)
  else:
    DisplayEndOfGameMessage(51)
    UpdateRecentScores(RecentScores, 51)

if __name__ == '__main__':
  for Count in range(1, 53):
    Deck.append(TCard())
  for Count in range(1, NO_OF_RECENT_SCORES + 1):
    RecentScores.append(TRecentScore())
  Choice = ''
  while Choice != 'Q' and Choice != "Quit":
    DisplayMenu()
    Choice = GetMenuChoice()
    if Choice == '1':
      LoadDeck(Deck)
      ShuffleDeck(Deck)
      PlayGame(Deck, RecentScores)
    elif Choice == '2':
      LoadDeck(Deck)
      PlayGame(Deck, RecentScores)
    elif Choice == '3':
      DisplayRecentScores(RecentScores)
    elif Choice == '4':
      ResetRecentScores(RecentScores)
    elif Choice == "5":
      DisplayOptions()
      OptionChoice = GetOptionChoice()
      SetOptionChoice(OptionChoice)

#Deck of Cards Questions:

#Task 3a:

#Question 1:
#Which function is responsible for getting the name from the user?

#GetPlayerName()

#Question 2:
#How will you ensure that the user is asked for the name repeatedly?

#By adding a while loop so that it ensures that the user enters anything but "".
#Also, by using the .isalpha, it ensures that the user is entering letters and not
#just a load of spaces

#Question 3:
#What additional variable will you need and what will its datatype be?

#.isalpha will be needed. It's datatype is boolean, so if the variable contains
#letters, then it will be true, but if there's anything in the varaible that's not
#letters then it will be false


#Task 3b:

#Question 1: Which function is responsible for adding scores to the table?
#UpdateRecentScores()


#Task 5:

#Question 1: What additional module will you need to import into the program?
#import datetime

#Question 2: Identify the four functions that will require changes.
#DisplayRecentScores(), where you'd have to bring forth the date and time to output it
#GetCurrentDate(), which I created to make it just for displaying the time
#UpdateRecentScores(), which was used to add the date and time to the record
#PlayGame(), where it would activate all 3 of the above functions and so would need to pass the value through

#Question 3: How do you convert a string in the format DD/MM/YY (e.g. 14/08/93) to a **date** type in Python?
#I did it by using the datetime.datetime.now() function to get the values of minute/hours/day/month/year/etc,
#then by naming that list of values individually so you get the values you need from that variable.
#e.g.
#DateNow = datetime.datetime.now()
#Current_Minute = DateNow.minute
#Current_hour = DateNow.hour
#Current_day = DateNow.day

#I then brought all these values into 1 variable called Current_Time, by using the .format to format the
#current date and time into a variable


# Additional tasks:

#Question 1: Describe each variable role in your own words

#Fixed value - A variable that is created, but cannot be altered or changed. This can be useful for
#remembering the number of variable elements in use

#Stepper - A counter that goes through a for loop and counts the number of itterations that proceed
#during the process

#Most Recent Holder - The most recent itteration of a variable, for example a running total, where the
#total is constantly changing and being added to

#Most Wanted Holder - The variable needed the most to complete the task set (e.g. having a while loop
#through a set of integers, and if the value needed to end the loop is over 30, then the most wanted
#holder will be 33 or 49, or anything above 30

#Gatherer - A variable that accepts all the individual values to end up with a running total at the end
#(e.g. adding up numbers. Or even adding up strings so you get a long string at the end)

#Transformation - A variable that uses the same calculation for each variable, but will use different
#variables to work out a final answer (e.g. finding the mean of a set of numbers. It will work the
#same way but because you're using different numbers, the total is different

#Follower - A variable that gets its new value from the old value of another variable, if you need to
#save that original value (e.g. a=2, b=a+2, c=b+a, etc)

#Temporary - A variable that only uses a value for a short period of time, such as a bubble sort, where
#you need to temporarly use that value


#Question 2: Give an example of variable from the program code for each variable role.

#Question 1: Describe the difference between passing by value and passing by reference in your own words

#Passing by reference is passing the location of that data on, whereas passing the value is only passing
#what already exists. Passing the reference is going directly to the value, whereas passing the value is
#similar to copying the value onto another variable location
