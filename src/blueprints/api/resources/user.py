from flask import jsonify, request
from flask.views import MethodView
from flask_simplelogin import login_required

from src.extensions.authentication import create_user
from src.extensions.database import db
from src.models.user import User


class UserAPI(MethodView):
    @login_required
    def get(self, user_id):
        if user_id is None:
            users = []

            for user in User.query.all():
                users.append(
                    {
                        "id": user.id,
                        "username": user.username,
                        "name": user.name,
                    }
                )
            return jsonify(users)
        else:
            user = User.query.get(user_id)
            if user is None:
                return {"ERROR": "User does not exists"}
            return {
                "id": user.id,
                "username": user.username,
                "name": user.name,
            }

    @login_required
    def post(self):
        body = request.get_json()
        username = body.get("username", None)
        password = body.get("password", None)
        name = body.get("name", None)

        if username is None:
            return {"ERROR": "Field 'username' must not be empty"}
        if password is None:
            return {"ERROR": "Field 'password' must not be empty"}

        try:
            user = create_user(username=username, password=password, name=name)
            return {
                "id": user.id,
                "username": user.username,
                "name": user.name,
            }
        except RuntimeError:
            return {"ERROR": "Username already registered"}

    @login_required
    def delete(self, user_id):
        user = User.query.get(user_id)
        if user is None:
            return {"ERROR": "User does not exists"}

        user_info = {
            "id": user.id,
            "username": user.username,
            "name": user.name,
        }
        db.session.delete(user)
        db.session.commit()

        return jsonify({"deleted_user": user_info})
