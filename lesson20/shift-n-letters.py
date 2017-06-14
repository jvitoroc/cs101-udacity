# Write a procedure, shift_n_letters which takes as its input a lowercase
# letter, a-z, and an integer n, and returns the letter n steps in the
# alphabet after it. Note that 'a' follows 'z', and that n can be positive,
#negative or zero.

def shift_n_letters(letter, n):
    z = ord('z')
    a = ord('a')
    let = ord(letter)
    if(let+n > z):
        return chr(a+((let+n)-z-1))
    elif(let+n < a):
        return chr(z-(a-(let+n))+1)
    return chr(let+n)
        

print shift_n_letters('a', -1)
#>>> t
print shift_n_letters('s', 2)
#>>> u
print shift_n_letters('s', 10)
#>>> c
print shift_n_letters('s', -10)
#>>> i
