from typing import List

from project.robots.base_robot import BaseRobot
from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.base_service import BaseService
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    VALID_SERVICE_TYPES = {"MainService": MainService,
                           "SecondaryService": SecondaryService}

    VALID_ROBOT_TYPES = {"FemaleRobot": FemaleRobot,
                         "MaleRobot": MaleRobot}

    def __init__(self):
        self.robots: List[BaseRobot] = []
        self.services: List[BaseService] = []

    def add_service(self, service_type: str, name: str):
        if service_type not in self.VALID_SERVICE_TYPES.keys():
            raise Exception("Invalid service type!")

        self.services.append(self.VALID_SERVICE_TYPES[service_type](name))
        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        if robot_type not in self.VALID_ROBOT_TYPES.keys():
            raise Exception("Invalid robot type!")

        self.robots.append(self.VALID_ROBOT_TYPES[robot_type](name, kind, price))
        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        robot = next(filter(lambda r: r.name == robot_name, self.robots))
        service = next(filter(lambda s: s.name == service_name, self.services))

        valid_combination = False
        if robot.__class__.__name__ == "FemaleRobot" and service.__class__.__name__ == "SecondaryService":
            valid_combination = True
        elif robot.__class__.__name__ == "MaleRobot" and service.__class__.__name__ == "MainService":
            valid_combination = True
        else:
            return "Unsuitable service."

        if service.capacity == len(service.robots):
            raise Exception("Not enough capacity for this robot!")

        if valid_combination:
            self.robots.remove(robot)
            service.robots.append(robot)
            return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        service = next(filter(lambda s: s.name == service_name, self.services))
        try:
            robot = next(filter(lambda r: r.name == robot_name, service.robots))
            service.robots.remove(robot)
            self.robots.append(robot)
            return f"Successfully removed {robot_name} from {service_name}."
        except StopIteration:
            raise Exception("No such robot in this service!")

    def feed_all_robots_from_service(self, service_name: str):
        service = next(filter(lambda s: s.name == service_name, self.services))
        fed_robots = [x.eating() for x in service.robots]
        return f"Robots fed: {len(fed_robots)}."

    def service_price(self, service_name: str):
        service = next(filter(lambda s: s.name == service_name, self.services))
        total_price = sum([x.price for x in service.robots])
        return f"The value of service {service_name} is {total_price:.2f}."

    def __str__(self):
        return "\n".join([s.details() for s in self.services])
