#! Data Types
#! we have below data types
#! int= numbers, float= 1.5, bool=True or False, str=abcde.., list=  , tuple=, set= , dict
#! Above datatypes are called a fundamental data types
#! Beyond that we can also create a "classes" and define our own data types. these will be custom types.
#! We also have Specialized Data Types, These are not build into python, but they are special packages and modules that we can use from libraries.
#! Finally we have also have another datatype called "None" name only says nothing it's kind of like the idea of zero in math.
#! Lets talk about our first 2 Datatypes "int & float"

#! int stands for integer and float stands for a floating point number.

#! here if i just add 2 + 4 and run this well nothing gets printed because again, we have to perform some action on these data.
#! One action what we learnt so far is print, so lets do this 
#! Below adding action (print) for 2 + 4
print (2 + 4)  #! Output is 6 
print (2 - 4)  #! Output is -2
print (2 * 4)  #! Output is 8
print (2 / 4)  #! Output is 0.5

#! So above we just added number but here we can give type 
print (type(2 + 4))  #! class int
print (type(2 - 4))  #! class int
print (type(2 * 4))  #! class int
print (type(2 / 4))  #! class float

#! Type is like hey what datatype is this
print (type( 3 + 3))
#! Just like maths it will go as print (type(6)) and then 6 is what? int so class is int &
#! ok i have print action so print it ou class int, Note: 6 will not printout only type will.
#! IF there are any decimal points then they are called as float.

#! Why do we need to make this distinction in programming and specifically in python?
#! Well, it's because a float takes up actually a lot more space in memory than an integer.
#! example: 6 (line 22) as we know machine i will store data in 0's &1's we have 6 so 6 will change to binary.
#! same for float as float we have 10.6777 its so hard to store in binary so it consumes more memory.

