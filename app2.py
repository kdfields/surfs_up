# 1. Import Flask
from flask import Flask, jsonify


# 2. Create an app
app = Flask(__name__)

# 3. Define index route
@app.route("/")
def home():
    return "Welcome to my API!"

# 4. Define the about route
@app.route("/about")
def about():
    return "Kyle Fields; Asheville, NC"

# 5. Define the contact route
@app.route("/contact")
def contact():
    return "email: kyle.fields@gmail.com"

# 6. Define main behavior

if __name__ == "__main__":
    app.run(debug=True)