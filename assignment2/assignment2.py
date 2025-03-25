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
