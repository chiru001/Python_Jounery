my_set = {1,2,3,4,5}
your_set = {4,5,6,7,8,9,10}

print(my_set.difference(your_set)) #! output {1, 2, 3} it will show only difference
print(my_set.discard(5)) #! None #! ignore 5 
print(my_set) #! {1, 2, 3}
print(my_set.difference_update(your_set)) #!remove all elements of another set from this set
print(my_set) #! {1, 2, 3}
print(my_set.intersection(your_set))

#! PENDING NEED TO UPDATE IT
