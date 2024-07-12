class Vehicle:
    def __init__(self, registration_number, make, model):
        self.registration_number = registration_number
        self.make = make
        self.model = model

    def display_info(self):
        return f"Registration Number: {self.registration_number}, Make: {self.make}, Model: {self.model}"


class Car(Vehicle):
    def __init__(self, registration_number, make, model, number_of_seats):
        super().__init__(registration_number, make, model)
        self.number_of_seats = number_of_seats

    def display_info(self):
        return f"{super().display_info()}, Number of Seats: {self.number_of_seats}"


class Truck(Vehicle):
    def __init__(self, registration_number, make, model, cargo_capacity):
        super().__init__(registration_number, make, model)
        self.cargo_capacity = cargo_capacity

    def display_info(self):
        return f"{super().display_info()}, Cargo Capacity: {self.cargo_capacity} kg"


class Motorcycle(Vehicle):
    def __init__(self, registration_number, make, model, engine_capacity):
        super().__init__(registration_number, make, model)
        self.engine_capacity = engine_capacity

    def display_info(self):
        return f"{super().display_info()}, Engine Capacity: {self.engine_capacity} cc"


class Fleet:
    def __init__(self):
        self.vehicles = [] 

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)
        print(f"Vehicle {vehicle.registration_number} added successfully.")

    def display_all_vehicles(self):
        if not self.vehicles:
            print("No vehicles in the fleet.")
        else:
            for vehicle in self.vehicles:
                print(vehicle.display_info())

    def search_vehicle_by_registration_number(self, registration_number):
        for vehicle in self.vehicles:
            if vehicle.registration_number == registration_number:
                print(f"Vehicle found: {vehicle.display_info()}")
                return
        print(f"No vehicle found with registration number {registration_number}.")


def main():

    fleet = Fleet()

    car1 = Car("KDP111Q", "Toyota", "Prado", 7)
    truck1 = Truck("ZQ113", "Isuzu", "FH16", 50000)
    motorcycle1 = Motorcycle("KMPD", "Boxer", "R1", 998)

    fleet.add_vehicle(car1)
    fleet.add_vehicle(truck1)
    fleet.add_vehicle(motorcycle1)

    print("Displaying all vehicles:")
    fleet.display_all_vehicles()

    print("Searching for vehicle with registration number 'TRK456':")
    fleet.search_vehicle_by_registration_number("TRK456")

    print("Searching for vehicle with registration number 'CAR000':")
    fleet.search_vehicle_by_registration_number("CAR000")


if __name__ == "__main__":
    main()