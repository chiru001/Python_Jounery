# Dictionary

#! we will be using "dict", its a way for us to organize our data in a form that is has some
#! different pros and cons in how we access it
#! Example: list( they can easily ordered we can access them through indexed like zero one)
#! What about dictionary?

Dictionary = {
     'a': 1,
     'b': 2
 }
print(Dictionary['a']) #! 1
#! Here we are using curly brackets here, which denotes a dictionary and unlike a list,we
#! we have what we call a key value pair.  key is string to grep a value here a is a key will gep value 1
#!* when call Dictionary it will not come in order like list . It is unordered key_value pair
Dictionary_one = {
     'a': [1,2,3],
     'b': 'hello',
     'c': True
 }

#! inside dict it can be anything we can create a list we can add string ...

#! we can do it using lists

my_list = [
    {
     'a': [1,2,3],
     'b': 'hello',
     'c': True
    },
    {
     'a': [4,5,6],
     'b': 'hello',
     'c': True
    }
    
]
print(my_list[0]['a'][2])
print(my_list[1]['a'][2])







