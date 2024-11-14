class History:
    def __init__(self):
        self.conversation = []

    def add_message(self, sender, message):
        self.conversation.append({"sender": sender, "message": message})

    def get_history(self):
        return self.conversation
