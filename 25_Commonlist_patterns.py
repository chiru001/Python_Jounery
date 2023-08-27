#! lets see some of the useful tricks using lists

basket = ['a','b','c', 'd', 'e', 'f', 'd', 'g' , 'd']

#! we already seen len function

print(len(basket))

#! another useful trick is to reverse a list
#basket.reverse()
#print (basket)
#! we can also rever it using list-slicing too
print(basket[::-1]) #!Note: it creates a new list means copy 
print (basket)

#! The another userful trick is using RANGE.
#! if i want generate a list from 1 to 100 range can help me to generate

print(range(1,100)) #! range(1, 100)

#! so now if we warp it with list then list is created

print(list(range(1,101)))
'''
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
'''
#! The last one is .join() which works on string

sentence = '!'
join_sentense = sentence.join(['hi', 'my', 'name', 'is', 'chiru'])
print(join_sentense)  #! hi!my!name!is!chiru

#! or for a easy way 
new_sentence = ' '.join(['hi', 'my', 'name', 'is', 'chiru'])
print(new_sentence)  #! hi my name is chiru
