from models.db import get_db

class User:
    @staticmethod
    def find_by_email(email):
        db = get_db()
        return db.users.find_one({"email": email})

    @staticmethod
    def create(user_data):
        db = get_db()
        return db.users.insert_one(user_data)
