team = input("what is the name of the team?")
wins = int(input("how many times did they win"))
loss = int(input("how many times did they lose"))
draw = int(input("how many times did they draw"))


winpoint = wins * 3
losspoint = 0
drawpoint = draw * 1
totalpoints = winpoint + drawpoint + losspoint
print(f"The total points {team} has is {totalpoints}")
