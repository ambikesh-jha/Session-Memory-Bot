from flask import session
from uuid import uuid4

def get_session_id():
    if "session_id" not in session:
        session["session_id"] = str(uuid4())  # Generate a unique session ID
    return session["session_id"]

