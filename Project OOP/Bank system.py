import tkinter as tk
from tkinter import ttk, messagebox
import time

class BankSystem:
    def __init__(self, account_name, account_number, balance):
        self.account_name = account_name
        self.account_number = account_number
        self.balance = balance

    def info(self):
        return f'User: {self.account_name}, Account Number: {self.account_number}, Balance: ${self.balance:.2f}'

class BankAccountGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Zenith Banking System - Bank of Africa")
        self.root.geometry("700x600")
        self.root.configure(bg='#f0f0f0')
        
        self.account_list = []
        self.current_account = None
        
        # Create main frame
        self.main_frame = ttk.Frame(root, padding="20")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Header
        header_label = ttk.Label(self.main_frame, 
                               text="Zenith Banking System\nBank of Africa", 
                               font=('Arial', 18, 'bold'),
                               foreground='#2c3e50',
                               justify=tk.CENTER)
        header_label.grid(row=0, column=0, columnspan=2, pady=20)
        
        # Create buttons frame
        self.create_buttons()
        
        # Create account selection frame
        self.create_account_selector()
        
        # Create output area
        self.create_output_area()
        
        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set("Welcome to Zenith Banking System")
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
        self.main_frame.rowconfigure(4, weight=1)

    def configure_styles(self):
        style = ttk.Style()
        style.configure('Header.TLabel', font=('Arial', 16, 'bold'))
        style.configure('Action.TButton', font=('Arial', 10, 'bold'))
        style.configure('Status.TLabel', font=('Arial', 9))

    def create_buttons(self):
        button_frame = ttk.Frame(self.main_frame)
        button_frame.grid(row=1, column=0, columnspan=2, pady=20)
        
        buttons = [
            ("Create Account", self.create_account_window),
            ("Deposit", self.deposit_window),
            ("Withdraw", self.withdraw_window),
            ("Check Balance", self.check_balance),
            ("Show All Accounts", self.show_all_accounts),
            ("Exit", self.root.quit)
        ]
        
        for i, (text, command) in enumerate(buttons):
            btn = ttk.Button(button_frame, text=text, command=command, style='Action.TButton')
            btn.grid(row=i//3, column=i%3, padx=10, pady=10, sticky='ew')
            button_frame.columnconfigure(i%3, weight=1)

    def create_account_selector(self):
        selector_frame = ttk.LabelFrame(self.main_frame, text="Account Selection", padding="10")
        selector_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=10)
        
        ttk.Label(selector_frame, text="Select Account:").grid(row=0, column=0, padx=5)
        
        self.account_var = tk.StringVar()
        self.account_combo = ttk.Combobox(selector_frame, textvariable=self.account_var, state="readonly")
        self.account_combo.grid(row=0, column=1, padx=5, sticky=(tk.W, tk.E))
        self.account_combo.bind('<<ComboboxSelected>>', self.on_account_selected)
        
        selector_frame.columnconfigure(1, weight=1)

    def create_output_area(self):
        output_frame = ttk.LabelFrame(self.main_frame, text="Transaction History", padding="10")
        output_frame.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=10)
        
        # Text widget with scrollbar
        self.output_text = tk.Text(output_frame, height=12, width=80, wrap=tk.WORD, 
                                  font=('Consolas', 10), bg='#f8f9fa')
        scrollbar = ttk.Scrollbar(output_frame, orient=tk.VERTICAL, command=self.output_text.yview)
        self.output_text.configure(yscrollcommand=scrollbar.set)
        
        self.output_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        
        output_frame.columnconfigure(0, weight=1)
        output_frame.rowconfigure(0, weight=1)

    def add_output(self, text):
        timestamp = time.strftime("%H:%M:%S")
        self.output_text.insert(tk.END, f"[{timestamp}] {text}\n")
        self.output_text.see(tk.END)
        self.status_var.set(text)

    def clear_output(self):
        self.output_text.delete(1.0, tk.END)

    def update_account_selector(self):
        accounts = [f"{acc.account_number} - {acc.account_name}" for acc in self.account_list]
        self.account_combo['values'] = accounts
        if accounts:
            self.account_combo.current(0)
            self.on_account_selected()

    def on_account_selected(self, event=None):
        selection = self.account_var.get()
        if selection:
            acc_number = int(selection.split(' - ')[0])
            for acc in self.account_list:
                if acc.account_number == acc_number:
                    self.current_account = acc
                    self.add_output(f"Selected account: {acc.account_name} ({acc.account_number})")
                    break

    def create_account_window(self):
        create_window = tk.Toplevel(self.root)
        create_window.title("Create New Account")
        create_window.geometry("400x300")
        create_window.transient(self.root)
        create_window.grab_set()
        
        ttk.Label(create_window, text="Create New Bank Account", 
                 font=('Arial', 14, 'bold')).grid(row=0, column=0, columnspan=2, pady=20)
        
        ttk.Label(create_window, text="Account Name:").grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
        name_entry = ttk.Entry(create_window, width=25, font=('Arial', 10))
        name_entry.grid(row=1, column=1, padx=10, pady=10)
        
        ttk.Label(create_window, text="Account Number:").grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
        number_entry = ttk.Entry(create_window, width=25, font=('Arial', 10))
        number_entry.grid(row=2, column=1, padx=10, pady=10)
        
        ttk.Label(create_window, text="Initial Balance:").grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)
        balance_entry = ttk.Entry(create_window, width=25, font=('Arial', 10))
        balance_entry.grid(row=3, column=1, padx=10, pady=10)
        
        def submit_account():
            name = name_entry.get().strip()
            number_text = number_entry.get().strip()
            balance_text = balance_entry.get().strip()
            
            if not name or not number_text or not balance_text:
                messagebox.showerror("Error", "All fields are required!")
                return
            
            try:
                number = int(number_text)
                balance = float(balance_text)
                
                # Check if account number already exists
                for acc in self.account_list:
                    if acc.account_number == number:
                        messagebox.showerror("Error", "Account number already exists!")
                        return
                
                if balance < 0:
                    messagebox.showerror("Error", "Initial balance cannot be negative!")
                    return
                
                # Create new account
                new_account = BankSystem(name, number, balance)
                self.account_list.append(new_account)
                self.update_account_selector()
                self.add_output(f"Account created successfully! {new_account.info()}")
                create_window.destroy()
                
            except ValueError:
                messagebox.showerror("Error", "Account number must be integer and balance must be number!")
        
        submit_btn = ttk.Button(create_window, text="Create Account", command=submit_account)
        submit_btn.grid(row=4, column=0, columnspan=2, pady=20)
        
        name_entry.focus()

    def deposit_window(self):
        if not self.current_account:
            messagebox.showwarning("Warning", "Please select an account first!")
            return
        
        deposit_window = tk.Toplevel(self.root)
        deposit_window.title("Deposit Money")
        deposit_window.geometry("350x200")
        deposit_window.transient(self.root)
        deposit_window.grab_set()
        
        ttk.Label(deposit_window, text=f"Deposit to: {self.current_account.account_name}",
                 font=('Arial', 12, 'bold')).grid(row=0, column=0, columnspan=2, pady=10)
        
        ttk.Label(deposit_window, text="Current Balance:").grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        ttk.Label(deposit_window, text=f"${self.current_account.balance:.2f}",
                 font=('Arial', 10, 'bold')).grid(row=1, column=1, padx=10, pady=5)
        
        ttk.Label(deposit_window, text="Deposit Amount:").grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
        amount_entry = ttk.Entry(deposit_window, width=20, font=('Arial', 10))
        amount_entry.grid(row=2, column=1, padx=10, pady=10)
        
        def process_deposit():
            amount_text = amount_entry.get().strip()
            if not amount_text:
                messagebox.showerror("Error", "Please enter deposit amount!")
                return
            
            try:
                amount = float(amount_text)
                if amount <= 0:
                    messagebox.showerror("Error", "Deposit amount must be positive!")
                    return
                
                self.current_account.balance += amount
                self.add_output(f"Deposited ${amount:.2f} to account {self.current_account.account_number}. New balance: ${self.current_account.balance:.2f}")
                deposit_window.destroy()
                
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid amount!")
        
        deposit_btn = ttk.Button(deposit_window, text="Deposit", command=process_deposit)
        deposit_btn.grid(row=3, column=0, columnspan=2, pady=10)
        
        amount_entry.focus()

    def withdraw_window(self):
        if not self.current_account:
            messagebox.showwarning("Warning", "Please select an account first!")
            return
        
        withdraw_window = tk.Toplevel(self.root)
        withdraw_window.title("Withdraw Money")
        withdraw_window.geometry("350x250")
        withdraw_window.transient(self.root)
        withdraw_window.grab_set()
        
        ttk.Label(withdraw_window, text=f"Withdraw from: {self.current_account.account_name}",
                 font=('Arial', 12, 'bold')).grid(row=0, column=0, columnspan=2, pady=10)
        
        ttk.Label(withdraw_window, text="Current Balance:").grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        ttk.Label(withdraw_window, text=f"${self.current_account.balance:.2f}",
                 font=('Arial', 10, 'bold')).grid(row=1, column=1, padx=10, pady=5)
        
        ttk.Label(withdraw_window, text="Withdraw Amount:").grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
        amount_entry = ttk.Entry(withdraw_window, width=20, font=('Arial', 10))
        amount_entry.grid(row=2, column=1, padx=10, pady=10)
        
        def process_withdraw():
            amount_text = amount_entry.get().strip()
            if not amount_text:
                messagebox.showerror("Error", "Please enter withdrawal amount!")
                return
            
            try:
                amount = float(amount_text)
                if amount <= 0:
                    messagebox.showerror("Error", "Withdrawal amount must be positive!")
                    return
                
                if amount > self.current_account.balance:
                    messagebox.showerror("Error", "Insufficient funds!")
                    return
                
                self.current_account.balance -= amount
                self.add_output(f"Withdrew ${amount:.2f} from account {self.current_account.account_number}. New balance: ${self.current_account.balance:.2f}")
                withdraw_window.destroy()
                
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid amount!")
        
        withdraw_btn = ttk.Button(withdraw_window, text="Withdraw", command=process_withdraw)
        withdraw_btn.grid(row=3, column=0, columnspan=2, pady=10)
        
        amount_entry.focus()

    def check_balance(self):
        if not self.current_account:
            messagebox.showwarning("Warning", "Please select an account first!")
            return
        
        self.clear_output()
        self.add_output(f"Account Balance for {self.current_account.account_name}:")
        self.add_output(f"  Account Number: {self.current_account.account_number}")
        self.add_output(f"  Current Balance: ${self.current_account.balance:.2f}")

    def show_all_accounts(self):
        self.clear_output()
        if not self.account_list:
            self.add_output("No accounts found in the system.")
        else:
            self.add_output(f"All Bank Accounts - Total: {len(self.account_list)}")
            for i, account in enumerate(self.account_list, 1):
                self.add_output(f"{i}. {account.info()}")

def main():
    root = tk.Tk()
    app = BankAccountGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()