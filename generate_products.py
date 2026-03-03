import csv
import random

brands = [
"Apple","Samsung","Sony","LG","Dell","HP","Lenovo","Asus",
"Xiaomi","Philips","Panasonic","Toshiba","Garmin","Logitech"
]

types = [
"Laptop","Monitor","Keyboard","Mouse","Headphones",
"Smartphone","Tablet","Smartwatch","TV","Speaker"
]

notes = [
"",
"New model",
"Limited stock",
"Seasonal item",
"Supplier discount",
"New arrival"
]

rows = []

for i in range(300):

    code = f"P{i:05d}"

    brand = random.choice(brands)

    product_type = random.choice(types)

    category = random.randint(1,5)

    price = round(random.uniform(50,2000),2)

    cost = round(price * random.uniform(0.4,0.7),2)

    note = random.choice(notes)

    rows.append([
        code,
        brand,
        product_type,
        category,
        price,
        cost,
        note
    ])

with open("products.csv","w",newline="",encoding="utf-8") as f:

    writer = csv.writer(f)

    writer.writerow([
        "code","brand","type","category","unit_price","cost","notes"
    ])

    writer.writerows(rows)

print("300 products generated")