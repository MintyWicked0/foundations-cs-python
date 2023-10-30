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
        
        if not row_input:
            break
        
        row = [int(element) for element in row_input.split()]
        matrix1.append(row)

    # Get elements for the second matrix separated values with spaces and press Enter after each row. Leave an empty line to finish
    print("Enter elements of the second matrix: ")
    while True:
        row_input = input()
        
        if not row_input:
            break
        
        row = [int(element) for element in row_input.split()]
        matrix2.append(row)

    #Check if one matrix is a rotation of the other
    is_rotation = True

    # Check if the columns of matrix1 are rows in matrix2
    if len(matrix1[0]) != len(matrix2):
        is_rotation = False

    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            if matrix1[i][j] != matrix2[j][i]:
                is_rotation = False
                break

    if is_rotation:
        print("The matrices are rotations of each other.")
    else:
        print("The matrices are not rotations of each other.")

def invertion():
    original_dict = {}
    inverted_dict = {}

    # Get the number of key-value pairs inputed by the user
    n = int(input("Enter the number of key-value pairs: "))

    # Input key-value pairs example(you have 5 keys, you input 5 and then each key with the corresponding value)
    for i in range(n):
        key = input("Enter the key: ")
        value = input("Enter the corresponding value: ")
        original_dict[key] = value

    # Invert the dictionary to
    for key, value in original_dict.items():
        try:
            inverted_dict[value].append(key)
        except KeyError: #we used except because our loop will not end without it and could not use else(researched about it)
            inverted_dict[value] = [key]

    # Display the original and inverted dictionaries
    print("Before inverting:")
    print(original_dict)
    print("After inverting:")
    print(inverted_dict)

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