# Product Import Automation (CSV → Selenium → Web Form → SQLite)

This project demonstrates a real-world automation workflow that imports products from a CSV dataset, automatically fills a web form using Selenium, and stores the data in a SQLite database through a local Flask application.

The goal of this project is to simulate a common business scenario: registering hundreds of products into a system without manual data entry.

---

# Overview

Manual product registration in admin systems is slow, repetitive, and error-prone.

This automation solves that by:

1. Reading product data from a CSV file  
2. Automatically opening a browser  
3. Logging into a web system  
4. Filling product registration forms  
5. Submitting the data  
6. Saving the results in a database  

The automation can register hundreds of products in seconds.

---

# Tech Stack

- Python  
- Selenium  
- Flask  
- SQLite  
- WebDriver Manager  
- CSV Processing  

---

# Project Structure

```
fake_store/
│
├── app.py
├── selenium_bot.py
├── generate_products.py
├── products.csv
├── requirements.txt
├── README.md
│
├── templates
│   ├── login.html
│   └── products.html
│
└── db.sqlite3
```

---

# Features

✔ Automated browser interaction using Selenium  
✔ CSV product dataset import  
✔ Local login system (Flask)  
✔ Web form automation  
✔ Automatic database storage  
✔ Scalable for hundreds of records  
✔ Realistic automation workflow  

---

# Example Dataset

```
code,brand,type,category,unit_price,cost,notes
CAHA000252,Hashtag,Shirt,2,25.00,11.00,Check stock
MOMU000111,Multilaser,Mouse,1,19.99,3.40,
BOHA000251,Hashtag,Cap,1,25.00,11.00,
```

Each row represents a product to be registered automatically.

---

# How the Automation Works

CSV file  
↓  
Python script reads rows  
↓  
Selenium opens browser  
↓  
Bot logs into system  
↓  
Bot fills product form  
↓  
Form is submitted  
↓  
Data stored in SQLite database  

---

# Setup

## Install Python

Make sure Python 3.9+ is installed.

Check with:

```
python --version
```

---

## Install dependencies

```
pip install -r requirements.txt
```

---

# Running the Project

## Start the web application

```
python app.py
```

Open in your browser:

```
http://127.0.0.1:5000/login
```

Login credentials (demo):

```
username: admin
password: 1234
```

---

## Generate sample product dataset (optional)

```
python generate_products.py
```

---

## Run the automation bot

Open a second terminal and run:

```
python selenium_bot.py
```

The bot will:

- open the browser  
- log into the system  
- register products automatically  

---

# Database

All products are stored in a SQLite database.

Database file:

```
db.sqlite3
```

Table:

```
products
```

You can inspect the database using **DB Browser for SQLite**.

---

# Why This Project Matters

This project demonstrates key automation skills used in real business systems:

- automating repetitive tasks  
- browser automation  
- data import pipelines  
- backend integration  
- database persistence  

It replicates a workflow commonly used in:

- ERP systems  
- e-commerce admin panels  
- inventory systems  
- internal business tools  

---

# Future Improvements

• Direct CSV import via backend (no Selenium)  
• Import progress tracking  
• Validation and error handling  
• REST API for product imports  
• Admin dashboard for uploads  

---

# Author

Automation project created for portfolio demonstration.

Technologies used reflect real-world automation scenarios combining Python scripting, web automation, and backend systems.