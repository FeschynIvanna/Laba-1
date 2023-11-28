from models import Driver, CarType, Car, User, Route, Order, DriverRating, AvailabilityCar, DriverCar, Feedback
from dao import DriverDAO, CarTypeDAO, CarDAO, UserDAO, RouteDAO, OrderDAO, DriverRatingDAO, AvailabilityCarDAO, DriverCarDAO, FeedbackDAO


class DriverService:
    @staticmethod
    def create_driver(driver_data):
        return DriverDAO.create_driver(driver_data)

    @staticmethod
    def get_all_drivers():
        return DriverDAO.get_all_drivers()

    @staticmethod
    def get_driver_by_id(driver_id):
        return DriverDAO.get_driver_by_id(driver_id)


class CarTypeService:
    @staticmethod
    def get_all_car_types():
        return CarTypeDAO.get_all_car_types()


class CarService:
    @staticmethod
    def get_all_cars():
        return CarDAO.get_all_cars()


class UserService:
    @staticmethod
    def get_all_users():
        return UserDAO.get_all_users()


class RouteService:
    @staticmethod
    def get_all_routes():
        return RouteDAO.get_all_routes()


class OrderService:
    @staticmethod
    def get_all_orders():
        return OrderDAO.get_all_orders()

    # Add other methods as needed

class DriverRatingService:
    @staticmethod
    def get_all_driver_ratings():
        return DriverRatingDAO.get_all_driver_ratings()

    # Add other methods as needed

class AvailabilityCarService:
    @staticmethod
    def get_all_availability_cars():
        return AvailabilityCarDAO.get_all_availability_cars()

    # Add other methods as needed

class DriverCarService:
    @staticmethod
    def get_all_driver_cars():
        return DriverCarDAO.get_all_driver_cars()

    # Add other methods as needed

class FeedbackService:
    @staticmethod
    def get_all_feedbacks():
        return FeedbackDAO.get_all_feedbacks()

    # Add other methods as needed