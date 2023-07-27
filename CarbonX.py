import random
import string
import re


def carbonx_chatbot():
    responses = [
        "I'm doing well, thanks for asking!",
        "I'm excited to be able to help people with their tasks.",
        "I'm still under development, but I'm learning new things every day.",
        "What can I help you with today?",
    ]
    return random.choice(responses)


def greeting(user_input):
    greetings = [
        "Hi there!",
        "Hello!",
        "Howdy!",
        "Hey there!",
    ]
    if re.match(r"hello|hi|hey", user_input):
        return random.choice(greetings)


def goodbye(user_input):
    goodbyes = [
        "Goodbye!",
        "See you later!",
        "Have a nice day!",
        "Talk to you soon!",
    ]
    if re.match(r"bye|goodbye|see you later", user_input):
        return random.choice(goodbyes)


def answer_question(user_input):
    questions = [
        "What is your name?",
        "What can you do?",
        "How are you?",
        "Where are you from?",
    ]
    if re.match(r"what is your name|who are you", user_input):
        return "My name is CarbonX. I am a chatbot created by Aditya Prakash."
    elif re.match(r"what can you do", user_input):
        return "I can help you with a variety of tasks, such as answering questions, generating text, and translating languages."
    elif re.match(r"how are you", user_input):
        return "I am doing well, thank you for asking!"
    elif re.match(r"where are you from", user_input):
        return "I am from the cloud."


def handle_input(user_input):
    if greeting(user_input):
        return greeting(user_input)
    elif goodbye(user_input):
        return goodbye(user_input)
    elif answer_question(user_input):
        return answer_question(user_input)
    else:
        return "I'm not sure how to respond to that."


def main():
    while True:
        user_input = input(">>> ")
        response = handle_input(user_input)
        print(response)


if __name__ == "__main__":
    main()
