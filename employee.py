import tkinter as tk
from tkinter import ttk, messagebox

import database


class EmployeeManagement:

    def __init__(self, root):

        self.root = root

        self.root.title("Employee Management System")
        self.root.geometry("1150x700")
        self.root.minsize(950, 600)

        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(3, weight=1)

        self.create_widgets()
        self.load_employees()

    # =====================================================
    # CREATE GUI
    # =====================================================

    def create_widgets(self):

        # ---------------- TITLE ----------------

        title_label = tk.Label(
            self.root,
            text="EMPLOYEE MANAGEMENT SYSTEM",
            font=("Arial", 22, "bold")
        )

        title_label.grid(
            row=0,
            column=0,
            pady=(15, 10)
        )

        # ---------------- FORM ----------------

        form_frame = tk.LabelFrame(
            self.root,
            text="Employee Details",
            font=("Arial", 11, "bold"),
            padx=10,
            pady=10
        )

        form_frame.grid(
            row=1,
            column=0,
            padx=20,
            pady=5,
            sticky="ew"
        )

        form_frame.columnconfigure(1, weight=1)
        form_frame.columnconfigure(3, weight=1)

        # Employee ID

        tk.Label(
            form_frame,
            text="Employee ID:"
        ).grid(
            row=0,
            column=0,
            padx=10,
            pady=8,
            sticky="w"
        )

        self.employee_id_entry = tk.Entry(
            form_frame,
            state="readonly"
        )

        self.employee_id_entry.grid(
            row=0,
            column=1,
            padx=10,
            pady=8,
            sticky="ew"
        )

        # Name

        tk.Label(
            form_frame,
            text="Name:"
        ).grid(
            row=0,
            column=2,
            padx=10,
            pady=8,
            sticky="w"
        )

        self.name_entry = tk.Entry(form_frame)

        self.name_entry.grid(
            row=0,
            column=3,
            padx=10,
            pady=8,
            sticky="ew"
        )

        # Email

        tk.Label(
            form_frame,
            text="Email:"
        ).grid(
            row=1,
            column=0,
            padx=10,
            pady=8,
            sticky="w"
        )

        self.email_entry = tk.Entry(form_frame)

        self.email_entry.grid(
            row=1,
            column=1,
            padx=10,
            pady=8,
            sticky="ew"
        )

        # Phone

        tk.Label(
            form_frame,
            text="Phone:"
        ).grid(
            row=1,
            column=2,
            padx=10,
            pady=8,
            sticky="w"
        )

        self.phone_entry = tk.Entry(form_frame)

        self.phone_entry.grid(
            row=1,
            column=3,
            padx=10,
            pady=8,
            sticky="ew"
        )

        # Department - DROPDOWN

        tk.Label(
            form_frame,
            text="Department:"
        ).grid(
            row=2,
            column=0,
            padx=10,
            pady=8,
            sticky="w"
        )

        self.department_entry = ttk.Combobox(
            form_frame,
            values=[
                "IT",
                "Marketing",
                "Human Resources",
                "Finance",
                "Sales",
                "Operations",
                "Customer Support",
                "Administration",
                "Other"
            ],
            state="readonly"
        )

        self.department_entry.grid(
            row=2,
            column=1,
            padx=10,
            pady=8,
            sticky="ew"
        )

        # Salary

        tk.Label(
            form_frame,
            text="Salary:"
        ).grid(
            row=2,
            column=2,
            padx=10,
            pady=8,
            sticky="w"
        )

        self.salary_entry = tk.Entry(form_frame)

        self.salary_entry.grid(
            row=2,
            column=3,
            padx=10,
            pady=8,
            sticky="ew"
        )

        # ---------------- BUTTONS ----------------

        button_frame = tk.Frame(self.root)

        button_frame.grid(
            row=2,
            column=0,
            pady=10
        )

        tk.Button(
            button_frame,
            text="Add Employee",
            width=15,
            bg= "#28a745",
            fg="white",
            activebackground="#218838",
            activeforeground="white",
            font=("Arial",10,"bold"),
            command=self.add_employee
        ).grid(
            row=0,
            column=0,
            padx=5
        )

        tk.Button(
            button_frame,
            text="Edit",
            width=15,
            bg= "#007bff",
            fg="white",
            activebackground="#0069d9",
            activeforeground="white",
            font=("Arial",10,"bold"),
            command=self.edit_employee
        ).grid(
            row=0,
            column=1,
            padx=5
        )

        tk.Button(
            button_frame,
            text="Update",
            width=15,
            bg= "#fd7e14",
            fg="white",
            activebackground="#e96b02",
            activeforeground="white",
            font=("Arial",10,"bold"),
            command=self.update_employee
        ).grid(
            row=0,
            column=2,
            padx=5
        )

        tk.Button(
            button_frame,
            text="Delete",
            width=15,
            bg= "#dc3545",
            fg="white",
            activebackground="#c82333",
            activeforeground="white",
            font=("Arial",10,"bold"),
            command=self.delete_employee
        ).grid(
            row=0,
            column=3,
            padx=5
        )

        tk.Button(
            button_frame,
            text="Clear",
            width=15,
            bg= "#6c757d",
            fg="white",
            activebackground="#5a6268",
            activeforeground="white",
            font=("Arial",10,"bold"),
            command=self.clear_form
        ).grid(
            row=0,
            column=4,
            padx=5
        )

        # ---------------- SEARCH ----------------

        search_frame = tk.LabelFrame(
            self.root,
            text="Search Employees",
            font=("Arial", 10, "bold")
        )

        search_frame.grid(
            row=3,
            column=0,
            padx=20,
            pady=(0, 10),
            sticky="nsew"
        )

        search_frame.columnconfigure(0, weight=1)
        search_frame.rowconfigure(1, weight=1)

        search_top_frame = tk.Frame(search_frame)

        search_top_frame.grid(
            row=0,
            column=0,
            padx=10,
            pady=8,
            sticky="ew"
        )

        search_top_frame.columnconfigure(1, weight=1)

        tk.Label(
            search_top_frame,
            text="Search:"
        ).grid(
            row=0,
            column=0,
            padx=5
        )

        self.search_entry = tk.Entry(
            search_top_frame
        )

        self.search_entry.grid(
            row=0,
            column=1,
            padx=5,
            sticky="ew"
        )

        tk.Button(
            search_top_frame,
            text="Search",
            width=12,
            command=self.search_employees
        ).grid(
            row=0,
            column=2,
            padx=5
        )

        tk.Button(
            search_top_frame,
            text="Show All",
            width=12,
            command=self.clear_search
        ).grid(
            row=0,
            column=3,
            padx=5
        )

        # ---------------- TREEVIEW ----------------

        tree_frame = tk.Frame(search_frame)

        tree_frame.grid(
            row=1,
            column=0,
            padx=10,
            pady=(0, 10),
            sticky="nsew"
        )

        tree_frame.columnconfigure(0, weight=1)
        tree_frame.rowconfigure(0, weight=1)

        columns = (
            "ID",
            "Name",
            "Email",
            "Phone",
            "Department",
            "Salary"
        )

        self.employee_tree = ttk.Treeview(
            tree_frame,
            columns=columns,
            show="headings",
            selectmode="browse"
        )

        self.employee_tree.heading(
            "ID",
            text="Employee ID"
        )

        self.employee_tree.heading(
            "Name",
            text="Name"
        )

        self.employee_tree.heading(
            "Email",
            text="Email"
        )

        self.employee_tree.heading(
            "Phone",
            text="Phone"
        )

        self.employee_tree.heading(
            "Department",
            text="Department"
        )

        self.employee_tree.heading(
            "Salary",
            text="Salary"
        )

        self.employee_tree.column(
            "ID",
            width=100,
            anchor="center"
        )

        self.employee_tree.column(
            "Name",
            width=170
        )

        self.employee_tree.column(
            "Email",
            width=230
        )

        self.employee_tree.column(
            "Phone",
            width=140,
            anchor="center"
        )

        self.employee_tree.column(
            "Department",
            width=150
        )

        self.employee_tree.column(
            "Salary",
            width=120,
            anchor="e"
        )

        # Scrollbars

        vertical_scrollbar = ttk.Scrollbar(
            tree_frame,
            orient="vertical",
            command=self.employee_tree.yview
        )

        horizontal_scrollbar = ttk.Scrollbar(
            tree_frame,
            orient="horizontal",
            command=self.employee_tree.xview
        )

        self.employee_tree.configure(
            yscrollcommand=vertical_scrollbar.set,
            xscrollcommand=horizontal_scrollbar.set
        )

        self.employee_tree.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        vertical_scrollbar.grid(
            row=0,
            column=1,
            sticky="ns"
        )

        horizontal_scrollbar.grid(
            row=1,
            column=0,
            sticky="ew"
        )

        self.employee_tree.bind(
            "<Double-1>",
            self.double_click_employee
        )

    # =====================================================
    # VALIDATION
    # =====================================================

    def validate_employee_data(self):

        name = self.name_entry.get().strip()
        email = self.email_entry.get().strip()
        phone = self.phone_entry.get().strip()
        department = self.department_entry.get().strip()
        salary = self.salary_entry.get().strip()

        if not name:
            messagebox.showerror(
                "Validation Error",
                "Please enter employee name."
            )
            return False

        if not email:
            messagebox.showerror(
                "Validation Error",
                "Please enter email."
            )
            return False

        if "@" not in email or "." not in email:
            messagebox.showerror(
                "Validation Error",
                "Please enter a valid email."
            )
            return False

        if not phone:
            messagebox.showerror(
                "Validation Error",
                "Please enter phone number."
            )
            return False

        if not phone.isdigit():
            messagebox.showerror(
                "Validation Error",
                "Phone number must contain only digits."
            )
            return False

        if len(phone) != 10:
            messagebox.showerror(
                "Validation Error",
                "Phone number must contain 10 digits."
            )
            return False

        if not department:
            messagebox.showerror(
                "Validation Error",
                "Please select a department."
            )
            return False

        if not salary:
            messagebox.showerror(
                "Validation Error",
                "Please enter salary."
            )
            return False

        try:

            salary_value = float(salary)

            if salary_value <= 0:
                messagebox.showerror(
                    "Validation Error",
                    "Salary must be greater than 0."
                )
                return False

        except ValueError:

            messagebox.showerror(
                "Validation Error",
                "Salary must be a valid number."
            )
            return False

        return True

    # =====================================================
    # ADD
    # =====================================================

    def add_employee(self):

        if not self.validate_employee_data():
            return

        name = self.name_entry.get().strip()
        email = self.email_entry.get().strip()
        phone = self.phone_entry.get().strip()
        department = self.department_entry.get().strip()
        salary = float(self.salary_entry.get().strip())

        employee_id = database.add_employee(
            name,
            email,
            phone,
            department,
            salary
        )

        messagebox.showinfo(
            "Success",
            f"Employee added successfully.\n\n"
            f"Employee ID: {employee_id}"
        )

        self.clear_form()
        self.load_employees()

    # =====================================================
    # LOAD EMPLOYEES
    # =====================================================

    def load_employees(self):

        for item in self.employee_tree.get_children():
            self.employee_tree.delete(item)

        employees = database.get_all_employees()

        for employee in employees:

            self.employee_tree.insert(
                "",
                tk.END,
                values=employee
            )

    # =====================================================
    # EDIT
    # =====================================================

    def edit_employee(self):

        selected = self.employee_tree.selection()

        if not selected:

            messagebox.showwarning(
                "Selection Required",
                "Please select an employee."
            )
            return

        item = self.employee_tree.item(
            selected[0]
        )

        values = item["values"]

        employee_id = values[0]
        name = values[1]
        email = values[2]
        phone = values[3]
        department = values[4]
        salary = values[5]

        # ID

        self.employee_id_entry.config(
            state="normal"
        )

        self.employee_id_entry.delete(
            0,
            tk.END
        )

        self.employee_id_entry.insert(
            0,
            employee_id
        )

        self.employee_id_entry.config(
            state="readonly"
        )

        # Name

        self.name_entry.delete(0, tk.END)
        self.name_entry.insert(0, name)

        # Email

        self.email_entry.delete(0, tk.END)
        self.email_entry.insert(0, email)

        # Phone

        self.phone_entry.delete(0, tk.END)
        self.phone_entry.insert(0, phone)

        # Department

        self.department_entry.set(department)

        # Salary

        self.salary_entry.delete(0, tk.END)
        self.salary_entry.insert(0, salary)

    # =====================================================
    # UPDATE
    # =====================================================

    def update_employee(self):

        employee_id = self.employee_id_entry.get().strip()

        if not employee_id:

            messagebox.showwarning(
                "Update",
                "Please select an employee and click Edit first."
            )
            return

        if not self.validate_employee_data():
            return

        name = self.name_entry.get().strip()
        email = self.email_entry.get().strip()
        phone = self.phone_entry.get().strip()
        department = self.department_entry.get().strip()
        salary = float(self.salary_entry.get().strip())

        database.update_employee(
            employee_id,
            name,
            email,
            phone,
            department,
            salary
        )

        messagebox.showinfo(
            "Success",
            "Employee updated successfully."
        )

        self.clear_form()
        self.load_employees()

    # =====================================================
    # DELETE
    # =====================================================

    def delete_employee(self):

        selected = self.employee_tree.selection()

        if not selected:

            messagebox.showwarning(
                "Selection Required",
                "Please select an employee."
            )
            return

        item = self.employee_tree.item(
            selected[0]
        )

        values = item["values"]

        employee_id = values[0]
        employee_name = values[1]

        confirmation = messagebox.askyesno(
            "Confirm Delete",
            f"Are you sure you want to delete?\n\n"
            f"Employee ID: {employee_id}\n"
            f"Name: {employee_name}"
        )

        if not confirmation:
            return

        database.delete_employee(
            employee_id
        )

        messagebox.showinfo(
            "Success",
            "Employee deleted successfully."
        )

        self.clear_form()
        self.load_employees()

    # =====================================================
    # SEARCH
    # =====================================================

    def search_employees(self):

        search_text = self.search_entry.get().strip()

        if not search_text:

            self.load_employees()
            return

        for item in self.employee_tree.get_children():
            self.employee_tree.delete(item)

        employees = database.search_employees(
            search_text
        )

        for employee in employees:

            self.employee_tree.insert(
                "",
                tk.END,
                values=employee
            )

    # =====================================================
    # CLEAR SEARCH
    # =====================================================

    def clear_search(self):

        self.search_entry.delete(
            0,
            tk.END
        )

        self.load_employees()

    # =====================================================
    # CLEAR FORM
    # =====================================================

    def clear_form(self):

        self.employee_id_entry.config(
            state="normal"
        )

        self.employee_id_entry.delete(
            0,
            tk.END
        )

        self.employee_id_entry.config(
            state="readonly"
        )

        self.name_entry.delete(
            0,
            tk.END
        )

        self.email_entry.delete(
            0,
            tk.END
        )

        self.phone_entry.delete(
            0,
            tk.END
        )

        self.department_entry.set("")

        self.salary_entry.delete(
            0,
            tk.END
        )

        self.name_entry.focus()

    # =====================================================
    # DOUBLE CLICK
    # =====================================================

    def double_click_employee(self, event):

        self.edit_employee()