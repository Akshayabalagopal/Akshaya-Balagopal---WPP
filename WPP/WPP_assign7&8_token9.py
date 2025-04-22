'''Create a tokenizer for your own language (mother tongue you speak). The tokenizer should
tokenize punctuations, dates, urls, emails, numbers (in all different forms such as “33.15”,
“3,22,243”, “313/77”), social media usernames/user handles. Use regular expressions to design
this. [Hint: Use unicode blocks for your language, check wikipedia pages]
'''
'''import re


class Tokenizer:
    def __init__(self):
        self.patterns = {
            'punctuation': r'[.,!?;:(){}[\]<>]',
            'date': r'\b(?:\d{2}/\d{2}/\d{4}|\d{4}-\d{2}-\d{2})\b',
            'url': r'https?://(?:www\.)?[a-zA-Z0-9-]+\.[a-zA-Z]{2,6}(/\S*)?',
            'email': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,6}\b',
            'number': r'\b(?:\d{1,3}(?:,\d{3})*|\d+(\.\d+)?|\d{1,3}/\d{1,3})\b',
            'username': r'@\w+'
        }
       
    def tokenize(self, text):
        combined_pattern = '|'.join(f'(?P<{key}>{value})' for key, value in self.patterns.items())
        matches = re.finditer(combined_pattern, text)
       
        tokens = []
        for match in matches:
            for key, value in match.groupdict().items():
                if value:
                    tokens.append((key, value))
        return tokens


def main():
    tokenizer = Tokenizer()


    while True:
       
        user_input = input("Enter a string to tokenize (or 'exit'): ")
       
        if user_input.lower() == 'exit':
            print("Exit")
            break


        tokens = tokenizer.tokenize(user_input)


        if tokens:
            print("Tokens found:")
            for token_type, token in tokens:
                print(f"{token_type}: {token}")
        else:
            print("No tokens found.")
       
if __name__ == "__main__":
    main()'''


import re

punctuation = r'[^\w\s]'
dates = r'\b(?:[0-2]?\d|3[01])[-/.](?:0?\d|1[0-2])[-/.](?:\d{2}|\d{4})\b'
urls = r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+'
emails = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
numbers = r'\b\d{1,3}(?:,\d{3})*(?:\.\d+)?|\d+/\d+\b'
usernames = r'@\w+'

combined_regex = f'({punctuation}|{dates}|{urls}|{emails}|{numbers}|{usernames})'

def tokenizer(text):
    # Find all matches in the text
    tokens = re.findall(combined_regex, text)
    return tokens

sample_text = "ചേർന്നാൽ 33.15@someemail.com https://example.com 31/12/2021, @username"

tokens = tokenizer(sample_text)
print(tokens)

