import random
import string
from password_gen import nr_letters,nr_numbers,nr_symbols,letters,numbers,symbols,total_char

#Generating Non Randomized Password.
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
def password_not_random():
    '''Generating Non Randomized Password.'''
    print("\n Generating Non Randomized Password.")


#Generating Randomized Password.
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
def password_randomized():
    '''Generating Randomized Password.'''
    print("\n Generating Randomized Password.")
    # Generate random letters
    pass_list = []
    for letter in range(0,nr_letters+1):
        pass_list = random.sample(letters, k=8)       
    # print("Random letters selected : ", pass_list, len(pass_list))
    # Generate random numbers
    
    pass_num = random.sample(range(0,10),k= nr_numbers)
    print("Random selected numbers : ", pass_num)
    print(str(pass_num))
    pass_list += str(pass_num)

    # Generate random symbols
    rand_symbols = []
    for sym in range(0, nr_symbols+1):
        rand_symbols += random.choice(symbols)
        # pass_list += random.sample(symbols,k=1)
    print(rand_symbols)
    pass_list += rand_symbols
    print("Random Selected symbols : ", pass_list, len(pass_list))
    if total_char != len(pass_list):
        print("Password generated has extra values")

    # Generate password
    print("\n Before Random shuffle : ", pass_list, len(pass_list))
    pass_rand = random.shuffle(pass_list)
    print("\n After Random : ", pass_list)

    passwords = ""
    for char in pass_list:
        passwords += char
    
    print("final Generated password : ", passwords)
    # print("Length of the password : ", len(passwords))