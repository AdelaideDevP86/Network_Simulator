from domain.component import Component
from domain.network_project import NetworkProject
from domain.verbinding import Verbinding
import analysis.analysis_service as analysis_service

pc1= Component("pc", "test1",'-', "192.245.245.254" )
pc2= Component("pc", "test2", "-", "192.245.245.253")
pc3= Component("pc", "test3", "-","192.245.245.255")

systeem = NetworkProject("systeem van Adelaide")

systeem.toevoegen_component(pc1)
systeem.toevoegen_component(pc2)

systeem.toevoegen_component(pc3)

verbinding = Verbinding(pc1, pc2, "UP")
verbinding2 = Verbinding(pc2, pc3, "DOWN")

systeem.toevoegen_verbinding(verbinding)
systeem.toevoegen_verbinding(verbinding2)

meldingen = analysis_service.analyseer(systeem)

for melding in meldingen:
    print(melding)

# for verbinding in systeem.verbindingen:
#     print(verbinding)

