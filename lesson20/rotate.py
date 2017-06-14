# Write a procedure, rotate which takes as its input a string of lower case
# letters, a-z, and spaces, and an integer n, and returns the string constructed
# by shifting each of the letters n steps, and leaving the spaces unchanged.
# Note that 'a' follows 'z'. You can use an additional procedure if you
# choose to as long as rotate returns the correct string.
# Note that n can be positive, negative or zero.
cache = {}
# {}
def cached_shift(cache,func,input1,input2):
    inpt = input1+'%'+str(input2)
    if inpt in cache:
        return cache[inpt]
    res = func(input1,input2)
    cache[inpt] = res
    return res

def shift_n_letters(letter, n):
    z = ord('z')
    a = ord('a')
    let = ord(letter)+n
    if(let > z):
        return chr((let)-26)
    elif(let < a):
        return chr((let)+26)
    return chr(let)
    
def rotate(string, n):
    output = ''
    for c in string:
        if(c == " "):
            output += " "
            continue
        output += cached_shift(cache,shift_n_letters,c,n)
    return output


print rotate ('sarah', 13)
#>>> 'fnenu'
print rotate('fnenu',13)
#>>> 'sarah'
print rotate('dave',5)
#>>>'ifaj'
print rotate('ifaj',-5)
#>>>'dave'
print rotate(("zw pfli tfuv nfibj tfiivtkcp pfl jyflcu "
                "sv rscv kf ivru kyzj"),-17)
#>>> ???
