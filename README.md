Sentiment Analysis with SpacyTextBlob
This project aims to perform sentiment analysis on text data using the SpacyTextBlob library. It utilizes the Spacy library for natural language processing and integrates the TextBlob library for sentiment analysis.
The project provides functions to clean text data, analyze sentiment, and calculate similarity between sentences.
To install the required libraries for this project, use the following command:
Ensure you have Python installed on your system.

1. Import the necessary libraries: `spacy`, `pandas`, and `SpacyTextBlob`.
2. Load the English language model using `spacy.load("en_core_web_sm")`.
3. Create an instance of the `SpacyTextBlob` class using `nlp.add_pipe('spacytextblob')`.
4. Define functions `clean_data()` and `sentiment_analysis()` to preprocess the text data and perform sentiment analysis, respectively.
5. Load the dataset (Amazon product reviews in this case) using `pd.read_csv()` and drop any rows with NaN values.
6. Extract a subset of reviews for analysis.
7. Clean the text data using the `clean_data()` function.
8. Analyze sentiment using the `sentiment_analysis()` function.
9. Use the `similarity()` function to calculate the similarity between two sentences.

This project was created by Jasmeen Bahlay. If you have any questions or suggestions, feel free to reach out.
