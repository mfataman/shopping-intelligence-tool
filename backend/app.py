from flask import Flask


def create_app():
    app = Flask(__name__)

    # Error handlers
    @app.errorhandler(404)
    def not_found(error):
        return {'message': 'Not found'}, 404

    @app.errorhandler(500)
    def internal_error(error):
        return {'message': 'Internal server error'}, 500

    # Register Blueprints
    from .blueprint import example_blueprint
    app.register_blueprint(example_blueprint)

    return app
