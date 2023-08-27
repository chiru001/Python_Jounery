#! Till now we know that string is an ordered sequence of characters, right?
#! String underneath the hood are stored in memory, as we discussed befor as an ordered sequence of characters.
#! lets take an example me me me here m will store in memory and e is storaged in memory and so on.

a = 'me me me'

print(a[0])  #! output is m=0
print(a[2])  #! output is "just space"because m=0 e=1 2= white space
#! [start:stop:stepover]

numbers = '01234567890'
print(numbers[0:15])
print(numbers[6:15])
print(numbers[0:15:2]) #! this will step over
print(numbers[1:]) #! what will happen??
print(numbers[:5])
print(numbers[::1])
print(numbers[-1]) #! in python -1 means start from last 
print(numbers[::-1])