#! LIST SLICING
#! If you remember with string slicing, we have things like helllooo and we were able to assign it to a string
string = 'helllooo'
print(string[0:2:1])

#! Same thing we can apply in list slicing let make our cart big
amazon_cart = ['notebooks', 
               'sunglasses',
               'pens',
               'fruits'] 

#! now you need to get all the iteams in card then we can do this
print(amazon_cart)
#! So lets use some list-silcing
print(amazon_cart[0:2])
print(amazon_cart[0::2]) #! leave 2 one

#! Here we will get intresting remember we discussed string are immutable? that means we can't change it
#! Using list we can able to change the content.

amazon_cart[0] = 'laptop'
print(amazon_cart)  #!check the outputs notebooks are replaced by laptop

#!* Which means strings are immutable & lists are mutable

print(amazon_cart[0:3])  #!outpu is ['laptop', 'sunglasses', 'pens']
print(amazon_cart)  #! output is ['laptop', 'sunglasses', 'pens', 'fruits']

#!* Here the important is we have chaged to laptop and we did slicing and the we printed amazon card here in last output we can able to see all the iteam but not slicing iteam why?
#!* List_slicing make a copy of the list so when weare running line 26 the outpu is a copy and while running 27 it is a actually list.

new_cart = amazon_cart
new_cart[0] = 'gum'
print (new_cart) #! ['laptop', 'sunglasses', 'pens']
print(amazon_cart) #! ['gum', 'sunglasses', 'pens', 'fruits']

#! from above we have taken new cart and changed the new cart entry but both are changed 
#! so to copy a cart use [:]
amazon_cart_one = ['notebooks', 
               'sunglasses',
               'pens',
               'fruits'] 

new_cart_one = amazon_cart_one[:]
new_cart_one[0] = 'gum'
print(new_cart_one)  #! ['gum', 'sunglasses', 'pens', 'fruits']
print(amazon_cart_one) #! ['notebooks', 'sunglasses', 'pens', 'fruits']

#! so see from above output our actual cart remain same only new cart has been changed.
