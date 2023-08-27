#! We have already learn about buildin function like len

basket = [1,2,3,4,5]
print(len(basket)) #! Note len() will check from 1 like humans not count from 0

#! Lets add item in basket
#! adding basket

add_item = basket.append(100)
print(add_item)  #! None why? lets print basket
print(basket) #! [1, 2, 3, 4, 5, 100]
#! here we can see basket output we can see 100 is added to basket but add_item we are seeing none?

#! That is because append changes the list in place. what is list in place 
#!* It means that it doesn't produce a value all it does is syaing, hey i am just going to append 100 to this basket that you gave me, but i don't care or not producing the result.
  
  
#! What we have , so we have insert, Insert is like we can add anyiteam anwhere using insert

basket_one = [1,2,3,4,5]
basket_one.insert(4, 100)
basket_one.extend([200, 300]) #! extend is something that you can loop over which is a list
print(basket_one) #! [1, 2, 3, 4, 100, 5, 200, 300]

#! removing
basket_one.pop()
print(basket_one) #![1, 2, 3, 4, 100, 5, 200] 

#! it has removed the last iteam from basked  which is 300
#! if we do one more time it will remove 200, lets do it
basket_one.pop()
print(basket_one) #! [1, 2, 3, 4, 100, 5]

#! We can also use like below
basket_one.pop(0)
print(basket_one) #! [2, 3, 4, 100, 5] it removed 1 

#! Now we need to remove a number we can user remove, here i want to remove 4
basket_one.remove(4)
print(basket_one) #! [2, 3, 100, 5]

#! To empyt the basket we can use clear
basket_one.clear()
print(basket_one) #! []

#!* NOTE: POP USING INDEX VALUE , WHERE AS REMOVE USING ACTUAL NUMBERs




