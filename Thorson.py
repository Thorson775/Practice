print("hello")
#Space Travel Calculator 
print("Welcome to the Space Travel Calculator ")
var1 = input("are you ready to be an astro-physicist?")
if var1 == "yes" or "Yes":
  print("lets get started")
elif var1 != "yes" or "Yes":
  input("you wanna reconsider? Cmon just say yes bruh")
  if var1 == "yes":
    print("lets get started")
var3 = "distance" 
var3 = input("what is the distance to the celestial object?")
var3 = int(var3)
var4 = "speed"
var4 = input("what is the speed of the spacecraft") 
var4 = float(var4)
var5 = "time"
var5 = (var3/var4)
print("time to travel to the celestial object is", var5) 




#Restaurant Ranker
print("lets play another game")
ask = input("how does a restaurant ranking game sound? Sounds good or sounds bad?")
if ask == "sounds good" or "yes":
  print("lets get started")
elif ask == "sounds bad" or "no":
  var6 = input("okay, you wanna change your mind fool?")
if ask == "sounds good" or "yes":
  print("You just got hired by restaurantboxd, the restaurant rating app. Your first task is to create a program that asks a user for their favorite restaurants and store these restaurants as a list.")
var1 = input("hello, what is your name?") 
print("That's great", var1, "before we order your food lets do a survey")
favorite_restaurant=input("what's your favorite restaurant?") 
places = []
while favorite_restaurant != "stop":
  favorite_restaurant=input("what's your favorite restaurant?")
  print(favorite_restaurant)
  if favorite_restaurant == "stop":
    break 
  places.append(favorite_restaurant)
  
print(places)




#Recylcing Machine 
total_count = { "aluminum": 135, "plastic": 102, "paper": 213} 
def sortItems(itemstring): 
  for letter in itemstring:
    if letter == "A" or letter == "a":
      total_count["aluminum"] += 1
    if letter == "P" or letter == "p":
      total_count["plastic"] += 1
    if letter == "R" or letter == "r":
      total_count["paper"] += 1
sortItems('AAPAARRRRPAAPPRRP')
print(total_count)

# var1 = input("you wanna play best out of three?") 
# if var1 == "yes":
#   print("okay, lets go") 
  # while input "enter either rock, paper, scissors":
  # if player1score == 2:
  #   print("player1 wins") 
  #   break 
  # if player2score == 2: 
  #   print("player2 wins")
  #   break 
# elif var1 == "no":
#   print("okay, just say yes next time")


#Rock, Paper, Sciccors 
player1score = 0
player2score = 0



def play_game():
  player1 = input ("enter either rock, paper, scissors") 
  player2 = input ("enter either rock, paper, scissors")
  
  if (player1 == "rock" and player2 == "rock"):
    print("draw") 
  
  if (player1 == "rock" and player2 == "scissors"):
    print("player1 wins") 
    player1score = player1score + 1
  
  if ("player1" == "rock" and player2 == "paper"):
    print("player1 wins")
    player1score = player1score + 1
  
  if (player1 == "paper" and player2 == "paper"):
    print("draw")
  
  if (player1 == "paper" and player2 == "rock"):
    print("player1 wins") 
    player1score = player1score + 1
  
  if (player1 == "paper" and player2 == "scissors"):
    print("player2 wins")
    player2score = player2score + 1
  
  if (player1 == "scissors" and player2 == "scissors"):
    print("draw")
  
  if (player1 == "scissors" and player2 == "rock"):
    print("player2 wins")
    player2score = player2score + 1
  
  if (player1 == "scissors" and player2 == "paper"):
    print("player1 wins")
    player1score = player1score + 1

while play_game():
  if player1score == 2:
    print("player1 wins") 
    break
  if player2score == 2: 
    print("player2 wins")
    break 

print ("player1 score is", player1score)
print ("player2 score is", player2score)