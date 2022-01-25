import json
import random
import requests
from urllib.request import urlopen


class Quoter:
    def __init__(self):
        with open('data/upliftingquotes.json') as f:
            self.storedquotes = json.load(f)

        with open('data/communityquotes.json') as c:
            self.communityquotes = json.load(c)
        
        # self.remotequotes = self.get_random_quotes()


    # def get_all_quotes(self):
    #     z = self.storedquotes + self.remotequotes

    #     return z

    def get_communityquote(self):
        allCommunityQuotations = self.communityquotes
        selectedquoteid = random.randint(0, len(allCommunityQuotations) - 1)

        return allCommunityQuotations[selectedquoteid]


    def get_markdown_community_quote(self):
        quoteDict = self.get_communityquote()
        quotation = quoteDict.get('text')
        author = quoteDict.get('author')
        textToSend = f"{quotation}\n_{author}_"

        return textToSend


    def get_quote(self):
        allQuotations = self.storedquotes
        selectedquoteid = random.randint(0, len(allQuotations) - 1)

        return allQuotations[selectedquoteid]


    def get_markdown_quote(self):
        quoteDict = self.get_quote()
        quotation = quoteDict.get('text')
        author = quoteDict.get('author')
        textToSend = f"{quotation}\n_{author}_"

        return textToSend


    # def get_quotes_size(self):
    #     # return self.storedquotes
    #     return len(self.storedquotes)

    # def get_live_sample_of_quotes(self):
    # https://zenquotes.io/api/quotes


    # def get_random_quotes(self):
    #     quotesUrl = 'https://zenquotes.io/api/quotes' 
    #     # todo: write out the URL to logs.
    #     contents = requests.get(quotesUrl).json()
    #     # print(type(contents))
    #     # print(contents)
    #     print("quotes fetched")
    #     return contents

