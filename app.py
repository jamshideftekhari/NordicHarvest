from flask import Flask, request, jsonify
#from flask_cors import CORS
from Repository import UserRepository

# Replace with your database credentials
db_host = "localhost"
db_user = "root"
db_password = "jam2003eft"
db_name = "nordicharvest"

# Initialize the repository
user_repo = UserRepository(host=db_host, user=db_user, password=db_password, database=db_name)

app = Flask(__name__)
#CORS(app)

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/api/user', methods=['POST'])
def create_user():
    data = request.get_json()
    #user_repo.create_user(data['title'], data['name'], data['email'])
    return jsonify({"message": "User created successfully."})

@app.route('/api/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    #user = user_repo.get_user_by_id(user_id)
    user = user_repo.get_user_by_id(user_id)
    return jsonify({"user": user})  # user is a tuple

app.run(port=5000)