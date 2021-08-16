# Python REST API Example
This is a simple example of a Python CRUD REST API. I used the Flask framework, SQLite and Python 3.9.5. Installation and setup is outlined below. The API is documented afterwards.

Some things to note:
 - PEP8 Compliant

# Installation and Setup
- Clone the repository and change into the created project directory
  - git clone git@github.com:onedeadgod/apitesting.git
  - cd apitesting
- Create a virtual environment
  - python3 -m venv venv
- Activate the environment
  - . venv/bin/activate
- Install Flask
  - pip install Flask
- Run the application
  - python3 main.py

# API Usage
Key: /path/params [json params] {request type}

- Create a new widget
  - /widget [name, part_count] {POST}
- Update a widget 
  - /widget [id, name, part_count] {PUT}
- Delete a widget
  - /widget [id] {DELETE}
- Get a widget 
  - /widget/<id> {GET}
- Get all widgets
  - /widgets {GET}

# Parameter Specifications
  - name: string 64 characters max
  - part_count: integer
  - id: integer
