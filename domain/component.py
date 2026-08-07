import validators.validators as validators


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
            validators.valideer_ipv4(self.ip_adres)

        if gateway:
            validators.valideer_ipv4(self.gateway)

        if prefix is not None:
            validators.valideer_prefix(self.prefix)

        if vlan is not None:
            validators.valideer_vlan(self.vlan)



    def __str__(self):
        return (f"Device-type: {self.component_type}\n"
                f"Naam device: {self.naam}\n"
                f"Device omschrijving: {self.beschrijving}\n"
                f"Ip-adres: {self.ip_adres}\n"
                f"Prefix: {str(self.prefix)} ")
