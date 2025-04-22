'''Create a class for representing any 2-D point or vector. The methods inside this class include
its magnitude and its rotation with respect to the X-axis. Using the objects define functions for
calculating the distance between two vectors, dot product, cross product of two vectors. Extend
the 2-D vectors into 3-D using the concept of inheritance. Update the methods according to 3-
D.
'''

import math

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)
    
    def rotation(self):
        return math.degrees(math.atan2(self.y, self.x))
    
    def distance(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
    
    def dot_product(self, other):
        return self.x * other.x + self.y * other.y
    
    def cross_product(self, other):
        return self.x * other.y - self.y * other.x
    
    def __str__(self):
        return f"Vector2D({self.x}, {self.y})"

class Vector3D(Vector2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)  # Initialize the 2D part (x, y)
        self.z = z
    
    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    
    def rotation(self):
        xy_rotation = math.degrees(math.atan2(self.y, self.x))
        z_rotation = math.degrees(math.atan2(self.z, math.sqrt(self.x**2 + self.y**2)))
        return xy_rotation, z_rotation
    
    def distance(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2 + (self.z - other.z)**2)
    
    def dot_product(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z
    
    def cross_product(self, other):
        cx = self.y * other.z - self.z * other.y
        cy = self.z * other.x - self.x * other.z
        cz = self.x * other.y - self.y * other.x
        return Vector3D(cx, cy, cz)
    
    def __str__(self):
        return f"Vector3D({self.x}, {self.y}, {self.z})"

def main():
    print("Choose operation:")
    print("1. Work with 2D vectors")
    print("2. Work with 3D vectors")
    choice = input("Enter choice (1/2): ")

    if choice == '1':
        print("\nEnter coordinates for 2D vector 1:")
        x1 = float(input("Enter x1: "))
        y1 = float(input("Enter y1: "))
        v1 = Vector2D(x1, y1)
        
        print("\nEnter coordinates for 2D vector 2:")
        x2 = float(input("Enter x2: "))
        y2 = float(input("Enter y2: "))
        v2 = Vector2D(x2, y2)

        while True:
            print("\nChoose operation:")
            print("1. Calculate magnitude of vector 1")
            print("2. Calculate rotation of vector 1")
            print("3. Calculate distance between vectors")
            print("4. Calculate dot product")
            print("5. Calculate cross product")
            print("6. Exit")
            operation = input("Enter choice (1-6): ")

            if operation == '1':
                print(f"Magnitude of vector 1: {v1.magnitude()}")
            elif operation == '2':
                print(f"Rotation of vector 1: {v1.rotation()} degrees")
            elif operation == '3':
                print(f"Distance between vector 1 and vector 2: {v1.distance(v2)}")
            elif operation == '4':
                print(f"Dot product of vector 1 and vector 2: {v1.dot_product(v2)}")
            elif operation == '5':
                print(f"Cross product of vector 1 and vector 2: {v1.cross_product(v2)}")
            elif operation == '6':
                break
            else:
                print("Invalid choice!")

    elif choice == '2':
        print("\nEnter coordinates for 3D vector 1:")
        x1 = float(input("Enter x1: "))
        y1 = float(input("Enter y1: "))
        z1 = float(input("Enter z1: "))
        v1 = Vector3D(x1, y1, z1)
        
        print("\nEnter coordinates for 3D vector 2:")
        x2 = float(input("Enter x2: "))
        y2 = float(input("Enter y2: "))
        z2 = float(input("Enter z2: "))
        v2 = Vector3D(x2, y2, z2)

        while True:
            print("\nChoose operation:")
            print("1. Calculate magnitude of vector 1")
            print("2. Calculate rotation of vector 1")
            print("3. Calculate distance between vectors")
            print("4. Calculate dot product")
            print("5. Calculate cross product")
            print("6. Exit")
            operation = input("Enter choice (1-6): ")

            if operation == '1':
                print(f"Magnitude of vector 1: {v1.magnitude()}")
            elif operation == '2':
                xy_rotation, z_rotation = v1.rotation()
                print(f"Rotation of vector 1: XY Rotation = {xy_rotation} degrees, Z Rotation = {z_rotation} degrees")
            elif operation == '3':
                print(f"Distance between vector 1 and vector 2: {v1.distance(v2)}")
            elif operation == '4':
                print(f"Dot product of vector 1 and vector 2: {v1.dot_product(v2)}")
            elif operation == '5':
                cross_prod = v1.cross_product(v2)
                print(f"Cross product of vector 1 and vector 2: {cross_prod}")
            elif operation == '6':
                break
            else:
                print("Invalid choice!")

    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
