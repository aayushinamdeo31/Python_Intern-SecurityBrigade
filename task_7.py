# Task 7

# Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols.
# The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.

# Extra:
# Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.

import random

def generatePassword(n, length):
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    
    l_alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',  
               'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 
               'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 
               'z'] 
      
    u_alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',  
               'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q', 
               'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 
               'Z'] 
      
    symbols = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',  
               '*', '(', ')', '!','^','+','='] 

    password = ''
    # Combines all the character arrays above to form one array 
    combined_list = digits + u_alpha + l_alpha + symbols
    
    if(n == 1):
        # Randomly select at least one character from each character set above 
        rand_digit = random.choice(digits) 
        rand_upper = random.choice(u_alpha) 
        rand_lower = random.choice(l_alpha) 
        rand_symbol = random.choice(symbols) 
          
        # Combine the character randomly selected above 
        password = rand_digit + rand_upper + rand_lower + rand_symbol 
          
          
        # Now that we are sure we have at least one character from each set
        for x in range(length - 4): 
            password += random.choice(combined_list)
            
        password = list(password)
        random.shuffle(password) 
  
    elif(n == 2):
        for p in range(length):
            password += random.choice(combined_list)
    elif(n == 3):
        for p in range(length):
            password += random.choice(l_alpha)

    print(''.join(password))
    print()
    askPassword()
    
    
def askPassword():
    answer = input('Do you want a new password ? (Y/N) ')

    print('-'*30)
    
    if(answer == 'Y'):
        print('1  -  Very Strong Password')
        print('2  -  Medium Password')
        print('3  -  Weak Password')
        print()
        n = int(input('Enter how strong password you want ? '))
        length = int(input('Enter the length of the password you want ? '))
        
        generatePassword(n, length)
        
    elif(answer == 'N'):
        print("Thank you for generating password !! ")
        
    else:
        print("Enter Valid Input !! ")
        askPassword()

        
# Driver Program

if __name__ == "__main__": 
    askPassword()
