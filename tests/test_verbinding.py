from domain.component import Component
from domain.network_project import NetworkProject
from domain.verbinding import Verbinding

pc1 = Component("pc", "test1", )
pc2 = Component("pc", "test2", "waarom hebben we een beschrijving")
pc3 = Component("pc", "test3", "waarom hebben we een beschrijving")

systeem = NetworkProject("systeem van Adelaide")

systeem.toevoegen_component(pc1)
systeem.toevoegen_component(pc2)

systeem.toevoegen_component(pc3)

verbinding = Verbinding(pc1, pc2, "UP")
systeem.toevoegen_verbinding(verbinding)

print(verbinding)

# for verbinding in systeem.verbindingen:
#     print(verbinding)
