suit = input("What is the suit? ").lower()

if suit == "hearts" or suit == "diamonds": 
    print("red")

elif suit == "spade" or suit == "club": 
    print("black")

else: 
    print("Invalid suit. ")

