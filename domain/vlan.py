class Vlan:
    def __init__(self, nummer, naam, subnet, beschrijving=""):
        self.nummer = nummer
        self.naam = naam
        self.subnet = subnet
        self.beschrijving = beschrijving

        # VLAN-nummer
        if not isinstance(nummer, int):
            raise ValueError("Ongeldig VLAN-nummer.")

        if nummer < 1 or nummer > 4094:
            raise ValueError("Ongeldig VLAN-nummer.")

        # Naam
        if not naam.strip():
            raise ValueError("Naam mag niet leeg zijn.")

        # Subnet moet bestaan uit IP/prefix
        subnet_delen = subnet.split("/")

        if len(subnet_delen) != 2:
            raise ValueError("Ongeldig subnet.")

        ip_adres = subnet_delen[0]
        prefix = subnet_delen[1]

        # IPv4 controleren
        delen = ip_adres.split(".")

        if len(delen) != 4:
            raise ValueError("Ongeldig subnet.")

        for deel in delen:
            try:
                getal = int(deel)
            except ValueError:
                raise ValueError("Ongeldig subnet.")

            if getal < 0 or getal > 255:
                raise ValueError("Ongeldig subnet.")

        # Prefix controleren
        try:
            prefix = int(prefix)
        except ValueError:
            raise ValueError("Ongeldig subnet.")

        if prefix < 0 or prefix > 32:
            raise ValueError("Ongeldig subnet.")

    def __str__(self):
        return f"VLAN {self.nummer} - {self.naam} - {self.subnet}"