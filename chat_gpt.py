import openai

class ChatGPT:
    def __init__(self, api_key):
        openai.api_key = api_key

    def chat_with_gpt(self, prompt):
        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=prompt,
            max_tokens=50,
            temperature=0.7,
            n=1,
            stop=None,
            timeout=10
        )
        
        if 'choices' in response and len(response['choices']) > 0:
            return response['choices'][0]['text'].strip()
        
        return None
    
    def chat(self, request):
        return self.chat_with_gpt(request)
        

# Example usage
# print("Welcome to ChatGPT! Enter 'quit' to exit.")
# api_key = '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'
# chatbot = ChatGPT(api_key)

# while True:
#     user_input = input("User: ")

#     # Check if user wants to quit
#     if user_input.lower() == 'quit':
#         break

#     # Get the chatbot's response
#     response = chatbot.chat_with_gpt(user_input)
#     print("ChatGPT:", response)
