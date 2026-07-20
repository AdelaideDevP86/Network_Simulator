from domain.component import Component
from domain.system_model import SystemModel
from tests.test_component import laptop

systeem = SystemModel("systeem van Adelaide")
systeem.toevoegen_component(laptop)

for comp in systeem.componenten:
    print(comp.naam)