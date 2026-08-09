from domain.component import Component
from domain.network_project import NetworkProject



laptop = Component("laptop", "laptop van Adelaide",
                   "prive en studie", "192.168.2.0",
                   "20", "192.168.2.70", 2000)

systeem = NetworkProject("systeem van Adelaide")
systeem.toevoegen_component(laptop)

component = systeem.component_zoeken(laptop.naam)