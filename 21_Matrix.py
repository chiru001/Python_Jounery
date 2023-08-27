#! Matrix
#! it looks something like below its array inside array.

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]
#! Above is 2d-Array but we can have mutiple ones.example we can have another array inside an array
matrix_one = [
    [[1],2,3],
    [4,5,6],
    [7,8,9]
    ]
#! It is used in AI and image processing.
matrix_final = [
    [1,5,1],               #!see here 0 row first coloum is 5
    [0,2,0],
    [1,0,3]
    ]
print (matrix_final[0][1])
print (matrix_final[1][1])
print (matrix_final[2][2])