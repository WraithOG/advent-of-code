import string
import re

# Prepare input file



# Read in data, add to array
file = open("clean_input.txt", "r")
lines = file.read().split('\n')
file_size = len(lines)

#Iterate through each item of the array
cal_val = []
for i in range(file_size):
    nums = []
    current_line = lines[i]
    # Identify digits, add to temp array
    nums += [int(s) for s in re.findall(r'\d', current_line)]
    # Gets the location of the last digit
    sizeof = len(nums) - 1
    # Create a string of the first number, append last num
    temp_val = str(nums[0]) + str(nums[sizeof])
    # Store the calibration value in global array
    cal_val.append(int(temp_val))

# Iterate through cal_val, add current number to total
total = 0
for number in cal_val:
    total = total + number
print(total)


