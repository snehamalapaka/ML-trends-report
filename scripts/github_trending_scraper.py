import requests
from bs4 import BeautifulSoup
import pandas as pd

# GitHub trending ML repositories URL
url = 'https://github.com/trending?since=daily&spoken_language_code=en'

response = requests.get(url)
if response.status_code != 200:
    print("Failed to retrieve the page")
    exit()

soup = BeautifulSoup(response.text, 'html.parser')

repos = []

# Each repo is under article with class 'Box-row'
for repo in soup.find_all('article', class_='Box-row'):
    title_tag = repo.h2.a
    repo_name = title_tag.text.strip().replace('\n', '').replace(' ', '')
    repo_url = 'https://github.com' + title_tag['href'].strip()
    description_tag = repo.p
    description = description_tag.text.strip() if description_tag else ''
    star_tag = repo.find('a', href=lambda x: x and x.endswith('/stargazers'))
    stars = star_tag.text.strip() if star_tag else '0'

    # Simple ML filter: check keywords in description or repo name
    keywords = ['ml', 'machine learning', 'deep learning', 'tensorflow', 'pytorch', 'transformer', 'llm', 'nlp']
    if any(keyword.lower() in (description + repo_name).lower() for keyword in keywords):
        repos.append({
            'repo_name': repo_name,
            'description': description,
            'stars': stars,
            'url': repo_url
        })

# Save to CSV
df = pd.DataFrame(repos)
df.to_csv('data/github_trending_ml.csv', index=False)
print(f"Saved {len(repos)} GitHub trending ML repos to data/github_trending_ml.csv")
