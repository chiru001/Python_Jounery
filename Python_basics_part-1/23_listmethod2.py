basket = ['a','b','c', 'd', 'e']

#! index
#! i am asking what is the index of d as per the basked it is 3
print(basket.index('d')) #! output is 3
print(basket.index('d',0,4)) #! its like finding d from 0 index to 4th index

#! The other way is we have keywords, we can aslo use of it for example in-keyword

print('d' in basket) #! True
print('x' in basket) #! False 

#! we can also do it for strings
print('i' in 'chiranjeevi') #! True

print('u' in 'chiranjeevi') #! False 

#! lets learn another one which is count
#! we can count how many times did same letter present in basket
print(basket.count('d')) #! 1

#! lets take new basket and perform this 

basket_one = ['a','b','c', 'd', 'e', 'f', 'd', 'g' , 'd']
print(basket_one.count('d')) #! 3
print(len(basket_one)) #! 9