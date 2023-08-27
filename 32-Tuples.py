# Tuple

#! Tuples are like lists, but unlike lists we cannot modifiy them. They are immutable
#! so you cna think of them as immutable lists and they look this below

my_tuple = (1,2,3,4,5,6,7)
# my_tuple[1] = 'abcd'  #! we can't do this like list we can not modify it.

print(my_tuple[2])
print( 5 in my_tuple)

#! Only difference is taht it's immutable, they are faster than list 
user= {
    'basket' : [1,2,3],
    'greet' : 'hello',
    'age' : 20
}


print(user.items())


