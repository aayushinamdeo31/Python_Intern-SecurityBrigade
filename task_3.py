# Task 3

# Take two lists, say for example these two:
#
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#
# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates).
# Make sure your program works on two lists of different sizes.
#
# Extras:
#   1. Randomly generate two lists to test this
#   2. Write this in one line of Python


# Function to return the common elements between 2 lists

def intersectionList(arr1, arr2):
    return(arr1 & arr2)  # Using intersention(&) set operator


# Driver Program
'''
Sample Lists
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
'''
array1 = set(list(map(int, input().split(','))))  # Take input of interger list 1
array2 = set(list(map(int, input().split(','))))  # Take input of interger list 2
answer = intersectionList(array1, array2)
print(answer)   
