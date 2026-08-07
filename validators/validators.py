########ipv4 validatie############
def valideer_ipv4( adres):
    delen = adres.split(".")

    if len(delen) != 4:
        raise ValueError("Ongeldig IP-adres.")

    for deel in delen:
        try:
            getal = int(deel)
        except ValueError:
            raise ValueError("Ongeldig IP-adres.")

        if getal < 0 or getal > 255:
            raise ValueError("Ongeldig IP-adres.")

############prefix validatie######################
def valideer_prefix(prefix):
    try:
        getal = int(prefix)
    except ValueError:
        raise ValueError("Prefix ongeldig.")

    if getal < 0 or getal > 32:
        raise ValueError("Prefix ongeldig.")

###################vlan validatie#####################
def valideer_vlan(vlan):
    try:
        getal = int(vlan)
    except ValueError:
        raise ValueError("Vlan ongeldig.")

    if getal < 1 or getal > 4094:
        raise ValueError("Vlan ongeldig.")

