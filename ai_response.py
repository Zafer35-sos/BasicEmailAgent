from ollama import chat

def chat_with_gmail_agent(email_text):
    response = chat(
        model='gemma3',
        messages=[
            {
                'role': 'user',
                'content': 'Summarize this email: ' + email_text,
            },
        ]
    )
    return response['message']['content'] 

def summarize_email(email_text):
    return chat_with_gmail_agent(email_text)

