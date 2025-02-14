# Task Manager

This is a simple Task Manager application built with FastAPI and MongoDB. It allows users to create, read, update, and delete tasks through a web interface.

# Features

Create new tasks with a title, description, and file name
<br>

View a list of all tasks
<br>

Update task details (title, description, file name)
<br>

Delete tasks
<br>

Store tasks in a MongoDB database

# Prerequisites

Before running the application, ensure you have the following installed:

Python
<br>

# Installation
Clone or Download the repository 
<br>
Navigate to the project directory
<br>
# Create a virtual environment (optional but recommended):
python -m venv venv
# Activate the virtual environment:
For Windows:
venv\Scripts\activate
<br>
For Unix/Linux:
source venv/bin/activate
# Install the dependencies:
pip install -r requirements.txt
# Set up the MongoDB connection:
replacing your-connection-string from MongoDB Cloud with your actual MongoDB connection string in MongoClient in main.py file
# Usage

Start the FastAPI server:
uvicorn main:app --reload
<br>
Open your web browser and visit http://localhost:8000 to access the Task Manager application.
<br>
Use the provided interface to create, view, update, and delete tasks.

