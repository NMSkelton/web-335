"""
    Title: skelton_usersp2.py
    Author: Nicholas Skelton
    Date: 26 February 2026
    Description: Hands-On 5.2: Python with MongoDB, Part II
"""

from pymongo import MongoClient
import datetime

# Build connection string
client = MongoClient(
    "mongodb+srv://web335_user:s3cret@bellevueuniversity.rjec3e0.mongodb.net/"
    "web335DB?retryWrites=true&w=majority"
)

# Access the database
db = client["web335DB"]

# Create new user document
print("Display newly created user")

muldoon = {
  "firstName": "Robert",
  "lastName": "Muldoon",
  "employeeId": "1051",
  "email": "stupidraptors@ingen.com",
  "dateCreated": datetime.datetime.now(datetime.UTC)
}

# Insert the document into the users collection
muldoon_user_id = db.users.insert_one(muldoon).inserted_id
print(muldoon_user_id)

# Prove the insert worked by searching the collection for the document
print(db.users.find_one({"employeeId": "1051"}))



# Create an update query to change the user's email address
print("Display updated email for new user")

db.users.update_one(
  {"employeeId": "1051"},
  {
    "$set": {
      "email": "cl3v3rg1rl@ingen.com"
    }
  }
)

# Prove the update worked by searching the collection for the user by employeeId
print(db.users.find_one({"employeeId": "1051"}))



# Delete the new user document
print("Display deleted new user")

result = db.users.delete_one({
  "employeeId": "1051"
})

# Display the results of the query
print(result)

# Prove the delete worked by searching the collection for the deleted document
print(db.users.find_one({"employeeId": "1051"}))

