from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey!"]
    ],
    [
        r"what is your name?",
        ["My name is Chatbot created by himanshu.", "People call me himzo Chatbot.", "I'm himanshu Chatbot."]
    ],
    [
        r"how are you?",
        ["I'm doing well, thanks for asking.", "I'm fine, thank you.", "I'm good, how are you?"]
    ],
    [
        r"what can you do?",
        ["I can answer simple questions, tell jokes, and chat with you.", "I can chat with you, tell jokes, and answer your questions.", "I'm a chatbot, so I can chat with you, answer questions, and tell jokes."]
    ],
    [
        r"what is the time?",
        ["Sorry, I don't know what time it is.", "I don't have a clock, so I can't tell you what time it is.", "I'm sorry, I don't know the time."]
    ],
    [
        r"what is your favorite color?",
        ["I'm a chatbot, so I don't have a favorite color.", "I don't have eyes, so I don't have a favorite color.", "I'm not capable of having a favorite color, sorry!"]
    ],
    [
        r"tell me a joke",
        ["Why was the math book sad? Because it had too many problems.", "Why did the tomato turn red? Because it saw the salad dressing!"]
    ],
    [
        r"bye|goodbye",
        ["Goodbye!", "Have a nice day!", "See you later!"]
    ]
]

chatbot = Chat(pairs, reflections)
chatbot.converse()



#pip install chatterbot
