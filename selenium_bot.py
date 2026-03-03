import csv
import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

BASE_URL = "http://127.0.0.1:5000"
USERNAME = "admin"
PASSWORD = "1234"

BASE_DIR = os.path.dirname(__file__)
CSV_PATH = os.path.join(BASE_DIR, "products.csv")

REQUIRED_HEADERS = ["code", "brand", "type", "category", "unit_price", "cost", "notes"]

def clear_and_type(el, value):
    el.clear()
    el.send_keys("" if value is None else str(value))

def read_products(path: str):
    # utf-8-sig removes BOM if present
    with open(path, newline="", encoding="utf-8-sig") as f:
        sample = f.read(2048)
        f.seek(0)

        # Detect comma vs semicolon
        try:
            dialect = csv.Sniffer().sniff(sample, delimiters=",;")
        except csv.Error:
            dialect = csv.get_dialect("excel")

        reader = csv.DictReader(f, dialect=dialect)

        if not reader.fieldnames:
            raise ValueError("CSV has no header row.")

        headers = [h.strip() for h in reader.fieldnames]
        missing = [h for h in REQUIRED_HEADERS if h not in headers]
        if missing:
            raise ValueError(
                f"Missing required headers: {missing}\n"
                f"Found headers: {headers}\n"
                f"Expected exactly: {REQUIRED_HEADERS}"
            )

        rows = list(reader)
        if not rows:
            raise ValueError("CSV has header but no data rows.")

        print("✅ CSV OK")
        print("Headers:", headers)
        print("Rows:", len(rows))
        print("First row preview:", rows[0])
        return rows

def main():
    if not os.path.exists(CSV_PATH):
        raise FileNotFoundError(f"CSV not found at: {CSV_PATH}")

    rows = read_products(CSV_PATH)

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    wait = WebDriverWait(driver, 15)

    try:
        # Login
        driver.get(f"{BASE_URL}/login")
        wait.until(EC.presence_of_element_located((By.ID, "username")))
        driver.find_element(By.ID, "username").send_keys(USERNAME)
        driver.find_element(By.ID, "password").send_keys(PASSWORD)
        driver.find_element(By.ID, "btn-login").click()

        # Wait for products page
        wait.until(EC.presence_of_element_located((By.ID, "code")))

        count = 0
        for row in rows:
            # These IDs MUST match templates/products.html
            clear_and_type(driver.find_element(By.ID, "code"), row["code"])
            clear_and_type(driver.find_element(By.ID, "brand"), row["brand"])
            clear_and_type(driver.find_element(By.ID, "product_type"), row["type"])
            clear_and_type(driver.find_element(By.ID, "category"), row["category"])
            clear_and_type(driver.find_element(By.ID, "unit_price"), row["unit_price"])
            clear_and_type(driver.find_element(By.ID, "cost"), row["cost"])
            clear_and_type(driver.find_element(By.ID, "notes"), row["notes"])

            driver.find_element(By.ID, "btn-save").click()

            # Wait for reload
            wait.until(EC.presence_of_element_located((By.ID, "code")))

            count += 1
            if count % 25 == 0:
                print(f"Registered: {count}")

            time.sleep(0.05)

        print(f"✅ Done! Total registered: {count}")

    finally:
        time.sleep(2)
        driver.quit()

if __name__ == "__main__":
    main()