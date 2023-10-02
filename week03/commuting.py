waking_hours = 16 
BAD_COMMUTE = 1.5 
GOOD_COMMUTE = 0.75 # 45 mins :) 

day1 = float(input("Hours on Monday? "))
day2 = float(input("Hours on Tuesday? "))
day3 = float(input("Hours on Wednesday "))
day4 = float(input("Hours on Thursday "))
day5 = float(input("Hours on Friday "))

day1_percent = day1  / waking_hours
day2_percent = day2  / waking_hours
day3_percent = day3  / waking_hours
day4_percent = day4  / waking_hours
day5_percent = day5  / waking_hours

average_commute = (day1+day2+day3+day4+day5)/5

print(f"{'Day':10}{'%':>10}")
print("-"*25)
print(f"{'Monday':15}{day1_percent:10.0%}")
print(f"{'Tuesday':15}{day2_percent:10.0%}")
print(f"{'Wednesday':15}{day3_percent:10.0%}")
print(f"{'Thursday':15}{day4_percent:10.0%}")
print(f"{'Friday':15}{day5_percent:10.0%}")

print("The average commute is{average_commute} hours!")

if average_commute >= BAD_COMMUTE:
    print("sorry xo")

elif average_commute <= GOOD_COMMUTE: 
    print("nice!")
else: 
  print("could be worse")
