class Component:
    def __init__(self,
                 component_type,
                 naam,
                 beschrijving="",
                 ip_adres= None,
                 prefix = None,
                 gateway = None,
                 vlan = None):

        self.component_type = component_type
        self.naam = naam
        self.beschrijving = beschrijving
        self.ip_adres = ip_adres
        self.prefix = prefix
        self.gateway = gateway
        self.vlan = vlan

        if ip_adres:
            self.valideer_ipv4(self.ip_adres)

        if gateway:
            self.valideer_ipv4(self.gateway)

        if prefix is not None:
            self.valideer_prefix()

        if vlan is not None:
            self.valideer_vlan()

    def valideer_ipv4(self, adres):
        delen = adres.split(".")

        if len(delen) != 4:
            raise ValueError("Ongeldig IP-adres.")

        for deel in delen:
            try:
                getal = int(deel)
            except ValueError:
                raise ValueError("Ongeldig IP-adres.")

            if getal < 0 or getal > 255:
                raise ValueError("Ongeldig IP-adres.")



    def valideer_prefix(self):
        try:
            getal = int(self.prefix)
        except ValueError:
            raise ValueError("Prefix ongeldig.")

        if getal < 0 or getal > 32:
            raise ValueError("Prefix ongeldig.")




    def valideer_vlan(self):
        try:
            getal = int(self.vlan)
        except ValueError:
            raise ValueError("Vlan ongeldig.")

        if getal < 1 or getal > 4094:
            raise ValueError("Vlan ongeldig.")



    def __str__(self):
        return (f"Device-type: {self.component_type}\n"
                f"Naam device: {self.naam}\n"
                f"Device omschrijving: {self.beschrijving}\n"
                f"Ip-adres: {self.ip_adres}\n"
                f"Prefix: {str(self.prefix)} ")
