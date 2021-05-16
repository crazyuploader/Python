## Progress

- [x] Question 1 | Level 1

Question:

Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.

Solution:

```
print("Number(s) divisible by 7 but not 5 in the range 2000, 3200 -\n")
number = []
for i in range(2000, 3201):
    if (i % 7 == 0) and (i % 5 != 0):
        number.append(str(i))
print(",".join(number))
```

- [x] Question 2 | Level 1

Question:

Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320

Solution:

```
def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)


print("Program to computer factorial of a number")
print("\nEnter a number: ")
number = int(input())
print("\nFactorial of {0} is = {1}".format(number, fact(number)))
```

- [x] Question 3 | Level 1

Question:

With a given integral number n, write a program to generate a dictionary that contains (i, i\*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
Suppose the following input is supplied to the program:
8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

Solution:

```
def create_dict(integer):
    dictionary = {}
    temp = 1
    while temp <= integer:
        dictionary[temp] = temp * temp
        temp += 1
    return dictionary


print("Enter an Integer")
integer = int(input())
if integer > 0:
    print(create_dict(integer))
else:
    print("Integer should be greater than 1!")
```

- [x] Question 4 | Level 1

Question:

Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')

Solution:

```
values = input("Enter Numbers: ")
li = values.split(",")
tu = tuple(li)
print(li)
print(tu)
```

- [x] Question 5 | Level 1

Question:
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

Solution:

```
class IOString(object):
    def __init__(self):
        self.string = ""

    def GetString(self):
        self.string = str(input("Enter String: "))

    def PrintString(self):
        print(self.string.upper())


st = IOString()
st.GetString()
st.PrintString()
```

- [x] Question 6 | Level 2

Question:
Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
Example
Let us assume the following comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24

Solution:

```
import math
def Calculate(data):
    list = []
    C = 50
    H = 30
    for number in data:
        list.append(str(round(math.sqrt((2*C*int(number)/H)))))
    print(",".join(list))

string = input("Input Number(s): ")
Calculate(string.split(","))
```

- [ ] Question 7 | Level 2
- [ ] Question 8 | Level 2
- [ ] Question 9 | Level 2
- [ ] Question 10 | Level 2
