import pandas as pd

s = pd.Series(['X', 'Y', 'T', 'Aaba', 'Baca', 'CABA', None, 'bird', 'horse', 'dog'])

s_upper = s.str.upper()
print("Upper case values:")
print(s_upper)

s_lower = s.str.lower()
print("\nLower case values:")
print(s_lower)

s_length = s.str.len()
print("\nLength of each string:")
print(s_length)
