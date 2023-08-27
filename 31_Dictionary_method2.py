user= {
    'basket' : [1,2,3],
    'greet' : 'hello',
    'age' : 20
}

#! They is one more other way,How to look for item inside dict
print('basket' in user) #!True
print('size' in user) #! False

#! Here it will get intresting, and this agin,is a another dictionary method that we can use.
#! First method is keys, what are the keys of user

print('age' in user.keys()) #!True
print('hello' in user.values()) #!True
print(user.items()) #! item  it will grep all the content in dict here its a tuple.
user.clear()
print(user)  #!empty dict

#! Copy_MEthod
user1= {
    'basket' : [1,2,3],
    'greet' : 'hello',
    'age' : 20
}
user2 = user1.copy()
print(user.clear())    #! here use1 data will be lost but we taken a copy so user2 will have
print(user2)

#! POP
user3= {
    'basket' : [1,2,3],
    'greet' : 'hello',
    'age' : 20
}

print(user3.pop('age')) #! 20 

#! here why we got output as 20 because POP will returns the value which has been remove.

print(user3) #! age has been removed.

#!UPDATE
print(user3.update({'age' : 55}))
print(user3)




