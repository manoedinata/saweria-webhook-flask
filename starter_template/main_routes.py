from flask import Blueprint

main = Blueprint("main_routes", __name__)

@main.route("/")
def home():
    return "Hello, World!"
