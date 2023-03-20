import random
import os
from time import sleep

# Encryption Working>>>>>>>>>>>>>>>>>>>

enc_word = input("Please enter your message to encrypt :")
list = ['adb', 'dsf', 'sdf', 'sdf', 'htr', 'rht', 'rth',
        'try', 'bdr', 'sdf', 'dsf', 'fgh', 'vbn', 'yui']
for i in range(0, len(enc_word)):
    for word in enc_word.split(" "):
        # using for checking for length of word
        if len(word) >= 3:
            # coding
            edit_str = word[1::]+word[0]
            final_str = random.choice(list)+edit_str+random.choice(list)
            with open("Encryption.txt", "a+") as file:
                file.write(final_str+" ")

        else:
            rev_word = word[::-1]
            with open("Encryption.txt", "a+") as file:
                file.write(rev_word+" ")
    with open("Encryption.txt", "a+") as file:
        file.write("\n")
    break  # Main loop ended




# Decryption Working >>>>>>>>>
with open("Encryption.txt") as file:
     ap = file.readline()
for i in range(0, len(ap)):
    for word in ap.split(" "):
        # using for checking for length of word
        if len(word) >= 3:
            # Decoding
            edit_str = word[3:-3:]
            final_str = edit_str[-1]+edit_str[0:-1:]
            with open("Decryption.txt", "a+") as file:
                file.write(final_str+" ")

        else:
            rev_word = word[::-1]
            with open("Decryption.txt", "a+") as file:
                file.write(rev_word+" ")
    break  # Main loop ended


# Waiting for 4 seconds to clear the screen
sleep(0.1)

# Clearing the Screen
os.system('cls')
