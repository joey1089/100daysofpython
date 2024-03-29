#Password Generator Project
import random
import string
import os

os.system('clear')

TOTAL_CHARS = 17 # Constant

print("Create Strong Password using PyPassword Generator!")
print(f"Create a strong password that has more than {TOTAL_CHARS} characters!!!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
letters = string.ascii_letters
# numbers = string.digits
symbols = string.punctuation

total_char = nr_letters + nr_numbers + nr_symbols

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

while total_char > TOTAL_CHARS:
    print("Generating Password! ...")
    # Generate random letters
    pass_list = []
    for letter in range(0,nr_letters):
        pass_list = random.sample(letters, k=nr_letters) # using random class method sample to get unique values instead of choice
       
    # Generate random numbers
    pass_num = random.sample(range(0,10),k= nr_numbers) # using sample method with range to get unique numbers
    for no in pass_num:
        pass_list.append(str(no)) # resolved conflicts of int on the list, by converting int into str right here than to deal later on
        # leave this code alone, its working and appends into the list as a string.

    # Generate random symbols
    for sym in range(0, nr_symbols):
        pass_list += random.choice(symbols)
        

    # check if total characters 
    # if total_char == len(pass_list): # used while making changes from random. choice to sample and range
    #     print("\nTotal no of characters are the same!")
    # else:
    #     print("Password generated has extra values")

    # Generate password
    print("\n Before Random shuffle : ", pass_list, len(pass_list)) #len() added to check if values, as expected!
    pass_rand = random.shuffle(pass_list)
    print("\n After Random : ", pass_list)

    # print("Length of the password : ", len(passwords))
    new_password = "".join(pass_list)
    print("\n Your randomly generated password : ",new_password)

    break

else:
    print(f"Choose more than {TOTAL_CHARS} characters to create password")

    