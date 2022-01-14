import json
import random
import requests
from urllib.request import urlopen


class Quoter:
    def __init__(self):
        with open('data/quotes.json') as f:
            self.storedquotes = json.load(f)
        self.remotequotes = self.get_random_quotes()


    def get_all_quotes(self):
        z = self.storedquotes + self.remotequotes

        return z


    def get_quote(self):
        allQuotations = self.get_all_quotes()
        selectedquoteid = random.randint(0, len(allQuotations) - 1)

        return allQuotations[selectedquoteid]


    def get_markdown_quote(self):
        quoteDict = self.get_quote()
        quotation = quoteDict.get('q')
        author = quoteDict.get('a')
        # textToSend = quotation + "\n_" + author + "_"
        textToSend = f"{quotation}\n_{author}_"

        return textToSend


    # def get_quotes_size(self):
    #     # return self.storedquotes
    #     return len(self.storedquotes)

    # def get_live_sample_of_quotes(self):
    # https://zenquotes.io/api/quotes


    def get_random_quotes(self):
        quotesUrl = 'https://zenquotes.io/api/quotes' 
        # todo: write out the URL to logs.
        contents = requests.get(quotesUrl).json()
        # print(type(contents))
        # print(contents)
        print("quotes fetched")
        return contents

