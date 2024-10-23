# app.py
from flask import Flask, request, jsonify
from Models import db, Customer
from config import Config
import pymysql
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)

# Initialize SQLAlchemy
db.init_app(app)
#db=SQLAlchemy(app)

@app.before_request
def create_tables():
    db.create_all()

# GET: Fetch all customers
@app.route('/api/customers', methods=['GET'])
def get_customers():
    customers = Customer.query.all()
    return jsonify([customer.to_dict() for customer in customers]), 200

# GET: Fetch a single customer by ID
@app.route('/api/customers/<int:id>', methods=['GET'])
def get_customer(id):
    customer = Customer.query.get_or_404(id)
    return jsonify(customer.to_dict()), 200

# POST: Create a new customer
@app.route('/api/customers', methods=['POST'])
def create_customer():
    data = request.json
    if not data or not all(key in data for key in ('CustomerTitle', 'ContactName', 'ContactEmail')):
        return jsonify({'message': 'Missing required fields'}), 400

    new_customer = Customer(
        CustomerTitle=data['CustomerTitle'],
        ContactName=data['ContactName'],
        ContactEmail=data['ContactEmail']
    )
    db.session.add(new_customer)
    db.session.commit()
    return jsonify(new_customer.to_dict()), 201

# PUT: Update an existing customer by ID
@app.route('/api/customers/<int:id>', methods=['PUT'])
def update_customer(id):
    customer = Customer.query.get_or_404(id)
    data = request.json

    if not data:
        return jsonify({'message': 'No input data provided'}), 400

    customer.CustomerTitle = data.get('CustomerTitle', customer.CustomerTitle)
    customer.ContactName = data.get('ContactName', customer.ContactName)
    customer.ContactEmail = data.get('ContactEmail', customer.ContactEmail)

    db.session.commit()
    return jsonify(customer.to_dict()), 200

# DELETE: Delete a customer by ID
@app.route('/api/customers/<int:id>', methods=['DELETE'])
def delete_customer(id):
    customer = Customer.query.get_or_404(id)
    db.session.delete(customer)
    db.session.commit()
    return jsonify({'message': 'Customer deleted successfully'}), 204

if __name__ == '__main__':
    app.run(debug=True)
