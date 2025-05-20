import sqlite3

try:
    with sqlite3.connect("../db/magazines.db") as conn:
        cursor = conn.cursor()
        cursor.execute("PRAGMA foreign_keys = ON;")

        cursor.execute(
            """
        CREATE TABLE IF NOT EXISTS publishers (
            publisher_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE
        )
        """
        )

        cursor.execute(
            """
        CREATE TABLE IF NOT EXISTS magazines (
            magazine_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE,
            publisher_id INTEGER NOT NULL,
            FOREIGN KEY (publisher_id) REFERENCES publishers(publisher_id)
        )
        """
        )

        cursor.execute(
            """
        CREATE TABLE IF NOT EXISTS subscribers (
            subscriber_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            address TEXT NOT NULL
        )
        """
        )

        cursor.execute(
            """
        CREATE TABLE IF NOT EXISTS subscriptions (
            subscription_id INTEGER PRIMARY KEY,
            subscriber_id INTEGER NOT NULL,
            magazine_id INTEGER NOT NULL,
            expiration_date TEXT NOT NULL,
            FOREIGN KEY (subscriber_id) REFERENCES subscribers(subscriber_id),
            FOREIGN KEY (magazine_id) REFERENCES magazines(magazine_id)
        )
        """
        )

        print("All tables created successfully.")

except sqlite3.Error as e:
    print(f"An error occurred while connecting to the database: {e}")


def create_publisher(conn, name):
    try:
        conn.execute("INSERT INTO publishers (name) VALUES (?)", (name,))
    except sqlite3.IntegrityError:
        print(f"Publisher '{name}' already exists.")


def create_magazine(conn, name, publisher_id):
    try:
        conn.execute(
            "INSERT INTO magazines (name, publisher_id) VALUES (?, ?)",
            (name, publisher_id),
        )
    except sqlite3.IntegrityError:
        print(
            f"Magazine '{name}' already exists or publisher_id {publisher_id} is invalid."
        )


def create_subscriber(conn, name, address):
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM subscribers WHERE name = ? AND address = ?", (name, address)
    )
    if cursor.fetchone():
        print(f"Subscriber '{name}, {address}' already exists.")
    else:
        try:
            conn.execute(
                "INSERT INTO subscribers (name, address) VALUES (?, ?)", (name, address)
            )
        except sqlite3.IntegrityError:
            print(f"Failed to insert subscriber: {name}, {address}")


def create_subscription(conn, subscriber_id, magazine_id, expiration_date):
    try:
        conn.execute(
            """
            INSERT INTO subscriptions (subscriber_id, magazine_id, expiration_date)
            VALUES (?, ?, ?)
        """,
            (subscriber_id, magazine_id, expiration_date),
        )
    except sqlite3.IntegrityError:
        print(f"Subscription already exists or foreign keys invalid.")


with sqlite3.connect("../db/magazines.db") as conn:
    conn.execute("PRAGMA foreign_keys = 1")
    cursor = conn.cursor()

    create_publisher(conn, "First publisher")
    create_publisher(conn, "2nd publisher")
    create_publisher(conn, "3rd publisher")

    create_magazine(conn, "First magazine", 1)
    create_magazine(conn, "2nd magazine", 2)
    create_magazine(conn, "3rd magazine", 3)

    create_subscriber(conn, "Jane Doe", "123 Brighton St")
    create_subscriber(conn, "John Doe", "456 5th Ave")
    create_subscriber(
        conn, "Jane Doe", "789 Ocean Parkway"
    )  # Same name, different address

    create_subscription(conn, 1, 1, "2025-12-31")
    create_subscription(conn, 1, 2, "2025-11-30")
    create_subscription(conn, 2, 3, "2025-10-15")

    conn.commit()
    print("Database populated successfully.")

with sqlite3.connect("../db/magazines.db") as conn:
    conn.execute("PRAGMA foreign_keys = 1")
    cursor = conn.cursor()

    print("\n All Subscribers ")
    cursor.execute("SELECT * FROM subscribers")
    for row in cursor.fetchall():
        print(row)

    print("\n All Magazines Sorted by Name ")
    cursor.execute("SELECT * FROM magazines ORDER BY name")
    for row in cursor.fetchall():
        print(row)

    print("\n Magazines Published by First publisher")
    cursor.execute(
        """
        SELECT magazines.*
        FROM magazines
        JOIN publishers ON magazines.publisher_id = publishers.publisher_id
        WHERE publishers.name = ?
    """,
        ("First publisher",),
    )
    for row in cursor.fetchall():
        print(row)
