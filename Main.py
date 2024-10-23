from Repository import UserRepository

# Replace with your database credentials
db_host = "localhost"
db_user = "root"
db_password = "jam2003eft"
db_name = "nordicharvest"

# Initialize the repository
user_repo = UserRepository(host=db_host, user=db_user, password=db_password, database=db_name)

# Create a new user
user_repo.create_user("Salling", "john_doe", "john.doe@example.com")

# Get a user by ID
user = user_repo.get_user_by_id(1)
print("User with ID 1:", user)

# Get all users
users = user_repo.get_all_users()
print("All users:", users)

# Update user email
#user_repo.update_user_email(1, "new_email@example.com")

# Delete a user
#user_repo.delete_user(1)
