from domain.component import Component

class SystemModel:
    def __init__(self, naam):
        self.naam = naam
        self.componenten = []

    def toevoegen_component(self, component):
        self.componenten.append(component)

    def component_zoeken(self, component_naam):
        for comp in self.componenten:
            if comp.naam == component_naam:
                return comp

        return None




