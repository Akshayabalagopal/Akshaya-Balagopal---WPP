'''Write a Python program to create a class representing a queue data structure. Include methods
for enqueueing and dequeuing elements.
'''

class Queue:
    def __init__(self):
        self.queue = [] 

    def enqueue(self, item):
        """insert at end"""
        self.queue.append(item)
        print(f"Enqueued: {item}")

    def dequeue(self):
        """delete"""
        if len(self.queue) == 0:
            print("Queue is empty. Cannot dequeue.")
        else:
            removed_item = self.queue.pop(0)  
            print(f"Dequeued: {removed_item}")
            return removed_item

    def display(self):
        """Display"""
        if len(self.queue) == 0:
            print("Queue is empty.")
        else:
            print("Current Queue: ", self.queue)

    def size(self):
        return len(self.queue)

def main():
    q = Queue()  

    while True:
        print("\nQueue Operations:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Display Queue")
        print("4. Get Queue Size")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter item to enqueue: ")
            q.enqueue(item)
        elif choice == '2':
            q.dequeue()
        elif choice == '3':
            q.display()
        elif choice == '4':
            print(f"Queue size: {q.size()}")
        elif choice == '5':
            print("Exit")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
