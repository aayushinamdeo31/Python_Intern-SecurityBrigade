# Task 9

# Please write a binary search function which searches an item in a sorted list.
# The function should return the index of element to be searched in the list.


# Returns index of x in a sorted array if present, else -1 
def binary_search(input1, left, right, element):

    if right >= left:
        mid = left + (right - left) // 2

        # If element is present at the middle 
        if input1[mid] == element:
            return mid

        # If element is smaller than mid then element can only be present in left subarray
        elif input1[mid] > element:
            return binary_search(input1, left, mid - 1, element)

        # Else the element can only be present in right subarray 
        else:
            return binary_search(input1, mid + 1, right, element)

    else:
        # Element is not present in the array 
        return -1


# Driver Code
user_input1 = list(map(int, input("Enter the elements of the array - ").split()))
element = int(input("Enter element to be searched - "))

result = binary_search(user_input1, 0, len(arr) - 1, element)

if result != -1:
    print("Element ", element, " is present at index - ", result)

else:
    print("Element ", element, " is not present in array !! ")
