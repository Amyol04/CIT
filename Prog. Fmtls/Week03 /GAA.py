POINTS_PER_GOAL = 3 

team = input("what is the name of the team?")
points = int(input("how many points did {team} score? "))
goals = int(input("how many goals did {team} score? "))


total_points = goals * POINTS_PER_GOAL + points

print(f"{team} scord {total_points} in total ! ")
