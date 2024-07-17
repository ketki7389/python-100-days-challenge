rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
game = [rock,paper,scissors]
user = int(input(" 0 for rock ,1 for paper or 2 for scissors\n"))
print(game[user])

rps= random.randint(0,2)
print(game[rps])

if (user == 0):
  if (rps == 0):
    print("It's a tie")
  elif (rps == 1):
    print("you lose")
  else :
    print("you win")

if (user == 1):
  if (rps == 1):
    print("It's a tie")
  elif (rps == 2):
    print("you lose")
  else :
    print("you win")

if (user == 2):
  if (rps == 2):
    print("It's a tie")
  elif (rps == 0):
    print("you lose")
  else :
    print("you win")

