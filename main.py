import telegram
import telegram.ext
from telegram.ext.dispatcher import run_async
import requests
import re
import string
import random
import quotes

with open('token.txt', 'r') as f:
    TOKEN = f.read()


def get_randomrobocat():
    letters = string.ascii_lowercase
    randomletters = ''.join(random.choice(letters) for i in range(8)) 
    url = 'https://robohash.org/'+ randomletters + '?set=set4' 
    print (url)
    # todo: write out the URL to logs.
    return url

def get_kitty_url():
    contents = requests.get('https://aws.random.cat/meow').json()
    url = contents['file']
    return url

def get_a_kitty():
    allowed_extension = ['jpg','jpeg','png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url = get_kitty_url()
        file_extension = re.search("([^.]*)$",url).group(1).lower()
    return url

@run_async
def bop(update, context):
    # url = get_a_kitty()
    url = get_randomrobocat()
    chat_id = update.message.chat_id
    context.bot.send_photo(chat_id=chat_id, photo=url)

# def get_random_quote():

def parse_messages(update, context):
    update.message.reply_text(f"Echo {update.message.text}")
    print(update.message.text)

def main():
    updater = telegram.ext.Updater(TOKEN, use_context=True)
    aquote = quotes.Quoter()

    print(aquote.get_quotes_size())
    # print(aquote.get_quote())
    print(type(aquote.get_quote()))
    
    tes = aquote.get_quote()
    print(tes.get('a'))
    print(tes.get('q'))
    

    dp = updater.dispatcher
    dp.add_handler(telegram.ext.CommandHandler('bop',bop))
    dp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, parse_messages ))
    # add handler for help, content, bop, evilmode, 
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
