try:
    num1 = int(input("Any Number1:"))
    num2 = int(input("Any Number2:"))
    Divsor = num2 / num1
except ZeroDivisionError as e:
    print(e)
    print("You can't divide by Zero BRO!!")
except ValueError as e:
    print(e)
    print("You cannot divided the number by String as well!!")
except Exception as e:
    print(e)
    print("Something Went Wrong:(")
else:
    print(Divsor)
finally:
    print("You always execute:(")

try:
    f = open('mamun.txt')
    if f.name == 'corrupt_file.txt':
        raise Exception
except FileNotFoundError as e:
    print(e)
    print("Sorry file does not exist!")
finally:
    print("Value Error")
