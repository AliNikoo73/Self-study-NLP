# Mini-Project 1 — Movie Review Text Cleaning

import nltk
from nltk.corpus import movie_reviews, stopwords
import spacy
from nltk.tokenize import word_tokenize
from collections import Counter

# Download dataset
nltk.download('movie_reviews')

# Load sample reviews
file_ids = movie_reviews.fileids()
print("Number of reviews:", len(file_ids))

# Take first review
sample_text = movie_reviews.raw(file_ids[0])
print(sample_text[:500])  # Print first 500 chars
print("\n" + "="*50 + "\n")


# Download extras
nltk.download('punkt')
nltk.download('stopwords')

# Load spacy model
nlp = spacy.load("en_core_web_sm")
stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    # Lowercase
    text = text.lower()
    # Tokenize
    tokens = word_tokenize(text)
    # Remove stopwords & non-alphabetic
    tokens = [w for w in tokens if w.isalpha() and w not in stop_words]
    # Lemmatize
    doc = nlp(" ".join(tokens))
    lemmas = [token.lemma_ for token in doc]
    return lemmas

# Try on one review
tokens = preprocess_text(sample_text)
print(tokens[:50])

# Frequency distribution
# Process multiple reviews (first 100 reviews)
all_tokens = []
for fid in file_ids[:100]:
    text = movie_reviews.raw(fid)
    all_tokens.extend(preprocess_text(text))

# Count most common words
word_freq = Counter(all_tokens)
print(word_freq.most_common(20))
