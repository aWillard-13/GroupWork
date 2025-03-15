import requests

def StrLookupWord(word):
    # API endpoint (replace with your actual API endpoint)
    api_url = f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}'

    # Send GET request to the API
    response = requests.get(api_url)

    # Check if the word was found
    if response.status_code == 200:
        data = response.json()
        # Extract and display the meaning (assuming the data has this structure)
        meanings = data[0]['meanings']
        for meaning in meanings:
            print(f"Part of speech: {meaning['partOfSpeech']}")
            for definition in meaning['definitions']:
                print(f"Definition: {definition['definition']}")
    else:
        print(f"Error: Could not find the word '{word}'.")

def main():
    strWord = input("Enter a word to look up: ")
    StrLookupWord(strWord)

if __name__ == '__main__':
    main()