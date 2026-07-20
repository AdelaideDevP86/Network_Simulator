class Component:
    def __init__(self, type, naam, beschrijving):
        self.type = type
        self.naam = naam
        self.beschrijving = beschrijving

    def __str__(self):
        return f"{self.type} {self.naam} {self.beschrijving}"
