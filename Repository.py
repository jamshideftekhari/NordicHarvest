import mysql.connector
from mysql.connector import Error

class UserRepository:
    """Repository class to handle user-related database operations."""

    def __init__(self, host, user, password, database):
        """Initialize the database connection."""
        try:
            self.connection = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )
            if self.connection.is_connected():
                print("Connected to the database")
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            self.connection = None

    def create_user(self, title, name, email):
        """Create a new user in the database."""
        try:
            cursor = self.connection.cursor()
            query = "INSERT INTO Customer (CustomerTitle, ContactName, ContactEmail) VALUES (%s, %s, %s)"
            cursor.execute(query, (title, name, email))
            self.connection.commit()
            print(f"User '{name}' added successfully.")
        except Error as e:
            print(f"Failed to insert user: {e}")

    def get_user_by_id(self, user_id):
        """Retrieve a user by their ID."""
        try:
            cursor = self.connection.cursor()
            query = "SELECT idCustomer, CustomerTitle, ContactName, ContactEmail FROM customer WHERE idCustomer = %s"
            cursor.execute(query, (user_id,))
            return cursor.fetchone()
        except Error as e:
            print(f"Failed to get user by ID: {e}")
            return None

    def get_all_users(self):
        """Retrieve all users from the database."""
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM Customer"
            cursor.execute(query)
            return cursor.fetchall()
        except Error as e:
            print(f"Failed to retrieve users: {e}")
            return []

    def update_user_email(self, user_id, new_email):
        """Update the email of a user."""
        try:
            cursor = self.connection.cursor()
            query = "UPDATE users SET email = %s WHERE id = %s"
            cursor.execute(query, (new_email, user_id))
            self.connection.commit()
            print(f"User ID {user_id}'s email updated successfully.")
        except Error as e:
            print(f"Failed to update user email: {e}")

    def delete_user(self, user_id):
        """Delete a user by ID."""
        try:
            cursor = self.connection.cursor()
            query = "DELETE FROM users WHERE id = %s"
            cursor.execute(query, (user_id,))
            self.connection.commit()
            print(f"User ID {user_id} deleted successfully.")
        except Error as e:
            print(f"Failed to delete user: {e}")

    def __del__(self):
        """Close the database connection when the object is destroyed."""
        if self.connection is not None and self.connection.is_connected():
            self.connection.close()
            print("Database connection closed.")
