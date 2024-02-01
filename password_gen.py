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
    print("Generating Password! ...")
    # Generate random letters

    pass_list = []
    for letter in range(0,nr_letters):
        pass_list = random.sample(letters, k=nr_letters)       
    # print("Random letters selected : ", pass_list, len(pass_list))
    # Generate random numbers
    
    pass_num = random.sample(range(0,10),k= nr_numbers)
    # print("Random selected numbers : ", pass_num)
    # print(pass_num)
    for no in pass_num:
        pass_list.append(str(no))
    # print("\n New List :- ",pass_list)

    # Generate random symbols

    for sym in range(0, nr_symbols):
        pass_list += random.choice(symbols)
        # pass_list += random.sample(symbols,k=1)
    # print("Random Selected symbols : ", pass_list, len(pass_list))

    # check if total characters 
    if total_char == len(pass_list):
        print("\nTotal no of characters are the same!")
    else:
        print("Password generated has extra values")

    # Generate password
    print("\n Before Random shuffle : ", pass_list, len(pass_list))
    pass_rand = random.shuffle(pass_list)
    print("\n After Random : ", pass_list)

    # print("Length of the password : ", len(passwords))
    new_password = "".join(pass_list)
    print("\n Your randomly generated password : ",new_password)

    break

else:
    print("Choose more than 16 characters to create password")

    