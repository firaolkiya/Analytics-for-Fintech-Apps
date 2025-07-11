from transformers.pipelines import pipeline
import pandas as pd




def analyze_sentiment_bert(df):
    sentiment_model = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english") # type: ignore
    results = sentiment_model(list(df['review'].astype(str)), truncation=True)

    df['sentiment_label'] = [r['label'].lower() for r in results]
    df['sentiment_score'] = [r['score'] for r in results]
    return df

df = pd.read_csv("data/clean_bank_reviews.csv")
df = analyze_sentiment_bert(df) 
df.to_csv('data/reviews_with_sentiment.csv', index=False)


sentiment_summary = df.groupby(['bank', 'rating'])['sentiment_score'].mean().reset_index()
print(sentiment_summary)

