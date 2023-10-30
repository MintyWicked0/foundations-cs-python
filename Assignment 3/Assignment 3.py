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
    # Create matrices that user will fill
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
    # Create dictionary that user will fill
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

def convertion():
    # Create list that user will fill
    user_matrix = []

    # Get the number of users from the user
    n = int(input("Enter the number of users: "))

    # Input user data into the matrix
    print("Enter user data (First Name, Last Name, ID, Job Title, Company) for each user:")
    for i in range(n):
        user_data = input("Enter user data: ").split()
        user_matrix.append(user_data)

    # Convert the matrix into a dictionary
    user_dict = {}
    for user in user_matrix:
        user_id = user[2]
        user_info = [user[0], user[1], user[3], user[4]]
        user_dict[user_id] = user_info

    # Display the user dictionary
    print("User Data Dictionary:")
    print(user_dict)

def checkingP(s):
    # Base case: If the string is empty or has only one character, it's a palindrome.
    if len(s) <= 1:
        return True
    
    # Check if the first and last characters of the string are the same.
    if s[0] == s[-1]:
        # Recursively check the remaining substring without the first and last characters.
        return checkingP(s[1:-1])
    
    return False

    # Get the input string from the user
    input_string = input("Enter a string: ")

    # Remove any leading and trailing spaces
    input_string = input_string.strip()

    # Check if the input string is a palindrome
    if checkingP(input_string):
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")
#(6) is purely researched and not completly my work.
def custom_sort(arr):
    # Custom sort function (selection sort)
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

def search_and_sort_list():
    # Initialize an empty list
    my_list = []

    # Get elements for the list
    n = int(input("Enter the number of elements in the list: "))
    for i in range(n):
        element = int(input(f"Enter element {i + 1}: "))
        my_list.append(element)

    # Get the element to search for
    search_element = int(input("Enter the element to search for: "))

    # Search for the element in the list
    if search_element in my_list:
        index = my_list.index(search_element)
        print(f"The element {search_element} was found at index {index}.")

        # Sort the list using the custom sort function
        custom_sort(my_list)

        print("Sorted list:", my_list)
    else:
        print(f"The element {search_element} was not found in the list.")

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
            convertion()
        elif choice == '5': #I had to research it since it was not very clear
            # Get the input string from the user
            input_string = input("Enter a string: ")

            # Remove any leading and trailing spaces
            input_string = input_string.strip()

            # Check if the input string is a palindrome
            if checkingP(input_string):
                print("The string is a palindrome.")
            else:
                print("The string is not a palindrome.")
        elif choice == '6':
            search_and_sort_list()
        elif choice == '7':
            print("End of the Program!")
            return
        else:
            print("Your input is invalid. Please enter a valid input from 1 to 7!")

main()