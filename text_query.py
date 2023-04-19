import spacy

import warnings
warnings.filterwarnings("ignore")
# print("Enter two words")
# words = input()

# Load a pre-trained spaCy model
nlp = spacy.load("en_core_web_lg")

# Define a list of POS tags that correspond to "content" words
content_tags = ["ADJ", "NOUN", "VERB", "ADV"]

# Define a function to extract keywords from a sentence
def extract_keywords(sentence):
    # Parse the sentence with spaCy
    doc = nlp(sentence)
    # Initialize a list to hold the extracted keywords
    keywords = []
    # Iterate over the tokens in the parsed sentence
    for token in doc:
        # If the token is a content word
        if token.pos_ in content_tags:
            # Add the token's lemma to the keywords list
            keywords.append(token.lemma_)
    # Return the list of keywords
    return keywords

def get_tags(sentence):
    # load tags.json and import the object into a dictionary
    # songs = json.load(codecs.open('tags.json', 'r', 'utf-8-sig'))

    #  read from file tags-processed-final.txt and split into words
    with open('tags-processed-final.txt', 'r') as file:
        words = file.read().replace(',', ' ')

    # Example usage
    # sentence = "i have review tomorrow and i am not ready"
    keywords = extract_keywords(sentence)
    # print(keywords)

    tokens = nlp(words)
    tags = []
    for tag in keywords:
        for token in tokens:
            if nlp(tag).similarity(token) >= 0.6:
                if token.text not in tags:
                    tags.append(token.text)
                    # print(tag, token.text, nlp(tag).similarity(token))
    return tags

print(get_tags("i have review tomorrow and i am not ready"))