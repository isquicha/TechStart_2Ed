from ..resources.marketplace import (
    ProductAPI,
    SellerAPI,
    CategoryAPI,
    MarketplaceAPI,
)

product_view = ProductAPI.as_view("product_api")
category_view = CategoryAPI.as_view("category_api")
seller_view = SellerAPI.as_view("seller_api")
marketplace_view = MarketplaceAPI.as_view("marketplace_api")


def init_app(bp):
    # * Sellers
    bp.add_url_rule(
        "/sellers/",
        defaults={"seller_id": None},
        view_func=seller_view,
        methods=["GET"],
    )
    bp.add_url_rule(
        "/sellers/",
        view_func=seller_view,
        methods=["POST"],
    )
    bp.add_url_rule(
        "/sellers/<int:seller_id>",
        view_func=seller_view,
        methods=["GET", "PUT", "DELETE"],
    )
