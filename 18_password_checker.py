#! Password lenght finder

#!here our goal is py wil ask username & password so as a result output should come as 
#! your password is ********* and lenght is 9 
#! it will printout the password but it is protected



Name = input('Enter you username: ')
Password = input('Enter you password: ')
size = len(Password)
Protected = '*' * size
print(f"your password is {Protected} and length is {size}")