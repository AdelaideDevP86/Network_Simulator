from domain.component import Component
from domain.network_project import NetworkProject
from domain.verbinding import Verbinding

pc1 = Component("pc", "test1", )
pc2 = Component("pc", "test2", "waarom hebben we een beschrijving")
pc3 = Component("pc", "test3", "waarom hebben we een beschrijving")
pc4 = Component("pc", "test4", )

systeem = NetworkProject("systeem van Adelaide")

systeem.toevoegen_component(pc1)
systeem.toevoegen_component(pc2)

systeem.toevoegen_component(pc3)
systeem.toevoegen_component(pc4)

verbinding1 = Verbinding(pc1, pc2, "UP")
verbinding2 = Verbinding(pc2, pc3, "DOWN")
verbinding3 = Verbinding(pc1, pc3, "UP")
verbinding4 = Verbinding(pc2, pc4, "UP")

systeem.toevoegen_verbinding(verbinding1)
systeem.toevoegen_verbinding(verbinding2)
systeem.toevoegen_verbinding(verbinding3)
systeem.toevoegen_verbinding(verbinding4)

buren = systeem.zoek_actieve_buren_component(pc2)
for buur in buren:
    print(buur.naam)
