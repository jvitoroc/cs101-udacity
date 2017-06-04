# A list is symmetric if the first row is the same as the first column,
# the second row is the same as the second column and so on. Write a
# procedure, symmetric, which takes a list as input, and returns the
# boolean True if the list is symmetric and False if it is not.

def transpose_matrix(l):
    transposed = []
    if(l == []):
        return transposed
    count = 0
    row_lenght = len(l[0])
    rowN = []
    while count < row_lenght: 
        for row in l:
            rowN.append(row[count])
        transposed.append(rowN)
        rowN = []
        count += 1
    return transposed

def check_square(l):
    rows = len(l)
    for row in l:
        if not(rows == len(row)):
            return False
    return True

def symmetric(l):
    if(check_square(l) == False):
        return False
    t = transpose_matrix(l)
    if t == l:
        return True
    return False
    
    
#print symmetric([["cat", "dog", "fish"],
#                ["dog", "dog", "dog"],
#                ["fish","fish","cat"]])
#>>> False

#print symmetric([[1, 2],
#                [2, 1]])
#>>> True

#print symmetric([[1, 2, 3, 4],
#                [2, 3, 4, 5],
#                [3, 4, 5, 6]])
#>>> False

#print symmetric([[1,2,3],
#                 [2,3,1]])
#>>> False
