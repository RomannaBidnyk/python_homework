# Task 1
def hello():
    return "Hello!"


print("\nTask 1")
print(hello())


# Task 2
def greet(name):
    return "Hello, " + name + "!"


print("\nTask 2")
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


print("\nTask 3")
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


print("\nTask 4")
print(data_type_conversion("5.5", "float"))


# Task 5
def grade(*args):
    try:
        average = sum(args) / len(args)
    except (TypeError, ZeroDivisionError):
        return "Invalid data was provided."

    if average >= 90:
        return "A"
    elif average >= 80 and average <= 89:
        return "B"
    elif average >= 70 and average <= 79:
        return "C"
    elif average >= 60 and average <= 69:
        return "D"
    else:
        return "F"


print("\nTask 5")
print(grade(75, 85, 95))
print(grade("three", "blind", "mice"))
print(grade())


# Task 6
def repeat(words, count):
    result = ""
    for _ in range(count):
        result += words
    return result


print("\nTask 6")
print(repeat("up,", 4))


# Task 7
def student_scores(operation, **kwargs):
    if operation == "mean":
        return sum(kwargs.values()) / len(kwargs)
    elif operation == "best":
        max = 0
        name = ""
        for key, value in kwargs.items():
            if value > max:
                max = value
                name = key
        return name


print("\nTask 7")
print(student_scores("mean", Tom=75, Dick=89, Angela=91))
print(student_scores("best", Tom=75, Dick=89, Angela=91, Frank=50))


# Task 8
def titleize(sentence):
    little_words = ["a", "on", "an", "the", "of", "and", "is", "in"]
    words = sentence.split()
    for i, word in enumerate(words):
        if i == 0 or i == len(words) - 1:
            words[i] = word.capitalize()
        elif word not in little_words:
            words[i] = word.capitalize()

    return " ".join(words)


print("\nTask 8")
print(titleize("after and on"))
print(titleize("a separate peace"))


# Task 9
def hangman(secret, guess):
    result = ""
    for letter in secret:
        if letter not in guess:
            result += "_"
        else:
            result += letter
    return result


print("\nTask 9")
print(hangman("difficulty", "ic"))


# Task 10
def pig_latin(sentence):
    words = sentence.split()
    changed_words = []
    for word in words:
        changed_words.append(change_one_word(word))
    return " ".join(changed_words)


def change_one_word(word):
    vowel = "aeiou"

    if word[0] in vowel:
        return word + "ay"

    count_consonants = 0
    for _ in word:
        if _ not in vowel:
            count_consonants += 1
        else:
            break

    if word[count_consonants - 1] == "q" and word[count_consonants] == "u":
        return word[count_consonants + 1 :] + word[: count_consonants + 1] + "ay"
    else:
        return word[count_consonants:] + word[:count_consonants] + "ay"


print("\nTask 10")
print(pig_latin("apple"))
print(pig_latin("banana"))
print(pig_latin("cherry"))
print(pig_latin("quiet"))
print(pig_latin("square"))
print(pig_latin("the quick brown fox"))
