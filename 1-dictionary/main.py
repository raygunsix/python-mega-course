import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def close_matches(word):
    return get_close_matches(word, data.keys(), cutoff=0.8)

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(close_matches(word)) > 0:
        yn = input("Did you mean %s? [y/n] " % close_matches(word)[0])
        if yn == "y":
            return data[close_matches(word)[0]]
        elif yn == "n":
            return "That word does not exist."
        else:
            return "We didn't understand your entry."
    else:
        return "That word does not exist."

word = input("Enter word: ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)