import spacy
import pandas as pd
from spacytextblob.spacytextblob import SpacyTextBlob


nlp = spacy.load("en_core_web_sm")
nlp.add_pipe('spacytextblob')

# Created a function to clean the data. By coverting to lower.
# Remove stoplist items.
# Remove any whitespaces, leading or trailing.
# Add both the cleaned (and original) data to dictionary. 

def clean_data(whole_review_data):
    cleaned_reviews = {}
    for review in whole_review_data:
        doc = nlp(review)
        cleaned_data = ''.join([token.text.lower() for token in doc if not
                                token.is_stop and token.text.strip()])
        cleaned_reviews[review] = cleaned_data
    return cleaned_reviews

# Created a function to test sentiment in cleaned data.
def sentiment_analysis(cleaned_text):
    for key, value in cleaned_text.items():
        doc = nlp(value)
        print(f'\nReview: {key}')
        print(f'\nSentiment: {doc._.blob.polarity}')

# Load Amazon data
# Remove all NaN values from the column
# Filter to test value
amazon_data = pd.read_csv("amazon_product_review.csv", sep=',')
amazon_data = amazon_data.dropna(subset=['reviews.text'])
review_data = amazon_data['reviews.text'].iloc[[0, 24, 43, 437, 2000, 6000, 
                                                9000, 11501, 13503, 17000, 25066]]

sentiment_analysis(clean_data(review_data))

first_review = amazon_data['reviews.text'][1500]
second_review = amazon_data['reviews.text'][2200]

nlp = spacy.load('en_core_web_md')

# Created a function to test similarity between 2 sentences.
def similarity(first, second):
    similarity_result = nlp(first).similarity(nlp(second))
    return similarity_result

print(f"\nReview One: {first_review}")
print(f"Review Two: {second_review}")
print(f"Similarity: {similarity(first_review,second_review)}")