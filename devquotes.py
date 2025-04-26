import json
import random

# Load quotes from the JSON file
with open('quotes.json', 'r') as file:
    quotes = json.load(file)

# Choose a random quote
quote = random.choice(quotes)

# Display the quote
print("\n💻 Developer Quote of the Day:\n")
print(f"\"{quote}\"")
