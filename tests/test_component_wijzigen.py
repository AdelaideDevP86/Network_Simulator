from domain.component import Component
from domain.network_project import NetworkProject



laptop = Component("laptop", "laptop van Adelaide",
                   "prive en studie", "192.168.2.0",
                   "20", "192.168.2.70", 2000)

systeem = NetworkProject("systeem van Adelaide")
systeem.toevoegen_component(laptop)


# systeem.component_wijzigen( "laptop van Adelaide", nieuwe_component_naam =  "Laptop van spiderman",
#                             ip_adres= "192.88.99.00", )
# print("test 1")
# print(laptop.naam, "\n")
# print(laptop.ip_adres, "\n")
# print(laptop.gateway, "\n")

systeem.component_wijzigen(
    "Bestaat niet",
    ip_adres="192.168.2.10"
)

