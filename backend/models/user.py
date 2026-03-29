from mongoengine import Document, StringField, EmailField, ListField, DateTimeField
from datetime import datetime

class User(Document):
    username = StringField(required=True, unique=True)
    email = EmailField(required=True, unique=True)
    password_hash = StringField(required=True)
    preferences = ListField(StringField(), default=[])  # To store user preferences
    created_at = DateTimeField(default=datetime.utcnow)
    updated_at = DateTimeField(default=datetime.utcnow)

    meta = {'collection': 'users'}
    
    def __str__(self):
        return self.username
    
    def set_password(self, password):
        # Logic to hash password
        pass
    
    def check_password(self, password):
        # Logic to check hashed password
        pass
