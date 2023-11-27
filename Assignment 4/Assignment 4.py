class Node:
    def __init__(self, data):
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
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def search_and_delete_node(self, value):
        current = self.head
        prev = None
        while current:
            if current.data == value:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                current = None
            else:
                prev = current
                current = current.next

class Student:
    def __init__(self, name, grade, midterm_grade, final_grade, good_attitude):
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
            print(student.name,"Midterm:",student.midterm_grade,"Final:",student.final_grade,"Attitude:",student.good_attitude)

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()
    
def evaluate_expression(expression):
    priority = {'+': 1, '-': 1, '*': 2, '/': 2}
    num_stack = Stack()
    op_stack = Stack()

    for char in expression:
        if char.isdigit():
            num_stack.push(int(char))
        elif char == '(':
            op_stack.push(char)
        elif char == ')':
            while op_stack.items[-1] != '(':
                process(num_stack, op_stack)
            op_stack.pop()
        else:
            while len(op_stack.items) > 0 and op_stack.items[-1] != '(' and priority[char] <= priority[op_stack.items[-1]]:
                process(num_stack, op_stack)
            op_stack.push(char)

    while len(op_stack.items) > 0:
        process(num_stack, op_stack)
    return num_stack.pop()

def process(num_stack, op_stack):
    num2 = num_stack.pop()
    num1 = num_stack.pop()
    op = op_stack.pop()

    if op == '+':
        num_stack.push(num1 + num2)
    elif op == '-':
        num_stack.push(num1 - num2)
    elif op == '*':
        num_stack.push(num1 * num2)
    elif op == '/':
        num_stack.push(num1 / num2)
            
            
class Vertex:
    def __init__(self, data):
        self.data = data
        self.neighbors = set()

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, data):
        if data not in self.vertices:
            self.vertices[data] = Vertex(data)
    
    def add_edge(self, data1, data2):
        if data1 in self.vertices and data2 in self.vertices:
            self.vertices[data1].neighbors.add(data2)
            self.vertices[data2].neighbors.add(data1)
    
    def remove_vertex(self, vertex):
        if vertex.data in self.vertices:
            del self.vertices[vertex.data]
            for v in self.vertices.values():
                v.neighbors.discard(vertex.data)

    def remove_edge(self, vertex1, vertex2):
        if vertex1.data in self.vertices and vertex2.data in self.vertices:
            self.vertices[vertex1.data].neighbors.discard(vertex2.data)
            self.vertices[vertex2.data].neighbors.discard(vertex1.data)
            
    def display_vertices_with_degree(self, degree):
        result = [vertex.data for vertex in self.vertices.values() if len(vertex.neighbors) >= degree]
        print("Vertices with a degree of", degree,"or more: ",result)
    
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
            grade = int(input("Enter overall grade (0-100): "))
            midterm_grade = int(input("Enter midterm grade (0-100): "))
            final_grade = int(input("Enter final grade (0-100): "))
            good_attitude = input("Does the student have a good attitude? (True/False): ").lower() == "true"
            student = Student(name, grade, midterm_grade, final_grade, good_attitude)
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
                break
                
def graph_menu(graph):
    while True:
        print("Graph Menu:")
        print("a. Add vertex")
        print("b. Add edge")
        print("c. Remove vertex")
        print("d. Remove edge")
        print("e. Display vertices with a degree of X or more")
        print("f. Return to main menu")

        choice = input("Enter your choice: ")
        consecutive_errors = 0

        if choice == 'a':
            data = input("Enter vertex data: ")
            vertex = Vertex(data)
            graph.add_vertex(vertex)
        elif choice == 'b':
            data1 = input("Enter the first vertex data: ")
            data2 = input("Enter the second vertex data: ")
            vertex1 = Vertex(data1)
            vertex2 = Vertex(data2)
            graph.add_edge(vertex1, vertex2)
        elif choice == 'c':
            data = input("Enter vertex data to remove: ")
            vertex = Vertex(data)
            graph.remove_vertex(vertex)
        elif choice == 'd':
            data1 = input("Enter the first vertex data: ")
            data2 = input("Enter the second vertex data: ")
            vertex1 = Vertex(data1)
            vertex2 = Vertex(data2)
            graph.remove_edge(vertex1, vertex2)
        elif choice == 'e':
            degree = int(input("Enter the degree value: "))
            graph.display_vertices_with_degree(degree)
        elif choice == 'f':
            break
        else:
            print("Invalid choice. Please try again.")
            consecutive_errors += 1
            if consecutive_errors >= 4:
                print("Too many consecutive errors. Exiting program.")
                break

def main():
    print("Welcome to the Program!")
    name = input("Please enter your first name: ")
    print("Hello, ", name,"!")
    
    linked_list = LinkedList()
    priority_queue = PriorityQueue()
    graph = Graph()
    consecutive_errors = 0
    
    while True:
        print("1. Singly Linked List")
        print("2. Check if Palindrome")
        print("3. Priority Queue")
        print("4. Evaluate an Infix Expression")
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
            expression = input("Enter an infix expression: ")
            result = evaluate_expression(expression)
            print("Result:", result)
        elif choice == '5':
            graph_menu(graph)
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