def matracies():
    rows = int(input("Enter number of rows: "))    #User will input the desired
    cols = int(input("Enter number of columns: ")) #size of the matrix
    mat1 = [] #
    mat2 = [] #creating empty matrices
    result = []  #

    for i in range(rows):
        mat1_row = [0] * cols
        mat2_row = [0] * cols
        result_row = [0] * cols

        mat1.append(mat1_row)
        mat2.append(mat2_row)
        result.append(result_row)
    
    for i in range(rows):
        for j in range(cols):
            result[i][j] = mat1[i][j] + mat2[i][j]
            
    print("The resulting matrix is:")
    for row in result:
        print(row)
    
def checkingR():
    mat1 = []
    mat2 = []

    print("Enter elements of the first matrix:")

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
        user.append(input

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