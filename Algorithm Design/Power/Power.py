import json

# pull up files and add asserts
def read_power_data(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            assert 'array' in data, "Error: 'array' key not found in JSON file."
            assert isinstance(data['array'], list), "Error: 'array' value is not a list."
            assert all(isinstance(x, int) for x in data['array']), "Error: 'array' contains non-integer values."
            return data['array']
    except FileNotFoundError:
        print("Error: File not found.")
        exit(1)
    except json.JSONDecodeError:
        print("Error: Invalid JSON format.")
        exit(1)
    except AssertionError as e:
        print(e)
        exit(1)

def get_subarray_size():
    try:
        return int(input("Enter the size of the sub-array: "))
    except ValueError:
        print("Error: Invalid input. Please enter an integer.")
        exit(1)

#calculate with the sub array
def calculate_average_power(power_data, subarray_size):
    assert subarray_size > 0, "Error: Sub-array size must be greater than 0."
    assert subarray_size <= len(power_data), "Error: Sub-array size exceeds the length of the array."
    averages = [sum(power_data[i:i+subarray_size]) / subarray_size for i in range(len(power_data) - subarray_size + 1)]
    return max(averages)

def main():
    filename = input("Enter the filename containing power data: ")
    power_data = read_power_data(filename)
    subarray_size = get_subarray_size()
    average_power = calculate_average_power(power_data, subarray_size)
    print(f"The average power for a sub-array of size {subarray_size} is: {average_power:.2f}")

if __name__ == "__main__":
    main()
# 1. Name:
#     Luke Marshall
# 2. Assignment Name:
#      Lab 13: Power
# 3. Assignment Description:
#      This is a program that will take a list then ask for a number of the contents of the list and give the mean of that ammount.
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part of this project would have to be creating the sub array. I had to research alot before i coukld get this to work. I also had some issues adding some asserts that could effectivly help the program.
# 5. How long did it take for you to complete the assignment?
#      8 hours