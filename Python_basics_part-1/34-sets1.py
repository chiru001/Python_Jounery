# set

#! Sets are simply unordered collections of unique objects

my_set = {1,2,3,4,5}  #! This called set
print(my_set) #! {1, 2, 3, 4, 5}

my_set1 = {1,2,3,4,5,5}
print(my_set) #! {1, 2, 3, 4, 5}  #! WHERE IS ANOTHER 5? see definition it will only show unique objects

my_set1.add(100)
my_set1.add(2)
print(my_set1) #! {1, 2, 3, 4, 5, 100}

#! here we also add 2 which is not there because 2 is already present in set(unique objects)

#! see we have list and list have different same values now we need to get only unique values in lists

my_list = [1,2,3,4,5,6,6,5]
print(set(my_list))  
print(len(my_list))
my_set3 = {1,2,3,4,5,6,7,8}  #!Created a set3
new_set = my_set3.copy()  #! created copy of set3 and loaded to variable new_set
my_set3.clear() #! clearing the set3
print(new_set) #! print 