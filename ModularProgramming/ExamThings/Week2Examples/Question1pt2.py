## Question 1##
def name_Time():
    name = input("what is your name! " )
    time_taken = int(input("please enter time taken: "))
    
    return name, time_taken

def encouragement(name, time_taken):
    if time_taken <= 60: 
        return f'well done {name} - Goal has been achived!'
    else:
        new_goal = time_taken - 5 
        return f'well done {name} - Youre new goal is {new_goal}'

def main():
    name , time_taken = name_Time()
    message = encouragement(name,time_taken)
    print(message)
    
main()