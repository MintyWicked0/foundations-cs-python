def matracies():
    print("Working 1")
    
def checkingR():
    print("Working 2")

def invertion():
    print("Working 3")
    
def conversation():
    print("Working 4")

def checkingP():
    print("Working 5")
    
def search():
    print("Working 6")
    

def main():
    print("Welcome to the Program!")
    name = input("Please enter your first name: ")
    print("Hello, ", name,"!")
    
    while True:
        print("\nMenu:")
        print("1. Add Matrices")
        print("2. Check Rotation")
        print("3. Invert Dictionary")
        print("4. Convert Matrix to Dictionary")
        print("5. Check Palindrome")
        print("6. Search for an Element & Merge Sort")
        print("7. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            matracies()
        elif choice == '2':
            checkingR()
        elif choice == '3':
            invertion()
        elif choice == '4':
            conversation()
        elif choice == '5':
            checkingP()
        elif choice == '6':
            search()
        elif choice == '7':
            print("End of the Program!")
            return
        else:
            print("Your input is invalid. Please enter a valid input from 1 to 7!")

main()