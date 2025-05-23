import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import re

# Load the dataset
df = pd.read_csv('data/arxiv_papers.csv')

# Combine all titles for keyword analysis
text = ' '.join(df['title'].dropna()).lower()

# Remove special characters and tokenize
words = re.findall(r'\b[a-z]{4,}\b', text)  # Only words with 4+ letters
stopwords = set(['using', 'model', 'models', 'paper', 'data', 'approach'])  # common words to ignore
filtered_words = [word for word in words if word not in stopwords]

# Count and print top keywords
word_counts = Counter(filtered_words)
print("🔍 Top 10 keywords in titles:")
for word, count in word_counts.most_common(10):
    print(f"{word}: {count}")

# Generate a word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(' '.join(filtered_words))
plt.figure(figsize=(12, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title("Top Keywords in Arxiv Titles")
plt.tight_layout()
plt.savefig('data/arxiv_title_wordcloud.png')
plt.show()
