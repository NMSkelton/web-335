/*
	Title: skelton-aggregates.js
  Author: Nicholas Skelton
  Date: 21 February 2026
  Description: Hands-On 6.1: Aggregate Queries
 */

// a. Display all students
db.students.find()

// b. Add a new student (done on multiple lines)
/*
student = {
... firstName: "Mariel",
... lastName: "Feathers",
... studentId: "s1019",
... houseId: "h1010"
... }
*/

db.students.insertOne(student)

// c. Update a property
db.students.updateOne({studentId:"s1019"},{$set:{houseId:"h1007"}});

// d. Delete the created student
db.students.deleteOne({studentId: "s1019"});

// e. Display all students by house
db.houses.aggregate([{ $lookup: { from: "students", localField: "houseId", foreignField: "houseId", as: "students_by_house" } }]);

// f. Display all students in house Gryffindor
db.houses.aggregate([ {$match: {"houseId": "h1007"}}, {$lookup: {from: "students", localField: "houseId", foreignField: "houseId", as: "students_in_gryffindor" } }]);

// g. Display all students in house with an eagle mascot
db.houses.aggregate([ {$match: {"mascot": "Eagle"}}, {$lookup: {from: "students", localField: "houseId", foreignField: "houseId", as: "eagle_students" } }]);