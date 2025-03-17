# Task 1
def hello():
    return "Hello!"


print(hello())


# Task 2
def greet(name):
    return "Hello, " + name + "!"


print(greet("James"))


# Task 3
# version 1
# def calc(a, b, operation="multiply"):
#     try:
#         if operation == "multiply":
#             return a * b
#         elif operation == "add":
#             return a + b
#         elif operation == "subtract":
#             return a - b
#         elif operation == "divide":
#             return a / b
#         elif operation == "modulo":
#             return a % b
#         elif operation == "int_divide":
#             return a // b
#         elif operation == "power":
#             return a**b
#         else:
#             return "Incorrect operation or value"
#     except ZeroDivisionError:
#         return "You can't divide by 0!"
#     except TypeError:
#         return "You can't multiply those values!"


# version 2
def calc(a, b, operation="multiply"):
    try:
        match operation:
            case "multiply":
                return a * b
            case "add":
                return a + b
            case "subtract":
                return a - b
            case "divide":
                return a / b
            case "modulo":
                return a % b
            case "int_divide":
                return a // b
            case "power":
                return a**b
            case _:
                return "Incorrect operation"
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return f"You can't {operation} those values!"


print(calc(5, 6, "add"))


# Task 4
def data_type_conversion(value, type_name):
    try:
        match type_name:
            case "int":
                return int(value)
            case "float":
                return float(value)
            case "str":
                return str(value)
            case _:
                return "Incorrect data type"
    except ValueError:
        return f"You can't convert {value} into a {type_name}."


print(data_type_conversion("5.5", "float"))
