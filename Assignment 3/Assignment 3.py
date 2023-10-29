def matracies():
    # Get the size of the matrices by the user input
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    
   # Create matrices that user will fill
    matrix1 = []
    matrix2 = []
    result = []
    
    
    # Get the elements of the first matrix  
    print("Enter elements for the first matrix:")
    for i in range(rows):
        row = []
        print("Enter elements for row", (i + 1),":")
        elements = input().split()
        for element in elements:
            row.append(int(element))
        matrix1.append(row)
   
    # Get elements for the second matrix
    print("Enter elements for the second matrix:")
    for i in range(rows):
        row = []
        print("Enter elements for row", (i + 1),":")
        elements = input().split()
        for element in elements:
            row.append(int(element))
        matrix2.append(row)
    
    # Add the matrices
    for i in range(rows):
        result_row = []
        for j in range(cols):
            result_row.append(matrix1[i][j] + matrix2[i][j])
        result.append(result_row)
    
    # Prints the resulting matrix calculatedd
    print("The resulting matrix is:")
    for row in result:
        print(row)
    

def checkingR():
    # Initialize empty matrices
    matrix1 = []
    matrix2 = []

    # Get elements for the first matrix separated values with spaces and press Enter after each row. Leave an empty line to finish
    print("Enter elements of the first matrix: ")

    while True:
        row_input = input()
        
        if row_input:
           row = []
           elements = row_input.split()
        
           for element in elements:
               row.append(int(element))
        
           matrix1.append(row)
        else:
            break

    # Get elements for the second matrix separated values with spaces and press Enter after each row. Leave an empty line to finish
    print("Enter elements of the second matrix: ")

    while True:
        row_input = input()
    
        if row_input:
            row = []
            elements = row_input.split()
        
            for element in elements:
                row.append(int(element))
        
            matrix2.append(row)
        else:
            break

    #Check if one matrix is a rotation of the other
    transposed_matrix1 = [list(row) for row in zip(*matrix1)]
    transposed_matrix2 = [list(row) for row in zip(*matrix2)]

    if transposed_matrix1 == matrix2 or transposed_matrix2 == matrix1:
        print("The matrices are rotations of each other.")
    else:
        print("The matrices are not rotations of each other.")


def invertion():
    ori = {}
    inv = {}

    n = int(input("Enter the number of key-value pairs: "))

def conversation():
    user_data = []

    n = int(input("Enter the number of users: "))

    for i in range(n):
        user = []
        user.append(input("Enter First Name: "))
        user.append(input("Enter Last Name: "))
        user.append(input("Enter ID: "))
        user.append(input("Enter Job Title: "))
        user.append(input("Enter Company: "))
        user_data.append(user)

    user_dict = ()

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