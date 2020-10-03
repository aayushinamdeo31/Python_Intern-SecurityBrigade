# Task 1

# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25])
# and makes a new list of only the first and last elements of the given list.
# For practice, write this code inside a function.

class ReturnNew:
    def __init__(self, user_input):  # Constructor that takes an array as an argument
        self.user_input1 = user_input

    def first_last(self):  # Method that returns the first and last element of the original array
        b_input = [self.user_input1[0], self.user_input1[-1]]
        return b_input


# Driver Program
user_input1 = list(map(int, input("Enter an array - ").split()))  # arr = [5, 10, 15, 20, 25] dummy list
return_new = ReturnNew(user_input1)  # Creating an object of ReturnNew class
answer = return_new.first_last()  # Storing the returned array in a variable
print(answer)
