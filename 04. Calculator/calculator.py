import art


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def get_valid_operation():
    while True:
        operation = input(
            "From these 4 operations, which one you would like to perform? : "
        )
        if operation in operations:
            return operation
        else:
            print("Please choose a valid operation")


def get_valid_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("That's not a valid number. Please enter a numeric value.")


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    continue_calculating = True
    number1 = get_valid_number("What is the first number? : ")
    while continue_calculating:
        print("Operations: \n '+' \n '-' \n '*' \n '/' ")
        operation = get_valid_operation()
        number2 = get_valid_number("What is the next number? : ")
        answer = operations[operation](number1, number2)
        print(f"The result of {number1} {operation} {number2} is: {answer}")
        choice = input(
            f"Would you like to perform any other operation to the result {answer}? Type 'yes' to continue or anything else to exit: "
        )
        if choice.lower() == "yes":
            number1 = answer
        else:
            continue_calculating = False


print(f"{art.logo}")
calculator()
