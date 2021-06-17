class Car:
    def __init__(self, speed, color, name, is_police: bool):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        print(self.name, "поехала")

    def stop(self):
        print(self.name, "остановилась")

    def turn(self, side: str):
        print(self.name, "повернула ", side)

    def show_speed(self):
        print(self.name, "скорость - ", self.speed)

class TownCar(Car):
    def show_speed(self):
        if(self.speed > 60):
            print ("Превышение скорости")
        else:
            super().show_speed

class WorkCar(Car):
    def show_speed(self):
        if(self.speed > 40):
            print ("Превышение скорости")
        else:
            super().show_speed()

class PoliceCar(Car):
    pass

class SportCar(Car):
    pass


town_car = TownCar(70, "white", "BMW", False)
town_car.go()
town_car.show_speed()
work_car = WorkCar(30, "black", "Камаз", False)
work_car.show_speed()
work_car.stop()
police_car = PoliceCar(50, "white", "Volkswagen", True)
police_car.turn("налево")
