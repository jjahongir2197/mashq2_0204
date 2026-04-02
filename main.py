class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.available = True

    def rent(self):
        if self.available:
            self.available = False
            print("Mashina ijaraga berildi.")
        else:
            print("Mashina mavjud emas.")

    def return_car(self):
        self.available = True
        print("Mashina qaytarildi.")

    def get_info(self):
        status = "Bo'sh" if self.available else "Band"
        return f"{self.brand} {self.model} | {self.price} so'm | {status}"


class CarRental:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def show_cars(self):
        print("\nMashinalar:")
        for car in self.cars:
            print(car.get_info())

    def find_car(self, model):
        for car in self.cars:
            if car.model == model:
                return car
        return None


def run_rental():
    rental = CarRental()

    c1 = Car("Toyota", "Camry", 500000)
    c2 = Car("BMW", "X5", 800000)

    rental.add_car(c1)
    rental.add_car(c2)

    rental.show_cars()

    car = rental.find_car("Camry")

    if car:
        car.rent()

    rental.show_cars()

    if car:
        car.return_car()

    rental.show_cars()


run_rental()
