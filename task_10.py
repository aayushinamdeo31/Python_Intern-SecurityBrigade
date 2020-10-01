# Task 10


# Assuming that we have some email addresses in the "username@companyname.com" format,
# please write program to print the company name of a given email address. Both user names and company names are composed of letters only.

# Example:
# If the following email address is given as input to the program:

# akita@securitybrigade.com

# Then, the output of the program should be:

# securitybrigade

# In case of input data being supplied to the question, it should be assumed to be a console input.



def companyName(email):

    # Using slicing and indexing
    try:
        ans = email[email.index('@')+1:email.index('.com')]
    except:
        ans = 'Company Name not found'
    return(ans)


def main():
    email = input('Enter email address from the user - ')
    answer = companyName(email)
    print(answer)


if __name__ == '__main__':
    print("---"*20)
    main()
