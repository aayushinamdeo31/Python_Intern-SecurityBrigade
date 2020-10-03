# Task 2

# Write a program (using functions!) that asks the user for a long string containing multiple words.
# Print back to the user the same string, except with the words in backwards order. For example, say I type the string:

# My name is Michele

# Then I would see the string:

#  Michele is name My

# shown back to me.

# Function to reverse the order of the string array
def reverse_sentence(word):
    word.reverse()  # Reversing the sentence list
    return word


# Driver Program
sentence = list(input("Enter a sentence - ").split())  # Take input of string with multiple words
answer = reverse_sentence(sentence)
print(' '.join(answer))