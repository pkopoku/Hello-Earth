"""Earth has been exciting so far, now we want to send messages back to our homeland to 
tell them about our exploits.
**This is an example from Codewars**
Write a class that, when given a string, 
will return an uppercase string with each letter shifted 
forward in the alphabet by however many spots the cipher was initialized to.

For example:

c = CaesarCipher(5); # creates a CipherHelper with a shift of five
c.encode('Codewars') # returns 'HTIJBFWX'
c.decode('BFKKQJX') # returns 'WAFFLES' """

import string

class CaesarCipher(object):
    def __init__(self, shift):
        self.shift = shift

    def encode(self, str):
        alpha = string.lowercase[:26]
        new_string = ""

        for i in str:
        	if i.isalpha():
            
	        	n = ord(i)%32
	        	sum = n + self.shift
	        	summ = sum%26
	        	new_string += alpha[summ-1]
	        else:
	        	new_string += i
        return new_string.upper()
        
    def decode(self, str):
    	alpha = string.lowercase[:26]
    	new_string2 = ""

    	for j in str.lower():
    		if j.isalpha():

	    		n = ord(j)%32
	        	sum = n - self.shift
	        	summ = sum%26
	        	new_string2 += alpha[summ-1]
	        else:
	        	new_string2 += j
        return new_string2.upper()
