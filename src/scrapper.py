import pandas as pd
from google_play_scraper import reviews, Sort
from datetime import datetime

banks = {
    'Commercial Bank of Ethiopia': 'com.combanketh.mobilebanking',
    'Abissiniya Bank': 'com.boa.boaMobileBanking',
    'Dashen Bank': 'com.dashen.dashensuperapp'
}
REVIEWS_PER_BANK = 500
LANG = 'en'
COUNTRY = 'us'

def scrape_reviews(app_id, bank_name, target_count):
    all_reviews = []

    while len(all_reviews) < target_count:
        review_batch, token = reviews(
            app_id,
            lang=LANG,
            country=COUNTRY,
            sort=Sort.NEWEST,
            count=target_count,
        )

        for r in review_batch:
            all_reviews.append({
                'review': r.get('content', '').strip(),
                'rating': r.get('score'),
                'date': r.get('at'),
                'bank': bank_name,
                'source': 'Google Play'
            })

        if not token:
            break

    return all_reviews

all_data = []

for bank_name, app_id in banks.items():
    print(f"Scraping reviews for: {bank_name}")
    bank_reviews = scrape_reviews(app_id, bank_name, REVIEWS_PER_BANK)
    all_data.extend(bank_reviews)

# --- CREATE DATAFRAME ---
df = pd.DataFrame(all_data)

## --- PREPROCESSING ---
print("🧹 Preprocessing...")

# Drop missing reviews or ratings
initial_count = len(df)
df.dropna(subset=['review', 'rating'], inplace=True)
after_missing = len(df)

df['date'] = pd.to_datetime(df['date']).dt.strftime('%Y-%m-%d')

# Remove duplicates based on review + bank
df.drop_duplicates(subset=['review', 'bank'], inplace=True)
final_count = len(df)

# --- SAVE TO CSV ---
csv_path = 'data/clean_bank_reviews.csv'
df.to_csv(csv_path, index=False)

# --- REPORT ---
missing_percent = (initial_count - after_missing) / initial_count * 100
print(f"✅ Final reviews count: {final_count}")
print(f"📉 Missing data dropped: {missing_percent:.2f}%")
print(f"📁 Clean CSV saved to: {csv_path}")