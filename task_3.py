# Task 3

# Take two lists, say for example these two:
#
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#
# write a program that returns a list that contains only the elements that are common between the lists
# Make sure your program works on two lists of different sizes.
#
# Extras:
#   1. Randomly generate two lists to test this
#   2. Write this in one line of Python

# Function to return the common elements between 2 lists

def intersection(arr1, arr2):
    return arr1 & arr2  # Using intersection(&) set operator


# Driver Program
'''
Sample Lists
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
'''
arr1 = set(list(map(int, input("Enter array 1 - ").split(','))))  # Take input of integer list 1
arr2 = set(list(map(int, input("Enter array 2 - ").split(','))))  # Take input of integer list 2
answer = intersection(arr1, arr2)
print(answer)
# To randomly generate a list : [random.randrange(1, 50, 1) for i in range(10)])
