"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Product, Supplier, Order
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def handle_hello():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200

def create_product ():
        product =Product(product_name="Mandarina", list_price = 0.2)
        db.session.add(product)
        db.session.commit()

def get_product(id):
    product = Product.query.get(1)
    print(product.product_name)

def create_order(city):
    order = Order(ship_city = city)
    db.session.add(order)
    db.session.commit()


def get_all_products():
    products = Product.query.all()
    for p in products:
        print(p)

def get_cheap_products():
    products = Product.query.filter(Product.list_price < 1).all ()
    for p in products:
        print(p)


def get_all_products_of_a_single_supplier(id):
    supplier= Supplier.query.get(id)
    print(f'Productos para la compañia: {supplier.company_name}')
    for p in supplier.products:
        print(p)

def insert_suppliers():
    cocacola = Supplier(company_name='Coca Cola', homepage='https://cocacola.com')
    db.session.add(cocacola)
    fruitco = Supplier(company_name='Fruits Company', homepage='https://piñacolada.com')
    db.session.add(fruitco)
    db.session.commit()



# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
   #app.run(host='0.0.0.0', port=PORT, debug=False)
    with app.app_context():
       # create_product()
       # get_product(1)
       # get_all_products()
       # get_cheap_products()
       insert_suppliers()
       #get_all_products_of_a_single_supplier(1)
       #create_order("Barcelona")
       
