# Python REST API Example
This is a simple example of a Python CRUD REST API. I used the Flask framework, SQLite and Python 3.9.5. Installation and setup is outlined below. The API is documented afterwards.

# Installation and Setup
- Create an application directory and clone the repository into that directory
  - mkdir apitest
  - cd apitest
  - git clone git@github.com:onedeadgod/apitesting.git .
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
