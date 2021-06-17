class Cell:

    def __init__(self, cell):
        self.cell = cell

    def get_cell(self):
        return self.cell

    def __add__(self, other):
        new_cell = Cell(self.get_cell() + other.get_cell())
        print(new_cell.get_cell())

    def __sub__(self, other):
        if self.cell - other.get_cell() >= 0:
            new_cell = Cell(self.cell - other.get_cell())
            print(new_cell.get_cell())
        else:
            print("Количество ячеек во второй клетке превышает количество ячеек в первой")

    def __mul__(self, other):
        new_cell = Cell(self.cell * other.get_cell())
        print(new_cell.get_cell())

    def __floordiv__(self, other):
        new_cell = Cell(self.cell / other.get_cell())
        print(new_cell.get_cell())

    def make_order(self, count: int):
        s = ""
        for i in range(count):
            if (i%5!=0):
               s += "*"
            else:
                s += '\n'
                s += "*"
        print(s)



cel = Cell(30)
cel2 = Cell(20)

Cell.__add__(cel, cel2)
Cell.__sub__(cel, cel2)
Cell.__mul__(cel, cel2)
Cell.__floordiv__(cel, cel2)
cel.make_order(15)