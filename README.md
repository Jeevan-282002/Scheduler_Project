# Scheduler_Project

TECHNOLOGY USED:

The Scheduler_Project is created in the Django framework with Python and other front-end technologies.
A default SQLite database is used.

REQUIREMENTS:

>> pip install django

CREDENTIALS:

Admin username: "admin"
Admin Password: "admin"

User name: Can be declared on the spot
User password: Can be declared on the spot


instructions followed:
1. admin can see a list of all Instructors (You can add random users)
2.  2. admin can add courses Course will have the following details
        a. Name
        b. Level
        c. Description
        d. Image
        e. Multiple Lectures (batches) -> can be added after the course is added. as one course can have multiple batches 
 
3. These lectures could be assigned to any instructor on any particular date. Once a lecture is assigned to an instructor on a particular date, The admin panel shouldn’t allow the instructor to be assigned to any other lecture on that date.
4. When a course is added the dates will be assigned to the selected instructor.
5. No other course can be assigned to that instructor on the same date again.
