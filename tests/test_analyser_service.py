from domain.component import Component
from domain.system_model import NetworkProject
from domain.verbinding import Verbinding
from domain.analysisservice import AnalysisService


pc1= Component("pc", "test1",'', "192.245.245.254" )
pc2= Component("pc", "test2", "waarom hebben we een beschrijving", "192.245.245.254")
pc3= Component("pc", "test3", "waarom hebben we een beschrijving","192.245.245.254")

systeem = NetworkProject("systeem van Adelaide")

systeem.toevoegen_component(pc1)
systeem.toevoegen_component(pc2)
analysis_service = AnalysisService()

systeem.toevoegen_component(pc3)

verbinding = Verbinding(pc1, pc2, "UP")
systeem.toevoegen_verbinding(verbinding)
analysis_service = AnalysisService()

meldingen = analysis_service.analyseer(systeem)

for melding in meldingen:
    print(melding)





# for verbinding in systeem.verbindingen:
#     print(verbinding)

