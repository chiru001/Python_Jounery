#! Escape String

#! What if we wanted to hvae a string that tells m, let's say, the weather and here we wan to write

#! weather = 'It's Sunny'
#! here python will take only IT and it do no take s Sunny how to fix that? we can use double quotations
weather = "'It's Sunny'"
print (weather)

#!Fine right now what if for the belwo statments?

#! weather_one = "it's " "kind of " sunny" 
#! Now we have another issue as a human languate we have single quoes and double quotes & apostrophes.

#! So in that cases we can use ESCAPE SEQUENCES (\).
weather_one = "it\'s \" \"kind of \" sunny" 
print(weather_one)

#! We can also use \ as text in few cases 
weather_two = "it\'s \\greeny"
print(weather_two)

#! We can also use (\t) what i will do? it will create a tab_space in output
weather_tab = "\t it\'s \" \"kind of \" sunny" 
print(weather_tab)

#! We can also add a new line (\n)
weather_line = "it\'s \" \"kind of \" sunny \n hope you have a great Morning!" 
print(weather_line)

#! Link: https://www.scaler.com/topics/escape-sequence-in-python/





