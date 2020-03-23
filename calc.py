#!/usr/bin/env python3

__author__ = "Jugal Kishore"
__version__ = "1.1"

print("///A Simple Calculator///")
while 1:
    num_a = input("\nEnter First Number: ")
    num_b = input("\nEnter Second Number: ")
    print("\nOptions: -")
    print("+ for Addition")
    print("- for Substraction")
    print("* for Multiplication")
    print("/ for Division")
    print("% for Modulus")
    print("Anything else to exit!")
    choice = input("\nChoice: ")
    if choice == "+":
        print(
            "\nAddition of {0} and {1} is = {2}".format(
                num_a, num_b, float(num_a) + float(num_b)
            )
        )
    elif choice == "-":
        print(
            "\nSubtraction of {0} and {1} is = {2}".format(
                num_a, num_b, float(num_a) - float(num_b)
            )
        )
    elif choice == "*":
        print(
            "\nMultiplication of {0} and {1} is = {2}".format(
                num_a, num_b, float(num_a) * float(num_b)
            )
        )
    elif choice == "/":
        if num_b == "0":
            print("\nYou can't divide '{0}' by zero.".format(num_a))
        else:
            print(
                "\nDivison of {0} and {1} is = {2}".format(
                    num_a, num_b, float(num_a) / float(num_b)
                )
            )
    elif choice == "%":
        if num_b == "0":
            print("\nYou can't divide '{0}' by zero.".format(num_a))
        else:
            print(
                "\nModulus of {0} and {1} is = {2}".format(
                    num_a, num_b, round(float(num_a) % float(num_b), 3)
                )
            )
    else:
        print("Uh-Oh, you decided to exit.")
        print("Exiting!")
        break
print("\nCreated by Jugal Kishore -- 2020")
