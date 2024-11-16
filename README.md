# Chocolate-House
Setup Instructions:
1. Install Python (>= 3.7) and SQLite.
2. Install Flask: pip install flask.
3. Run the application: python chocolate_house.py.

Endpoints:
1. GET /flavors: Retrieve all seasonal flavors.
2. POST /flavors: Add a new flavor (JSON: {"flavor_name": "...", "description": "..."}).
3. GET /ingredients: Retrieve ingredient inventory.
4. POST /ingredients: Add ingredients (JSON: {"ingredient_name": "...", "stock": ...}).
5. POST /feedback: Submit feedback (JSON: {"customer_name": "...", "flavor_suggestion": "...", "allergy_concern": "..."}).

Test Steps:
1. Use Postman or similar tools to test the endpoints.
2. Verify the database using SQLite Browser to ensure data persistence.

Docker Instructions:
1. Build Docker Image: docker build -t chocolate-house .
2. Run Docker Container: docker run -p 5000:5000 chocolate-house.
