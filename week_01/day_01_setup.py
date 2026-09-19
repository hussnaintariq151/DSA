# O(1) - Constant Time Example 

def get_first_element(arr):
    """
    Returns the first element of Array
    """
    if len(arr) == 0:
        return None
    return arr[0]

big_list = list(range(1000000))
small_list = [10, 20, 30] 

print("Small list pehla element:", get_first_element(small_list))
print("Big list pehla element:", get_first_element(big_list)) 


# O(n) - Linear Time Example
def find_number(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

numbers = [4, 2, 7, 1, 9, 3, 8, 5, 6] 
  
print("7 ka index:", find_number(numbers, 7)) 
print("100 ka index:", find_number(numbers, 100))

# O(n^2) - Quadratic Time Example 
def has_duplicate(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                return True
    return False


            
