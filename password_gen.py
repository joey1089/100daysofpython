#Password Generator Project
import random
import string
import os

letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

# print("Letters : ",letters)
# print("Numbers : ",numbers)
# print("Symbols : ",symbols)
# all_combine = letters+numbers+symbols
# print("All combined together values : ",all_combine)


# print("Create Strong Password using PyPassword Generator!")
# print("Create a strong password that has more than 15 characters!!!")
# nr_letters= int(input("How many letters would you like in your password?\n")) 
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))

#test values
nr_letters = 10
nr_numbers = 4
nr_symbols = 3
total_char = nr_letters + nr_numbers + nr_symbols

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

while total_char > 16:
    print("\n Generating Password! ...")
    # Generate random letters
       

    break

else:
    print("Choose more than 16 characters to create password")

    