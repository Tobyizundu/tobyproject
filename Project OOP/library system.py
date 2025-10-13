import tkinter as tk
from tkinter import ttk, messagebox
import time

class Library_catalog:
    def __init__(self, title, author, id):
        self.title = title 
        self.author = author 
        self.id = id

    def output(self):
        return f'The book "{self.title}" by the author: {self.author} with the ID: {self.id}'
    
    def find(self):
        return f"User has searched for '{self.title}' by the author: {self.author}, with the book ID: {self.id}"

class LibrarySystemGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("National Library System")
        self.root.geometry("600x500")
        
        self.library_list = []
        
        self.main_frame = ttk.Frame(root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Welcome 
        welcome_label = ttk.Label(self.main_frame, 
                                text="Welcome to the National Library System", 
                                font=('Arial', 16, 'bold'))
        welcome_label.grid(row=0, column=0, columnspan=2, pady=10)
        
        # Create 
        self.create_buttons()
        
        # Creat
        self.create_output_area()
        
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.rowconfigure(4, weight=1)

    def create_buttons(self):
        button_frame = ttk.Frame(self.main_frame)
        button_frame.grid(row=1, column=0, columnspan=2, pady=10)
        
        self.add_btn = ttk.Button(button_frame, text="Add Book", 
                                 command=self.add_book_window)
        self.add_btn.grid(row=0, column=0, padx=5, pady=5)
        
        self.search_btn = ttk.Button(button_frame, text="Search Book", 
                                    command=self.search_book_window)
        self.search_btn.grid(row=0, column=1, padx=5, pady=5)
        
        self.availability_btn = ttk.Button(button_frame, text="Check Availability", 
                                          command=self.check_availability_window)
        self.availability_btn.grid(row=0, column=2, padx=5, pady=5)
        
        self.info_btn = ttk.Button(button_frame, text="Show All Books", 
                                  command=self.show_all_books)
        self.info_btn.grid(row=0, column=3, padx=5, pady=5)
        
        self.exit_btn = ttk.Button(button_frame, text="Exit", 
                                  command=self.root.quit)
        self.exit_btn.grid(row=0, column=4, padx=5, pady=5)

    def create_output_area(self):
        # Output label
        output_label = ttk.Label(self.main_frame, text="System Output:", 
                                font=('Arial', 12, 'bold'))
        output_label.grid(row=2, column=0, sticky=tk.W, pady=(10, 5))
        
        # Text widget for output with scrollbar
        text_frame = ttk.Frame(self.main_frame)
        text_frame.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)
        
        self.output_text = tk.Text(text_frame, height=15, width=70, wrap=tk.WORD)
        scrollbar = ttk.Scrollbar(text_frame, orient=tk.VERTICAL, command=self.output_text.yview)
        self.output_text.configure(yscrollcommand=scrollbar.set)
        
        self.output_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        
        text_frame.columnconfigure(0, weight=1)
        text_frame.rowconfigure(0, weight=1)

    def add_output(self, text):
        """Add text to the output area with timestamp"""
        timestamp = time.strftime("%H:%M:%S")
        self.output_text.insert(tk.END, f"[{timestamp}] {text}\n")
        self.output_text.see(tk.END)

    def clear_output(self):
        
        self.output_text.delete(1.0, tk.END)

    def add_book_window(self):
        
        add_window = tk.Toplevel(self.root)
        add_window.title("Add New Book")
        add_window.geometry("400x200")
        
        ttk.Label(add_window, text="Title:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        title_entry = ttk.Entry(add_window, width=30)
        title_entry.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(add_window, text="Author:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        author_entry = ttk.Entry(add_window, width=30)
        author_entry.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(add_window, text="ID:").grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        id_entry = ttk.Entry(add_window, width=30)
        id_entry.grid(row=2, column=1, padx=5, pady=5)
        
        def submit_book():
            title = title_entry.get().strip()
            author = author_entry.get().strip()
            id_text = id_entry.get().strip()
            
            if not title or not author or not id_text:
                messagebox.showerror("Error", "All fields are required!")
                return
            
            try:
                book_id = int(id_text)
                # Check if ID already exists
                for book in self.library_list:
                    if book.id == book_id:
                        messagebox.showerror("Error", f"Book ID {book_id} already exists!")
                        return
                
                # Add the book
                new_book = Library_catalog(title, author, book_id)
                self.library_list.append(new_book)
                self.add_output(f"Book '{title}' by {author} (ID: {book_id}) has been successfully added!")
                add_window.destroy()
                
            except ValueError:
                messagebox.showerror("Error", "ID must be a number!")
        
        submit_btn = ttk.Button(add_window, text="Add Book", command=submit_book)
        submit_btn.grid(row=3, column=0, columnspan=2, pady=10)
        
        # Set focus to first entry
        title_entry.focus()

    def search_book_window(self):
        """Create a new window for searching books"""
        search_window = tk.Toplevel(self.root)
        search_window.title("Search Book")
        search_window.geometry("400x150")
        
        ttk.Label(search_window, text="Enter title or author:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        search_entry = ttk.Entry(search_window, width=30)
        search_entry.grid(row=0, column=1, padx=5, pady=5)
        
        def perform_search():
            search_term = search_entry.get().strip().lower()
            if not search_term:
                messagebox.showwarning("Warning", "Please enter a search term!")
                return
            
            self.clear_output()
            self.add_output(f"Searching for: '{search_term}'")
            
            found_books = []
            for book in self.library_list:
                if search_term in book.title.lower() or search_term in book.author.lower():
                    found_books.append(book)
            
            if found_books:
                self.add_output(f"Found {len(found_books)} book(s):")
                for book in found_books:
                    self.add_output(f"  - {book.output()}")
            else:
                self.add_output("No books found matching your search.")
            
            search_window.destroy()
        
        search_btn = ttk.Button(search_window, text="Search", command=perform_search)
        search_btn.grid(row=1, column=0, columnspan=2, pady=10)
        
        search_entry.focus()

    def check_availability_window(self):
        """Create a new window for checking book availability"""
        availability_window = tk.Toplevel(self.root)
        availability_window.title("Check Book Availability")
        availability_window.geometry("400x150")
        
        ttk.Label(availability_window, text="Enter book ID:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        id_entry = ttk.Entry(availability_window, width=30)
        id_entry.grid(row=0, column=1, padx=5, pady=5)
        
        def check_availability():
            id_text = id_entry.get().strip()
            if not id_text:
                messagebox.showwarning("Warning", "Please enter a book ID!")
                return
            
            try:
                book_id = int(id_text)
                self.clear_output()
                self.add_output(f"Checking availability for book ID: {book_id}")
                
                found = False
                for book in self.library_list:
                    if book.id == book_id:
                        self.add_output(f"✓ Book is available: {book.output()}")
                        found = True
                        break
                
                if not found:
                    self.add_output("✗ Book is not available in the library.")
                
                availability_window.destroy()
                
            except ValueError:
                messagebox.showerror("Error", "ID must be a number!")
        
        check_btn = ttk.Button(availability_window, text="Check Availability", command=check_availability)
        check_btn.grid(row=1, column=0, columnspan=2, pady=10)
        
        id_entry.focus()

    def show_all_books(self):
        """Display all books in the library"""
        self.clear_output()
        if not self.library_list:
            self.add_output("No books in the library catalog.")
        else:
            self.add_output(f"Library Catalog - Total Books: {len(self.library_list)}")
            for i, book in enumerate(self.library_list, 1):
                self.add_output(f"{i}. {book.output()}")

def main():
    root = tk.Tk()
    app = LibrarySystemGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()