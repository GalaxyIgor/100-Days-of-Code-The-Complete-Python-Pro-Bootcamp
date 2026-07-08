def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operation = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print("Welcome to the calculator program!")
    # print(operation["+"](2, 3))

    num1 = float(input("What is the first number?: "))
    
    should_continue = True
    while should_continue:
        input_operation = input("What operation would you like to perform? (+, -, *, /): ")
        num2 = float(input("What is the second number?: "))
        
        answer = operation[input_operation](num1, num2)
        print(f"{num1} {input_operation} {num2} = {answer}")
    
        input_continue = input(f"Type 'y' to continue calculation with {answer} or type 'n' to exit: ")

        if input_continue == "y":
            num1 = answer
        else:
            should_continue = False
            print("\n" * 20)
            calculator()
            return

calculator()