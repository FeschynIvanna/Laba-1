# dao.py
from database import db
from models import Driver, CarType, Car, User, Route, Order, DriverRating, AvailabilityCar, DriverCar, Feedback


class DriverDAO:
    @staticmethod
    def get_all_drivers():
        return Driver.query.all()

    @staticmethod
    def get_driver_by_id(driver_id):
        return Driver.query.get(driver_id)

    @staticmethod
    def create_driver(driver_data):
        new_driver = Driver(**driver_data)
        db.session.add(new_driver)
        db.session.commit()
        return new_driver

    def update_driver_by_id(driver_id, driver_data):
        driver = Driver.query.get(driver_id)
        if driver:
            # Update driver information
            driver.name = driver_data.get('name', driver.name)
            driver.surname = driver_data.get('surname', driver.surname)
            driver.phone = driver_data.get('phone', driver.phone)

            db.session.commit()
            return driver
        return None

    @staticmethod
    def delete_driver_by_id(driver_id):
        driver = Driver.query.get(driver_id)
        if driver:
            db.session.delete(driver)
            db.session.commit()
            return True
        return False


class CarTypeDAO:
    @staticmethod
    def get_all_car_types():
        return CarType.query.all()


class CarDAO:
    @staticmethod
    def get_all_cars():
        return Car.query.all()


class UserDAO:
    @staticmethod
    def get_all_users():
        return User.query.all()


class RouteDAO:
    @staticmethod
    def get_all_routes():
        return Route.query.all()


class OrderDAO:
    @staticmethod
    def get_all_orders():
        return Order.query.all()

    # Add other methods as needed

class DriverRatingDAO:
    @staticmethod
    def get_all_driver_ratings():
        return DriverRating.query.all()

    # Add other methods as needed

class AvailabilityCarDAO:
    @staticmethod
    def get_all_availability_cars():
        return AvailabilityCar.query.all()

    # Add other methods as needed

class DriverCarDAO:
    @staticmethod
    def get_all_driver_cars():
        return DriverCar.query.all()

    # Add other methods as needed

class FeedbackDAO:
    @staticmethod
    def get_all_feedbacks():
        return Feedback.query.all()

    # Add other methods as needed