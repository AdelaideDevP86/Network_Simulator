
class NetworkProject:
    def __init__(self, naam):
        self.naam = naam
        self.componenten = []
        self.verbindingen= []

    def toevoegen_component(self, component):
        self.componenten.append(component)

    def component_zoeken(self, component_naam):
        for comp in self.componenten:
            if comp.naam == component_naam:
                return comp

        return None

    def toevoegen_verbinding(self, verbinding):

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





