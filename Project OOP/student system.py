import tkinter as tk
from tkinter import ttk, messagebox
import tkinter.simpledialog as simpledialog

class StudentManagementSystem:
    def __init__(self, name, last_name, student_set, student_id):
        self.name = name
        self.last_name = last_name
        self.set = student_set
        self.id = student_id

    def information(self):
        return f'Student: {self.name} {self.last_name}, Set: {self.set}, ID: {self.id}'

class ManagementSystemGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("800x600")
        self.root.configure(bg='#f5f5f5')
        
        self.student_list = []
        
        # Create main frame
        self.main_frame = ttk.Frame(root, padding="20")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Header
        header_label = ttk.Label(self.main_frame, 
                               text="Student Database Management System", 
                               font=('Arial', 18, 'bold'),
                               foreground='#2c3e50',
                               justify=tk.CENTER)
        header_label.grid(row=0, column=0, columnspan=2, pady=20)
        
        # Create buttons frame
        self.create_buttons()
        
        # Create search frame
        self.create_search_frame()
        
        # Create student list display
        self.create_student_list()
        
        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set("Welcome to Student Management System")
        status_bar = ttk.Label(self.main_frame, textvariable=self.status_var, 
                              relief=tk.SUNKEN, style='Status.TLabel')
        status_bar.grid(row=5, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=10)
        
        # Configure styles
        self.configure_styles()
        
        # Grid configuration
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.columnconfigure(1, weight=1)
        self.main_frame.rowconfigure(3, weight=1)

    def configure_styles(self):
        style = ttk.Style()
        style.configure('Header.TLabel', font=('Arial', 16, 'bold'))
        style.configure('Action.TButton', font=('Arial', 10, 'bold'))
        style.configure('Status.TLabel', font=('Arial', 9))
        style.configure('Treeview', font=('Arial', 10))
        style.configure('Treeview.Heading', font=('Arial', 11, 'bold'))

    def create_buttons(self):
        button_frame = ttk.Frame(self.main_frame)
        button_frame.grid(row=1, column=0, columnspan=2, pady=20)
        
        buttons = [
            ("Add Student", self.add_student_window),
            ("Update Student", self.update_student_window),
            ("Delete Student", self.delete_student),
            ("Show All Students", self.show_all_students),
            ("Clear All", self.clear_all),
            ("Exit", self.root.quit)
        ]
        
        for i, (text, command) in enumerate(buttons):
            btn = ttk.Button(button_frame, text=text, command=command, style='Action.TButton')
            btn.grid(row=i//3, column=i%3, padx=8, pady=8, sticky='ew')
            button_frame.columnconfigure(i%3, weight=1)

    def create_search_frame(self):
        search_frame = ttk.Frame(self.main_frame)
        search_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=10)
        
        ttk.Label(search_frame, text="Search:", font=('Arial', 10, 'bold')).grid(row=0, column=0, padx=5)
        
        self.search_var = tk.StringVar()
        search_entry = ttk.Entry(search_frame, textvariable=self.search_var, width=30)
        search_entry.grid(row=0, column=1, padx=5)
        search_entry.bind('<KeyRelease>', self.search_students)
        
        ttk.Button(search_frame, text="Clear Search", 
                  command=self.clear_search).grid(row=0, column=2, padx=5)
        
        search_frame.columnconfigure(1, weight=1)

    def create_student_list(self):
        list_frame = ttk.LabelFrame(self.main_frame, text="Student Records", padding="10")
        list_frame.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=10)
        
        # Create treeview with scrollbar
        columns = ('ID', 'First Name', 'Last Name', 'Set')
        self.student_tree = ttk.Treeview(list_frame, columns=columns, show='headings', height=15)
        
        # Define headings
        self.student_tree.heading('ID', text='Student ID')
        self.student_tree.heading('First Name', text='First Name')
        self.student_tree.heading('Last Name', text='Last Name')
        self.student_tree.heading('Set', text='Set')
        
        # Define columns
        self.student_tree.column('ID', width=100, anchor=tk.CENTER)
        self.student_tree.column('First Name', width=150, anchor=tk.W)
        self.student_tree.column('Last Name', width=150, anchor=tk.W)
        self.student_tree.column('Set', width=100, anchor=tk.CENTER)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.student_tree.yview)
        self.student_tree.configure(yscrollcommand=scrollbar.set)
        
        # Grid treeview and scrollbar
        self.student_tree.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        
        # Bind double-click event
        self.student_tree.bind('<Double-1>', self.on_student_double_click)
        
        list_frame.columnconfigure(0, weight=1)
        list_frame.rowconfigure(0, weight=1)

    def update_status(self, message):
        self.status_var.set(message)

    def refresh_student_list(self, students=None):
        """Refresh the student list in the treeview"""
        if students is None:
            students = self.student_list
        
        # Clear existing items
        for item in self.student_tree.get_children():
            self.student_tree.delete(item)
        
        # Add students to treeview
        for student in students:
            self.student_tree.insert('', tk.END, values=(
                student.id, student.name, student.last_name, student.set
            ))
        
        self.update_status(f"Displaying {len(students)} student(s)")

    def search_students(self, event=None):
        search_term = self.search_var.get().lower()
        if not search_term:
            self.refresh_student_list()
            return
        
        filtered_students = []
        for student in self.student_list:
            if (search_term in str(student.id).lower() or 
                search_term in student.name.lower() or 
                search_term in student.last_name.lower() or 
                search_term in student.set.lower()):
                filtered_students.append(student)
        
        self.refresh_student_list(filtered_students)

    def clear_search(self):
        self.search_var.set("")
        self.refresh_student_list()

    def on_student_double_click(self, event):
        selection = self.student_tree.selection()
        if selection:
            item = selection[0]
            student_data = self.student_tree.item(item, 'values')
            messagebox.showinfo("Student Information", 
                              f"ID: {student_data[0]}\n"
                              f"Name: {student_data[1]} {student_data[2]}\n"
                              f"Set: {student_data[3]}")

    def add_student_window(self):
        add_window = tk.Toplevel(self.root)
        add_window.title("Add New Student")
        add_window.geometry("400x300")
        add_window.transient(self.root)
        add_window.grab_set()
        
        ttk.Label(add_window, text="Add New Student", 
                 font=('Arial', 14, 'bold')).grid(row=0, column=0, columnspan=2, pady=20)
        
        # Form fields
        fields = [
            ("First Name:", "name"),
            ("Last Name:", "last_name"),
            ("Set:", "set"),
            ("Student ID:", "id")
        ]
        
        entries = {}
        for i, (label, key) in enumerate(fields, 1):
            ttk.Label(add_window, text=label).grid(row=i, column=0, padx=10, pady=10, sticky=tk.W)
            entry = ttk.Entry(add_window, width=25, font=('Arial', 10))
            entry.grid(row=i, column=1, padx=10, pady=10)
            entries[key] = entry
        
        def submit_student():
            # Get values from entries
            name = entries['name'].get().strip()
            last_name = entries['last_name'].get().strip()
            student_set = entries['set'].get().strip()
            id_text = entries['id'].get().strip()
            
            # Validation
            if not all([name, last_name, student_set, id_text]):
                messagebox.showerror("Error", "All fields are required!")
                return
            
            try:
                student_id = int(id_text)
                
                # Check if ID already exists
                for student in self.student_list:
                    if student.id == student_id:
                        messagebox.showerror("Error", f"Student ID {student_id} already exists!")
                        return
                
                # Create new student
                new_student = StudentManagementSystem(name, last_name, student_set, student_id)
                self.student_list.append(new_student)
                self.refresh_student_list()
                self.update_status(f"Student '{name} {last_name}' added successfully!")
                add_window.destroy()
                
            except ValueError:
                messagebox.showerror("Error", "Student ID must be a number!")
        
        submit_btn = ttk.Button(add_window, text="Add Student", command=submit_student)
        submit_btn.grid(row=5, column=0, columnspan=2, pady=20)
        
        entries['name'].focus()

    def update_student_window(self):
        if not self.student_list:
            messagebox.showwarning("Warning", "No students in the system!")
            return
        
        update_window = tk.Toplevel(self.root)
        update_window.title("Update Student")
        update_window.geometry("400x350")
        update_window.transient(self.root)
        update_window.grab_set()
        
        ttk.Label(update_window, text="Update Student Information", 
                 font=('Arial', 14, 'bold')).grid(row=0, column=0, columnspan=2, pady=20)
        
        # Student selection
        ttk.Label(update_window, text="Select Student:").grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
        
        student_var = tk.StringVar()
        student_combo = ttk.Combobox(update_window, textvariable=student_var, state="readonly", width=30)
        student_combo['values'] = [f"{s.id} - {s.name} {s.last_name}" for s in self.student_list]
        student_combo.grid(row=1, column=1, padx=10, pady=10)
        
        # Update fields
        ttk.Label(update_window, text="New First Name:").grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
        name_entry = ttk.Entry(update_window, width=25, font=('Arial', 10))
        name_entry.grid(row=2, column=1, padx=10, pady=5)
        
        ttk.Label(update_window, text="New Last Name:").grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
        last_name_entry = ttk.Entry(update_window, width=25, font=('Arial', 10))
        last_name_entry.grid(row=3, column=1, padx=10, pady=5)
        
        ttk.Label(update_window, text="New Set:").grid(row=4, column=0, padx=10, pady=5, sticky=tk.W)
        set_entry = ttk.Entry(update_window, width=25, font=('Arial', 10))
        set_entry.grid(row=4, column=1, padx=10, pady=5)
        
        def update_student():
            selection = student_var.get()
            if not selection:
                messagebox.showwarning("Warning", "Please select a student!")
                return
            
            student_id = int(selection.split(' - ')[0])
            
            # Find student
            for student in self.student_list:
                if student.id == student_id:
                    new_name = name_entry.get().strip() or student.name
                    new_last_name = last_name_entry.get().strip() or student.last_name
                    new_set = set_entry.get().strip() or student.set
                    
                    # Update student
                    student.name = new_name
                    student.last_name = new_last_name
                    student.set = new_set
                    
                    self.refresh_student_list()
                    self.update_status(f"Student {student_id} updated successfully!")
                    update_window.destroy()
                    return
        
        update_btn = ttk.Button(update_window, text="Update Student", command=update_student)
        update_btn.grid(row=5, column=0, columnspan=2, pady=20)
        
        student_combo.focus()

    def delete_student(self):
        if not self.student_list:
            messagebox.showwarning("Warning", "No students in the system!")
            return
        
        selection = self.student_tree.selection()
        if not selection:
            messagebox.showwarning("Warning", "Please select a student from the list!")
            return
        
        item = selection[0]
        student_data = self.student_tree.item(item, 'values')
        student_id = int(student_data[0])
        student_name = f"{student_data[1]} {student_data[2]}"
        
        result = messagebox.askyesno("Confirm Delete", 
                                   f"Are you sure you want to delete student:\n{student_name} (ID: {student_id})?")
        
        if result:
            # Remove student from list
            self.student_list = [s for s in self.student_list if s.id != student_id]
            self.refresh_student_list()
            self.update_status(f"Student {student_name} deleted successfully!")

    def show_all_students(self):
        self.refresh_student_list()

    def clear_all(self):
        if not self.student_list:
            messagebox.showinfo("Info", "No students to clear!")
            return
        
        result = messagebox.askyesno("Confirm Clear", 
                                   "Are you sure you want to clear ALL students from the system?")
        
        if result:
            self.student_list.clear()
            self.refresh_student_list()
            self.update_status("All students cleared from the system!")

def main():
    root = tk.Tk()
    app = ManagementSystemGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()