from random import Random, random


palindrome = lambda string: string == string [::-1]

print(palindrome(input("Escribe una palabra:")))
