# Guessing Game
pasword = 'khaldric'
guess = ""
count = 0
limit = 4
bol = False
while guess != pasword and not  bol:
    if count < limit:
      print(f"you try pasword {count}")
      guess = input('guess password : ').strip().lower()
      count += 1
    elif count == limit:
        bol = True
        print(f"you are loste !")
      
if guess == pasword:
        print("CORECTE PASSWORD !")
