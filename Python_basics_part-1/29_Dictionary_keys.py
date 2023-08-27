Dictionary = {
    'weapons' : [1,2,3],
    'greeting' : 'hello',
    'is_Magic' : True
}

#! Till now we have used a string can we usewith number or bool? lets find out
''' 
Dictionary_one = {
    123 : [1,2,3],
    True : 'hello',
    [100] : True
}
print(Dictionary_one[123]) #! OUTPUT is [1,2,3]
print(Dictionary_one[True]) #! hello
#print(Dictionary_one[100]) #! error: unhashable type: 'list what does it means?
'''
#! Dictionary keys need to have a special property a key needs to be immutable.
#! That means a key cannot change, numbers and boolean, this is a value that cannot change
#! list is mutable if we change data might lost so dic don't want that so we are getting error.
#! Dictionary key always immutable.

#! What if i have same key name in dic?
Dictionary_two = {
    123 : [1,2,3],
    123 : 'hello',
}
print(Dictionary_two[123]) #! hello

#! A key in a dict has to be unique because there can only be one key, because that key is going to represent a bookshelf in that memory space.
#! So any time i do the same key and maybe add a value, it's going to overwrite
#! So in our case [1,2,3] is no longer exist 
 