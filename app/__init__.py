from flask import Flask


def create_app(test_config: dict | None = None) -> Flask:
    """Create and configure the portfolio application."""
    app = Flask(__name__)

    if test_config:
        app.config.from_mapping(test_config)

    from .routes import main

    app.register_blueprint(main)
    return app
