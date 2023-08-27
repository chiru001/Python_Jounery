# formatted strings

#! Up untill now we've just written simple strings, but we want a program that's dynamic, that'static 
#! Lets say we have amazon page and e're working at Amazon, actually. 
#! And a user logs into teir profile, we want to display their name or what they have in te cart.
#! Ideally what we can do is have something dynamic where let' say its a profile page and we simple use the name variable and we display that on the page.

name = "Chiranjeevi"
age = 55
print(name)
#! here we also need to greet that person
print('hi '+ name)
print('hi ' + name + '. You are ' + str(age) + ' Years old')
#! Now we will use Formatted_strings
print(f'hi {name} . You are {age}  Years old')

#! We can also do using format (python 2 uses)
print('hi{}. you are {} years old'.format(name,age))

#! what if i need to change orger like first i need to get age and then name 
print('hi{1}. you are {0} years old'.format(name,age))

#! Now we can also create a custom varables

#! print('hi{0}. you are {1} years old'.format(new_name='dcr', age=100))

#! from the above line we will be getting error range something to fix this we just need to add
#! varaible names inside {}
print('hi{new_name}. you are {age} years old'.format(new_name=' dcr', age=100))
