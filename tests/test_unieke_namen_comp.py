from domain.component import Component
from domain.network_project import NetworkProject


laptop = Component("laptop", "laptop van Adelaide",
                   "prive en studie", "192.168.2.0",
                   "20", "192.168.2.70", 2000)

systeem = NetworkProject("systeem van Adelaide")
systeem.toevoegen_component(laptop)


laptop2 = Component("laptop", "laptop van Adelaide9",
                   "prive en studie", "192.168.2.0",
                   "20", "192.168.2.70", 2000)
systeem.toevoegen_component(laptop2)

