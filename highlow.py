from art import logo, vs
from game_data import data
import random
print(logo)
from replit import clear

def ran():
  pick = random.choice(data)
  return pick
def greater(a,b):
  if a > b:
    return a
  else:
    return b

isContinue = True

p1 = ran()
count = 0
while isContinue == True:
  print(f"Compare A: {p1['name']}, a {p1['description']}, from {p1['country']}")
  print(vs)
  p2 = ran()
  print(f"Compare B: {p2['name']}, a {p2['description']}, from {p2['country']}")
  choose = input("Who has more followers? Type 'A' or 'B': ").lower()
  if (choose == "a" and p1['follower_count'] > p2['follower_count']) or ( choose == "b" and p1['follower_count'] < p2['follower_count']):
    p1 = p2
    count += 1
    clear()
    print(logo)
    print(f"You're right! Current score: {count}")
  else:
    clear()
    print(logo)
    print(f"sorry, that's wrong. Final score is {count}")
    isContinue = False



#def compare(a,b):

#print(f"Compare")
