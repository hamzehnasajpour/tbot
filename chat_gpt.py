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
    
    def chat(self, api_key, request):
        # if api_key is openai.api_key:
        return self.chat_with_gpt(request)
        return "API_KEY is not yours!!!"
