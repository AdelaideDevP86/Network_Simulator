from domain.component import Component
from domain.network_project import NetworkProject
from domain.verbinding import Verbinding


laptop = Component("laptop", "Laptop")
switch = Component("switch", "Switch")
router = Component("router", "Router")

verbinding_1 = Verbinding(laptop, switch, "UP")
verbinding_2 = Verbinding(laptop, router, "UP")

systeem = NetworkProject("Testnetwerk")

systeem.toevoegen_component(laptop)
systeem.toevoegen_component(switch)
systeem.toevoegen_component(router)

systeem.toevoegen_verbinding(verbinding_1)
systeem.toevoegen_verbinding(verbinding_2)

print("VOOR:")
for verbinding in systeem.verbindingen:
    print(verbinding)

systeem.component_verwijderen("Laptop")

print("\nNA:")
for verbinding in systeem.verbindingen:
    print(verbinding)