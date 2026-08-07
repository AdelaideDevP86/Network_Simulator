class Vlan:
    def __init__(self, nummer, naam, beschrijving=""):
        self.nummer = nummer
        self.naam = naam
        self.beschrijving = beschrijving

        # VLAN-nummer
        if not isinstance(nummer, int):
            raise ValueError("Ongeldig VLAN-nummer.")

        if nummer < 1 or nummer > 4094:
            raise ValueError("Ongeldig VLAN-nummer.")

        # Naam
        if not naam.strip():
            raise ValueError("Naam mag niet leeg zijn.")



    def __str__(self):
        return f"VLAN {self.nummer} - {self.naam} "