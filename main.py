import telegram
import telegram.ext
from telegram.ext.dispatcher import run_async
import requests
import re
import string
import random
import quotes
from telegram import ParseMode

with open('token.txt', 'r') as f:
    TOKEN = f.read()


def get_randomrobocat():
    letters = string.ascii_lowercase
    randomletters = ''.join(random.choice(letters) for i in range(16)) 
    url = 'https://robohash.org/' + randomletters + '?set=set4' 
    # print (url)
    # todo: write out the URL to logs.
    return url
 

@run_async
def gief_robokitty(update, context):
    # url = get_a_kitty()
    url = get_randomrobocat()
    print(update.message.from_user.id)

    chat_id = update.message.chat_id
    context.bot.send_photo(chat_id=chat_id, photo=url)


def get_kitty_url():
    contents = requests.get('https://aws.random.cat/meow').json()
    url = contents['file']
    return url


def gief_kitty(update, context):
    allowed_extension = ['jpg','jpeg','png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url = get_kitty_url()
        file_extension = re.search("([^.]*)$",url).group(1).lower()

    chat_id = update.message.chat_id
    context.bot.send_photo(chat_id=chat_id, photo=url)


def get_quote(update, context):
    textToSend = quotesList.get_markdown_quote()
    update.message.reply_text(text=textToSend, parse_mode=ParseMode.MARKDOWN)


def parse_messages(update, context):
    update.message.reply_text(f"Echo {update.message.text}")
    print(update.message.text)

def give_kitty_hug(update, context):
    kittyhugtype = random.randint(0, 100)
    print(kittyhugtype)
    if (kittyhugtype <= 33):
        update.message.reply_text(f"Hey {update.message.from_user.first_name}, here's some words of wisdom to reflect upon.")
        get_quote(update, context)
    elif (kittyhugtype <= 90):
        update.message.reply_text(f"Hey {update.message.from_user.first_name}; you poor thing, here's a cat I found on the internet.")
        gief_kitty(update, context)
    else :
        update.message.reply_text(f"I'm sorry {update.message.from_user.first_name}; You poor thing, here I made a special kitty just for you!")
        gief_robokitty(update, context)



def main():
    updater = telegram.ext.Updater(TOKEN, use_context=True)

    global quotesList
    quotesList = quotes.Quoter()
    
    dp = updater.dispatcher
    dp.add_handler(telegram.ext.CommandHandler('gief_robokitty', gief_robokitty))
    dp.add_handler(telegram.ext.CommandHandler('gief_kitty', gief_kitty))
    dp.add_handler(telegram.ext.CommandHandler('get_quote', get_quote))
    dp.add_handler(telegram.ext.CommandHandler('give_kitty_hug', give_kitty_hug))
    # dp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, parse_messages ))

    # dp.add_handler(telegram.ext.CommandHandler('give_kitty_hug', give_kitty_hug))
    # add handler for help, content, bop, evilmode, 
    updater.start_polling(poll_interval = 10, drop_pending_updates = True, bootstrap_retries = 0)
    updater.idle()


if __name__ == '__main__':
    main()
