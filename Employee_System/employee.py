import sqlite3

class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

class EmployeesManager:
    def __init__(self):
        self.conn = sqlite3.connect('employees.db')
        self.cur = self.conn.cursor()
        self.cur.execute('''CREATE TABLE IF NOT EXISTS employees
                            (name text, age integer, salary real)''')
        self.conn.commit()

    def add_employee(self, employee):
        self.cur.execute("INSERT INTO employees VALUES (?, ?, ?)", (employee.name, employee.age, employee.salary))
        self.conn.commit()

    def print_employees(self):
        self.cur.execute("SELECT * FROM employees")
        rows = self.cur.fetchall()
        if len(rows) == 0:
            print("No employees at the moment!")
        else:
            for row in rows:
                print(f"{row[0]} has an age of {row[1]} and the gained salary is : {row[2]}")

    def delete_by_age(self, start_age, end_age):
        self.cur.execute("DELETE FROM employees WHERE age >= ? AND age <= ?", (start_age, end_age))
        self.conn.commit()

    def update_salary_by_name(self, name, new_salary):
        self.cur.execute("UPDATE employees SET salary = ? WHERE name = ?", (new_salary, name))
        self.cur.execute("SELECT(changes())")
        if self.cur.fetchone()[0] == 0:
            print("No employee found with that name.")
        else:
            print("Salary updated successfully!")
        self.conn.commit()

class FrontendManager:
    def __init__(self):
        self.employees_manager = EmployeesManager()

    def print_menu(self):
        print("Program options:")
        print("1) Add new employee")
        print("2) Print all employees")
        print("3) Delete employees by age")
        print("4) Update salary by name")
        print("5) Quit the program")

    def get_choice(self):
        while True:
            try:
                choice = int(input("Please enter your choice (1-5): "))
                if choice in [1, 2, 3, 4, 5]:
                    return choice
                else:
                    print("Invalid choice. Please enter a number between 1 and 5.")
            except ValueError:
                print("Invalid choice. Please enter a number between 1 and 5.")


    def run(self):
        while True:
            self.print_menu()
            choice = self.get_choice()
            if choice == 1:
                while True:
                    name = input("Enter employee name: ")
                    if name.isalpha() or ' ' in name:
                        break
                    else:
                        print("Please enter a valid name (letters and spaces only).")
                while True:
                    try:
                        age = int(input("Enter employee age: "))
                        break
                    except ValueError:
                        print("Please enter a valid age (integer).")
                while True:
                    try:
                        salary = float(input("Enter employee salary: "))
                        break
                    except ValueError:
                        print("Please enter the salary in numbers.")
                employee = Employee(name, age, salary)
                self.employees_manager.add_employee(employee)


            elif choice == 2:
                self.employees_manager.print_employees()
            elif choice == 3:
                start_age = int(input("Enter start age: "))
                end_age = int(input("Enter end age: "))
                self.employees_manager.delete_by_age(start_age, end_age)
            elif choice == 4:
                name = input("Enter employee name: ")
                new_salary = float(input("Enter new salary: "))
                self.employees_manager.update_salary_by_name(name, new_salary)
            elif choice == 5:
                print("Program terminated.")
                self.employees_manager.conn.close()
                break

from employee import FrontendManager

def main():
    frontend = FrontendManager()
    frontend.run()

if __name__ == '__main__':
    main()


#------------------------------------------------------#


# import sqlite3
# from tkinter import *

# class Employee:
#     def __init__(self, name, age, salary):
#         self.name = name
#         self.age = age
#         self.salary = salary


# class EmployeesManager:
#     def __init__(self):
#         self.conn = sqlite3.connect('employees.db')
#         self.cur = self.conn.cursor()
#         self.cur.execute('''CREATE TABLE IF NOT EXISTS employees
#                             (name text, age integer, salary real)''')
#         self.conn.commit()    

# class FrontendManager:
#     def __init__(self):
#         self.employees_manager = EmployeesManager()
#         self.root = Tk()
#         self.root.title("Employees Management")

#         # Add employee frame
#         self.add_frame = Frame(self.root)
#         self.add_frame.pack()

#         Label(self.add_frame, text="Name").grid(row=0, column=0)
#         self.name_entry = Entry(self.add_frame)
#         self.name_entry.grid(row=0, column=1)

#         Label(self.add_frame, text="Age").grid(row=1, column=0)
#         self.age_entry = Entry(self.add_frame)
#         self.age_entry.grid(row=1, column=1)

#         Label(self.add_frame, text="Salary").grid(row=2, column=0)
#         self.salary_entry = Entry(self.add_frame)
#         self.salary_entry.grid(row=2, column=1)

#         Button(self.add_frame, text="Add Employee", command=self.add_employee).grid(row=3, column=0, columnspan=2)

#         # Options frame
#         self.options_frame = Frame(self.root)
#         self.options_frame.pack()

#         # ... Add other options frames and buttons

#         self.root.mainloop()

#     def add_employee(self):
#         name = self.name_entry.get()
#         age = int(self.age_entry.get())
#         salary = float(self.salary_entry.get())
#         employee = Employee(name, age, salary)
#         self.employees_manager.add_employee(employee)

# def main():
#     frontend = FrontendManager()

# if __name__ == '__main__':
#     main()



# import sqlite3
# from tkinter import *

# class Employee:
#     def __init__(self, name, age, salary):
#         self.name = name
#         self.age = age
#         self.salary = salary


# class EmployeesManager:
#     def __init__(self):
#         self.conn = sqlite3.connect('employees.db')
#         self.cur = self.conn.cursor()
#         self.cur.execute('''CREATE TABLE IF NOT EXISTS employees
#                             (name text, age integer, salary real)''')
#         self.conn.commit()

# class FrontendManager:
#     def __init__(self):
#         self.employees_manager = EmployeesManager()
#         self.root = Tk()
#         self.root.title("Employees Management")
        
#         # Add employee frame
#         self.add_frame = Frame(self.root)
#         self.add_frame.pack()

#         Label(self.add_frame, text="Name").grid(row=0, column=0)
#         self.name_entry = Entry(self.add_frame)
#         self.name_entry.grid(row=0, column=1)

#         Label(self.add_frame, text="Age").grid(row=1, column=0)
#         self.age_entry = Entry(self.add_frame)
#         self.age_entry.grid(row=1, column=1)

#         Label(self.add_frame, text="Salary").grid(row=2, column=0)
#         self.salary_entry = Entry(self.add_frame)
#         self.salary_entry.grid(row=2, column=1)

#         Button(self.add_frame, text="Add Employee", command=self.add_employee).grid(row=3, column=0, columnspan=2)

#         # Options frame
#         self.options_frame = Frame(self.root)
#         self.options_frame.pack()

#         Button(self.options_frame, text="Print Employees", command=self.print_employees).pack()
#         Button(self.options_frame, text="Delete Employees", command=self.delete_employees).pack()
#         Button(self.options_frame, text="Update Salary", command=self.update_salary).pack()
#         Button(self.options_frame, text="Quit", command=self.root.quit).pack()

#         self.root.mainloop()

#     def add_employee(self):
#         name = self.name_entry.get()
#         age = self.age_entry.get()
#         salary = self.salary_entry.get()
#         if not name or not age or not salary:
#             errmsg = "Please fill out all fields."
#             Label(self.add_frame, text=errmsg, fg="red").grid(row=4, column=0, columnspan=2)
#             return
#         try:
#             age = int(age)
#             salary = float(salary) 
#         except ValueError:
#             errmsg = "Invalid age or salary. Please enter numbers."
#             Label(self.add_frame, text=errmsg, fg="red").grid(row=4, column=0, columnspan=2)
#             return
#         employee = Employee(name, age, salary)
#         self.employees_manager.add_employee(employee)
#         errmsg = "Employee added successfully!"
#         Label(self.add_frame, text=errmsg, fg="green").grid(row=4, column=0, columnspan=2)

#     def print_employees(self):
#         self.employees_manager.print_employees()

#     def delete_employees(self):
#         start_age = self.start_age_entry.get()
#         end_age = self.end_age_entry.get()
#         if not start_age or not end_age:
#             errmsg = "Please enter both start and end age."
#             Label(self.options_frame, text=errmsg, fg="red").pack()
#             return
#         try:
#             start_age = int(start_age) 
#             end_age = int(end_age)
#         except ValueError:
#             errmsg = "Invalid age range. Please enter numbers."
#             Label(self.options_frame, text=errmsg, fg="red").pack()
#             return
#         self.employees_manager.delete_by_age(start_age, end_age)
#         errmsg = f"Employees aged {start_age} to {end_age} deleted."
#         Label(self.options_frame, text=errmsg, fg="green").pack()

#     def update_salary(self):
#         name = self.name_entry.get()
#         new_salary = self.new_salary_entry.get()
#         if not name or not new_salary:
#             errmsg = "Please enter both employee name and new salary."
#             Label(self.options_frame, text=errmsg, fg="red").pack()
#             return
#         try:
#             new_salary = float(new_salary)
#         except ValueError:
#             errmsg = "Invalid salary. Please enter a number."
#             Label(self.options_frame, text=errmsg, fg="red").pack()
#             return
#         self.employees_manager.update_salary_by_name(name, new_salary)
#         errmsg = "Salary updated successfully!"
#         Label(self.options_frame, text=errmsg, fg="green").pack()

# def main(): 
#     frontend = FrontendManager()

# if __name__ == '__main__': 
#     main()


# import tkinter as tk
# import tkinter.messagebox as messagebox
# import sqlite3

# class Employee:
#     def __init__(self, name, age, salary):
#         self.name = name
#         self.age = age
#         self.salary = salary

# class EmployeesManager:
#     def __init__(self):
#         self.conn = sqlite3.connect('employees.db')
#         self.cur = self.conn.cursor()
#         self.cur.execute('''CREATE TABLE IF NOT EXISTS employees
#                             (name text, age integer, salary real)''')
#         self.conn.commit()

#     def add_employee(self, employee):
#         self.cur.execute("INSERT INTO employees VALUES (?, ?, ?)", (employee.name, employee.age, employee.salary))
#         self.conn.commit()

#     def get_employees(self):
#         self.cur.execute("SELECT * FROM employees")
#         return self.cur.fetchall()

#     def delete_by_age(self, start_age, end_age):
#         self.cur.execute("DELETE FROM employees WHERE age >= ? AND age <= ?", (start_age, end_age))
#         self.conn.commit()

#     def update_salary_by_name(self, name, new_salary):
#         self.cur.execute("UPDATE employees SET salary = ? WHERE name = ?", (new_salary, name))
#         self.cur.execute("SELECT changes()")
#         if self.cur.fetchone()[0] == 0:
#             messagebox.showerror("Error", "No employee found with that name.")
#         else:
#             messagebox.showinfo("Success", "Salary updated successfully!")
#         self.conn.commit()

# class FrontendManager:
#     def __init__(self):
#         self.employees_manager = EmployeesManager()
#         self.root = tk.Tk()
#         self.root.title("Employee Management System")

#     def add_employee_window(self):
#         def add_employee():
#             name = name_entry.get()
#             age = age_entry.get()
#             salary = salary_entry.get()

#             if name and age and salary:
#                 try:
#                     age = int(age)
#                     salary = float(salary)
#                     employee = Employee(name, age, salary)
#                     self.employees_manager.add_employee(employee)
#                     messagebox.showinfo("Success", "Employee added successfully!")
#                     add_window.destroy()
#                 except ValueError:
#                     messagebox.showerror("Error", "Invalid age or salary. Please enter valid values.")
#             else:
#                 messagebox.showerror("Error", "Please fill in all the fields.")

#         add_window = tk.Toplevel(self.root)
#         add_window.title("Add Employee")

#         name_label = tk.Label(add_window, text="Name:")
#         name_label.pack()
#         name_entry = tk.Entry(add_window)
#         name_entry.pack()

#         age_label = tk.Label(add_window, text="Age:")
#         age_label.pack()
#         age_entry = tk.Entry(add_window)
#         age_entry.pack()

#         salary_label = tk.Label(add_window, text="Salary:")
#         salary_label.pack()
#         salary_entry = tk.Entry(add_window)
#         salary_entry.pack()

#         add_button = tk.Button(add_window, text="Add", command=add_employee)
#         add_button.pack()

#     def print_employees_window(self):
#         employees = self.employees_manager.get_employees()

#         if len(employees) == 0:
#             messagebox.showinfo("Information", "No employees at the moment!")
#         else:
#             employees_window = tk.Toplevel(self.root)
#             employees_window.title("Employees List")

#             scrollbar = tk.Scrollbar(employees_window)
#             scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

#             employees_listbox = tk.Listbox(employees_window, yscrollcommand=scrollbar.set)
#             employees_listbox.pack(side=tk.LEFT, fill=tk.BOTH)
#         for employee in employees:
#             employees_listbox.insert(tk.END, f"Name: {employee[0]}, Age: {employee[1]}, Salary: {employee[2]}")

#         scrollbar.config(command=employees_listbox.yview)

# def delete_employees_window(self):
#     def delete_employees():
#         start_age = start_age_entry.get()
#         end_age = end_age_entry.get()

#         if start_age and end_age:
#             try:
#                 start_age = int(start_age)
#                 end_age = int(end_age)
#                 self.employees_manager.delete_by_age(start_age, end_age)
#                 messagebox.showinfo("Success", "Employees deleted successfully!")
#                 delete_window.destroy()
#             except ValueError:
#                 messagebox.showerror("Error", "Invalid age values. Please enter valid integers.")
#         else:
#             messagebox.showerror("Error", "Please fill in both start age and end age.")

#     delete_window = tk.Toplevel(self.root)
#     delete_window.title("Delete Employees")

#     start_age_label = tk.Label(delete_window, text="Start Age:")
#     start_age_label.pack()
#     start_age_entry = tk.Entry(delete_window)
#     start_age_entry.pack()

#     end_age_label = tk.Label(delete_window, text="End Age:")
#     end_age_label.pack()
#     end_age_entry = tk.Entry(delete_window)
#     end_age_entry.pack()

#     delete_button = tk.Button(delete_window, text="Delete", command=delete_employees)
#     delete_button.pack()

# def update_salary_window(self):
#     def update_salary():
#         name = name_entry.get()
#         new_salary = new_salary_entry.get()

#         if name and new_salary:
#             try:
#                 new_salary = float(new_salary)
#                 self.employees_manager.update_salary_by_name(name, new_salary)
#                 update_window.destroy()
#             except ValueError:
#                 messagebox.showerror("Error", "Invalid salary. Please enter a valid number.")
#         else:
#             messagebox.showerror("Error", "Please fill in both employee name and new salary.")

#     update_window = tk.Toplevel(self.root)
#     update_window.title("Update Salary")

#     name_label = tk.Label(update_window, text="Employee Name:")
#     name_label.pack()
#     name_entry = tk.Entry(update_window)
#     name_entry.pack()

#     new_salary_label = tk.Label(update_window, text="New Salary:")
#     new_salary_label.pack()
#     new_salary_entry = tk.Entry(update_window)
#     new_salary_entry.pack()

#     update_button = tk.Button(update_window, text="Update", command=update_salary)
#     update_button.pack()

# def print_menu(self):
#     menu = tk.Toplevel(self.root)
#     menu.title("Program Options")

#     add_button = tk.Button(menu, text="Add New Employee", command=self.add_employee_window)
#     add_button.pack()

#     print_button = tk.Button(menu, text="Print All Employees", command=self.print_employees_window)
#     print_button.pack()

#     delete_button = tk.Button(menu, text="Delete Employees by Age", command=self.delete_employees_window)
#     delete_button.pack()

#     update_button = tk.Button(menu, text="Update Salary by Name", command=self.update_salary_window)
#     update_button.pack()

#     quit_button = tk.Button(menu, text="Quit", command=self.root.quit)
#     quit_button.pack()
    
# def run(self):
#     self.root.mainloop()

# def main():
#     frontend = FrontendManager()
#     frontend.run()

# if __name__ == '__main__':
#     main()




