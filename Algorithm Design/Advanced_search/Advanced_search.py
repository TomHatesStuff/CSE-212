import json  # Import the json module to work with JSON files
from json.decoder import JSONDecodeError  # Import JSONDecodeError for handling empty JSON files

def read_file(filename):
    try:
        with open(filename, 'r') as file:  # Open the file in read mode
            try:
                data = json.load(file)  # Load the JSON data from the file
                return data['array']  # Return the 'array' key from the JSON data
            except JSONDecodeError:  # Handle the case of an empty JSON file
                print(f"File '{filename}' is empty or contains invalid JSON data.")
                return []
    except FileNotFoundError:  # Handle the case when the file is not found
        print(f"File '{filename}' not found.")
        return []

def advanced_search(array, name):
    start, end = 0, len(array) - 1  # Initialize the start and end indices of the array
    while start <= end:  # Continue looping until the start index is less than or equal to the end index
        mid = start + (end - start) // 2  # Calculate the middle index of the array
        if array[mid] == name:  # Check if the middle element is equal to the name
            return True  # Return True if the name is found
        elif array[mid] < name:  # If the middle element is less than the name
            start = mid + 1  # Update the start index to search in the right half of the array
        else:  # If the middle element is greater than the name
            end = mid - 1  # Update the end index to search in the left half of the array
    return False  # Return False if the name is not found in the array

def main():
    filename = input("What is the name of the file? ")  # Get the filename from the user
    array = read_file(filename)  # Read the file and store the array of names
    if not array:  # Check if the array is empty (file not found or empty JSON file)
        return  # Exit the program if the file is not found or the JSON file is empty

    name = input("What name are we looking for? ")  # Get the name to search for from the user
    if advanced_search(array, name):  # Call the advanced_search function to search for the name
        print(f"We found {name} in {filename}.")  # Print a message if the name is found
    else:
        print(f"{name} was not found in {filename}.")  # Print a message if the name is not found

if __name__ == "__main__":
    main()  # Call the main function if the script is run directly (not imported as a module)
# 1. Name:
#     Luke Marshall
# 2. Assignment Name:
#      Lab 06: Advanced Search
# 3. Assignment Description:
#      Search through a list in a quicker way
# 4. Algorithmic Efficiency
#      It splits in the middle of the list and then searches over and over again. I would say that it is O(Log N) Because the bigger the data it will increase but slowly level out since the data splits in halves.
# 5. What was the hardest part? Be as specific as possible.
#      The making it 2 min
# 6. How long did it take for you to complete the assignment?
#      5 hours