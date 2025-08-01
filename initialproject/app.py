from math import *

def calculator():

    number1 = int(input("Enter a number: "))
    operation = input("Enter a operation: ")
    number2 = int(input("Enter another number: "))
    if operation == "+":
        return number1 + number2
    elif operation == "-":
        return number1 - number2
    elif operation == "*":
        print(number1 * number2)
    elif operation == "/":
        return number1 / number2


    #for x in calc:
        #if x.isnumeric():
         #   numbers.append(int(x))
        #else:
            #numbers.append(x)
    #while len(numbers) != 0:
     #   hold = numbers.pop(0)

      #  if hold == "*":
       #     res
calculator()