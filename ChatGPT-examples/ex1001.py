import nltk
import spacy
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download required resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punkt_tab')

# Example text
text = "NLP is amazing! I am learning how to process text with Python."

# 1. Lowercase
text_lower = text.lower()
print("Lowercase:", text_lower)

# 2. Tokenize
tokens = word_tokenize(text_lower)
print("Tokens:", tokens)

# 3. Remove stopwords
stop_words = set(stopwords.words('english'))
filtered_tokens = [w for w in tokens if w not in stop_words and w.isalpha()]
print("Without stopwords:", filtered_tokens)

# 4. Lemmatization with SpaCy
nlp = spacy.load("en_core_web_sm")
doc = nlp(" ".join(filtered_tokens))
lemmas = [token.lemma_ for token in doc]
print("Lemmas:", lemmas)
