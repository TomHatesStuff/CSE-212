import json

def read_file(filename):
    try:
        with open(filename, 'r') as file:  # Open the file in read mode
            try:
                data = json.load(file)  # Load the JSON data from the file
                assert 'array' in data, f"Key 'array' not found in JSON data in file '{filename}'"
                assert isinstance(data['array'], list), f"Value for key 'array' is not a list in JSON data in file '{filename}'"
                return data['array']  # Return the 'array' key from the JSON data
            except json.JSONDecodeError:  # Handle the case of an empty JSON file
                print(f"File '{filename}' is empty or contains invalid JSON data.")
                return []
    except FileNotFoundError:  # Handle the case when the file is not found
        print(f"File '{filename}' not found.")
        return []

# Ask the user for the name of the JSON file
filename = input("What is the name of the file? ")

# Read the file and get the list of names
names = read_file(filename)

# Check if the array is empty
if not names:
    print("The array is empty or the file was not found.")
else:
    # Sort the list of names using the bubble sort algorithm
    def bubble_sort(arr):
        """Sorts a list using the bubble sort algorithm."""
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr

    sorted_names = bubble_sort(names)

    # Display the sorted list with formatting
    print("The values in {} are:".format(filename))
    for name in sorted_names:
        print("\t{}".format(name))


# 1. Name:
#      Luke Marshall
# 2. Assignment Name:
#      Lab 08: Sort
# 3. Assignment Description:
#      Using the bubble_sort alogorithm the program runs through the json array and sorts it in alphabetical order.
# 4. What was the hardest part? Be as specific as possible.
#      I think that the hardest part of this assignments was researching how the bubble array works. Honestly the hardest part in most of these is the studying. I did not have any bugs so i was pretty Lucky. The coolest part is that i could just incorporate the empty file and no file found from our previous assignment.
# 5. How long did it take for you to complete the assignment?
#      4 hours.