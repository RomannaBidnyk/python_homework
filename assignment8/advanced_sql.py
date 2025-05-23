import sqlite3

with sqlite3.connect("../db/lesson.db") as conn:
    conn.execute("PRAGMA foreign_keys = 1")
    cursor = conn.cursor()

    print("TASK 1")
    query = """
    SELECT orders.order_id, SUM(products.price * line_items.quantity) AS total_price
        FROM orders 
            JOIN line_items ON orders.order_id = line_items.order_id
            JOIN products ON line_items.product_id = products.product_id
        GROUP BY orders.order_id
        ORDER BY orders.order_id
        LIMIT 5;
    """

    cursor.execute(query)
    results = cursor.fetchall()

    print("Order ID - Total Price")
    for row in results:
        print(str(row[0]) + " - " + str(row[1]))

    print("\n\nTASK 2")
    query2 = """
    SELECT customers.customer_name, AVG(order_totals.total_price) AS average_total_price
        FROM customers
        LEFT JOIN (
            SELECT orders.customer_id, SUM(products.price * line_items.quantity) AS total_price
                FROM orders
                JOIN line_items ON orders.order_id = line_items.order_id
                JOIN products ON line_items.product_id = products.product_id
            GROUP BY orders.order_id
        ) order_totals ON customers.customer_id = order_totals.customer_id
        GROUP BY customers.customer_id;
    """

    cursor.execute(query2)
    results2 = cursor.fetchall()

    print("\nCustomer Name - Average Order Price")
    for name, avg_price in results2:
        print(str(name) + " - " + str(avg_price))

    print("\n\nTASK 3")

    cursor.execute(
        "SELECT customer_id FROM customers WHERE customer_name = 'Perez and Sons'"
    )
    customer_id = cursor.fetchone()[0]

    cursor.execute(
        "SELECT employee_id FROM employees WHERE first_name = 'Miranda' AND last_name = 'Harris'"
    )
    employee_id = cursor.fetchone()[0]

    cursor.execute("SELECT product_id FROM products ORDER BY price ASC LIMIT 5")
    product_ids = []
    for row in cursor.fetchall():
        product_ids.append(row[0])

    print("\nCreating new order for 'Perez and Sons'...")

    try:
        cursor.execute(
            "INSERT INTO orders (customer_id, employee_id, date) VALUES (?, ?, DATE('now')) RETURNING order_id;",
            (customer_id, employee_id),
        )
        order_id = cursor.fetchone()[0]

        # Insert 5 line_items with quantity = 10
        for pid in product_ids:
            cursor.execute(
                "INSERT INTO line_items (order_id, product_id, quantity) VALUES (?, ?, ?);",
                (order_id, pid, 10),
            )

        conn.commit()
        print(f"Order created with ID {order_id}")

    except Exception as e:
        conn.rollback()
        print("Transaction failed:", e)

    query3 = """
        SELECT line_items.line_item_id, line_items.quantity, products.product_name
            FROM line_items 
            JOIN products ON line_items.product_id = products.product_id
        WHERE line_items.order_id = ?;
    """
    cursor.execute(query3, (order_id,))
    results3 = cursor.fetchall()

    print("\nLine Items for New Order")
    print("Line Item ID - Quantity - Product Name")
    for line_id, qty, product_name in results3:
        print(str(line_id) + " - " + str(qty) + " - " + str(product_name))

    print("\n\nTASK 4")
    query4 = """
        SELECT employees.employee_id, employees.first_name, employees.last_name, COUNT(orders.order_id) AS order_count
            FROM employees
            JOIN orders ON employees.employee_id = orders.employee_id
        GROUP BY employees.employee_id, employees.first_name, employees.last_name
        HAVING COUNT(orders.order_id) > 5;
    """

    cursor.execute(query4)
    results4 = cursor.fetchall()

    print("\nEmployees with More Than 5 Orders")
    print("Employee ID - First Name - Last Name - Order Count")
    for emp_id, fname, lname, count in results4:
        print(
            str(emp_id) + " - " + str(fname) + " - " + str(lname) + " - " + str(count)
        )
