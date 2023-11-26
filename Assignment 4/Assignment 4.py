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
        
    def enqueue(self, student):
        new_node = Node(student)
        if self.isEmpty():
            self.head = new_node
        else:
            current = self.head
            prev = None
            while current and current.data.grade >= student.grade:
                prev = current
                current = current.next
            if prev:
                prev.next = new_node
            else:
                self.head = new_node
            new_node.next = current
            
    def dequeue(self):
        if self.isEmpty():
            print("Priority queue is empty")
            return None
        student = self.head.data
        self.head = self.head.next
        return student
    
    def isEmpty(self):
        return self.head is None

    def add_student(self, student):
        self.enqueue(student)
        
    def interview_student(self):
        if self.isEmpty():
            print("Priority queue is empty. No students to interview.")
        else:
            student = self.dequeue()
            print("Interviewing", (student.name), "Midterm: ", student.midterm_grade, "Final: ", student.final_grade, "Attitude: ", student.good_attitude)
    
def palindrome_check():
    string = input("Enter a string: ")
    if string == string[::-1]:
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")

    
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
            value = int(input("Enter a numerical value: "))
            linked_list.add_node(value)
        elif choice == "b":
            linked_list.display_nodes()
        elif choice == "c":
            value = int(input("Enter a value to search and delete: "))
            linked_list.search_and_delete_node(value)
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
    
    linked_list = LinkedList()
    priority_queue = PriorityQueue()
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
            linked_list_menu(linked_list)
        elif choice == '2':
            palindrome_check()
        elif choice == '3':
            priority_queue_menu(priority_queue)
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