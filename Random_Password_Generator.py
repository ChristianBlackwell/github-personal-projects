import random

#function to shuffle characters in string
def shuffle(string):
    temp_list = list(string)
    random.shuffle(temp_list)
    return ''.join(temp_list)

#main program starts here

uppercase_letter_1=chr(random.randint(65,90)) #generates random uppercase letter (based on ASCII code)
uppercase_letter_2=chr(random.randint(65,90))
uppercase_letter_3=chr(random.randint(65,90))
uppercase_letter_4=chr(random.randint(65,90))

lowercase_letter_1=chr(random.randint(97,122)) #generates random lowercase letter (based on ASCII code)
lowercase_letter_2=chr(random.randint(97,122))
lowercase_letter_3=chr(random.randint(97,122))
lowercase_letter_4=chr(random.randint(97,122))

symbol_char_1=chr(random.randint(32,64)) #generates random symbol/digit character (based on ASCII code)
symbol_char_2=chr(random.randint(32,64))
symbol_char_3=chr(random.randint(32,64))
symbol_char_4=chr(random.randint(32,64))

#generate password using all the characters, in random order
#password = uppercase_letter_1 + uppercase_letter_2 + uppercase_letter_3 + uppercase_letter_4 + lowercase_letter_1 + lowercase_letter_2 + lowercase_letter_3 + lowercase_letter_4 + symbol_char_1 + symbol_char_2 + symbol_char_3 + symbol_char_4

password = uppercase_letter_1 + uppercase_letter_2 + uppercase_letter_3 + uppercase_letter_4
password = password + lowercase_letter_1 + lowercase_letter_2 + lowercase_letter_3 + lowercase_letter_4
password = password + symbol_char_1 + symbol_char_2 + symbol_char_3 + symbol_char_4

password = shuffle(password)

#output
print("Your new password is:", password)