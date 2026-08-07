from domain.component import Component
from domain.system_model import NetworkProject
from domain.vlan import Vlan

pc1= Component("pc", "test1",'', "192.245.245.254" )
pc2= Component("pc", "test2", "waarom hebben we een beschrijving", "192.245.245.254")
pc3= Component("pc", "test3", "waarom hebben we een beschrijving","192.245.245.254")

systeem = NetworkProject("systeem van Adelaide")

vlan1 = Vlan(1, "kantoor",  "test")
vlan2 = Vlan(2, "kantoor",  "test2")
vlan3 = Vlan(3, "kantoor",  "test3")
vlan4 = Vlan(3, "kantoor",  "test3")

systeem.toevoegen_vlan(vlan1)
systeem.toevoegen_vlan(vlan2)
systeem.toevoegen_vlan(vlan3)
systeem.toevoegen_vlan(vlan4)

for vlan in systeem.vlans:
    print(vlan)