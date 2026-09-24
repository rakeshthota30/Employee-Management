import sqlite3


DATABASE_NAME = "employees.db"


def connect_database():
    """
    Connect to SQLite database.
    If the database does not exist,
    SQLite will create it automatically.
    """
    return sqlite3.connect(DATABASE_NAME)


def create_table():
    """
    Create employees table if it does not already exist.
    """

    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT NOT NULL,
            department TEXT NOT NULL,
            salary REAL NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def add_employee(name, email, phone, department, salary):
    """
    Add a new employee to the database.
    """

    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO employees
        (name, email, phone, department, salary)
        VALUES (?, ?, ?, ?, ?)
    """, (
        name,
        email,
        phone,
        department,
        salary
    ))

    connection.commit()

    employee_id = cursor.lastrowid

    connection.close()

    return employee_id


def get_all_employees():
    """
    Get all employees from database.
    """

    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, name, email, phone, department, salary
        FROM employees
        ORDER BY id ASC
    """)

    employees = cursor.fetchall()

    connection.close()

    return employees


def get_employee(employee_id):
    """
    Get one employee using Employee ID.
    """

    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, name, email, phone, department, salary
        FROM employees
        WHERE id = ?
    """, (employee_id,))

    employee = cursor.fetchone()

    connection.close()

    return employee


def update_employee(
    employee_id,
    name,
    email,
    phone,
    department,
    salary
):
    """
    Update an existing employee.
    """

    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE employees
        SET
            name = ?,
            email = ?,
            phone = ?,
            department = ?,
            salary = ?
        WHERE id = ?
    """, (
        name,
        email,
        phone,
        department,
        salary,
        employee_id
    ))

    connection.commit()

    connection.close()


def delete_employee(employee_id):
    """
    Delete employee using Employee ID.
    """

    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        DELETE FROM employees
        WHERE id = ?
    """, (employee_id,))

    connection.commit()

    connection.close()


def search_employees(search_text):
    """
    Search employees by ID, name, email,
    phone or department.
    """

    connection = connect_database()
    cursor = connection.cursor()

    search_value = f"%{search_text}%"

    cursor.execute("""
        SELECT id, name, email, phone, department, salary
        FROM employees
        WHERE
            CAST(id AS TEXT) LIKE ?
            OR name LIKE ?
            OR email LIKE ?
            OR phone LIKE ?
            OR department LIKE ?
        ORDER BY id ASC
    """, (
        search_value,
        search_value,
        search_value,
        search_value,
        search_value
    ))

    employees = cursor.fetchall()

    connection.close()

    return employees