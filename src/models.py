from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
    
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(120), nullable=False)
    list_price = db.Column(db.Float, nullable=False)

    supplier_id = db.Column(db.Integer, db.ForeignKey('supplier.id'), nullable=True)

    supplier = relationship('Supplier', backref='products')

    def __repr__(self):
        return f'<Product {self.product_name} - {self.list_price}> $ y pertenece al proveedor {self.supplier.company_name}>'



class Supplier(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_name =  db.Column(db.String(120),unique=True, nullable=False)
    # Aún hay empresas sin página Web...
    homepage = db.Column(db.String(120))

    def __repr__(self):
        return f'<Supplier {self.company_name}'
    
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ship_city = db.Column(db.String(80), unique=False, nullable=False)