print("Question 1")
a = 10*(90+2)-5 #915
b = 10*90+2-5  #897
c = 10*90+(2-5) #897
d = 10.0*(90+2)-5 #915
e = 120/(20+40)-(6-2)/4 #1
f = 5.0/2 #2.5
g = 5/2 #2.5
h = 5.0/2.0 #2.5
i = 5/2.0 #2.5
j = 678%3*(8-(9/4)) #0

print(int(a))
print(int(b))
print(int(c))
print(float(d))
print(int(e))
print(float(f))
print(int(g))
print(float(h))
print(float(i))
print(int(j))
#BREAK
print()
print("Question 2")
ID = input("Enter ID: ")  
name = input("Enter name: ")
dob = input("Enter date of birth (DD-MM-YYYY): ")
address = input("Enter address: ")

if len(ID) == 1:
    ID = '0' + ID

name = name.upper()
dob = dob.replace('-', '/')
address = address.lower()

print("Your profile - ID:", ID, ", name:", name, ", DOB:", dob ,", Address:", address)
#BREAK
print()
print("Question 3")
number = input("Enter a number: ")
num_digits = len(number)

print(number, "has", num_digits, "digits.")
#BREAK
print()
print("Question 4")
grade = int(input("Enter your grade: "))
letter_grade = ""

if grade >= 97:
  letter_grade = "A+"
elif grade >= 93:
  letter_grade = "A"
elif grade >= 90:
  letter_grade = "A-"
elif grade >= 87:
  letter_grade = "B+"
elif grade >= 83:
  letter_grade = "B"
elif grade >= 80:
  letter_grade = "B-"
elif grade >= 77:
  letter_grade = "C+"
elif grade >= 73:
  letter_grade = "C"
elif grade >= 70:
  letter_grade = "C-"
elif grade >= 67:
  letter_grade = "D+"
elif grade >= 63:
  letter_grade = "D"
elif grade >= 60:
  letter_grade = "D-"
else:
  letter_grade = "F"

print(grade, "is equivalent to a", letter_grade)
#BREAK
print()
print("Question 5")
n = int(input("Enter a number: "))
for i in range(1, n*2):
    if i <= n:
        print('*' * i)
    else:
        print('*' * (n*2 - i))
#BREAK
print()
print("Question 6")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

while num2 < num1:
    print("The second number can't be smaller than the first number.")
    num2 = int(input("Enter the second number: "))

for i in range(num1, num2 + 1):
    if i % 2 == 0:
        print(i)
#END OF ANSWERS.