# Search-Engine

## 📌 Project Overview

This is a simple web-based search engine built with Flask. It allows users to search for terms across a list of URLs stored in a CSV file. The application scrapes content from those URLs, indexes the words, and provides a basic search functionality.

---

## 🚀 Features

- Web interface with search functionality.
- Scrapes and indexes URL content.
- Highlights matched search terms.
- Lightweight and easy to deploy via Docker.
- Organized and containerized backend with Docker and Docker Compose.

---

## 🛠 Tech Stack

- *Frontend:* HTML/CSS (Jinja2 templating)
- *Backend:* Python, Flask
- *Scraping:* BeautifulSoup, Requests
- *Database:* SQLite
- *Containerization:* Docker, Docker Compose

---

## 📁 Folder Structure


search-engine/
├── app.py
├── database.py
├── scraper.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── templates/
│   ├── index.html
│   └── results.html
└── urls.csv


---

## ⚙ Setup Instructions

### ✅ Run Locally

1. *Install dependencies:*

   bash
   pip install -r requirements.txt
   

2. *Start the Flask app:*

   bash
   python app.py
   

3. *Open your browser:*  
   Go to http://127.0.0.1:5000

---

### 🐳 Run with Docker

1. *Build Docker image:*

   bash
   docker build -t search-engine .
   

2. *Run container:*

   bash
   docker run -p 5000:5000 search-engine
   

---

### 🧩 Run with Docker Compose

1. *Start services:*

   bash
   docker-compose up
   

2. *Access the app at:*  
   [http://localhost:5000](http://localhost:5000)

---

## 🐙 DockerHub

The Docker image is available at:  
https://hub.docker.com/repository/docker/daliamostafa/search_engine/general

---

## 👨‍💻 Team
-Mariam Adel Abass
-Basmallah Emad Hassan
-Dalia Mostafa Zaki
-Waleed Mohamed Abdelhamed
-Youssef Mahmoud Ragab
