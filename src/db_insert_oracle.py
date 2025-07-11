import cx_Oracle
import pandas as pd

# Load data
df = pd.read_csv('data/reviews_with_sentiment.csv')

# Connect to Oracle XE
conn = cx_Oracle.connect("username/password@localhost/XEPDB1")
cursor = conn.cursor()

# Insert banks and keep track of IDs
bank_ids = {}
for bank in df['bank'].unique():
    cursor.execute("INSERT INTO banks (name) VALUES (:1) RETURNING id INTO :2", [bank, cursor.var(cx_Oracle.NUMBER)])
    bank_id = cursor.fetchone()[0]
    bank_ids[bank] = bank_id

# Insert reviews
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO reviews (review_text, rating, review_date, sentiment_label, sentiment_score, bank_id, source)
        VALUES (:1, :2, TO_DATE(:3, 'YYYY-MM-DD'), :4, :5, :6, :7)
    """, (
        row['review'],
        row['rating'],
        row['date'],
        row['sentiment_label'],
        row['sentiment_score'],
        bank_ids[row['bank']],
        row['source']
    ))

conn.commit()
print("✅ Data inserted into Oracle.")
cursor.close()
conn.close()
