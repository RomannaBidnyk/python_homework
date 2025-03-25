import csv

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
