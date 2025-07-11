# 📊 Bank Reviews Sentiment Analysis & Insights

This project analyzes user reviews of Ethiopian banking apps from the Google Play Store to uncover key satisfaction drivers, pain points, and actionable insights. It simulates a real-world data engineering workflow including web scraping, sentiment analysis, thematic clustering, Oracle database storage, and insightful visualizations.

---

## 📁 Project Structure

```bash
bank-reviews-scraper/
├── data/                  # Cleaned and enriched datasets
├── plots/                 # Generated visualizations
├── reports/               # Final insights report
├── sql/                   # Oracle schema and dump
├── src/                   # Python scripts for each task
├── README.md              # Project documentation
├── requirements.txt       # Python dependencies

```
🚀 Workflow Overview
<details> <summary><strong>1. Web Scraping</strong></summary>
Used google-play-scraper to extract reviews from:

Commercial Bank of Ethiopia (CBE)

Awash Bank

Bank of Abyssinia (BOA)

Target: 1,200+ reviews (400+ per bank)

</details> <details> <summary><strong>2. Preprocessing</strong></summary>
Removed duplicates

Handled missing data

Normalized dates (YYYY-MM-DD)

Saved cleaned data as clean_bank_reviews.csv

</details> <details> <summary><strong>3. Sentiment Analysis</strong></summary>
Tools: VADER + distilbert-base-uncased-finetuned-sst-2-english

Labeled reviews as positive, negative, or neutral

Output: reviews_with_sentiment.csv

</details> <details> <summary><strong>4. Thematic Analysis</strong></summary>
Extracted keywords using TF-IDF

Grouped into 3–5 themes per bank (e.g., UI, Login Issues, Support)

Output: theme_keywords.csv

</details> <details> <summary><strong>5. Oracle Database Integration</strong></summary>
Created tables: banks, reviews

Inserted data using cx_Oracle

SQL schema stored in sql/schema.sql

</details> <details> <summary><strong>6. Insights & Visualization</strong></summary>
Visuals: sentiment bar charts, rating histograms, word clouds

Insights: drivers & pain points per bank

Report includes ethical analysis

</details>
📈 Visualizations
Chart Type	Description
Sentiment Distribution	Reviews by sentiment per bank
Rating Histogram	1–5 star ratings across banks
Word Clouds	Top keywords per bank
Sentiment Trend (optional)	Sentiment over time (if dated)

All plots saved in the plots/ folder.

💡 Insights Summary
Bank	✅ Drivers	⚠️ Pain Points
CBE	Simple UI, fast response	Login & OTP issues
Awash	Easy transfer process	App crashes on some devices
BOA	Good UX design	Poor customer support response

🛠 Technologies Used
Tool	Purpose
Python, Pandas	Core scripting, preprocessing
Seaborn, Matplotlib	Data visualization
VADER, Transformers	Sentiment classification
TF-IDF, spaCy	Keyword extraction
Oracle XE	Relational database storage
cx_Oracle	Python–Oracle DB connector

✅ KPIs Achieved
✅ 1,200+ reviews scraped

✅ <5% missing data

✅ Sentiment scores for 90%+ reviews

✅ 3+ themes per bank

✅ 3–5 clean visualizations

✅ Oracle insert script + SQL dump

✅ Final 4-page insights report with ethical notes

📜 Ethics Note
Online reviews may exhibit bias. Dissatisfied users are often more likely to post reviews, which can lead to a negativity bias. For fair analysis, sentiment results should be cross-validated with internal usage analytics when possible.

📄 Screen shoot
<img width="663" height="494" alt="Image" src="https://github.com/user-attachments/assets/e2516541-45bf-4777-a687-837ab253a549" />
<img width="663" height="494" alt="Image" src="https://github.com/user-attachments/assets/955f7dd7-47de-4ae3-888f-3887227f8219" />
<img width="830" height="486" alt="Image" src="https://github.com/user-attachments/assets/c297d00a-4ed6-43eb-b664-b79f53a59475" />
<img width="822" height="563" alt="Image" src="https://github.com/user-attachments/assets/f9e91e98-a62a-4fd5-9c52-f4ec09525057" />

📦 Setup Instructions
Clone the repo:

```bash
git clone https://github.com/your-username/bank-reviews-scraper.git
cd bank-reviews-scraper
```
Install dependencies:

```bash
pip install -r requirements.txt
```
Run analysis scripts:

```bash
python src/sentiment_analysis.py
python src/thematic_analysis.py
python src/visualize_insights.py
python src/db_insert_oracle.py
```
✍️ Author
Firaol Bulo
Software Engineering Student @ ASTU | A2SV Trainee | Mobile App Developer
