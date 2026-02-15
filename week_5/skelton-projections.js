/*
	Title: skelton-projections.js
  Author: Nicholas SKelton
  Date: 15 February 2026
  Description: Hands-On 5.1: MongoDB Document Manipulation and Projections
 */


// Add a new user

/*
This was the code as typed, using multiple lines hence the (...). Copying and pasting with those dots gave errors, so it's commented out.

Atlas atlas-13bzsw-shard-0 [primary] web335DB> user = {
... firstName: "Pyotr",
... lastName: "Tchaikovsky",
... employeeId: "1013",
... email: "thetchaiguy@hotmail.com",
... dateCreated: new Date()
... };
*/

db.users.insertOne(user);

// Update email address
db.users.updateOne({employeeId:"1009"},{$set:{email:"mozart@me.com"}});

// Display all users first names, last names, and emails
db.users.find({}, {firstName:1, lastName: 1, email: 1});