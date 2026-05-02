from app.backend.db import DB
from app.backend.table_object_classes.feedback import Feedback
from app.backend.table_object_classes.user import User

class DBFeedbackFunctions:
    def __init__(self, db_:DB):
        self.db = db_

    def add_feedback(self, feedback:Feedback):
        """
        Takes a feedback object and adds it to the database.
        """
        query = "INSERT INTO FeedbackForms (form_type, form_content) VALUES (?, ?)"
        params = (feedback.type, feedback.content)
        self.db.execute_command(query, params)

    def get_last_feedback(self, user:User):
        """
        Given a User object, searches the database and returns the Feedback object with the most recent timestamp.
        """
        query = "SELECT * FROM FeedbackForms WHERE user_id = ? ORDER BY timestamp DESC LIMIT 1"
        params = (user.id,)
        return self.db.get_one(query, params)