#!/usr/bin/env python
# coding: utf-8

# In[27]:


# CHATBOT USING FLASK
import re
import random

def chatbot_response(user_input):
    responses = [
        (r"hi|hello|hey", ["Hello! ACE Students", "Hi ACE Students!", "Hey! ACE Students, How can I help you?"]),
        (r"how are you\?", ["I'm just a bot, but I'm doing great!", "I'm doing well, thanks for asking!"]),
        (r"who are you\?", ["I am a chatbot here to assist you.", "I am ChatBot, your virtual assistant!"]),
        (r"what is your name\?", ["I am a chatbot. You can call me ChatBot!", "My name is ChatBot."]),
        (r"who created you\?", ["I was created by a programmer who can assist you.", "I am just a basic chatbot, no real creator!"]),
        (r"bye|goodbye", ["Goodbye!", "Have a great day!", "Bye! Enjoy your day."]),

        # Exam-related Questions
        (r"when is the exam\?", ["Check your university/college website for the latest exam schedule.", "You can ask your professor or check the notice board for the exam date."]),
        (r"how to manage time for studies\?", ["Make a timetable and stick to it. Prioritize important subjects.", "Use the Pomodoro technique: 25 minutes study, 5 minutes break."]),
        (r"how to avoid exam stress", ["Relax, take breaks, and practice mindfulness. A healthy mind performs better.", "Believe in yourself and stay positive!"]),

        # Assignment and Project Help
        (r"how to complete my assignment", ["Start early, break it into smaller tasks, and research properly.", "Seek help from teachers or online resources if needed."]),
        (r"can you help me with my project\?", ["Sure! What is your project about?", "I'd be happy to guide you. Tell me more about your project."]),

        # Motivation and Encouragement
        (r"i feel stressed", ["Take a deep breath. You’re doing great!", "It’s okay to feel stressed. Take breaks and keep going."]),
        (r"i am not able to focus", ["Try studying in a quiet place and eliminate distractions.", "Break tasks into smaller goals and take short breaks."]),
        (r"i failed in my exam", ["Failure is just a step towards success. Learn from mistakes and try again!", "Don’t be discouraged. Every failure is a learning opportunity."]),
    ]

    user_input = user_input.lower()
    
    # Check for matching patterns
    for pattern, responses_list in responses:
        if re.search(pattern, user_input):
            return random.choice(responses_list)

    return "I'm sorry, I don't understand that. Can you rephrase?"


# In[2]:


import os
os.system('jupyter nbconvert --to script "chatbot.ipynb"')


# In[1]:


# python app.py in cmd prompt


# In[ ]:


# Now, open your web browser and visit:
# 👉 http://127.0.0.1:5000/


# In[ ]:




