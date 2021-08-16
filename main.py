"""
    Python CRUD REST API Example
    PyCharm Pro has special support for the Flask framework
"""
from flask import Flask, jsonify, request
import widgeter
from database import create_tables
from datetime import datetime

app = Flask(__name__)


@app.route('/widgets', methods=["GET"])
def get_widgets():
    widgets = widgeter.get_widgets()
    return jsonify(widgets)


@app.route("/widget", methods=["POST"])
def insert_widget():
    widget_details = request.get_json()
    name = widget_details["name"]
    part_count = widget_details["part_count"]
    created_date = datetime.now()
    result = widgeter.insert_widget(name, part_count, created_date)
    return jsonify(result)


@app.route("/widget", methods=["PUT"])
def update_widget():
    widget_details = request.get_json()
    id = widget_details["id"]
    name = widget_details["name"]
    part_count = widget_details["part_count"]
    update_date = datetime.now()
    result = widgeter.update_widget(id, name, part_count, update_date)
    return jsonify(result)


@app.route("/widget/<id>", methods=["DELETE"])
def delete_widget(id):
    result = widgeter.delete_widget(id)
    return jsonify(result)


@app.route("/widget/<id>", methods=["GET"])
def get_widget_by_id(id):
    widget = widgeter.get_by_id(id)
    return jsonify(widget)


"""
Enable CORS. Disable it if you don't need CORS
"""


@app.after_request
def after_request(response):
    response.headers[
        "Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    response.headers["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS, " \
                                                       "PUT, DELETE"
    response.headers[
        "Access-Control-Allow-Headers"] = "Accept, Content-Type, " \
                                          "Content-Length, Accept-Encoding, " \
                                          "X-CSRF-Token, Authorization "
    return response


if __name__ == "__main__":
    create_tables()
    app.run(host='0.0.0.0', port=8000, debug=True)
