#! /usr/bin/env python

from alien_crypt import CaesarCipher

if __name__ == "main":
    c = CaesarCipher(5)
    c.encode('Codewars')
    c.decode('BFKKQJX')
