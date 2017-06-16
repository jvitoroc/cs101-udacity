# Double Gold Star

# Khayyam Triangle

# The French mathematician, Blaise Pascal, who built a mechanical computer in
# the 17th century, studied a pattern of numbers now commonly known in parts of
# the world as Pascal's Triangle (it was also previously studied by many Indian,
# Chinese, and Persian mathematicians, and is known by different names in other
# parts of the world).

# The pattern is shown below:

#                    1
#                   1 1
#                  1 2 1
#                 1 3 3 1
#                1 4 6 4 1
#                   ...

# Each number is the sum of the number above it to the left and the number above
# it to the right (any missing numbers are counted as 0).

# Define a procedure, triangle(n), that takes a number n as its input, and
# returns a list of the first n rows in the triangle. Each element of the
# returned list should be a list of the numbers at the corresponding row in the
# triangle.

cache = {}
def cached_rows(cache,i,fore_row):
    if i in cache:
        return cache[i]
    row = [1]
    for j in range(0,i):
            fore_row_len = len(fore_row)
            if(j+1<fore_row_len):
                row.append(fore_row[j]+fore_row[j+1])
    row.append(1)
    cache[i] = row
    return row
    
def triangle(n):
    rows = [[1],[1,1]]
    for i in range(2,n):
        row = (cached_rows(cache,i,rows[i-1]))
        rows.append(row)      
    return rows[0:n]

#For example:

#print triangle(10)
#>>> []

#print triangle(1)
#>>> [[1]]

#print triangle(2)
#>> [[1], [1, 1]]

#print triangle(3)
#>>> [[1], [1, 1], [1, 2, 1]]

#print triangle(6)
#>>> [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]
