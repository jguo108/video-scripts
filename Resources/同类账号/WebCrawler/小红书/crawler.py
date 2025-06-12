import glob
import os
from bs4 import BeautifulSoup
import sys
import pandas as pd
from pathlib import Path

titles = []
counts = []
links = []

if len(sys.argv) < 2:
    print("Usage: python crawler.py <blogger>")
    exit()

blogger = sys.argv[1]

p = Path(blogger)
if not any(p.iterdir()):
    for i in range(10):
        with open(os.path.join(blogger, 'feeds' + str(i + 1) + '.html'), 'w') as f:
            pass

all_files = glob.glob(os.path.join(
    blogger, '**', '*.html'), recursive=True)

if not all_files:
    print("No HTML files found.")
    exit()

for file_path in all_files:
    html = ''
    # Open the file in read mode ('r' is default for text files)
    with open(file_path, 'r', encoding='utf-8') as file:
        # Read the entire content as a single string
        html = file.read()

    soup = BeautifulSoup(html, 'html.parser')

    for note in soup.find_all('section', class_='note-item'):
        link = note.find('a', class_='cover mask ld').get('href')
        link = "https://www.xiaohongshu.com/explore" + link[link.rfind('/'):]

        if link in links:
            continue

        links.append(link)

        footer = note.find('div', class_='footer')

        title = footer.find('a', class_='title').find(
            'span').get_text(strip=True)
        count = footer.find('span', class_='count').get_text(strip=True)

        if "赞" in count:
            continue

        if count[-1] == '万':
            num = count[:-1]
            count = str(int(float(num) * 10000))

        titles.append(title)
        counts.append(count)

        # print(link)
        # print(title)
        # print(count)

if len(links) == 0 or len(counts) == 0 or len(links) == 0:
    print("No data found.")
    exit()

combined = list(zip(counts, titles, links))
sorted_combined = sorted(combined, key=lambda x: int(x[0]), reverse=True)
counts, titles, links = zip(*sorted_combined)
counts = list(counts)
title = list(titles)
links = list(links)


df = pd.DataFrame({'Title': titles, 'Likes': counts, 'Link': links})
df.to_excel(os.path.join(blogger, "statistics.xlsx"),
            index=False, engine='openpyxl')

# df.to_csv(f'{blogger}.csv', index=False)
