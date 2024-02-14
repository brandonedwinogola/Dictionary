
import json
from difflib import get_close_matches

# Load the data from the JSON file
data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()] 
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        print("Did you mean %s instead?" % get_close_matches(word, data.keys())[0])
        decide = input("Press y for yes or n for no: ")
        if decide == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif decide == "n":
            return "Pugger your paw steps on working keys"
        else:
            return "You have entered wrong input. Please enter just y or n"
    else:
        print("You have entered wrong keys. Try again")

# Prompt the user to enter a word to search
word = input("Enter the word you want to search: ")

# Translate the word and store the output
output = translate(word)

# Check the type of output and print accordingly
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)



    