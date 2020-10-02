# Task 1

# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25])
# and makes a new list of only the first and last elements of the given list.
# For practice, write this code inside a function.

class ReturnNew:
    def __init__(self, arr):  # Constructor that takes an array as an argument
        self.arr = arr

    def first_last(self):  # Method that returns the first and last element of the original array
        b_arr = [self.arr[0], self.arr[-1]]
        return b_arr


# Driver Program
arr = list(map(int, input("Enter an array - ").split()))  # arr = [5, 10, 15, 20, 25] dummy list
obj1 = ReturnNew(arr)  # Creating an object of ReturnNew class
answer = obj1.first_last()  # Storing the returned array in a variable
print(answer)
