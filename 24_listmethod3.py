basket = ['a','b','c', 'd', 'e', 'f', 'd', 'g' , 'd']

#! The next metho is called sort
print(basket.sort()) #! we are getting NONE it will jsut do its duty but not display so

basket.sort()
print(basket) #! ['a', 'b', 'c', 'd', 'd', 'd', 'e', 'f', 'g']

#! As seeing the output it will arragne in order.

#!** unlike sort we can also use sorted. sort will not display but sorted will
basket_one = ['a','b','c', 'd', 'e', 'f', 'd', 'g' , 'd']
print(sorted(basket)) #! ['a', 'b', 'c', 'd', 'd', 'd', 'e', 'f', 'g']

#! now lets print basket 

print(basket_one) #!['a', 'b', 'c', 'd', 'e', 'f', 'd', 'g', 'd']

#! Basket has not modified? because sorted will take copy of the basket so there will no
#! changes in actual basket.

#! We have another method which is called reverse
basket_two = ['a','b','c', 'd', 'e', 'f', 'd', 'g' , 'd']
print(basket_one.reverse()) #! NONE
basket_two.reverse()
print(basket_two) #! ['d', 'g', 'd', 'f', 'e', 'd', 'c', 'b', 'a']