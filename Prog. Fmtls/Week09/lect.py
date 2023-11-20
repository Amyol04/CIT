#                                    ~reading and making files~ 


#                                      ✧*̥ ˚writing files *̥˚✧ 

import random
connection = open("numbers.txt", "w")  #creats file  

for i in range(10):
    print(random.randint(1, 100),file=connection) # writes random nums 1-10 in said file.

connection.close() # closes connection

#### shorter way of doing the tiop 

with connection("numbers.txt", 'a') as connection: 
    for i in range(10):
      print(random.randint(1, 100),file=connection)

######
#                                       ✧*̥˚ reading files *̥˚✧ 


source_file = open("numbers.txt", 'r')

all_data = source_file.read()

source_file.close()

print(all_data)


##

source_file = open('numbers.txt', 'r')

total = 0

for line in source_file: 
     line = line.strip() # strips out whitespace 
     total += int(line) # makes an interger of the string from the file 
     print(line) 


source_file.close()
print(total)

####
#                                     ✧*̥˚ cars example! *̥˚✧ 

# Nissan,Leaf,2019,Electric,32000
# Ford,Ka,2016,Petrol,12000
# Audi,A5,2010,Diesel,10000

# for the file

cars_file = open('cars.txt', 'r')

output=open("output_cars.txt", 'w')

for line in cars_file: 
    line= line.strip() # gets rid of final \n
    line= line.split(',') #splits it up , sep my commas 
    make = line[0]  # gets first item and store in make 
    model = line[1]
    year = int(line[2]) 
    engine = line[3]
    price = float(line[4]) 
    print(f"{make:10}{model:10}{year:5}{engine:10}{price:10.2f}",file=output)





cars_file.close()
output.close()

#########
#                                     ✧*̥˚ student example! *̥˚✧         


student_file = open('student.txt', 'r')
total = 0 
number_student = 0 
oldest_name = ''
oldest_age = 0

for line in student_file: 
    line = line.strip() # strips out white space 
    line = line.split(',') # split into list of items 
    name = line[0] # extraxt to variables 
    age = int(line[1])
    grade = float(line[2])
    number_student += 1 # average. 
    total += grade
    if age> oldest_age: 
        oldest_age = name

student_file.close

average = total / number_student
print(average)
print(oldest_name)
