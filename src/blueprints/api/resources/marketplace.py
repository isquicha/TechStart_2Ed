from flask import jsonify, request
from flask.views import MethodView

from src.extensions.database import db
from src.models.marketplace import Seller, Product, Category, Marketplace


class SellerAPI(MethodView):
    def get(self, seller_id):
        if seller_id is None:
            sellers = []

            for seller in Seller.query.all():
                sellers.append(
                    {
                        "id": seller.id,
                        "fantasy_name": seller.fantasy_name,
                        "company_name": seller.company_name,
                    }
                )

            return jsonify(sellers)

        seller = Seller.query.get(seller_id)
        if seller is None:
            return {"ERROR": "Seller does not exists"}, 400

        return jsonify(
            {
                "id": seller.id,
                "fantasy_name": seller.fantasy_name,
                "company_name": seller.company_name,
                "tax_code": seller.tax_code,
                "email": seller.email,
                "phone": seller.phone,
                "address": seller.address,
            }
        )

    def post(self):
        body = request.get_json()

        fantasy_name = body.get("fantasy_name", None)
        company_name = body.get("company_name", None)
        tax_code = body.get("tax_code", None)
        email = body.get("email", None)
        phone = body.get("phone", None)
        address = body.get("address", None)

        if fantasy_name is None:
            return {"ERROR": "Field 'fantasy_name' must not be empty"}, 400
        if company_name is None:
            return {"ERROR": "Field 'company_name' must not be empty"}, 400
        if tax_code is None:
            return {"ERROR": "Field 'tax_code' must not be empty"}, 400
        if email is None:
            return {"ERROR": "Field 'email' must not be empty"}, 400
        if phone is None:
            return {"ERROR": "Field 'phone' must not be empty"}, 400
        if address is None:
            return {"ERROR": "Field 'address' must not be empty"}, 400

        if Seller.query.filter_by(company_name=company_name).first():
            return {"ERROR": "Company name already registered"}, 400
        if Seller.query.filter_by(tax_code=tax_code).first():
            return {"ERROR": "Company tax code already registered"}, 400

        seller = Seller(
            fantasy_name=fantasy_name,
            company_name=company_name,
            tax_code=tax_code,
            email=email,
            phone=phone,
            address=address,
        )

        try:
            db.session.add(seller)
            db.session.commit()
        except Exception:
            return {"ERROR": "Seller could not be created"}, 500

        return {"id": seller.id, "fantasy_name": seller.fantasy_name}

    def put(self, seller_id):
        seller = Seller.query.get(seller_id)
        if seller is None:
            return {"ERROR": "Seller does not exists"}, 400

        body = request.get_json()

        try:
            seller.fantasy_name = body.get("fantasy_name", seller.fantasy_name)
            seller.company_name = body.get("company_name", seller.company_name)
            seller.tax_code = body.get("tax_code", seller.tax_code)
            seller.email = body.get("email", seller.email)
            seller.phone = body.get("phone", seller.phone)
            seller.address = body.get("address", seller.address)
            db.session.commit()
        except Exception:
            return {"ERROR": "Seller could not be updated"}, 500

        return jsonify(
            {
                "id": seller.id,
                "fantasy_name": seller.fantasy_name,
                "company_name": seller.company_name,
                "tax_code": seller.tax_code,
                "email": seller.email,
                "phone": seller.phone,
                "address": seller.address,
            }
        )

    def delete(self, seller_id):
        seller = Seller.query.get(seller_id)
        if seller is None:
            return {"ERROR": "Seller does not exists"}, 400

        seller_info = {
            "id": seller.id,
            "fantasy_name": seller.fantasy_name,
            "company_name": seller.company_name,
        }
        try:
            db.session.delete(seller)
            db.session.commit()
        except Exception:
            return {"ERROR": "Seller could not be deleted"}, 500

        return jsonify({"deleted_seller": seller_info})


class ProductAPI(MethodView):
    def get(self, product_id):
        if product_id is None:
            products = []

            for product in Product.query.all():
                products.append(
                    {
                        "id": product.id,
                        "name": product.name,
                        "price": product.price,
                    }
                )

            return jsonify(products)

        product = Product.query.get(product_id)
        if product is None:
            return {"ERROR": "Product does not exists"}, 400

        return jsonify(
            {
                "id": product.id,
                "name": product.name,
                "price": product.price,
                "description": product.description,
                "categories": [
                    {
                        "id": category.id,
                        "name": category.name,
                    }
                    for category in product.categories
                ],
            }
        )

    def post(self):
        body = request.get_json()

        name = body.get("name", None)
        price = body.get("price", None)
        description = body.get("description", None)
        categories = body.get("categories", None)

        if name is None:
            return {"ERROR": "Field 'name' must not be empty"}, 400
        if price is None:
            return {"ERROR": "Field 'price' must not be empty"}, 400
        if description is None:
            return {"ERROR": "Field 'description' must not be empty"}, 400

        try:
            price = float(price)
        except ValueError:
            return {"ERROR": "Field 'price' must be a float"}, 400

        errors = []
        categories_list = []
        if categories is not None:
            for category in categories:
                category_to_add = Category.query.get(category)
                if category_to_add is not None:
                    categories_list.append(category_to_add)
                else:
                    errors.append(
                        f"Category '{category}' not found. "
                        "Creating product without it"
                    )

        product = Product(
            name=name,
            price=price,
            description=description,
        )

        for category in categories_list:
            product.categories.append(category)

        try:
            db.session.add(product)
            db.session.commit()
        except Exception:
            return {"ERROR": "Product could not be created"}, 500

        if len(errors) > 0:
            return {
                "id": product.id,
                "name": product.name,
                "price": product.price,
                "errors": errors,
            }
        return {"id": product.id, "name": product.name, "price": product.price}

    def put(self, product_id):
        product = Product.query.get(product_id)
        if product is None:
            return {"ERROR": "Product does not exists"}, 400

        body = request.get_json()
        if body is None:
            return {"ERROR": "A request body must be provided"}, 400

        price = body.get("price", product.price)
        try:
            if price is not None:
                product.price = float(price)
        except ValueError:
            return {"ERROR": "Field 'price' must be a float"}, 400

        errors = []
        categories_to_add = body.get("categories_to_add", None)
        categories_to_remove = body.get("categories_to_remove", None)

        categories_list = []
        if categories_to_add is not None:
            for category in categories_to_add:
                category_to_add = Category.query.get(category)
                if category_to_add is not None:
                    categories_list.append(category_to_add)
                else:
                    errors.append(
                        f"Category '{category}' not found. "
                        "Not adding it to product"
                    )
            for category in categories_list:
                product.categories.append(category)

        categories_list = []
        if categories_to_remove is not None:
            for category in categories_to_remove:
                category_to_remove = Category.query.get(category)
                if category_to_remove is not None:
                    categories_list.append(category_to_remove)
                else:
                    errors.append(
                        f"Category '{category}' not found. "
                        "Not removing it to product"
                    )
            for category in categories_list:
                product.categories.remove(category)

        try:
            product.name = body.get("name", product.name)
            product.description = body.get("description", product.description)
            db.session.commit()
        except Exception:
            return {"ERROR": "Product could not be updated"}, 500

        if len(errors) > 0:
            return {
                "id": product.id,
                "name": product.name,
                "price": product.price,
                "errors": errors,
            }
        return {"id": product.id, "name": product.name, "price": product.price}

    def delete(self, product_id):
        product = Product.query.get(product_id)
        if product is None:
            return {"ERROR": "Product does not exists"}, 400

        product_info = {
            "id": product.id,
            "name": product.name,
            "price": product.price,
            "description": product.description,
            "categories": [
                {
                    "id": category.id,
                    "name": category.name,
                }
                for category in product.categories
            ],
        }

        try:
            db.session.delete(product)
            db.session.commit()
        except Exception:
            return {"ERROR": "Product could not be deleted"}, 500

        return {"deleted_product": product_info}


class CategoryAPI(MethodView):
    def get(self, category_id):
        if category_id is None:
            categories = []

            for category in Category.query.all():
                categories.append(
                    {
                        "id": category.id,
                        "name": category.name,
                        "description": category.description,
                    }
                )

            return jsonify(categories)

        category = Category.query.get(category_id)
        if category is None:
            return {"ERROR": "Category does not exists"}, 400

        return jsonify(
            {
                "id": category.id,
                "name": category.name,
                "description": category.description,
                "products": [
                    {
                        "id": product.id,
                        "name": product.name,
                    }
                    for product in category.products
                ],
            }
        )

    def post(self):
        body = request.get_json()

        if body is None:
            return {"ERROR": "A body must be provided"}

        name = body.get("name", None)
        description = body.get("description", None)
        products = body.get("products", None)

        if name is None:
            return {"ERROR": "Field 'name' must not be empty"}, 400
        if description is None:
            return {"ERROR": "Field 'description' must not be empty"}, 400

        errors = []
        products_list = []
        if products is not None:
            for product in products:
                product_to_add = Product.query.get(product)
                if product_to_add is not None:
                    products_list.append(product_to_add)
                else:
                    errors.append(
                        f"Product '{product}' not found. "
                        "Creating category without it"
                    )

        category = Category(
            name=name,
            description=description,
        )

        for product in products_list:
            category.products.append(product)

        try:
            db.session.add(category)
            db.session.commit()
        except Exception:
            return {"ERROR": "Category could not be created"}, 500

        if len(errors) > 0:
            return {
                "id": category.id,
                "name": category.name,
                "description": category.description,
                "errors": errors,
            }
        return {
            "id": category.id,
            "name": category.name,
            "description": category.description,
        }

    def put(self, category_id):
        category = Product.query.get(category_id)
        if category is None:
            return {"ERROR": "Category does not exists"}, 400

        body = request.get_json()

        if body is None:
            return {"ERROR": "A body must be provided"}

        errors = []
        products_to_add = body.get("products_to_add", None)
        products_to_remove = body.get("products_to_remove", None)

        products_list = []
        if products_to_add is not None:
            for product in products_to_add:
                product_to_add = Product.query.get(product)
                if product_to_add is not None:
                    products_list.append(product_to_add)
                else:
                    errors.append(
                        f"Product '{product}' not found. "
                        "Not adding it to category"
                    )
            for product in products_list:
                category.categories.append(product)

        products_list = []
        if products_to_remove is not None:
            for product in products_to_remove:
                product_to_remove = Product.query.get(product)
                if product_to_remove is not None:
                    products_list.append(product_to_remove)
                else:
                    errors.append(
                        f"Product '{product}' not found. "
                        "Not removing it to category"
                    )
            for product in products_list:
                category.categories.remove(product)

        try:
            category.name = body.get("name", category.name)
            category.description = body.get(
                "description", category.description
            )
            db.session.commit()
        except Exception:
            return {"ERROR": "Category could not be updated"}, 500

        if len(errors) > 0:
            return {
                "id": category.id,
                "name": category.name,
                "description": category.description,
                "errors": errors,
            }
        return {
            "id": category.id,
            "name": category.name,
            "description": category.description,
        }

    def delete(self, category_id):
        category = Category.query.get(category_id)
        if category is None:
            return {"ERROR": "Category does not exists"}, 400

        category_info = {
            {
                "id": category.id,
                "name": category.name,
                "description": category.description,
                "products": [
                    {
                        "id": product.id,
                        "name": product.name,
                    }
                    for product in category.products
                ],
            }
        }

        try:
            db.session.delete(category)
            db.session.commit()
        except Exception:
            return {"ERROR": "Category could not be deleted"}, 500

        return {"deleted_category": category_info}


class MarketplaceAPI(MethodView):
    def get(self, marketplace_id):
        if marketplace_id is None:
            marketplaces = []

            for marketplace in Marketplace.query.all():
                marketplaces.append(
                    {
                        "id": marketplace.id,
                        "name": marketplace.name,
                        "description": marketplace.description,
                    }
                )

            return jsonify(marketplaces)

        marketplace = Marketplace.query.get(marketplace_id)
        if marketplace is None:
            return {"ERROR": "Marketplace does not exists"}, 400

        return {
            "id": marketplace.id,
            "name": marketplace.name,
            "description": marketplace.description,
            "email": marketplace.email,
            "phone": marketplace.phone,
            "website": marketplace.website,
            "technical_contact": marketplace.technical_contact,
        }

    def post(self):
        body = request.get_json()

        name = body.get("name", None)
        description = body.get("description", None)
        email = body.get("email", None)
        phone = body.get("phone", None)
        website = body.get("website", None)
        technical_contact = body.get("technical_contact", None)

        if name is None:
            return {"ERROR": "Field 'name' must not be empty"}, 400
        if description is None:
            return {"ERROR": "Field 'description' must not be empty"}, 400
        if email is None:
            return {"ERROR": "Field 'email' must not be empty"}, 400
        if phone is None:
            return {"ERROR": "Field 'phone' must not be empty"}, 400
        if website is None:
            return {"ERROR": "Field 'website' must not be empty"}, 400
        if technical_contact is None:
            return {
                "ERROR": "Field 'technical_contact' must not be empty"
            }, 400

        if Marketplace.query.filter_by(name=name).first():
            return {"ERROR": "Marketplace name already registered"}, 400

        marketplace = Seller(
            name=name,
            description=description,
            email=email,
            phone=phone,
            website=website,
            technical_contact=technical_contact,
        )

        try:
            db.session.add(marketplace)
            db.session.commit()
        except Exception:
            return {"ERROR": "Marketplace could not be created"}, 500

        return {"id": marketplace.id, "name": marketplace.name}

    def put(self, marketplace_id):
        marketplace = Seller.query.get(marketplace_id)
        if marketplace is None:
            return {"ERROR": "Marketplace does not exists"}, 400

        body = request.get_json()

        try:
            marketplace.name = body.get("name", marketplace.name)
            marketplace.description = body.get(
                "description", marketplace.description
            )
            marketplace.email = body.get("email", marketplace.email)
            marketplace.phone = body.get("phone", marketplace.phone)
            marketplace.website = body.get("website", marketplace.website)
            marketplace.technical_contact = body.get(
                "technical_contact", marketplace.technical_contact
            )
            db.session.commit()
        except Exception:
            return {"ERROR": "Marketplace could not be updated"}, 500

        return {
            "id": marketplace.id,
            "name": marketplace.name,
            "description": marketplace.description,
            "email": marketplace.email,
            "phone": marketplace.phone,
            "website": marketplace.website,
            "technical_contact": marketplace.technical_contact,
        }

    def delete(self, marketplace_id):
        marketplace = Seller.query.get(marketplace_id)
        if marketplace is None:
            return {"ERROR": "Marketplace does not exists"}, 400

        marketplace_info = {
            "id": marketplace.id,
            "name": marketplace.name,
            "description": marketplace.description,
            "email": marketplace.email,
            "phone": marketplace.phone,
            "website": marketplace.website,
            "technical_contact": marketplace.technical_contact,
        }
        try:
            db.session.delete(marketplace)
            db.session.commit()
        except Exception:
            return {"ERROR": "Marketplace could not be deleted"}, 500

        return {"deleted_marketplace": marketplace_info}
