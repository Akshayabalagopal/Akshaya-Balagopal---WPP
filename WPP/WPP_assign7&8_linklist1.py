'''Write a Python program to create a class representing a linked list data structure. Include
methods for displaying linked list data, inserting and deleting nodes.
'''

class Node:
    def __init__(self, data):
        self.data = data  
        self.next = None 

class LinkedList:
    def __init__(self):
        self.head = None  

    def insert(self, data):
        '''insert at end'''
        new_node = Node(data)
        if not self.head:  
            self.head = new_node
        else:
            current = self.head
            while current.next: 
                current = current.next
            current.next = new_node  

    def delete(self, value):
        """Delete the first node"""
        current = self.head
        if current is None: 
            print("The list is empty.")
            return
        
        if current.data == value:
            self.head = current.next  
            current = None  
            return

        prev = None
        while current and current.data != value:
            prev = current
            current = current.next

        if current is None:  
            print(f"Node with value {value} not found.")
            return
        
        prev.next = current.next
        current = None  

    def display(self):
        current = self.head
        if current is None:
            print("The list is empty.")
            return
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

def main():
    link = LinkedList()  

    while True:
        print("\nLinked List Operations:")
        print("1. Insert a node")
        print("2. Delete a node")
        print("3. Display linked list")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            data = int(input("Enter the data to insert: "))
            link.insert(data)
            print(f"Node with value {data} inserted.")
        elif choice == '2':
            value = int(input("Enter the value to delete: "))
            link.delete(value)
        elif choice == '3':
            print("Linked List:")
            link.display()
        elif choice == '4':
            print("Exit")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
