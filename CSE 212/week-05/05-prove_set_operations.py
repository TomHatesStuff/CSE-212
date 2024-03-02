"""
CSE212 
(c) BYU-Idaho
05-Prove - Problem 1

It is a violation of BYU-Idaho Honor Code to post or share this code with others or 
to post it online.  Storage into a personal and private repository (e.g. private
GitHub repository, unshared Google Drive folder) is acceptable.
"""

def intersection(set1, set2):
    """
    Perform an intersection between 2 sets.  An intersection will contain
    the items in common between both sets.  Do not use the set 
    operators (+, -, *, &, |) and functions (intersection, union) 
    that are built-in to Python.
    """
        # Create an empty set to store the common items
    intersect_set = set()
    
    # Go through each item in set1
    for item in set1:
        # Check if the item is also in set2
        if item in set2:
            # If it is, add it to the intersection set
            intersect_set.add(item)
    
    # Return the set containing common items
    return intersect_set
    pass

def union(set1, set2):
    """
    Perform a union between 2 sets.  A union will contain all the items
    from both sets.   Do not use the set operators (+, -, *, &, |)
    and functions (intersection, union) that are built-in to Python.
    """
        # Create an empty set to store all items without duplicates
    union_set = set()
    
    # Go through each item in set1
    for item in set1:
        # Add the item to the union set
        union_set.add(item)
    
    # Go through each item in set2
    for item in set2:
        # Check if the item is not already in the union set
        if item not in union_set:
            # If it's not, add it to the union set
            union_set.add(item)
    
    # Return the set containing all unique items
    return union_set
    pass

s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
print(intersection(s1,s2))  # Should show {4, 5}
print(union(s1,s2)) # Should show {1, 2, 3, 4, 5, 6, 7, 8}

s1 = {1,2,3,4,5}
s2 = {6,7,8,9,10}
print(intersection(s1,s2))  # Should show an empty set
print(union(s1,s2)) # Should show {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

