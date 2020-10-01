# Task 2

# Write a program (using functions!) that asks the user for a long string containing multiple words.
# Print back to the user the same string, except with the words in backwards order. For example, say I type the string:

# My name is Michele

# Then I would see the string:

#  Michele is name My

# shown back to me.

# Function to reverse the order of the string array
def reverseString(string):
  string.reverse()  # Reversing the string list
  return string

  
# Driver Program
string = list(input().split())  # Take input of string with multiple words
answer = reverseString(string)  
print(' '.join(answer))
