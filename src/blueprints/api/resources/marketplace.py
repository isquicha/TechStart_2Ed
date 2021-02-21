from flask import jsonify, request
from flask.views import MethodView

from src.extensions.database import db
from src.models.marketplace import Seller


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
        pass

    def post(self):
        pass

    def put(self, product_id):
        pass

    def delete(self, product_id):
        pass


class CategoryAPI(MethodView):
    def get(self, category_id):
        pass

    def post(self):
        pass

    def put(self, category_id):
        pass

    def delete(self, category_id):
        pass


class MarketplaceAPI(MethodView):
    def get(self, marketplace_id):
        pass

    def post(self):
        pass

    def put(self, marketplace_id):
        pass

    def delete(self, marketplace_id):
        pass
