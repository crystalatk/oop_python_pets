class Treat:
    def __init__(self, health, full=10):
        self.health = health
        self.full = full


class ColdPizza(Treat):
    def __init__(self):
        super().__init__(15, 20)


class Bacon(Treat):
    def __init__(self):
        super().__init__(30, 30)


class VeganSnack(Treat):
    def __init__(self):
        super().__init__(2, 1)
