class Component:
    def __init__(self, component_type, naam, beschrijving="", ip_adres= None):
        self.component_type = component_type
        self.naam = naam
        self.beschrijving = beschrijving
        self.ip_adres = ip_adres

        delen = ip_adres.split(".")

        if len(delen) != 4:
            raise ValueError("Ongeldig IP-adres.")

        for deel in delen:
            try:
                getal = int(deel)
            except ValueError:
                raise ValueError("Ongeldig IP-adres.")

            if getal < 0 or getal > 255:
                raise ValueError("Ongeldig IP-adres.")


    def __str__(self):
        return f"{self.type} {self.naam} {self.beschrijving}"
