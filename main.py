import tkinter as tk

import database
from employee import EmployeeManagement


def main():

    # Create database table
    database.create_table()

    # Create main window
    root = tk.Tk()

    # Create Employee Management application
    EmployeeManagement(root)

    # Start application
    root.mainloop()


if __name__ == "__main__":
    main()