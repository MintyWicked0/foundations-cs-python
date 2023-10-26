#Question 1
def reverse():
  return print(s[::-1] * i)


s = "Hello"
i = 2
reverse()

print("")


#Question 2
def rearrange(b):
  upper = ""
  lower = ""
  for char in s:
    if char.isupper():
      upper += char
    elif char.islower():
      lower += char
  return print(upper + lower)


b = "Hello World"
rearrange(b)

print("")


#Question 3
def reorder(s1, s2):
  return print(sorted(s1) == sorted(s2))


s1 = "abcde"
s2 = "edacb"
reorder(s1, s2)

print("")


#Question 4
def maximum(lst):
  if len(lst) > 0:
    max_v = lst[0]
    max_i = 0

    for i in range(1, len(lst)):
      if lst[i] > max_v:
        max_v = lst[i]
        max_i = i
    return print("The highest value in the list is", max_v, " at index ",
                 max_i)
  else:
    print("The list is empty")
    return


lst = [5, 6, 3, 2, 7, 2, 0, 1, 6]
maximum(lst)


def minimum(lst):
  if len(lst) > 0:
    min_v = lst[0]
    min_i = 0

    for i in range(1, len(lst)):
      if lst[i] < min_v:
        min_v = lst[i]
        min_i = i
    return print("The lowest value in the list is", min_v, "at index", min_i)
  else:
    print("The list is empty")
    return


lst = [5, 6, 3, 2, 7, 2, 0, 1, 6]
minimum(lst)

print("")


#Question 5
def calculate(num):
  if num == 0:
    return 0
  else:
    return num % 10 + calculate(num // 10)


num = 348
print(calculate(num))

print("")


#Question 6
def removeDupes(x):
  if len(x) <= 1:
    return x
  elif x[0] == x[1]:
    return removeDupes(x[1:])
  else:
    return x[0] + removeDupes(x[1:])


x = "hhheeellllllllllllllooooo wwwwwwwoooorllllddddd"
print(removeDupes(x))

print("")


#Question 7
def reverseInt(n):
  if n < 10:
    return n
  else:
    return n % 10 + reverseInt(n // 10) * 10

n = 50
print(reverseInt(n)) #since it is optional i will leave it until i see how it is done.