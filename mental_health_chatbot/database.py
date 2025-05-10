import tkinter as tk
from tkinter import messagebox, scrolledtext, Toplevel
import sqlite3
from datetime import datetime
import re

class MentalHealthChatbot:
    def __init__(self):
        # Initialize database
        self.init_db()
        
        # Keywords and responses
        self.keyword_responses = {
            # Academic stress
            "academic": ["exam", "study", "assignment", "grade", "fail", "pass", "test"],
            "academic_responses": [
                "It's normal to feel stressed about academics. Have you tried breaking your work into smaller tasks?",
                "Many students find the Pomodoro technique helpful - 25 minutes of focused work followed by a 5-minute break.",
                "Remember that your worth isn't defined by your grades. You're more than your academic performance."
            ],
            
            # Financial stress
            "financial": ["money", "rent", "tuition", "loan", "broke", "expensive", "cost"],
            "financial_responses": [
                "Financial stress is common among students. Have you checked with the university's financial aid office?",
                "Many universities offer emergency grants or food banks for students in need.",
                "Creating a budget can help you feel more in control of your finances."
            ],
            
            # Anxiety
            "anxiety": ["anxious", "worry", "nervous", "panic", "overwhelm", "scared", "fear"],
            "anxiety_responses": [
                "Anxiety can feel overwhelming. Try taking slow, deep breaths - in for 4 counts, hold for 4, out for 6.",
                "Grounding techniques can help with anxiety. Try naming 5 things you can see, 4 you can touch, 3 you can hear, 2 you can smell, and 1 you can taste.",
                "Remember that anxiety is temporary, even when it doesn't feel that way."
            ],
            
            # Depression
            "depression": ["depressed", "sad", "hopeless", "empty", "numb", "worthless", "useless"],
            "depression_responses": [
                "I'm sorry you're feeling this way. You're not alone in this.",
                "Even small steps like getting out of bed or showering are victories when you're feeling depressed.",
                "Would you like me to help you connect with counseling services?"
            ],
            
            # Loneliness
            "loneliness": ["lonely", "alone", "isolated", "friendless", "left out", "excluded"],
            "loneliness_responses": [
                "Many students feel lonely when they first arrive at university. It often gets better with time.",
                "Joining clubs or societies can be a great way to meet people with similar interests.",
                "Would you like some suggestions for social activities happening on campus?"
            ],
            
            # Sleep issues
            "sleep": ["tired", "sleep", "insomnia", "exhausted", "awake", "restless"],
            "sleep_responses": [
                "Poor sleep can really affect your mood and studies. Try maintaining a consistent sleep schedule.",
                "Avoid screens for at least an hour before bed, and try relaxation techniques like reading or light stretching.",
                "The university health center may be able to help if sleep problems persist."
            ],
            
            # Crisis keywords (will trigger emergency protocol)
            "crisis": ["suicide", "kill myself", "end it all", "want to die", "harm myself", "self-harm"],
            
            # Positive sentiment
            "positive": ["happy", "good", "great", "better", "improve", "progress", "excited"],
            "positive_responses": [
                "I'm glad to hear you're feeling positive!",
                "That's wonderful news!",
                "It's great to hear you're doing well."
            ]
        }
        
        # Create main window
        self.root = tk.Tk()
        self.root.title("Student Mental Health Support")
        self.root.geometry("400x400")
        self.root.configure(bg="#f0f8ff")  # Alice blue background
        
        # Show welcome screen with login/signup options
        self.show_welcome_screen()
        
        # Start main loop
        self.root.mainloop()
    
    def init_db(self):
        """Initialize the SQLite database for user accounts and conversations."""
        self.conn = sqlite3.connect('mental_health_chatbot.db')
        self.cursor = self.conn.cursor()
        
        # Create users table if it doesn't exist
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id TEXT UNIQUE,
                name TEXT,
                password TEXT,
                terms_accepted BOOLEAN,
                registration_date TEXT,
                last_login TEXT
            )
        ''')
        
        # Create conversations table if it doesn't exist
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS conversations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                timestamp TEXT,
                user_message TEXT,
                bot_response TEXT,
                sentiment TEXT,
                FOREIGN KEY(user_id) REFERENCES users(id)
            )
        ''')
        
        self.conn.commit()
    
    def show_welcome_screen(self):
        """Show the initial welcome screen with login and signup options."""
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
        self.welcome_frame.destroy()
        
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
            command=self.back_to_welcome
        )
        back_btn.pack(pady=5)
    

    
    
    def show_signup_frame(self):
        """Show the signup interface."""
        self.welcome_frame.destroy()
        
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
            command=self.back_to_welcome
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
    
    def back_to_welcome(self):
        """Return to the welcome screen."""
        if hasattr(self, 'login_frame'):
            self.login_frame.destroy()
        if hasattr(self, 'signup_frame'):
            self.signup_frame.destroy()
        self.show_welcome_screen()
    
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
        self.cursor.execute("SELECT id FROM users WHERE student_id = ?", (student_id,))
        if self.cursor.fetchone():
            messagebox.showerror("Error", "An account with this student ID already exists.")
            return
        
        # Hash password (in a real app, use proper hashing like bcrypt)
        hashed_password = password  # In production, replace with actual hashing
        
        # Insert new user with all required fields
        try:
            self.cursor.execute(
                "INSERT INTO users (student_id, name, password, terms_accepted, registration_date, last_login) VALUES (?, ?, ?, ?, ?, ?)",
                (student_id, name, hashed_password, True, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
            self.conn.commit()
            messagebox.showinfo("Success", "Account created successfully! Please login.")
            self.signup_frame.destroy()
            self.show_login_frame()
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Database error: {e}")
    
    def handle_login(self):
        """Handle the login process."""
        student_id = self.login_id_entry.get().strip()
        password = self.login_password_entry.get()
        
        # Validate inputs
        if not student_id or not password:
            messagebox.showerror("Error", "Please enter both student ID and password.")
            return
        
        # Check credentials
        self.cursor.execute(
            "SELECT id, name, password FROM users WHERE student_id = ?",
            (student_id,)
        )
        user_data = self.cursor.fetchone()
        
        if not user_data:
            messagebox.showerror("Error", "Student ID not found. Please sign up first.")
            return
        
        user_id, name, stored_password = user_data
        
        # In production, use proper password verification with hashing
        if password != stored_password:
            messagebox.showerror("Error", "Incorrect password.")
            return
        
        # Update last login time
        self.cursor.execute(
            "UPDATE users SET last_login = ? WHERE id = ?",
            (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), user_id)
        )
        self.conn.commit()
        
        # Store user info and proceed to main menu
        self.user_id = user_id
        self.current_user = name
        self.login_frame.destroy()
        self.create_main_menu()
    
    def create_main_menu(self):
        """Create the main menu with support options."""
        self.menu_frame = tk.Frame(self.root, bg="#f0f8ff")
        self.menu_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)
        
        # Welcome message
        welcome_label = tk.Label(
            self.menu_frame,
            text=f"Welcome, {self.current_user}!",
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


    def check_user_exists(self, student_id):
        """Check if a user exists with the given student ID"""
        self.cursor.execute("SELECT id FROM users WHERE student_id = ?", (student_id,))
        return self.cursor.fetchone() is not None

    def update_password(self, student_id, new_password):
        """Update a user's password"""
        try:
            self.cursor.execute(
                "UPDATE users SET password = ? WHERE student_id = ?",
                (new_password, student_id)
            )
            self.conn.commit()
            return True
        except sqlite3.Error:
            return False





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
        self.menu_frame.destroy()
        self.show_welcome_screen()
    
    def start_chat(self, topic):
        """Start a chat session about the selected topic."""
        self.menu_frame.destroy()
        
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
            command=self.back_to_menu
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
        self.add_bot_message(f"Hello {self.current_user}! You've selected '{topic}'. How can I help you today?")
        
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
    
    def back_to_menu(self):
        """Return to the main menu."""
        self.chat_frame.destroy()
        self.create_main_menu()
    
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
        
        # Analyze sentiment and detect crisis
        sentiment = self.analyze_sentiment(message)
        is_crisis = self.detect_crisis(message)
        
        # Generate response
        if is_crisis:
            response = self.handle_crisis()
        else:
            response = self.generate_response(message, sentiment)
        
        # Add bot response
        self.add_bot_message(response, is_crisis)
        
        # Log conversation
        self.log_conversation(message, response, sentiment)
    
    def analyze_sentiment(self, message):
        """Basic sentiment analysis using keyword matching."""
        message_lower = message.lower()
        
        # Check for positive words
        for word in self.keyword_responses["positive"]:
            if word in message_lower:
                return "positive"
        
        # Check for negative words in each category
        negative_categories = ["academic", "financial", "anxiety", "depression", "loneliness", "sleep"]
        for category in negative_categories:
            for word in self.keyword_responses[category]:
                if word in message_lower:
                    return "negative"
        
        return "neutral"
    
    def detect_crisis(self, message):
        """Check for crisis keywords in the message."""
        message_lower = message.lower()
        for word in self.keyword_responses["crisis"]:
            if word in message_lower:
                return True
        return False
    
    def handle_crisis(self):
        """Handle crisis situations with appropriate response."""
        # University counseling service info
        uni_help = "\nUniversity Counseling Service:\nPhone: 0800 123 4567\nEmail: counselling@university.edu\n24/7 available"
        
        # National helplines
        national_help = (
            "\n\nFor immediate help, contact:\n"
            "Samaritans: 116 123 (UK)\n"
            "National Suicide Prevention Lifeline: 988 (US)\n"
            "Crisis Text Line: Text HOME to 741741 (US/UK)"
        )
        
        return (
            "I'm concerned about what you've shared. Your feelings matter and help is available. "
            f"{uni_help}"
            f"{national_help}"
            "\n\nYou're not alone in this. Would you like me to help you connect with someone now?"
        )
    
    def generate_response(self, message, sentiment):
        """Generate an appropriate response based on the message content and sentiment."""
        message_lower = message.lower()
        
        # Check each category for matching keywords
        for category in ["academic", "financial", "anxiety", "depression", "loneliness", "sleep"]:
            for word in self.keyword_responses[category]:
                if word in message_lower:
                    # Return a random response from the appropriate category
                    import random
                    responses = self.keyword_responses[f"{category}_responses"]
                    return random.choice(responses)
        
        # Positive sentiment response
        if sentiment == "positive":
            import random
            return random.choice(self.keyword_responses["positive_responses"])
        
        # Default response if no keywords matched
        default_responses = [
            "I'm here to listen. Can you tell me more about how you're feeling?",
            "Thank you for sharing. What's been on your mind lately?",
            "I want to understand better. Could you explain more about what you're experiencing?",
            "That sounds challenging. How has this been affecting you?"
        ]
        import random
        return random.choice(default_responses)
    
    def log_conversation(self, user_message, bot_response, sentiment):
        """Log the conversation to the database."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        self.cursor.execute(
            "INSERT INTO conversations (user_id, timestamp, user_message, bot_response, sentiment) VALUES (?, ?, ?, ?, ?)",
            (self.user_id, timestamp, user_message, bot_response, sentiment)
        )
        self.conn.commit()
    
    def show_emergency_help(self):
        """Show emergency contact information."""
        emergency_info = (
            "Emergency Contacts:\n\n"
            "University Counseling Service:\n"
            "Phone: 0800 123 4567\n"
            "Email: counselling@university.edu\n"
            "Open: Mon-Fri 9am-5pm\n\n"
            "24/7 Helplines:\n"
            "Samaritans: 116 123 (UK)\n"
            "National Suicide Prevention Lifeline: 988 (US)\n"
            "Crisis Text Line: Text HOME to 741741 (US/UK)\n\n"
            "In immediate danger? Call 999 (UK) or 911 (US)"
        )
        
        messagebox.showinfo("Emergency Help", emergency_info)

if __name__ == "__main__":
    chatbot = MentalHealthChatbot()