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
        methods=["GET", "PATCH", "DELETE"],
    )

    # * Products
    bp.add_url_rule(
        "/products/",
        defaults={"product_id": None},
        view_func=product_view,
        methods=["GET"],
    )
    bp.add_url_rule(
        "/products/",
        view_func=product_view,
        methods=["POST"],
    )
    bp.add_url_rule(
        "/products/<int:product_id>",
        view_func=product_view,
        methods=["GET", "PATCH", "DELETE"],
    )

    # * Categories
    bp.add_url_rule(
        "/categories/",
        defaults={"category_id": None},
        view_func=category_view,
        methods=["GET"],
    )
    bp.add_url_rule(
        "/categories/",
        view_func=category_view,
        methods=["POST"],
    )
    bp.add_url_rule(
        "/categories/<int:category_id>",
        view_func=category_view,
        methods=["GET", "PATCH", "DELETE"],
    )

    # * Marketplaces
    bp.add_url_rule(
        "/marketplaces/",
        defaults={"marketplace_id": None},
        view_func=marketplace_view,
        methods=["GET"],
    )
    bp.add_url_rule(
        "/marketplaces/",
        view_func=marketplace_view,
        methods=["POST"],
    )
    bp.add_url_rule(
        "/marketplaces/<int:marketplace_id>",
        view_func=marketplace_view,
        methods=["GET", "PATCH", "DELETE"],
    )
