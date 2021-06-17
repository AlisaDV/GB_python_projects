class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return self.name, self.surname

    def get_full_income(self):
        return sum(self._income.values())


worker = Position("Oleg", "Osipov", "CuteLoli", 3000, 5000)
print(worker.get_full_name())
print(worker.get_full_income())