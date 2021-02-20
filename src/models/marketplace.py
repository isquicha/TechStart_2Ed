from src.extensions.database import db

CHARACTERS = 200


class Seller(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fantasy_name = db.Column(db.String(CHARACTERS), nullable=False)
    company_name = db.Column(db.String(CHARACTERS), nullable=False)
    tax_code = db.Column(db.String(CHARACTERS), nullable=False)  # ? or CNPJ
    email = db.Column(db.String(CHARACTERS), nullable=False)
    phone = db.Column(db.String(CHARACTERS), nullable=False)
    address = db.Column(db.Text, nullable=False)


# ? Table for a many to many relationship
products_categories = db.Table(
    "products_categories",
    db.Column(
        "product_id",
        db.Integer,
        db.ForeignKey("products.id"),
        primary_key=True,
    ),
    db.Column(
        "category_id",
        db.Integer,
        db.ForeignKey("categories.id"),
        primary_key=True,
    ),
)


class Category(db.Model):
    __tablename__ = "categories"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(CHARACTERS), nullable=False)
    description = db.Column(db.Text, nullable=False)


class Product(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(CHARACTERS), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)

    # ? Many to many relationship
    categories = db.relationship(
        "Category",
        secondary=products_categories,
        backref=db.backref("products", lazy=True),
    )


class Marketplace(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(CHARACTERS), nullable=False)
    description = db.Column(db.Text, nullable=False)
    email = db.Column(db.String(CHARACTERS), nullable=False)
    phone = db.Column(db.String(CHARACTERS), nullable=False)
    website = db.Column(db.String(CHARACTERS), nullable=False)
    technical_contact = db.Column(db.String(CHARACTERS), nullable=False)
