import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def sum(l): 
  addt = 0
  for i in l:
    addt += i
  return addt

def ace(someone):
  for i in someone:
    if i == 11:
      if sum(someone) < 22:
        return
      else:
        k = someone.index(i)
        someone[k] = 1

def card():
  user = random.sample(cards,2)
  
  dealer = random.sample(cards,2)

  print(f"user = {user}")

  if sum(dealer) == 21:
    print("Dealer Wins")
    print(f"user = {user} dealer = {dealer}")
    return
  elif sum(user) == 21:
    print("You Win")
    print(f"user = {user} dealer = {dealer}")
    return

  ace(user)
  ace(dealer)

  if sum(user) > 21:
    print("Dealer Wins")
    print(f"user = {user} dealer = {dealer}")
    return

  print(f"Here is dealer card {dealer[0]}")

  repeat_again = True

  while repeat_again:
    again = input("User: Do you want to pick another card? \n")

    if again == "y":
      next = random.sample(cards,1)
       
      for object in next:
        user.append(object)
        if sum(user) > 21:
          print("Dealer Wins")
          print(f"user = {user} dealer = {dealer}")
          return
        elif sum(user) == 21:
          print("You Win")
          print(f"user = {user} dealer = {dealer}")
          return

          
    else:
      repeat_again = False

    print(f"user = {user}")

  if sum(dealer) > 16:
    if sum(dealer) > sum(user):
      print("Dealer Wins")
      print(f"user = {user} dealer = {dealer}")
      return
    elif sum(dealer) == sum(user):
      print("It's a PUSH")
      print(f"user = {user} dealer = {dealer}")
      return
    else:
      print("You Win")
      print(f"user = {user} dealer = {dealer}")
      return
  else:
    loop = True
    while loop == True:
      next2 = random.sample(cards,1)
      for object in next:
        dealer.append(object)
        if sum(dealer) > 16:
          if sum(dealer) > sum(user):
            print("Dealer Wins")
            print(f"user = {user} dealer = {dealer}")
            return
          elif sum(dealer) == sum(user):
            print("It's a PUSH")
            print(f"user = {user} dealer = {dealer}")
            return
          else:
            print("You Win")
            print(f"user = {user} dealer = {dealer}")
            return
        else:
          continue
          
        

card()

while True:
  user_in = input("Do you want to play again? y or n \n")
  if user_in == "y":
    card()
  else:
    break

