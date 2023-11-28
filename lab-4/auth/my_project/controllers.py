from flask import Flask, jsonify
from flask import jsonify
from flask import request
from database import db  # Додайте цей імпорт
from models import Driver, CarType, Car, User, Route, Order, DriverRating, AvailabilityCar, DriverCar, Feedback

from dao import (
    DriverDAO, CarTypeDAO, CarDAO, UserDAO, RouteDAO, OrderDAO,
    DriverRatingDAO, AvailabilityCarDAO, DriverCarDAO, FeedbackDAO
)

from schema import (
    DriverSchema, CarTypeSchema, CarSchema, UserSchema, RouteSchema, OrderSchema, DriverRatingSchema, AvailabilityCarSchema,
    DriverCarSchema, FeedbackSchema
)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Ivanna2223@localhost/Laba1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

driver_schema = DriverSchema()
car_type_schema = CarTypeSchema()
car_schema = CarSchema()
user_schema = UserSchema()
route_schema = RouteSchema()
order_schema = OrderSchema()
driver_rating_schema = DriverRatingSchema()
availability_car_schema = AvailabilityCarSchema()
driver_car_schema = DriverCarSchema()
feedback_schema = FeedbackSchema()


@app.route('/drivers', methods=['GET'])
def get_all_drivers():
    drivers = DriverDAO.get_all_drivers()
    return jsonify(driver_schema.dump(drivers, many=True))


@app.route('/drivers/<int:driver_id>', methods=['GET'])
def get_driver_by_id(driver_id):
    driver = DriverDAO.get_driver_by_id(driver_id)
    if driver:
        return jsonify(driver_schema.dump(driver))
    return jsonify({'message': 'Driver not found'}), 404



@app.route('/drivers', methods=['POST'])
def create_driver():
    try:
        # Отримайте дані від клієнта у форматі JSON
        driver_data = request.get_json()

        # Створіть нового водія та додайте його до бази даних
        new_driver = DriverDAO.create_driver(driver_data)

        # Поверніть створеного водія у відповідь
        return jsonify(driver_schema.dump(new_driver)), 201
    except Exception as e:
        # Обробте помилку, якщо вона виникне
        return jsonify({'error': str(e)}), 400



@app.route('/drivers/<int:driver_id>', methods=['PUT'])
def update_driver(driver_id):
    driver_data = request.json
    updated_driver = DriverDAO.update_driver_by_id(driver_id, driver_data)
    if updated_driver:
        return jsonify(driver_schema.dump(updated_driver))
    return jsonify({'message': f'Driver with ID {driver_id} not found'}), 404


@app.route('/drivers/<int:driver_id>', methods=['DELETE'])
def delete_driver(driver_id):
    success = DriverDAO.delete_driver_by_id(driver_id)
    if success:
        return jsonify({'message': f'Driver with ID {driver_id} deleted successfully'})
    return jsonify({'message': f'Driver with ID {driver_id} not found'}), 404

@app.route('/cars_type_types', methods=['GET'])
def get_all_car_types():
    car_types = CarTypeDAO.get_all_car_types()
    return jsonify(car_type_schema.dump(car_types, many=True))


@app.route('/cars', methods=['GET'])
def get_all_cars():
    cars = CarDAO.get_all_cars()
    return jsonify(car_schema.dump(cars, many=True))


@app.route('/users', methods=['GET'])
def get_all_users():
    users = UserDAO.get_all_users()
    return jsonify(user_schema.dump(users, many=True))


@app.route('/routes', methods=['GET'])
def get_all_routes():
    routes = RouteDAO.get_all_routes()
    return jsonify(route_schema.dump(routes, many=True))


@app.route('/orders', methods=['GET'])
def get_all_orders():
    orders = OrderDAO.get_all_orders()
    return jsonify(order_schema.dump(orders, many=True))


@app.route('/driver_ratings', methods=['GET'])
def get_all_driver_ratings():
    driver_ratings = DriverRatingDAO.get_all_driver_ratings()
    return jsonify(driver_rating_schema.dump(driver_ratings, many=True))


@app.route('/availability_cars', methods=['GET'])
def get_all_availability_cars():
    availability_cars = AvailabilityCarDAO.get_all_availability_cars()
    return jsonify(availability_car_schema.dump(availability_cars, many=True))


@app.route('/driver_cars', methods=['GET'])
def get_all_driver_cars():
    driver_cars = DriverCarDAO.get_all_driver_cars()
    return jsonify(driver_car_schema.dump(driver_cars, many=True))


@app.route('/feedbacks', methods=['GET'])
def get_all_feedbacks():
    feedbacks = FeedbackDAO.get_all_feedbacks()
    return jsonify(feedback_schema.dump(feedbacks, many=True))


# Новий маршрут для отримання інформації про автомобілі разом із типами
@app.route('/cars_with_types', methods=['GET'])
def get_cars_with_types():
    cars_with_types = db.session.query(Car, CarType).join(CarType).all()
    result = [
        {
            'car_id': car.id,
            'model': car.model,
            'license_plate': car.license_plate,
            'car_type': {
                'id': car_type.id,
                'type_name': car_type.type_name,
                'description': car_type.description
            }
        }
        for car, car_type in cars_with_types
    ]
    return jsonify(result)


# Новий маршрут для отримання інформації про замовлення разом із даними про користувачів, маршрути та автомобілі
@app.route('/orders_with_details', methods=['GET'])
def get_orders_with_details():
    orders_with_details = db.session.query(Order, User, Route, Car).join(User).join(Route).join(Car).all()
    result = [
        {
            'order_id': order.id,
            'pickup_time': order.pickup_time,
            'status': order.status,
            'user': {
                'id': user.id,
                'surname': user.surname,
                'name': user.name,
                'phone': user.phone
            },
            'route': {
                'id': route.id,
                'start_location': route.start_location,
                'end_location': route.end_location,
                'distance': route.distance
            },
            'car': {
                'id': car.id,
                'model': car.model,
                'license_plate': car.license_plate
            }
        }
        for order, user, route, car in orders_with_details
    ]
    return jsonify(result)
