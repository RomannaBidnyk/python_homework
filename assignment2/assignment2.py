import csv
import os
import custom_module
from datetime import datetime

# Task 2
print("\nTask 2")


def read_employees():
    employees_dict = {}
    employees_list = []

    try:
        with open("../csv/employees.csv", "r") as file:
            reader = csv.reader(file)
            header = next(reader)
            employees_dict["fields"] = header

            for row in reader:
                employees_list.append(row)

            employees_dict["rows"] = employees_list

    except Exception as e:
        print("An exception occurred:", e)

    return employees_dict


employees = read_employees()
print(f"Employees: {employees}")


# Task 3
print("\nTask 3")


def column_index(column):
    return employees["fields"].index(column)


employee_id_column = column_index("employee_id")
print(f"Index for employee_id is {employee_id_column}")

# Task 4
print("\nTask 4")


def first_name(row_number):
    first_name_col = column_index("first_name")
    return employees["rows"][row_number][first_name_col]


print(first_name(0))

# Task 5
print("\nTask 5")


def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id

    matches = list(filter(employee_match, employees["rows"]))
    return matches


print(employee_find(15))

# Task 6
print("\nTask 6")


def employee_find_2(employee_id):
    matches = list(
        filter(
            lambda row: int(row[employee_id_column]) == employee_id, employees["rows"]
        )
    )
    return matches


print(employee_find(15))

# Task 7
print("\nTask 7")


def sort_by_last_name():
    last_name_col = column_index("last_name")
    employees["rows"].sort(key=lambda row: row[last_name_col])
    return employees["rows"]


print(sort_by_last_name())

# Task 8
print("\nTask 8")

# version 1
# def employee_dict(row):
#     employee_data = {}

#     for i, field in enumerate(employees["fields"]):
#         if field != "employee_id":
#             employee_data[field] = row[i]
#     return employee_data


# version 2
def employee_dict(row):
    zipped_data = zip(employees["fields"], row)
    employee_data = dict(zipped_data)
    employee_data.pop("employee_id", None)
    return employee_data


print(employee_dict(employees["rows"][0]))

# Task 9
print("\nTask 9")


def all_employees_dict():
    all_employees = {}
    for row in employees["rows"]:
        all_employees[row[employee_id_column]] = employee_dict(row)
    return all_employees


print(all_employees_dict())

# Task 10
print("\nTask 10")


def get_this_value():
    return os.getenv("THISVALUE")


print(get_this_value())


# Task 11
print("\nTask 11")


def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)


set_that_secret("very_secret_secret")
print(custom_module.secret)

# Task 12
print("\nTask 12")


def read_minutes():
    minutes1 = read_minutes_from_csv("../csv/minutes1.csv")
    minutes2 = read_minutes_from_csv("../csv/minutes2.csv")
    return minutes1, minutes2


def read_minutes_from_csv(filepath):
    try:
        with open(filepath, "r") as file:
            reader = csv.DictReader(file)
            fields = reader.fieldnames
            rows = [tuple(row.values()) for row in reader]
            return {"fields": fields, "rows": rows}
    except Exception as e:
        print("An exception occurred:", e)


minutes1, minutes2 = read_minutes()
print(f"\nminutes1: {minutes1}")
print(f"\nminutes2: {minutes2}")

# Task 13
print("\nTask 13")


def create_minutes_set():
    set1 = set(minutes1["rows"])
    set2 = set(minutes2["rows"])
    return set1.union(set2)


minutes_set = create_minutes_set()
print(f"minutes_set: {minutes_set}")

# Task 14
print("\nTask 14")


def create_minutes_list():
    minutes_list_raw = list(minutes_set)
    converted_list = list(
        map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes_list_raw)
    )
    return converted_list


minutes_list = create_minutes_list()

print(f"minutes list: {minutes_list}")

# Task 15
print("\nTask 15")


def write_sorted_list():
    sorted_list = sorted(minutes_list, key=lambda x: x[1])
    converted_list = list(
        map(lambda x: (x[0], x[1].strftime("%B %d, %Y")), sorted_list)
    )
    with open("./minutes.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(minutes1["fields"])
        writer.writerows(converted_list)

    return converted_list


print(write_sorted_list())
