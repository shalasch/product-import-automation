from flask import Flask, render_template, request, redirect, url_for, session, flash
from functools import wraps
import sqlite3
import os

app = Flask(__name__)
app.secret_key = "dev-secret-key"  # local training only

DB_PATH = os.path.join(os.path.dirname(__file__), "db.sqlite3")

# Fixed credentials for training
USERNAME = "admin"
PASSWORD = "1234"


def init_db():
    with sqlite3.connect(DB_PATH) as con:
        con.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                code TEXT,
                brand TEXT,
                product_type TEXT,
                category TEXT,
                unit_price TEXT,
                cost TEXT,
                notes TEXT
            )
        """)
        con.commit()


def login_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if not session.get("logged_in"):
            return redirect(url_for("login"))
        return fn(*args, **kwargs)
    return wrapper


@app.route("/", methods=["GET"])
def home():
    return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form.get("username", "")
        pwd = request.form.get("password", "")

        if user == USERNAME and pwd == PASSWORD:
            session["logged_in"] = True
            return redirect(url_for("products"))

        flash("Invalid username or password.")
        return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


@app.route("/products", methods=["GET"])
@login_required
def products():
    with sqlite3.connect(DB_PATH) as con:
        cur = con.execute("""
            SELECT code, brand, product_type, category, unit_price, cost, notes
            FROM products
            ORDER BY id DESC
            LIMIT 50
        """)
        rows = cur.fetchall()

    return render_template("products.html", rows=rows)


@app.route("/products/save", methods=["POST"])
@login_required
def save_product():
    data = {
        "code": request.form.get("code", ""),
        "brand": request.form.get("brand", ""),
        "product_type": request.form.get("product_type", ""),
        "category": request.form.get("category", ""),
        "unit_price": request.form.get("unit_price", ""),
        "cost": request.form.get("cost", ""),
        "notes": request.form.get("notes", ""),
    }

    with sqlite3.connect(DB_PATH) as con:
        con.execute("""
            INSERT INTO products (code, brand, product_type, category, unit_price, cost, notes)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            data["code"],
            data["brand"],
            data["product_type"],
            data["category"],
            data["unit_price"],
            data["cost"],
            data["notes"],
        ))
        con.commit()

    return redirect(url_for("products"))


if __name__ == "__main__":
    init_db()
    app.run(host="127.0.0.1", port=5000, debug=True)