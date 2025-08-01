#!/usr/bin/env python
# coding: utf-8

# In[1]:


def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input:
        return "Hi!"
    elif "how are you" in user_input:
        return "I'm fine, thanks!"
    elif "bye" in user_input:
        return "Goodbye!"
    elif "your name" in user_input:
        return "I'm a simple chatbot."
    else:
        return "Sorry, I don't understand."

def run_chatbot():
    print("🤖 Chatbot: Hello! Type something to talk to me (type 'bye' to exit).")
    while True:
        user_input = input("You: ")
        reply = chatbot_response(user_input)
        print("🤖 Chatbot:", reply)
        if "bye" in user_input.lower():
            break

run_chatbot()


# In[ ]:




