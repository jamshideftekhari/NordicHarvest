# models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Customer(db.Model):
    __tablename__ = 'Customer'
    idCustomer = db.Column(db.Integer, primary_key=True)
    CustomerTitle = db.Column(db.String(45), nullable=False)
    ContactName = db.Column(db.String(45), nullable=False)
    ContactEmail = db.Column(db.String(45), nullable=False)

    def __repr__(self):
        return f"<Customer {self.CustomerTitle}>"

    def to_dict(self):
        """Convert customer object to dictionary."""
        return {
            'idCustomer': self.idCustomer,
            'CustomerTitle': self.CustomerTitle,
            'ContactName': self.ContactName,
            'ContactEmail': self.ContactEmail
        }
