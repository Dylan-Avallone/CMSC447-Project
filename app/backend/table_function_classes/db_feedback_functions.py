from app.backend.db import DB
from app.backend.table_object_classes.feedback import Feedback
from app.backend.table_object_classes.user import User

class DBFeedbackFunctions:
    def __init__(self, db_:DB):
        self.db = db_

    def add_feedback(self, feedback:Feedback):
        command = "INSERT INTO FeedbackForms (form_type, form_content) VALUES (?, ?)"
        params = (feedback.type, feedback.content)
        self.db.execute_command(command, params)

    def get_last_feedback(self, user:User):
        pass