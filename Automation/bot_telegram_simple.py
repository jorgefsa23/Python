import telebot

# my Telegram API key is storaged into a .txt:
file_key = open('API-KEI.txt', 'r')
API_KEY = file_key.readline()
file_key.close()

bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=["pizza"])
def pizza(message):
    bot.send_message(message.chat.id, "Preparing your pizza!\nWaiting time: 40min.\n\nTo continue click /start")

@bot.message_handler(commands=["hamburguer"])
def hamburguer(message):
    bot.send_message(message.chat.id, "Your BigBiggerBurguer is almost ready\n\nTo continue click /start")

@bot.message_handler(commands=["salad"])
def salad(message):
    bot.send_message(message.chat.id, "Your salad is ready!\n\nTo continue click /start")


@bot.message_handler(commands=["option1"])
def option1(message1):
    text_menu = """
    Select options:
    /pizza
    /hamburguer
    /salad"""
    bot.send_message(message1.chat.id, text_menu)

@bot.message_handler(commands=["option2"])
def option2(message2):
    bot.send_message(message2.chat.id, "To follow you order\nPlease, insert you code in:\nmyorder.com\n\nTo continue click /start")

@bot.message_handler(commands=["option3"])
def option3(message3):
    bot.send_message(message3.chat.id, "Please, Send a message to:\nbot_admin@chat.net\n\nTo continue click /start")




#function to check if there is a message by user
def check_message(is_there_message):
    return True

#functions decorator 
@bot.message_handler(func=check_message)
#functions to reply messages
def reply(messages):
    text = """
    Select an option to continue:
    /option1: Place order
    /option2: Follow order
    /option3: Send a message to Admin
    Choose any option to continue"""
    bot.reply_to(messages, text)


#'activating' bot interactions  
bot.polling()