passGrade = 40

grade1 = int(input("Grade 1 >>> "))
grade2 = int(input("Grade 2 >>> "))
grade3 = int(input("Grade 3 >>> "))


average = (grade1 + grade2 + grade3) / 3 

if average > passGrade: 
    print(f"With an average of{average:.2f}% you have passed :D !! ")
elif average < passGrade: 
    print(f"With an average of{average:.2f}% you have failed :(  !! ")

else: 
    print(f"With an average of{average:.2f}% you have passed - just :/ !! ")
