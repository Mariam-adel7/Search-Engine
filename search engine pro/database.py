# inverted_index.py

import sqlite3
import re
from scraper import scrape_url
import openpyxl
import csv


def search_word(query):
    results = []
    query_words = query.lower().strip().split()

    with open('urls.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            if row:
                row_strs = [cell.lower().strip() for cell in row if cell]
                if all(any(word in cell for cell in row_strs) for word in query_words):
                    results.append(row)
    return results


def tokenize(text):
    return re.findall(r'\b\w+\b', text.lower())

def build_index(urls):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute('''
        CREATE TABLE IF NOT EXISTS urls (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT UNIQUE,
            title TEXT
        )
    ''')

    c.execute('''
        CREATE TABLE IF NOT EXISTS inverted_index (
            word TEXT,
            url_id INTEGER,
            FOREIGN KEY(url_id) REFERENCES urls(id)
        )
    ''')

    for url in urls:
        data = scrape_url(url)
        if not data: continue

        c.execute("INSERT OR IGNORE INTO urls (url, title) VALUES (?, ?)", (data['url'], data['title']))
        c.execute("SELECT id FROM urls WHERE url = ?", (data['url'],))
        url_id = c.fetchone()[0]

        words = set(tokenize(data['content']))
        for word in words:
            c.execute("INSERT INTO inverted_index (word, url_id) VALUES (?, ?)", (word, url_id))

        print(f"✔ Indexed: {url}")

    conn.commit()
    conn.close()

