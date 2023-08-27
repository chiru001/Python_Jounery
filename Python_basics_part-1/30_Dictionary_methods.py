Dictionary = {
    'basket' : [1,2,3],
    'greet' : 'hello',
}
print(Dictionary['basket'])

#! Fine, we can abel to access the basked, But what if we don't know what this dictionary is?
#! may dict is somewher but we want to know if this let's call this user if this user has manybe propery like age
user = {
    'basket' : [1,2,3],
    'greet' : 'hello',
}
#print(user['age'])
#! do they have this age key? if the run the program we will get errors,
#! But errors in our programs is not good after print if will have a code the enitre code is ignored.
#! so if we want to check age is present in dict means we can use get
print(user.get('age')) #! .get is a method we will get None now there is no error

print(user.get('age', 55)) #! output is 55

#! hey if age is not present then add 55 to it 

#! Now what if age is present in dict?
user_one = {
    'basket' : [1,2,3],
    'greet' : 'hello',
    'age' : 20
}
print(user_one.get('age', 55)) #! output is 20

#! if age is present they give it, if not they add 55

#! we can create in another method too

user2 = dict(name = 'chiranjeevi')
print(user2) #! {'name': 'chiranjeevi'}  #! this was is not very common

