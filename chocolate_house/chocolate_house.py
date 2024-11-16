import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

DB_FILE = "chocolate_house.db"


# Initialize the database
def init_db():
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()

        # Seasonal flavor offerings table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS seasonal_flavors (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                flavor_name TEXT NOT NULL,
                description TEXT
            )
        """)

        # Ingredient inventory table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS ingredients (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ingredient_name TEXT NOT NULL,
                stock INTEGER NOT NULL
            )
        """)

        # Customer suggestions and allergy concerns table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS customer_feedback (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                customer_name TEXT,
                flavor_suggestion TEXT,
                allergy_concern TEXT
            )
        """)

        conn.commit()


@app.route('/flavors', methods=['GET', 'POST'])
def manage_flavors():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    if request.method == 'POST':
        data = request.get_json()
        flavor_name = data.get("flavor_name")
        description = data.get("description")

        cursor.execute("INSERT INTO seasonal_flavors (flavor_name, description) VALUES (?, ?)",
                       (flavor_name, description))
        conn.commit()
        return jsonify({"message": "Flavor added successfully"}), 201

    elif request.method == 'GET':
        cursor.execute("SELECT * FROM seasonal_flavors")
        flavors = cursor.fetchall()
        return jsonify(flavors)


@app.route('/ingredients', methods=['GET', 'POST'])
def manage_ingredients():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    if request.method == 'POST':
        data = request.get_json()
        ingredient_name = data.get("ingredient_name")
        stock = data.get("stock")

        cursor.execute("INSERT INTO ingredients (ingredient_name, stock) VALUES (?, ?)",
                       (ingredient_name, stock))
        conn.commit()
        return jsonify({"message": "Ingredient added successfully"}), 201

    elif request.method == 'GET':
        cursor.execute("SELECT * FROM ingredients")
        ingredients = cursor.fetchall()
        return jsonify(ingredients)


@app.route('/feedback', methods=['POST'])
def handle_feedback():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    data = request.get_json()
    customer_name = data.get("customer_name")
    flavor_suggestion = data.get("flavor_suggestion")
    allergy_concern = data.get("allergy_concern")

    cursor.execute("""
        INSERT INTO customer_feedback (customer_name, flavor_suggestion, allergy_concern)
        VALUES (?, ?, ?)
    """, (customer_name, flavor_suggestion, allergy_concern))

    conn.commit()
    return jsonify({"message": "Feedback submitted successfully"}), 201


if __name__ == '__main__':
    init_db()
    app.run(debug=True)
