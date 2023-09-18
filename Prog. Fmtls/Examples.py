print("hello world :D!!!") # string. collection of characters, 
print('hellooo')
print("hello", "there") #printing two thingzz 
print(''' slay
      yyy
      yyy
      yyy''') # triples ! prints exactly wha you type 


#^^ Strings 


print("hello \n","there") ## \n new line, begining of escape sequence
print("hello \n\t","there") # \n\t new tab 
print("\"Romeo, Romeo ect \"")   # awk way to add quotes 
print('"Romeo, Romeo ect"') # more friendly way of doing quotes <3 

## ^^ formatting 


print("hello", "there",  sep='****', end='$$$$')  # change behavor and seprate. only applies to current print.
print("hello", "there !! ",  sep='****', end='\n\t') # override behavor 
print("hello", "there :) ")


# 


greeting = "hello"
class_name = "comp1c"
print(greeting, class_name)

welcome = greeting + " " + class_name
print(welcome)

# String Variables ^^  .. putting them together. makes a new string.  String Concatenation

print(greeting*3) ## multiplying string by whole number. only whole. pls 
print("-"*30)

#operators 

# Numbers 

#name them right or lecture will bate ya 

x = 9.0  # a whOle number woah 
y = 8.0 # omg another whole number 

print(x+y) # add 
print(x-y) # subtract 
print(x*y) # multiply 
print(x/y) # divide

# 
x = 20  
y = 4  ## two non standard operators 

print(20//6) 

print(20 % 6) 

## Long division. 

x = 20  
y = 4 
result = x + y 
print(f"{x} + {y} = {result}") ## cleaner way of typing the sentence. has to be f as format string. 
print(x, "+", y, "=", result ) ## old way but works i guess. 
 # both achive same , ones cleaner and more modren. 

