from datetime import datetime
import re
import random

class MentalHealthChatbot:
    def __init__(self, db_manager):
        self.db_manager = db_manager
        self.current_user = None
        self.user_id = None
        
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
    
    def set_current_user(self, user_id, name):
        """Set the current user of the chatbot."""
        self.user_id = user_id
        self.current_user = name
    
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
                    responses = self.keyword_responses[f"{category}_responses"]
                    return random.choice(responses)
        
        # Positive sentiment response
        if sentiment == "positive":
            return random.choice(self.keyword_responses["positive_responses"])
        
        # Default response if no keywords matched
        default_responses = [
            "I'm here to listen. Can you tell me more about how you're feeling?",
            "Thank you for sharing. What's been on your mind lately?",
            "I want to understand better. Could you explain more about what you're experiencing?",
            "That sounds challenging. How has this been affecting you?"
        ]
        return random.choice(default_responses)
    
    def process_message(self, message):
        """Process a user message and return a response."""
        if not message:
            return ""
            
        # Analyze sentiment and detect crisis
        sentiment = self.analyze_sentiment(message)
        is_crisis = self.detect_crisis(message)
        
        # Generate response
        if is_crisis:
            response = self.handle_crisis()
        else:
            response = self.generate_response(message, sentiment)
        
        # Log conversation if we have a user
        if self.user_id:
            self.db_manager.log_conversation(self.user_id, message, response, sentiment)
        
        return response
    
    def get_emergency_contacts(self):
        """Return formatted emergency contact information."""
        return (
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