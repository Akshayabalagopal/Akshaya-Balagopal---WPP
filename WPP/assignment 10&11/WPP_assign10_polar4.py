'''4. Take N (N >= 10) random 2-dimensional points represented in cartesian coordinate space.
Store them in a numpy array. Convert them to polar coordinates.'''

import numpy as np

def cartesian_to_polar(N):
    x = np.random.rand(N)  
    y = np.random.rand(N)  
    
    r = np.sqrt(x**2 + y**2)  
    theta = np.arctan2(y, x)  
    
    polar_coords = np.column_stack((r, theta))
    
    return polar_coords

N = int(input("Enter the no: "))
polar_coords = cartesian_to_polar(N)

print("Cartesian to Polar Coordinates:")
print("Radius (r) and Angle (theta) in radians:")
print(polar_coords)
