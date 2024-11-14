from langchain.llms import Ollama

class Chatbot:
    def __init__(self):
        self.llm = Ollama(model="mistral:latest")

    def get_response(self, user_input):
        try:
            response = self.llm(user_input)  
            return response
        except Exception as e:
            print(f"Error in getting response: {e}")
            return "Error processing request."
