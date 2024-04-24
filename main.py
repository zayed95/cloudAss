import nltk
import string
nltk.download('punkt')
from nltk.corpus import stopwords
from collections import Counter

nltk.download('stopwords')

with open("/app/paragraphs.txt", "r") as file:
    text = file.read()

punctuation = string.punctuation
no_punct_text = text.translate(str.maketrans('', '', punctuation))

stopwords_english = stopwords.words('english')

words = nltk.word_tokenize(no_punct_text)

processed_text = [word for word in words if word not in stopwords_english]


word_counts = Counter(processed_text)

print(word_counts)