from flask import Flask

def create_app():
    app = Flask(__name__)

    # Main routes
    from starter_template.main_routes import main as main_routes
    app.register_blueprint(main_routes)

    return app
