class Robot:
    def __init__(self, name):
        self.name = name
        self.__battery_level = 100

    def status(self):
        return f"{self.name} has {self.getter()}% battery."

    def move(self):
        pass  

    def getter(self):
        return self.__battery_level

    def setter(self, value):
        if 0 <= value <= 100:
            self.__battery_level = value
        else:
            print("Invalid battery level.")

class GroundRobot(Robot):
    def __init__(self, name, wheel):
        super().__init__(name)
        self.wheel = wheel

    def move(self):
        print(f"{self.name} is moving on {self.wheel} wheels.")

class AerialRobot(Robot):
    def __init__(self, name, rotors):
        super().__init__(name)
        self.rotors = rotors

    def move(self):
        print(f"{self.name} is flying with {self.rotors} rotors.")

class FleetManagement:
    def __init__(self):
        self.fleet = []

    def add_robot(self, robot):
        if isinstance(robot, Robot):
            self.fleet.append(robot)
        else:
            print(f"Cannot add {robot}: not a Robot instance.")

    def move_fleet(self):
        for robot in self.fleet:
            robot.move()

    def fleet_status(self):
        for robot in self.fleet:
            print(robot.status())
ground_robot = GroundRobot("Rover", 4)
aerial_robot = AerialRobot("Drone", 6)
fleet = FleetManagement()
fleet.add_robot(ground_robot)
fleet.add_robot(aerial_robot)
print("Fleet movement:")
fleet.move_fleet()

print("\nFleet status:")
fleet.fleet_status()
