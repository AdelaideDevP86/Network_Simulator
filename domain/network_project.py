from domain.component import Component
from domain.vlan import Vlan
from domain.verbinding import Verbinding


class NetworkProject:
    def __init__(self, naam):
        self.naam = naam
        self.componenten = []
        self.verbindingen = []
        self.vlans = []

    def toevoegen_component(self, component):
        if not isinstance(component, Component):
            raise TypeError("Alleen Component-objecten kunnen worden toegevoegd.")
        self.componenten.append(component)

    def component_zoeken(self, component_naam):
        for comp in self.componenten:
            if comp.naam == component_naam:
                return comp

        return None


    def component_wijzigen(self, component_naam, naam=None, ip_adres=None,
                           prefix=None, gateway=None, vlan=None):
       for component in self.componenten:
           if component.naam == component_naam:
             if self.naam is not None:
                 self.naam = naam
                 print(self.naam)
             if ip_adres is not None:
                 self.ip_adres = ip_adres

    else:
        raise ValueError("Apparaat niet gevonden")

    def toevoegen_verbinding(self, verbinding):

        if not isinstance(verbinding, Verbinding):
            raise TypeError("Alleen Verbinding-objecten kunnen worden toegevoegd.")

        if verbinding.component_a not in self.componenten:
            raise ValueError("Component A bestaat niet in het project.")

        if verbinding.component_b not in self.componenten:
            raise ValueError("Component B bestaat niet in het project.")

        for bestaande_verbinding in self.verbindingen:

            if (
                    bestaande_verbinding.component_a == verbinding.component_a
                    and bestaande_verbinding.component_b == verbinding.component_b
            ) or (
                    bestaande_verbinding.component_a == verbinding.component_b
                    and bestaande_verbinding.component_b == verbinding.component_a
            ):
                raise ValueError("Verbinding bestaat al.")

        self.verbindingen.append(verbinding)

    def toevoegen_vlan(self, vlan):
        if not isinstance(vlan, Vlan):
            raise TypeError("Alleen Vlan-objecten kunnen worden toegevoegd.")

        for bestaande_vlan in self.vlans:
            if bestaande_vlan.nummer == vlan.nummer:
                raise ValueError("Vlan bestaat al.")

        self.vlans.append(vlan)
