#! We can also do slicing too 
my_tuple = (1,2,3,4,5,6,7)
new_tuple = my_tuple[1:2]
print(new_tuple) #! output is (2,)

#!  if i give 4 
my_tuple = (1,2,3,4,5,6,7)
new_tuple = my_tuple[1:4]
print(new_tuple) #! (2, 3, 4)
#! Tuples methods are only2 count() , index()
print(my_tuple.count(5)) #! there is only one 5 so output is 1

print(my_tuple.index(2)) #! whats the index of 2 which is 1 
print(my_tuple.index(5)) #! 4
print(len(my_tuple))
