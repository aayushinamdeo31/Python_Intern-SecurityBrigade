# Task 1

# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25])
# and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function.

class ReturnList:
    
    def __init__(self, array):  # Constructor that takes an array as an argument
      self.array = array
    
    def first_last(self):  # Method that returns the first and last element of the original array
      b_array = [self.array[0], self.array[-1]]
      return(b_array)


#Driver Program
a = list(map(int, input().split()))  # a = [5, 10, 15, 20, 25] dummy list
r1 = ReturnList(a)  # Creating an object of ReturnList class
answer = r1.first_last()  # Storing the returned array in a variable
print(answer)   
