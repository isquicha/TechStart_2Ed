from ..resources.user import UserAPI

user_view = UserAPI.as_view("user_api")


def init_app(bp):
    bp.add_url_rule(
        "/users/",
        defaults={"user_id": None},
        view_func=user_view,
        methods=[
            "GET",
        ],
    )
    bp.add_url_rule(
        "/users/",
        view_func=user_view,
        methods=[
            "POST",
        ],
    )
    bp.add_url_rule(
        "/users/<int:user_id>",
        view_func=user_view,
        methods=["GET", "DELETE"],
    )
