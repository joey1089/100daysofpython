# Using Functions to make it more efficient to Generate password.
# Here trying to impliment another level of learning.
import os
import random
import string
# from password_gen import nr_letters,nr_numbers,nr_symbols, total_char
from wonderwords import RandomSentence


# Declare all Constants 
letters = string.ascii_letters
symbols = string.punctuation
no_letters = 12
no_numbers = 5
no_symbols = 3
TOTAL_CHARS = 20 # Constant are all caps
os.system('clear')


#Generating passphrase and randomize the caps on it

def passphrase():
    '''Generating a passphrase.'''      
    # refer:- https://wonderwords.readthedocs.io/en/latest/api_docs/random_sentence.html
    # Get a random sentence with a subject, predicate, direct object and adjective
    s = RandomSentence() 
    with_space_sentence = s.sentence()
    print(f"\n Remember this Passpharse:-  {with_space_sentence} \n")
    rm_space_sentence = with_space_sentence.replace(".","").replace(" ","")
    userchoice = input("Do you want just the Passphrase type '1' or Want to randomise with nos & symbols :- ")
    if userchoice == 1:
        print("\n You choose to go with the just the Passphrase! \n")
        print("Terminating...")
        exit()
    else:
        rm_space_sentence = with_space_sentence.replace(".","").replace(" ","") 
        # here join is used to convert to a lower and upper string at random.
        rm_space_sentence = ''.join(random.choice((str.upper, str.lower))(char) for char in rm_space_sentence)
        print("Removed Space and Randomized Caps on the passphrase :- ",rm_space_sentence)
        # add random numbers and sysmbols, next level 
        pass_list = []
        # Generate random numbers
        pass_num = random.sample(range(0,10),k= no_numbers) 
        for no in pass_num:
            pass_list.append(str(no)) #

        # Generate random symbols
        for sym in range(0, no_symbols):
            pass_list += random.choice(symbols)
        # Adding the random numbers and symbols to the passphrase
        print("Random Generate numbers and symbols :- ", pass_list)
        convert2list = str(rm_space_sentence.split())
        print(convert2list)
        pass_list.append(convert2list)
        print("After appending to the random list : ",pass_list)
    
        random.shuffle(pass_list)
        add2passphrase = ""
        add2passphrase = "".join(pass_list)
        final_passphrase = add2passphrase.replace("[","").replace("]","").replace("'","")
        print(f"\n Your randomized Passphrase:-  {final_passphrase} \n")
        




#Generating Randomized Password.
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
def password_randomized():
    '''Generating Randomized Password.'''
    print("\n Generating Randomized Password.")
    # Generate random letters
    pass_list = []
    for letter in range(0,no_letters):
        pass_list = random.sample(letters, k=no_letters) 
       
    # Generate random numbers
    pass_num = random.sample(range(0,100),k= no_numbers) 
    for no in pass_num:
        pass_list.append(str(no)) #

    # Generate random symbols
    for sym in range(0, no_symbols):
        pass_list += random.choice(symbols)
        
    # Generate password
    print(f"\n Before Random shuffle is {pass_list} and total characters is {len(pass_list)}") 
    random.shuffle(pass_list)
    print("\n After Random : ", pass_list)

    new_password = "".join(pass_list)
    print("\n Your randomly generated password : ",new_password)


print("Generate Strong Password or Passphrases!!!")
userchoice = int(input(f"\n Want Strong Random password type '1' or want passphrases type '2' :- " ))
if userchoice == 1:
    print("Proceeding to create strong randomized password")
    password_randomized()
else:
    print("Proceeding to create a passphrase")
    passphrase()