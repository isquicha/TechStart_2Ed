from flask_simplelogin import SimpleLogin
from werkzeug.security import check_password_hash, generate_password_hash
from src.extensions.database import db
from src.models.user import User


def verify_login(user: dict) -> bool:
    """Validate username and password to verify user login


    Parameters
    ----------
    user : dict
        Must have `username` and `password` keys

    Returns
    -------
    bool
        True if username and password exists and are correct, False otherwise
    """
    username = user.get("username")
    password = user.get("password")
    if not username or not password:
        return False
    existing_user = User.query.filter_by(username=username).first()
    if not existing_user:
        return False
    if check_password_hash(existing_user.password, password):
        return True
    return False


def create_user(username: str, password: str, name: str = "") -> User:
    """Creates a new user


    Parameters
    ----------
    username : str
        The name that will be used to log in
    password : str
        The password that will be used to log in
    name : str, optional
        The name that will be displayed in panel, by default ''

    Returns
    -------
    User
        The new created user object

    Raises
    ------
    RuntimeError
        If the username is already registered
    """
    if User.query.filter_by(username=username).first():
        raise RuntimeError(f"{username} already exists!")
    user = User(
        username=username, password=generate_password_hash(password), name=name
    )
    db.session.add(user)
    db.session.commit()
    return user


def init_app(app):
    SimpleLogin(app, login_checker=verify_login)
