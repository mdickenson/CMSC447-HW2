# Running Instructions #
Pull all files from github
Ensure you are in the correct directory

Run the following commands:
source venv/bin/activate (on mac) or venv\Scripts\activate (on windows)
virtualenv venv
pip install flask
python app.py

Open the website it says --> http://127.0.0.1:5000

# Overview #
I made a simple user management CURD application which allows you to add new users, search for existing users, and it also displays a list of users with their details in a table.

# Features $
Add User: Input name, ID, and points of a new user and add them to the system
Search User: Users can search for existing users by entering their name or ID
Display Users: Users are displayed in a table format with columns for their details
Delete User: There is a delete button in the table which allows to delete users
Buttons Darken when hovered over