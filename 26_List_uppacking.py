# there is one last thing when it comes o list and it's called LIST_UNPACKING, it's a nice feature.

#! here i have created a list and assign a variable to it 
basket = [1,2,3]
#! but what if i need to assign a variable to all the item in the list? 
a,b,c = [1,2,3]
print(a)
print(b)
print(c)
#! example what if i have list and i need to unpack he list ?
a,b,c, *other = [1,2,3,4,5,6,7,8,9,0]
#! here from the above list i need to unpack the 123 from list 
print(other) #! [4, 5, 6, 7, 8, 9, 0]

#! we will learn more about unpacking later.



