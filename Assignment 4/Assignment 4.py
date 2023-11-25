class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
    
    def display_nodes(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")
    
    def search_and_delete_node(self, value):
        current = self.head
        prev = None
        while current:
            if current.value == value:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                current = None
            else:
                prev = current
                current = current.next

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
    
def priority_queue_menu(priority_queue):
    while True:
        print("Priority Queue Menu:")
        print("a. Add a student")
        print("b. Interview a student")
        print("c. Return to main menu")
        consecutive_errors = 0
        choice = input("Enter your choice: ")

        if choice == "a":
            name = input("Enter student name: ")
            midterm_grade = int(input("Enter midterm grade (0-100): "))
            final_grade = int(input("Enter final grade (0-100): "))
            good_attitude = input("Does the student have a good attitude? (True/False): ").lower() == "true"
            student = Student(name, midterm_grade, final_grade, good_attitude)
            priority_queue.add_student(student)
        elif choice == "b":
            priority_queue.interview_student()
        elif choice == "c":
            break
        else:
            print("Invalid choice. Please try again.")
            consecutive_errors += 1
            if consecutive_errors >= 4:
                print("Too many consecutive errors. Exiting program.")
                break
def linked_list_menu(linked_list):
    while True:
        print("Singly Linked List Menu:")
        print("a. Add Node")
        print("b. Display Nodes")
        print("c. Search for & Delete Node")
        print("d. Return to main menu")
        consecutive_errors = 0  
        choice = input("Enter your choice: ")
        if choice == "a":
            print("")
        elif choice == "b":
            print("")
        elif choice == "c":
            print("")
        elif choice == "d":
            break
        else:
            print("Invalid choice. Please try again.")
            consecutive_errors += 1
            if consecutive_errors >= 4:
                print("Too many consecutive errors. Exiting program.")

def main():
    print("Welcome to the Program!")
    name = input("Please enter your first name: ")
    print("Hello, ", name,"!")
    consecutive_errors = 0
    
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
            break
        else:
            print("Your input is invalid. Please enter a valid input from 1 to 6!")
            consecutive_errors += 1
            if consecutive_errors >= 4:
                print("Too many consecutive errors. Exiting program.")
                break

main()