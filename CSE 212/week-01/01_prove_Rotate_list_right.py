def rotate_list_right(data, amount):
    """
    Rotate the 'data' to the right by the 
    'amount'.   For example, if the data is 
    [1, 2, 3, 4, 5, 6, 7, 8, 9] and an amount
    is 5 then the list returned should be 
    [5, 6, 7, 8, 9, 1, 2, 3, 4].  The value 
    of amount will be in the range of 1 and 
    len(data).
    """
    # Check if the amount is within the valid range
    if 1 <= amount <= len(data):
        # Rotate the list using slicing
        result = data[-amount:] + data[:-amount]
        return result
    else:
        # Handle invalid amount (you can choose to raise an exception or handle it differently)
        print("Invalid amount. Please provide a value between 1 and len(data).")
        return None

# Test cases
print(rotate_list_right([1,2,3,4,5,6,7,8,9], 1))  # [9, 1, 2, 3, 4, 5, 6, 7, 8]
print(rotate_list_right([1,2,3,4,5,6,7,8,9], 5))  # [5, 6, 7, 8, 9, 1, 2, 3, 4]
print(rotate_list_right([1,2,3,4,5,6,7,8,9], 9))  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
