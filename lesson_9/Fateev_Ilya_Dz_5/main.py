class Stationery:
    def __init__(self, title: str):
        self.title = title

    def draw(self):
        print ("start drawing", self.title)

class Pen(Stationery):
    def draw(self):
        print ("starting drawing with pen", self.title)

class Pencil(Stationery):
    def draw(self):
        print ("starting drawing with pencil", self.title)

class Marker(Stationery):
    def draw(self):
        print ("starting drawing with marker", self.title)


stationery = Stationery("Apple")
stationery.draw()
pen = Pen("Apple")
pen.draw()
pencil = Pencil("Apple")
pencil.draw()
marker = Marker("Apple")
marker.draw()