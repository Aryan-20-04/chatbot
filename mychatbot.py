import nltk
from nltk.chat.util import Chat,reflections

pattern=[
    (r'Hello|Hi',['Hello','Hi there']),
    (r'How are you',['I am fine','Nice']),
    (r'bye',['Goodbye','See you'])
]
chatbot=Chat(pattern,reflections)
def get_response(user_input):
    if user_input=='Weather' or user_input=='weather':
        return 'Click here for weather update: https://www.accuweather.com/en'
    elif user_input=='Jokes' or user_input=='jokes':
        return 'Here is a joke: Why don\'t scientists trust atoms? Because they make up everything.'
    elif user_input=='News' or user_input=='news':
        return 'Click here to get the latest news: https://www.bbc.com/news'
    else:
        response = chatbot.respond(user_input)
        return response if response else 'Sorry, I did not understand that.'
def start_chat():
    print("Hello I am your chat bot")
    name=input("What is your name: ")
    print(f'Hello {name}')

    while True:
        response=input("Press 'start' to start a new conversation or 'bye' to end the conversation: ").strip().lower()
        if response in ['bye','exit','quit']:
            print("It was nice chatting with you")
            break
        elif response in ['start','open','begin']:
            while True:
                print('Commands: Hello,Hi/How are you/bye/Weather/Jokes/News')
                user_input=input('What would you like to know: ')
                if user_input in ['bye','end']:
                    print(f'Nice talking to you {name}')
                    break
                else:
                    print(get_response(user_input))

start_chat()
