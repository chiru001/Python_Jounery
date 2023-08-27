#! Lets talk about another dataype which is str stands fro strings
#! A string is simply a peice of text, example a string can be written with quotation marks
#! 'hi' we can also make strings with double quotes "hi!"

print("Hi")
print(type("Hi"))

#! Now we can use this in many ways, For example, imagine you're creating a logic form and
#! we wan to collect somebodies username and password.
username = 'chiranjeevi'
password = 'Test@12345'
#! We can also use long string
long_string = '''
WOW THIS IS 
COOL 
HAAHAH
O O
---
'''
print(long_string)

#! Ltes do one more example

first_name = 'Chiranjeeevi'
last_name = "Dronamraju"
full_name = first_name + last_name
print(full_name) #!output will be ChiranjeeviDronamraju

#! here you can oberver there is no space :( how we can fix 
#! you cn just add space in last_name= " Dronamraju"
#! or we can add string in full_name = first_name + ' ' + last_name
full_name_space = first_name + ' ' + last_name
print(full_name_space)

#! +++++++++++++++++++++++++++String_Concatenation++++++++++++++++++++++++++++++++++++
#!  what is concatenation??
#! Adding strings together like 'chiranjeevi' + ' dronamraju'
print ('chiranjeevi' + " Dronamraju")
#! what if we add 5?
#! print ('chiranjeevi' + 5) #! output Error can only concaenate sr(no "int") to str
#! what if i type 100 now as we know 100 is a inegere but what will i add datatype str before 100?
#! lets do it alone lets find type also 
print(type(100))  #! output is int

print(type(str(100)))  #! output is str so now using str we can able to add integers.


print ('chiranjeevi' + str(5)) #!output is chiranjeevi5 This time no errors :)
 
#! can you find what it is?
print(type(int(str(100))))  #!output will be int but why?

#! point1: 100 became string - which is step1
#! point2: now that string became integer because we wrapped int on str - which is step2
#! point3: After that we used type so answer will be "int"
#! To understand better
a = str(1001)
b = int(a)
c = type(b)
print(c)

#! This is the idea of Type conversion


