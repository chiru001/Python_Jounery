#! Lets create a program that will guess your age

brith_year = int(input('what is your birth_year: '))

#! Here to calculate we use a logic brith year - current year 
#!note: when we give year it will store year in brith_year as a string so we uses int to conver str to number
age = 2023 - brith_year

print(f'hey! your age is {age}')