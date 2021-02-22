import pytest
from src.app import create_app
from src.extensions.database import db


@pytest.fixture(scope="module")
def app():
    app = create_app()
    with app.app_context():
        db.create_all()
    return app
