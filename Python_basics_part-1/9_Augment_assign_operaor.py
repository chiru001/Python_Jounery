#! Augment Assign Operator?

#! We know that we can create a variables like "some_values = 5" so to increase the some_value i can do that
#! some_value = 5 + 2 =7 or i can also do something like this some_value = some_value + 2.
#!  Instead of doing like above we can use AUGMENT ASSIGN OPERATOR some_value += 2
#!Normal_Method

some_values = 5       #! 5
some_value = 5 + 2   #! 7
some_value = some_value + 2 #!9

#! Augment Assign Operator
some_value += 2 #! 11

print(some_value)  #!output is 11

some_mutiply = 5
some_mutiply *= 2

print(some_mutiply) #!output is 10


substract = 10
substract -=5
print(substract) #!output is 5

