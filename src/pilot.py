import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv("data/reviews_with_sentiment")

sns.countplot(data=df, x='sentiment_label', hue='bank')
plt.title('Sentiment Distribution by Bank')
plt.xlabel('Sentiment')
plt.ylabel('Review Count')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('plots/sentiment_by_bank.png')
