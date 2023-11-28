from flask import Flask, jsonify
from database import init_db
from flask import request
from models import Driver, CarType, Car, User, Route, Order, DriverRating, AvailabilityCar, DriverCar, Feedback

from controllers import (
    get_all_drivers, get_driver_by_id, create_driver, delete_driver,
    get_all_car_types, get_all_cars, get_all_users,
    get_all_routes, get_all_orders, get_all_driver_ratings,
    get_all_availability_cars, get_all_driver_cars, get_all_feedbacks, get_cars_with_types, get_orders_with_details)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Ivanna2223@localhost/Laba1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'cairocoders-ednalan'
app.config['SQLALCHEMY_ECHO'] = True

init_db(app)

# Маршрути
@app.route('/')
def index():
    return jsonify({'message': 'Welcome to your Flask app!'})


@app.route('/drivers', methods=['GET', 'POST', 'PUT'])
def drivers():
    if request.method == 'GET':
        return get_all_drivers()
    elif request.method == 'POST':
        return create_driver()
    elif request.method == 'DELETE':
        return delete_driver()





@app.route('/drivers/<int:driver_id>', methods=['GET'])
def driver(driver_id):
    return get_driver_by_id(driver_id)


@app.route('/cars_type', methods=['GET'])
def car_types():
    return get_all_car_types()


@app.route('/cars', methods=['GET'])
def cars():
    return get_all_cars()


@app.route('/users', methods=['GET'])
def users():
    return get_all_users()


@app.route('/routes', methods=['GET'])
def routes():
    return get_all_routes()

# Orders
@app.route('/orders', methods=['GET'])
def orders():
    return get_all_orders()

# Driver Ratings
@app.route('/driver-ratings', methods=['GET'])
def driver_ratings():
    return get_all_driver_ratings()

# Availability Cars
@app.route('/availability-cars', methods=['GET'])
def availability_cars():
    return get_all_availability_cars()

# Driver Cars
@app.route('/driver-cars', methods=['GET'])
def driver_cars():
    return get_all_driver_cars()

# Feedback
@app.route('/feedbacks', methods=['GET'])
def feedbacks():
    return get_all_feedbacks()


# Додайте нові маршрути
@app.route('/cars_with_types', methods=['GET'])
def cars_with_types():
    return get_cars_with_types()

@app.route('/orders_with_details', methods=['GET'])
def orders_with_details():
    return get_orders_with_details()



# Запуск додатку
if __name__ == '__main__':
    app.run(debug=True)