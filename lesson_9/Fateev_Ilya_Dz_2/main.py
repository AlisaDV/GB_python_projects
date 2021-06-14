class Road:

    def __init__(self, length, wide):
        self._length = length
        self._wide = wide

    def calculation(self, mass, depth):
        print(int((self._length * self._wide * mass * depth)/100), "т")

while True:
    try:
        print("Enter values")
        road = Road(int(input()), int(input()))
        road.calculation(int(input()), int(input()))
        break
    except ValueError:
        print("Enter int values, pls")