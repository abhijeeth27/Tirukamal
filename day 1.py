print ('a'*10) # to give same output multiple times 

price = 100 #int
raing = 4.3 #float
name = 'pen' # string
# avilable = True / False #boolean
# print(avilable)

name = input("Hey, Whats your name ? ") # taking input
print("Hello "+ name)
color = input("whats your fav colour ? ")
print(name + ' fav colour is '+ color)

year = input("your birth year")
age = 2024 - int(year) # converts the input string to integer
print(type(age)) # used to find the typr of the veriable
print(age)

# converting lbs to kg
weight = input("your weight in lbs : ")
weight_kg = int(weight)*0.45
print(weight_kg)

#string
s1 = 'hi my name is "abhi"?'
s2 = "hi ther's a cat"
s3 = ''' hi,
         i am abhijeeth from technical team
         nice to meet you'''

# formated strings
first_name = "Abhijeeth"
last_name = "Varma"
msg = f'{first_name} [{last_name}] is a coder'
print(msg)

print(len(s3)) # used to print the length of the string