#Password Generator Project
import random
import string
import os

letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Letters : ",letters)
print("Numbers : ",numbers)
print("Symbols : ",symbols)
all_combine = letters+numbers+symbols
# print("All combined together values : ",all_combine)


print("Welcome to the PyPassword Generator!")
print("Create a strong password that has more than 15 characters!!!")
# nr_letters= int(input("How many letters would you like in your password?\n")) 
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))

#test values
nr_letters = 8
nr_numbers = 4 
nr_symbols = 4
total_char = nr_letters + nr_numbers + nr_symbols

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

while total_char > 15:
    print("\n Generating Password! ...")
    # Generate random letters
    pass_list = []
    for letter in range(0,nr_letters):
        pass_list = random.sample(letters, k=8)       
    print("Random letters selected : ", pass_list, len(pass_list))
    # Generate random numbers
 
    for number in range(0,nr_numbers):
        pass_list += random.sample(numbers, k= 4)
    print("Random selected numbers : ", pass_list, len(pass_list))
    # Generate random symbols
    rand_symbols = []
    for sym in range(0, nr_symbols):
        pass_list += random.sample(symbols,k=4)
    print("Random Selected symbols : ", pass_list, len(pass_list))

    # Generate password
    print("\n Before Random shuffle : ", pass_list)
    pass_rand = random.shuffle(pass_list)
    print("\n After Random : ", pass_list)

    passwords = ""
    for char in pass_list:
        passwords += char
    
    print("final Generated password : ", passwords)



  
    

    break

else:
    print("Choose more than 15 characters to create password")

    