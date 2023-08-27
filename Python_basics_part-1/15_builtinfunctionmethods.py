#! numbers had some functions that we can use some built in functions.
#! well, string also has a very useful one called Len, which stands for lenght
len('helllo')  #! calculating lenght of string 
#! Link: https://www.w3schools.com/python/python_ref_functions.asp
#! NOTE: LEN WILL NOT START FROM 0 

greet = 'hellloooo'
print(greet[0:3])
print(greet[0:len(greet)])

quote = 'to be or not to be'
print(quote.upper())
print(quote.lower())
print(quote.capitalize())
print(quote.find('be'))
print(quote.replace('be', 'me'))
#! we have done many changes but atlast if we are using quote we are getting same output from
#! variable quote remember string are immutable
print(quote) 