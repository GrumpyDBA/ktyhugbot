import json

class Quoter:
    def __init__(self):
        with open('data/quotes.json') as f:
            self.storedquotes = json.load(f)

    def get_quote(self):
        return self.storedquotes[1]

    def get_all_quotes(self):
        # return self.storedquotes
        return self.storedquotes

    def get_quotes_size(self):
        # return self.storedquotes
        return len(self.storedquotes)
