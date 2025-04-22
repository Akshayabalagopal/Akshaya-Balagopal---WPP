import numpy as np

def adjust_strings(array):
    left_justified = []
    centered = []
    right_justified = []
    
    for string in array:
        left_justified.append(string.ljust(15, '_'))
        
        centered.append(string.center(15, '_'))
        
        right_justified.append(string.rjust(15, '_'))
    
    left_justified_array = np.array(left_justified)
    centered_array = np.array(centered)
    right_justified_array = np.array(right_justified)
    
    return left_justified_array, centered_array, right_justified_array

N = int(input("Enter the number of strings: "))  
strings = []

for i in range(N):
    user_input = input(f"Enter string {i+1}: ")  
    strings.append(user_input)

strings_array = np.array(strings)

left_justified, centered, right_justified = adjust_strings(strings_array)

print("\nLeft-Justified:")
print(left_justified)

print("\nCentered:")
print(centered)

print("\nRight-Justified:")
print(right_justified)
