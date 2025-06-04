responses={"hi":"Hello! How can I assist you today?",
           "how are you":"I'm just a computer program, but thanks for asking! How can I help you?",
           "what is your name":"I am a chatbot created to assist you. You can call me Chatbot.",
           "what can you do":"I can answer questions, provide information, and assist with various tasks. Just ask!",
           "what answers do you provide":"I can provide the answers to the Questions related to my capabilities which are defined",
           "what does your comapany do":"We are a IT service provider company that offers IT solutions to the clients.",
           "what are your services":"We provide lot of services like web devlopment,app development,grapics designing,editind,content writing,seo and many more.",
           "how can i contact you":"You can contact via email at 'common@ramitsolution,com'or call us at +91 9439439435",
           "i need a":"Sure!Please provide all the details related to your work at 'common@ramitsolution,com'",
           "have a nice day":"Thank you! You too have a great day ahead!",
           "thank you":"You're welcome and if you any queries feel free to ask."}

def get_response(user_input):
    user_input=user_input.lower()
    for key in responses:
        if key in user_input:
            return responses[key]
    return"I'm sorry,at present I don't have any answers to your question.If you other than this feel free to ask"
name=input("Can I know your good name?")
while True:
    user_input=input(f'{name}:')
    if user_input.lower() in ["bye","exit","quit",'goodbye']:
        print("bot: Goodbye,It was nice talking to you!Have a great day!")
        break
    response=get_response(user_input)
    print(f'bot:{response}')