
def str_reverse(s):
    return s[::-1]

def check_palindrome(s):
    return s == s[::-1]

#pig_it('Pig latin is cool') # igPay atinlay siay oolcay
#pig_it('Hello world !')     # elloHay orldway !

def pig_it(text):
    return (" ").join(map(lambda x: x[1:]+x[0]+'ay' if x.isalpha() else x, text.split(" ")))
