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