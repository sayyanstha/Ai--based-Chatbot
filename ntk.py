import nltk
from nltk.chat.util import Chat, reflections

# Define a set of rules for the chatbot
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?",]
    ],
    [
        r"what is your name?",
        ["My name is Chatbot and I'm here to help you.",]
    ],
    [
        r"how are you?",
        ["I'm doing well, thank you!",]
    ],
    [
        r"(.*) (good|well|fine)",
        ["That's great to hear!",]
    ],
    [
        r"quit",
        ["Goodbye! Have a great day.",]
    ],
]

# Create the chatbot
chatbot = Chat(pairs, reflections)

# Start the conversation
print("Hi, I'm Chatbot. Type 'quit' to exit.")
chatbot.converse()
