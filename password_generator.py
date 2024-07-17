# Importiing random module
import random

# Some alphanumeric characters and symbols for the requirement of password
letters = ['a', 'b', 'c', 'd','e', 'f', 'g', 'h', 'i', 'j', 'k', 'l,' 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
          'A', 'B', 'C', 'D','E', 'F', 'G', 'H', 'I', 'J', 'K', 'L,' 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '(', ')', '*', '/']

print('Welcome to Password Generator!!!')

# Taking input from user 
n_letters = int(input('How many letters you want in your password?\n'))
n_symbols = int(input('How many symbols you want in your password?\n'))
n_numbers = int(input('How many numbers you want in your passowrd?\n'))

password_1 = []       # An empty list

# Logic 
for i in range(1, n_letters + 1):
    char = random.choice(letters)
    password_1 += char

for i in range(1, n_symbols + 1):
    char = random.choice(symbols)
    password_1 += char

for i in range(1, n_numbers + 1):
    char = random.choice(numbers)
    password_1 += char 

random.shuffle(password_1)
password = ""

for char in password_1:
    password += char
print('🔐',password)