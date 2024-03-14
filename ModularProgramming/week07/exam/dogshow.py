# Amy o leary
# R00246749
# dog show code 



def get_competition_and_numbers():# question 2, getting the list comp and numbers! 
    print("Name : Amy o leary \nStudent Number: R00246749")
    competition_name = input("please enter the name of the competition: ")
    num_dogs = int(input("please enter the number of dogs: "))
    return competition_name, num_dogs

def get_dog_names_and_scores(competition_name, num_dogs): # question 3, getting the dogs names and scores!
    print("\n" + competition_name + " competition")
    print("\n""------------------------")
    dog_names = [input(f"please enter the name(s) of the dog(s) {i+1}: ") for i in range(num_dogs)]
    dog_scores = [int(input(f"please enter the score for {dog}: ")) for dog in dog_names]
    print("\n""------------------------")
    return dog_names, dog_scores   # this takes the dogs scores and names and puts them into "dog_names" and "dog_scores"

def get_range_of_score(score_list): # question 4, getting the range of scores! 
    min_score = min(score_list) # gets the smallest number.
    max_score = max(score_list) # gets the largest number.
    print("\n" f"The range of scores are from {min_score} to {max_score}.") 
    print("\n""------------------------")
    
def get_list_of_dogs_to_proceed(names, scores): # question 5, list of qualifying dogs
    qualified_dogs = [] 
    for i in range(len(names)):
        if scores[i] > 6:# checking if dog score is above 6 
            qualified_dogs += [names[i]] # for loop to make a new list for qualifying dogs 
    return qualified_dogs

def main(): # question one, the main funtion! 
    competition_name, num_dogs = get_competition_and_numbers()
    dog_names, dog_scores = get_dog_names_and_scores(competition_name, num_dogs)

    get_range_of_score(dog_scores)
 
    qualified_dogs = get_list_of_dogs_to_proceed(dog_names, dog_scores)
    print("\n"f"The number of dogs proceeding to the next round is {len(qualified_dogs)}:")
    for dog in qualified_dogs:
        print(dog)  #prints the dogs that have a score over 6. 

main() # calling main!
