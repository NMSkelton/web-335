"""
    Title: skelton_usersp1.py
    Author: Nicholas Skelton
    Date: 21 February 2026
    Description: Hands-On 4.2: Python with MongoDB, Part I
"""

from pymongo import MongoClient

# Build connection string
client = MongoClient(
    "mongodb+srv://web335_user:s3cret@bellevueuniversity.rjec3e0.mongodb.net/"
    "web335DB?retryWrites=true&w=majority"
)

# Access the database
db = client["web335DB"]

# Display all documents in user's collection

print("Display all users in the document")
for user in db.users.find():
    print(user)

# Display employee with the ID of 1011

print("Display employee with ID 1011")
print(db.users.find_one({"employeeId": "1011"}))

# Display employee with the last name of Mozart

print("Display employee with last name Mozart")
print(db.users.find_one({"lastName": "Mozart"}))