import telegram
import telegram.ext
from telegram.ext.dispatcher import run_async
import requests
import re
import string
import random
import quotes
from telegram import ParseMode
import os


# with open('token_test.txt', 'r') as f:
#     TOKEN = f.read()
TOKEN = os.environ["TOKEN"]


def get_robocat_fromremote(aSeed):
    url = 'https://robohash.org/' + aSeed + '?set=set4' 
    # todo: write out the URL to logs.
    return url


@run_async
def gief_robokitty(update, context):
    letters = string.ascii_lowercase
    randomletters = ''.join(random.choice(letters) for i in range(16)) 

    url = get_robocat_fromremote(randomletters)

    chat_id = update.message.chat_id
    update.message.reply_text(f"{update.message.from_user.first_name}, It'll be ok - Let me summon a kitty to help you....")
    context.bot.send_photo(chat_id=chat_id, photo=url, caption= "Meow!")


@run_async
def gief_my_robokitty(update, context):
    userid = str(update.message.from_user.id)
    url = get_robocat_fromremote(userid)

    update.message.reply_text(f"Hey {update.message.from_user.first_name}, here is your unique to you Kitty lovingly delivered by Robohash.org")

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
    context.bot.send_photo(chat_id=chat_id, photo=url, caption=f"Hey {update.message.from_user.first_name}; have a hug, also here's a cat I found for you, Meow")


def get_quote(update, context):
    textToSend = f"{update.message.from_user.first_name}, here's something to reflect upon: \n\n"
    textToSend = textToSend + quotesList.get_markdown_quote()

    update.message.reply_text(text=textToSend, parse_mode=ParseMode.MARKDOWN)

def get_communityquote(update, context):
    textToSend = f"{update.message.from_user.first_name}, here's something I pulled from the KTY tg archives: \n\n"
    textToSend = textToSend + quotesList.get_markdown_community_quote()

    update.message.reply_text(text=textToSend, parse_mode=ParseMode.MARKDOWN)

# def get_aboutauthor(update, context):
#     textToSend = """The universe amazes me. Billions of years ago, some stuff went down, to date the best minds don't fully understand it as of yet.
#                     We know that there was a huge amount of energy and hydrogen created, it clumped together, early stars formed, these then went pop and their remanents went on to form more stars with heavier elements that were forged during their deaths. 
#                     The cycle continued of stars forming, exploding and birthing more stars in their wake, until some 4.6 billion years ago our very own sun was born.
#                     So aye, we are indeed all children of the stars, literlly made from stardust.
#                     But consider this, you and I here today; is literal proof, that if you take enough Hydrogen and give it enough time, it will seek to understand itself.
#                     That to me is the most astounding thing about our existence.

#                     I'm a simple man, not particularly smart or driven, but if I can make this brief existence just a little bit more joyful, then that's a life well lived.
#                     Dav
#                     """
#     update.message.reply_text(text=textToSend)  


# def parse_messages(update, context):
#     update.message.reply_text(f"Echo {update.message.text}")
#     print(update.message.text)


def give_kitty_hug(update, context):
    kittyhugtype = random.randint(0, 100)
    if (kittyhugtype <= 33):
        get_quote(update, context)
    elif (kittyhugtype <= 90):
        gief_kitty(update, context)
    elif (kittyhugtype <= 95):
        get_communityquote(update, context)
    else :
        gief_robokitty(update, context)



def main():
    updater = telegram.ext.Updater(TOKEN, use_context=True)
    global quotesList
    quotesList = quotes.Quoter()
    
    dp = updater.dispatcher
    # dp.add_handler(telegram.ext.CommandHandler('gief_robokitty', gief_robokitty))
    dp.add_handler(telegram.ext.CommandHandler('gief_my_kitty', gief_my_robokitty))
    # dp.add_handler(telegram.ext.CommandHandler('gief_kitty', gief_kitty))
    # dp.add_handler(telegram.ext.CommandHandler('get_quote', get_quote))
    dp.add_handler(telegram.ext.CommandHandler('hugz', give_kitty_hug))
    # dp.add_handler(telegram.ext.CommandHandler('abouttheauthor', get_aboutauthor))
    # dp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, parse_messages ))

    # dp.add_handler(telegram.ext.CommandHandler('give_kitty_hug', give_kitty_hug))
    # add handler for help, content, bop, evilmode, 
    updater.start_polling(poll_interval = 10, drop_pending_updates = True, bootstrap_retries = 0)
    updater.idle()


if __name__ == '__main__':
    main()

