class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, value):
        new_node = Node(value)
        if self.head:
            self.head = new_node

class Student:
    def __init__(self,name,grade,midterm_grade,final_grade,good_attitude):
        self.name = name
        self.grade = grade
        self.midterm_grade = midterm_grade
        self.final_grade = final_grade
        self.good_attitude = good_attitude
        
class PriorityQueue:
    def __init__(self):
        self.head = None
    def enqueue(self):
        new_node = Node()
        if self.isEmpty():
            self.head = new_node
    def dequeue(self):
        if self.isEmpty():
            print("Priority queue is empty")
            return None
        student = self.head.data
        self.head = self.head.next
        return student

def main():
    print("Welcome to the Program!")
    name = input("Please enter your first name: ")
    print("Hello, ", name,"!")
    
    while True:
        print("1. Singly Linked List")
        print("2. Check if Palindrome")
        print("3. Priority Queue")
        print("4. CEvaluate an Infix Expression")
        print("5. Graph")
        print("6. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            print(" ")
        elif choice == '2':
            print(" ")
        elif choice == '3':
            print(" ")
        elif choice == '4':
            print(" ")
        elif choice == '5':
            print(" ")
        elif choice == '6':
            print("End of the Program!")
            print("Have great day!")
            return
        else:
            print("Your input is invalid. Please enter a valid input from 1 to 6!")

main()