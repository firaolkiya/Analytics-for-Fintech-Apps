
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer # type: ignore
import nltk # type: ignore
from nltk.corpus import stopwords # type: ignore
import re

nltk.download('stopwords')
STOPWORDS = set(stopwords.words('english'))

def clean_text(text):
    text = re.sub(r'\W+', ' ', str(text).lower())
    return ' '.join([word for word in text.split() if word not in STOPWORDS and len(word) > 2])

def extract_keywords(df, top_n=15):
    df['cleaned'] = df['review'].apply(clean_text)

    tfidf = TfidfVectorizer(ngram_range=(1, 2), max_features=500)
    tfidf_matrix = tfidf.fit_transform(df['cleaned'])

    scores = zip(tfidf.get_feature_names_out(), tfidf_matrix.sum(axis=0).tolist()[0])
    sorted_keywords = sorted(scores, key=lambda x: x[1], reverse=True)
    
    return sorted_keywords[:top_n]


df = pd.read_csv("data/reviews_with_sentiment.csv")

df[['review', 'rating', 'date', 'bank', 'source', 'sentiment_label', 'sentiment_score']]\
  .to_csv('data/reviews_with_sentiment.csv', index=False)

import pandas as pd

# Sample manual theme-keyword mapping (customize with real TF-IDF keywords)
theme_data = [
    # CBE
    ('Commercial Bank of Ethiopia', 'Account Access Issues', 'login problem'),
    ('Commercial Bank of Ethiopia', 'Account Access Issues', 'otp failed'),
    ('Commercial Bank of Ethiopia', 'Transaction Performance', 'transfer failed'),
    ('Commercial Bank of Ethiopia', 'Transaction Performance', 'transaction delay'),
    
    # Awash
    ('Awash Bank', 'App Stability', 'app crash'),
    ('Awash Bank', 'App Stability', 'freeze'),
    ('Awash Bank', 'User Experience (UX)', 'easy to use'),
    
    # BOA
    ('Bank of Abyssinia', 'Customer Support', 'poor service'),
    ('Bank of Abyssinia', 'Customer Support', 'no response'),
    ('Bank of Abyssinia', 'Feature Request', 'add fingerprint login'),
]

# Create DataFrame
df_theme_keywords = pd.DataFrame(theme_data, columns=['bank', 'theme', 'keyword'])

# Save to CSV
df_theme_keywords.to_csv('data/theme_keywords.csv', index=False)
print("✅ Saved: data/theme_keywords.csv")

