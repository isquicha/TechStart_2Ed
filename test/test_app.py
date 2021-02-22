def test_app_is_created(app):
    assert app.name == "src.app"


def test_config_debug(config):
    assert config.get("DEBUG") is False


def test_db_is_in_memory(config):
    assert config.get("SQLALCHEMY_DATABASE_URI") == "sqlite:///:memory:"
