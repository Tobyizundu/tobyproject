import tkinter as tk
from tkinter import messagebox, scrolledtext, Toplevel
from datetime import datetime  # Added this import
from database import DatabaseManager
from chatbot_backend import MentalHealthChatbot

class MentalHealthApp:
    def __init__(self):
        # Initialize database and chatbot
        self.db_manager = DatabaseManager()
        self.db_manager.initialize_database()
        self.chatbot = MentalHealthChatbot(self.db_manager)
        
        # Create main window
        self.root = tk.Tk()
        self.root.title("Student Mental Health Support")
        self.root.geometry("400x400")
        self.root.configure(bg="#f0f8ff")  # Alice blue background
        
        # Show welcome screen with login/signup options
        self.show_welcome_screen()
        
        # Start main loop
        self.root.mainloop()
    
    def show_welcome_screen(self):
        """Show the initial welcome screen with login and signup options."""
        self.clear_window()
        
        self.welcome_frame = tk.Frame(self.root, bg="#f0f8ff")
        self.welcome_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)
        
        # Title
        title_label = tk.Label(
            self.welcome_frame,
            text="Student Mental Health Support",
            font=("Helvetica", 20, "bold"),
            bg="#f0f8ff",
            fg="#2b5876"
        )
        title_label.pack(pady=20)
        
        # Subtitle
        subtitle_label = tk.Label(
            self.welcome_frame,
            text="Welcome to the confidential support chatbot",
            font=("Helvetica", 12),
            bg="#f0f8ff",
            fg="#4e4376"
        )
        subtitle_label.pack(pady=5)
        
        # Login button
        login_btn = tk.Button(
            self.welcome_frame,
            text="Login",
            font=("Helvetica", 14, "bold"),
            bg="#4b6cb7",
            fg="white",
            width=15,
            command=self.show_login_frame
        )
        login_btn.pack(pady=10)
        
        # Signup button
        signup_btn = tk.Button(
            self.welcome_frame,
            text="Sign Up",
            font=("Helvetica", 14, "bold"),
            bg="#2c3e50",
            fg="white",
            width=15,
            command=self.show_signup_frame
        )
        signup_btn.pack(pady=10)
        
        # Privacy notice
        privacy_label = tk.Label(
            self.welcome_frame,
            text="All conversations are confidential and anonymized.",
            font=("Helvetica", 8),
            bg="#f0f8ff",
            fg="#666666"
        )
        privacy_label.pack(side=tk.BOTTOM, pady=5)
    
    def show_login_frame(self):
        """Show the login interface."""
        self.clear_window()
        
        self.login_frame = tk.Frame(self.root, bg="#f0f8ff")
        self.login_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)
        
        # Title
        title_label = tk.Label(
            self.login_frame,
            text="Login",
            font=("Helvetica", 24, "bold"),
            bg="#f0f8ff",
            fg="#2b5876"
        )
        title_label.pack(pady=10)
        
        # Student ID entry
        id_frame = tk.Frame(self.login_frame, bg="#f0f8ff")
        id_frame.pack(pady=5)
        tk.Label(
            id_frame,
            text="Student ID:",
            font=("Helvetica", 12),
            bg="#f0f8ff"
        ).pack(side=tk.LEFT)
        self.login_id_entry = tk.Entry(
            id_frame,
            font=("Helvetica", 12),
            width=25
        )
        self.login_id_entry.pack(side=tk.LEFT, padx=5)
        
        # Password entry
        password_frame = tk.Frame(self.login_frame, bg="#f0f8ff")
        password_frame.pack(pady=5)
        tk.Label(
            password_frame,
            text="Password:",
            font=("Helvetica", 12),
            bg="#f0f8ff"
        ).pack(side=tk.LEFT)
        self.login_password_entry = tk.Entry(
            password_frame,
            font=("Helvetica", 12),
            width=25,
            show="*"
        )
        self.login_password_entry.pack(side=tk.LEFT, padx=5)
        
        # Login button
        login_btn = tk.Button(
            self.login_frame,
            text="Login",
            font=("Helvetica", 14, "bold"),
            bg="#4b6cb7",
            fg="white",
            command=self.handle_login
        )
        login_btn.pack(pady=20)

        # Back button
        back_btn = tk.Button(
            self.login_frame,
            text="Back",
            font=("Helvetica", 10),
            bg="#95a5a6",
            fg="white",
            command=self.show_welcome_screen
        )
        back_btn.pack(pady=5)
    
    def show_signup_frame(self):
        """Show the signup interface."""
        self.clear_window()
        
        self.signup_frame = tk.Frame(self.root, bg="#f0f8ff")
        self.signup_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)
        
        # Title
        title_label = tk.Label(
            self.signup_frame,
            text="Sign Up",
            font=("Helvetica", 24, "bold"),
            bg="#f0f8ff",
            fg="#2b5876"
        )
        title_label.pack(pady=10)
        
        # Name entry
        name_frame = tk.Frame(self.signup_frame, bg="#f0f8ff")
        name_frame.pack(pady=5)
        tk.Label(
            name_frame,
            text="Full Name:",
            font=("Helvetica", 12),
            bg="#f0f8ff"
        ).pack(side=tk.LEFT)
        self.signup_name_entry = tk.Entry(
            name_frame,
            font=("Helvetica", 12),
            width=25
        )
        self.signup_name_entry.pack(side=tk.LEFT, padx=5)
        
        # Student ID entry
        id_frame = tk.Frame(self.signup_frame, bg="#f0f8ff")
        id_frame.pack(pady=5)
        tk.Label(
            id_frame,
            text="Student ID:",
            font=("Helvetica", 12),
            bg="#f0f8ff"
        ).pack(side=tk.LEFT)
        self.signup_id_entry = tk.Entry(
            id_frame,
            font=("Helvetica", 12),
            width=25
        )
        self.signup_id_entry.pack(side=tk.LEFT, padx=5)
        
        # Password entry
        password_frame = tk.Frame(self.signup_frame, bg="#f0f8ff")
        password_frame.pack(pady=5)
        tk.Label(
            password_frame,
            text="Password:",
            font=("Helvetica", 12),
            bg="#f0f8ff"
        ).pack(side=tk.LEFT)
        self.signup_password_entry = tk.Entry(
            password_frame,
            font=("Helvetica", 12),
            width=25,
            show="*"
        )
        self.signup_password_entry.pack(side=tk.LEFT, padx=5)
        
        # Confirm Password entry
        confirm_frame = tk.Frame(self.signup_frame, bg="#f0f8ff")
        confirm_frame.pack(pady=5)
        tk.Label(
            confirm_frame,
            text="Confirm Password:",
            font=("Helvetica", 12),
            bg="#f0f8ff"
        ).pack(side=tk.LEFT)
        self.signup_confirm_entry = tk.Entry(
            confirm_frame,
            font=("Helvetica", 12),
            width=25,
            show="*"
        )
        self.signup_confirm_entry.pack(side=tk.LEFT, padx=5)




    def show_forgot_password_frame(self):
        """Show the forgot password interface"""
        self.clear_window()
        
        self.forgot_frame = tk.Frame(self.root, bg="#f0f8ff")
        self.forgot_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)


        # In the show_login_frame method, add this after the back button:

        # Forgot password link
        forgot_link = tk.Label(
            self.login_frame,
            text="Forgot Password?",
            font=("Helvetica", 10, "underline"),
            bg="#f0f8ff",
            fg="#3498db",
            cursor="hand2"
        )
        forgot_link.pack(pady=5)
        forgot_link.bind("<Button-1>", lambda e: self.show_forgot_password_frame())
        
        # Title
        title_label = tk.Label(
            self.forgot_frame,
            text="Reset Password",
            font=("Helvetica", 24, "bold"),
            bg="#f0f8ff",
            fg="#2b5876"
        )
        title_label.pack(pady=10)
        
        # Student ID entry
        id_frame = tk.Frame(self.forgot_frame, bg="#f0f8ff")
        id_frame.pack(pady=5)
        tk.Label(
            id_frame,
            text="Student ID:",
            font=("Helvetica", 12),
            bg="#f0f8ff"
        ).pack(side=tk.LEFT)
        self.forgot_id_entry = tk.Entry(
            id_frame,
            font=("Helvetica", 12),
            width=25
        )
        self.forgot_id_entry.pack(side=tk.LEFT, padx=5)
        
        # New Password entry
        new_pass_frame = tk.Frame(self.forgot_frame, bg="#f0f8ff")
        new_pass_frame.pack(pady=5)
        tk.Label(
            new_pass_frame,
            text="New Password:",
            font=("Helvetica", 12),
            bg="#f0f8ff"
        ).pack(side=tk.LEFT)
        self.new_pass_entry = tk.Entry(
            new_pass_frame,
            font=("Helvetica", 12),
            width=25,
            show="*"
        )
        self.new_pass_entry.pack(side=tk.LEFT, padx=5)
        
        # Confirm New Password entry
        confirm_frame = tk.Frame(self.forgot_frame, bg="#f0f8ff")
        confirm_frame.pack(pady=5)
        tk.Label(
            confirm_frame,
            text="Confirm Password:",
            font=("Helvetica", 12),
            bg="#f0f8ff"
        ).pack(side=tk.LEFT)
        self.confirm_pass_entry = tk.Entry(
            confirm_frame,
            font=("Helvetica", 12),
            width=25,
            show="*"
        )
        self.confirm_pass_entry.pack(side=tk.LEFT, padx=5)
        
        # Reset button
        reset_btn = tk.Button(
            self.forgot_frame,
            text="Reset Password",
            font=("Helvetica", 14, "bold"),
            bg="#4b6cb7",
            fg="white",
            command=self.handle_password_reset
        )
        reset_btn.pack(pady=20)

        # Back button
        back_btn = tk.Button(
            self.forgot_frame,
            text="Back to Login",
            font=("Helvetica", 10),
            bg="#95a5a6",
            fg="white",
            command=self.show_login_frame
        )
        back_btn.pack(pady=5)
    
    def handle_password_reset(self):
        """Handle the password reset process"""
        student_id = self.forgot_id_entry.get().strip()
        new_password = self.new_pass_entry.get()
        confirm_password = self.confirm_pass_entry.get()
        
        # Validate inputs
        if not student_id or not new_password or not confirm_password:
            messagebox.showerror("Error", "All fields are required.")
            return
        
        if not (student_id.isdigit() and len(student_id) == 8 and student_id.startswith("28")):
            messagebox.showerror("Error", "Invalid student ID. Must be 8 digits starting with '28'.")
            return
        
        if len(new_password) < 6:
            messagebox.showerror("Error", "Password must be at least 6 characters.")
            return
        
        if new_password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match.")
            return
        
        # Check if user exists
        if not self.db_manager.check_user_exists(student_id):
            messagebox.showerror("Error", "No account found with this student ID.")
            return
        
        # Update password 
        if self.db_manager.update_password(student_id, new_password):
            messagebox.showinfo("Success", "Password updated successfully! Please login with your new password.")
            self.show_login_frame()
        else:
            messagebox.showerror("Error", "Failed to update password. Please try again.")





        
        # Terms checkbox
        self.terms_var = tk.BooleanVar()
        terms_check = tk.Checkbutton(
            self.signup_frame,
            text="I agree to the Terms and Conditions",
            variable=self.terms_var,
            bg="#f0f8ff",
            font=("Helvetica", 10),
            command=self.show_terms
        )
        terms_check.pack(pady=10)
        
        # Signup button
        signup_btn = tk.Button(
            self.signup_frame,
            text="Sign Up",
            font=("Helvetica", 14, "bold"),
            bg="#4b6cb7",
            fg="white",
            command=self.handle_signup
        )
        signup_btn.pack(pady=10)
        
        # Back button
        back_btn = tk.Button(
            self.signup_frame,
            text="Back",
            font=("Helvetica", 10),
            bg="#95a5a6",
            fg="white",
            command=self.show_welcome_screen
        )
        back_btn.pack(pady=5)
    
    def show_terms(self):
        """Show terms and conditions in a new window."""
        if hasattr(self, 'terms_window') and self.terms_window.winfo_exists():
            return
            
        self.terms_window = Toplevel(self.root)
        self.terms_window.title("Terms and Conditions")
        self.terms_window.geometry("500x400")
        
        terms_text = """
        TERMS AND CONDITIONS FOR MENTAL HEALTH CHATBOT
        
        1. CONFIDENTIALITY
        - All conversations with the chatbot are confidential.
        - However, if we believe you or someone else is at risk of harm, we may need to contact appropriate services.
        
        2. DATA USAGE
        - Your data will be stored securely and used only to provide support services.
        - Conversations are anonymized for research and improvement purposes.
        
        3. LIMITATIONS
        - This chatbot is not a substitute for professional mental health care.
        - In emergencies, please contact local emergency services.
        
        4. ACCEPTABLE USE
        - You agree to use this service respectfully and not for harmful purposes.
        - Misuse may result in account termination.
        
        5. CONSENT
        - By using this service, you confirm you are a student at this institution.
        - You understand the limitations of automated support.
        
        Last updated: """ + datetime.now().strftime("%Y-%m-%d")
        
        text_widget = scrolledtext.ScrolledText(
            self.terms_window,
            wrap=tk.WORD,
            font=("Helvetica", 10)
        )
        text_widget.insert(tk.INSERT, terms_text)
        text_widget.config(state=tk.DISABLED)
        text_widget.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)
        
        close_btn = tk.Button(
            self.terms_window,
            text="I Understand",
            command=self.terms_window.destroy
        )
        close_btn.pack(pady=5)
    
    def clear_window(self):
        """Clear all widgets from the root window."""
        for widget in self.root.winfo_children():
            widget.destroy()
    
    def handle_signup(self):
        """Handle the signup process."""
        name = self.signup_name_entry.get().strip()
        student_id = self.signup_id_entry.get().strip()
        password = self.signup_password_entry.get()
        confirm_password = self.signup_confirm_entry.get()
        
        # Validate inputs
        if not all([name, student_id, password, confirm_password]):
            messagebox.showerror("Error", "All fields are required.")
            return
        
        if not (student_id.isdigit() and len(student_id) == 8 and student_id.startswith("28")):
            messagebox.showerror("Error", "Invalid student ID. Must be 8 digits starting with '28'.")
            return
        
        if len(password) < 6:
            messagebox.showerror("Error", "Password must be at least 6 characters.")
            return
        
        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match.")
            return
        
        if not self.terms_var.get():
            messagebox.showerror("Error", "You must agree to the Terms and Conditions.")
            return
        
        # Check if user already exists
        existing_user = self.db_manager.get_user(student_id)
        if existing_user:
            messagebox.showerror("Error", "An account with this student ID already exists.")
            return
        
        # Create user (in a real app, use proper password hashing)
        user_id = self.db_manager.create_user(student_id, name, password)
        if user_id:
            messagebox.showinfo("Success", "Account created successfully! Please login.")
            self.show_login_frame()
    
    def handle_login(self):
        """Handle the login process."""
        student_id = self.login_id_entry.get().strip()
        password = self.login_password_entry.get()
        
        # Validate inputs
        if not student_id or not password:
            messagebox.showerror("Error", "Please enter both student ID and password.")
            return
        
        # Check credentials
        user_data = self.db_manager.get_user(student_id)
        
        if not user_data:
            messagebox.showerror("Error", "Student ID not found. Please sign up first.")
            return
        
        user_id, name, stored_password = user_data
        
        # In production, use proper password verification with hashing
        if password != stored_password:
            messagebox.showerror("Error", "Incorrect password.")
            return
        
        # Update last login time
        self.db_manager.update_last_login(user_id)
        
        # Set current user in chatbot
        self.chatbot.set_current_user(user_id, name)
        
        # Proceed to main menu
        self.show_main_menu()
    
    def show_main_menu(self):
        """Show the main menu after successful login."""
        self.clear_window()
        
        self.menu_frame = tk.Frame(self.root, bg="#f0f8ff")
        self.menu_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)
        
        # Welcome message
        welcome_label = tk.Label(
            self.menu_frame,
            text=f"Welcome, {self.chatbot.current_user}!",
            font=("Helvetica", 20, "bold"),
            bg="#f0f8ff",
            fg="#2b5876"
        )
        welcome_label.pack(pady=10)
        
        # Instructions
        instr_label = tk.Label(
            self.menu_frame,
            text="How can we support you today?",
            font=("Helvetica", 12),
            bg="#f0f8ff"
        )
        instr_label.pack(pady=10)
        
        # Support options
        options = [
            ("Academic Stress", "#4b6cb7"),
            ("Financial Worries", "#4b6cb7"),
            ("Anxiety", "#4b6cb7"),
            ("Low Mood", "#4b6cb7"),
            ("Loneliness", "#4b6cb7"),
            ("Sleep Issues", "#4b6cb7"),
            ("Just need to talk", "#4b6cb7")
        ]
        
        for text, color in options:
            btn = tk.Button(
                self.menu_frame,
                text=text,
                font=("Helvetica", 12),
                bg=color,
                fg="white",
                width=20,
                command=lambda t=text: self.start_chat(t)
            )
            btn.pack(pady=5)
        
        # Logout button
        logout_btn = tk.Button(
            self.menu_frame,
            text="Logout",
            font=("Helvetica", 12, "bold"),
            bg="#e74c3c",
            fg="white",
            command=self.logout
        )
        logout_btn.pack(pady=20)
    
    def logout(self):
        """Log out the user and return to welcome screen."""
        self.chatbot.set_current_user(None, None)
        self.show_welcome_screen()
    
    def start_chat(self, topic):
        """Start a chat session about the selected topic."""
        self.clear_window()
        
        self.chat_frame = tk.Frame(self.root, bg="#f0f8ff")
        self.chat_frame.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)
        
        # Chat header
        header_frame = tk.Frame(self.chat_frame, bg="#f0f8ff")
        header_frame.pack(fill=tk.X, pady=5)
        
        tk.Label(
            header_frame,
            text=f"Chat: {topic}",
            font=("Helvetica", 16, "bold"),
            bg="#f0f8ff",
            fg="#2b5876"
        ).pack(side=tk.LEFT)
        
        # Back button
        tk.Button(
            header_frame,
            text="Back to Menu",
            font=("Helvetica", 10),
            bg="#4b6cb7",
            fg="white",
            command=self.show_main_menu
        ).pack(side=tk.RIGHT)
        
        # Chat display
        self.chat_display = scrolledtext.ScrolledText(
            self.chat_frame,
            font=("Helvetica", 12),
            wrap=tk.WORD,
            width=50,
            height=15,
            state=tk.DISABLED
        )
        self.chat_display.pack(pady=10, padx=5, fill=tk.BOTH, expand=True)
        
        # Configure tags for different message types
        self.chat_display.tag_config("user", foreground="#2c3e50")
        self.chat_display.tag_config("bot", foreground="#2980b9")
        self.chat_display.tag_config("crisis", foreground="red")
        
        # Welcome message
        self.add_bot_message(f"Hello {self.chatbot.current_user}! You've selected '{topic}'. How can I help you today?")
        
        # Input area
        input_frame = tk.Frame(self.chat_frame, bg="#f0f8ff")
        input_frame.pack(fill=tk.X, pady=10)
        
        self.user_input = tk.Entry(
            input_frame,
            font=("Helvetica", 12),
            width=40
        )
        self.user_input.pack(side=tk.LEFT, padx=5)
        self.user_input.bind("<Return>", lambda e: self.process_user_message())
        
        send_btn = tk.Button(
            input_frame,
            text="Send",
            font=("Helvetica", 12),
            bg="#4b6cb7",
            fg="white",
            command=self.process_user_message
        )
        send_btn.pack(side=tk.LEFT)
        
        # Emergency button
        tk.Button(
            self.chat_frame,
            text="Emergency Help",
            font=("Helvetica", 10, "bold"),
            bg="#e74c3c",
            fg="white",
            command=self.show_emergency_help
        ).pack(side=tk.BOTTOM, pady=5)
    
    def add_user_message(self, message):
        """Add a user message to the chat display."""
        self.chat_display.config(state=tk.NORMAL)
        self.chat_display.insert(tk.END, f"You: {message}\n", "user")
        self.chat_display.config(state=tk.DISABLED)
        self.chat_display.see(tk.END)
    
    def add_bot_message(self, message, crisis=False):
        """Add a bot message to the chat display."""
        self.chat_display.config(state=tk.NORMAL)
        tag = "crisis" if crisis else "bot"
        self.chat_display.insert(tk.END, f"Chatbot: {message}\n", tag)
        self.chat_display.config(state=tk.DISABLED)
        self.chat_display.see(tk.END)
    
    def process_user_message(self):
        """Process the user's message and generate a response."""
        message = self.user_input.get().strip()
        if not message:
            return
        
        # Add user message to chat
        self.add_user_message(message)
        self.user_input.delete(0, tk.END)
        
        # Get response from chatbot
        response = self.chatbot.process_message(message)
        
        # Check if this is a crisis response
        is_crisis = self.chatbot.detect_crisis(message)
        
        # Add bot response
        self.add_bot_message(response, is_crisis)
    
    def show_emergency_help(self):
        """Show emergency contact information."""
        emergency_info = self.chatbot.get_emergency_contacts()
        messagebox.showinfo("Emergency Help", emergency_info)

if __name__ == "__main__":
    app = MentalHealthApp()