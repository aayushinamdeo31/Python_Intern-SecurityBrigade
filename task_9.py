# Task 9

# Please write a binary search function which searches an item in a sorted list.
# The function should return the index of element to be searched in the list.


# Returns index of x in a sorted array if present, else -1 
def binarySearch (array, left, right, x): 

    if(right >= left): 
        mid = left + (right - left) // 2
  
        # If element is present at the middle 
        if(array[mid] == x): 
            return(mid) 
          
        # If element is smaller than mid then element can only be present in left subarray 
        elif(array[mid] > x): 
            return(binarySearch(array, left, mid-1, x))
  
        # Else the element can only be present in right subarray 
        else: 
            return(binarySearch(array, mid + 1, right, x))
  
    else: 
        # Element is not present in the array 
        return(-1)
  
# Driver Code

array = list(map(int, input("Enter the elements of the array - ").split()))
x = int(input("Enter element to be searched - "))
                            
result = binarySearch(array, 0, len(array)-1, x) 
  
if(result != -1): 
    print("Element ",x," is present at index - ",result) 
else: 
    print("Element ",x," is not present in array !! ")
