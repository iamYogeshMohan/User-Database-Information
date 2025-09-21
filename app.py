from flask import Flask, request
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["users"]

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    age = request.form.get('age')
    blood_group = request.form.get('blood_group')
    phone = request.form.get('phone')
    email = request.form.get('email')

    # Basic validation
    if not (name and age and blood_group and phone and email):
        return "<h2 style='text-align:center;'>Please fill in all fields!</h2>"

    try:
        age = int(age)
    except ValueError:
        return "<h2 style='text-align:center;'>Invalid age format!</h2>"

    # Insert into MongoDB
    collection.insert_one({
        "name": name,
        "age": age,
        "blood_group": blood_group,
        "phone": phone,
        "email": email
    })

    

if __name__ == '__main__':
    app.run(debug=True)
