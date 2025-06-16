Pizza Restaurant API
A RESTful API for a Pizza Restaurant built using Flask, SQLAlchemy, and Flask-Migrate. This API allows you to manage restaurants, pizzas, and the many-to-many relationship between them using a join table called RestaurantPizza.

📁 Project Structure
bash
Copy
Edit
.
├── server/
│   ├── app.py                    # Flask app and setup
│   ├── config.py                 # Database configuration
│   ├── seed.py                   # Database seeding script
│   ├── models/
│   │   ├── __init__.py
│   │   ├── restaurant.py         # Restaurant model
│   │   ├── pizza.py              # Pizza model
│   │   └── restaurant_pizza.py   # Join table model with validation
│   ├── controllers/
│   │   ├── __init__.py
│   │   ├── restaurant_controller.py
│   │   ├── pizza_controller.py
│   │   └── restaurant_pizza_controller.py
├── migrations/                   # Flask-Migrate directory
├── challenge-1-pizzas.postman_collection.json
└── README.md

Setup Instructions

1. Clone the repository
git clone https://github.com/Ayub-002/Pizza-Restaurants

2. Install dependencies
pipenv install flask flask_sqlalchemy flask_migrate
pipenv shell

3. Set environment variable
export FLASK_APP=server/app.py

4. Run database migrations
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

5. Seed the database
python server/seed.py

📡 API Routes
🍽 Restaurants
GET /restaurants

Returns all restaurants.

GET /restaurants/<id>

Returns a single restaurant with its pizzas.
If not found, returns:

json
Copy
Edit
{ "error": "Restaurant not found" }
DELETE /restaurants/<id>

Deletes a restaurant and all related RestaurantPizza entries.

Success: 204 No Content

Error:

json
Copy
Edit
{ "error": "Restaurant not found" }
🍕 Pizzas
GET /pizzas

Returns all pizzas.

🔗 Restaurant Pizzas
POST /restaurant_pizzas

Create a new relationship between a restaurant and a pizza.

Request:

json
Copy
Edit
{
  "price": 5,
  "pizza_id": 1,
  "restaurant_id": 2
}
Success Response:

json
Copy
Edit
{
  "id": 4,
  "price": 5,
  "pizza_id": 1,
  "restaurant_id": 2,
  "pizza": {
    "id": 1,
    "name": "Emma",
    "ingredients": "Dough, Tomato Sauce, Cheese"
  },
  "restaurant": {
    "id": 2,
    "name": "Kiki's Pizza",
    "address": "456 Cheese Blvd"
  }
}
Error Response (Invalid price):

json
Copy
Edit
{
  "errors": ["Price must be between 1 and 30"]
}
🔍 Validations
RestaurantPizza.price must be between 1 and 30, otherwise a 400 Bad Request is returned.

📬 Postman Testing
Open Postman

Import the file challenge-1-pizzas.postman_collection.json

Run and test all the API endpoints with sample data

✅ Submission Checklist
 MVC folder structure

 Models with validations and relationships

 Routes implemented and functional

 Postman collection included

 Well-written README.md

🛠 Built With
Flask

SQLAlchemy

Flask-Migrate

SQLite (default)

Postman (for testing)