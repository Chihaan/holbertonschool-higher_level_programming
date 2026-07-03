#!/usr/bin/python3

from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/items')
def items():
    with open('items.json', 'r') as f:
        data = json.load(f)
    return render_template('items.html', items=data.get("items", []))


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    if source == 'csv':
        with open('products.csv', 'r') as f:
            reader = csv.DictReader(f)
            products = list(reader)
    elif source == 'json':
        with open('products.json', 'r') as f:
            products = json.load(f)
    elif source == 'sql':
        try:
            conn = sqlite3.connect('products.db')
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute(
                'SELECT id, name, category, price '
                'FROM Products'
            )
            rows = cursor.fetchall()
            conn.close()
        except sqlite3.Error:
            return render_template('product_display.html',
                                   error="Database error")
        products = [dict(row) for row in rows]
    else:
        return render_template('product_display.html', error="Wrong source")
    if product_id:
        products = [p for p in products if int(p["id"]) == product_id]
        if not products:
            return render_template('product_display.html',
                                   error="Product not found")
    return render_template('product_display.html', products=products)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
