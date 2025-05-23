import arxiv
import pandas as pd
from datetime import datetime, timedelta

# Define search parameters
query = 'cat:cs.LG OR cat:cs.AI OR cat:stat.ML'
today = datetime.today()
last_week = today - timedelta(days=7)

# Search latest papers
search = arxiv.Search(
    query=query,
    max_results=50,
    sort_by=arxiv.SortCriterion.SubmittedDate
)

papers = []
for result in search.results():
    papers.append({
        "title": result.title,
        "summary": result.summary,
        "authors": [author.name for author in result.authors],
        "published": result.published.date(),
        "url": result.entry_id
    })

# Save to CSV
df = pd.DataFrame(papers)
df.to_csv('data/arxiv_papers.csv', index=False)
print(" Saved latest Arxiv papers to data/arxiv_papers.csv")
