# -------------------------
# IPv4-validatie
# -------------------------
def valideer_ipv4(adres):
    delen = adres.split(".")

    if len(delen) != 4:
        raise ValueError("Ongeldig IP-adres,  format: xx.xx.xx.xx")

    for deel in delen:
        try:
            getal = int(deel)
        except ValueError:
            raise ValueError("Ongeldig IP-adres, voer een getallen in, format: xx.xx.xx.xx.")

        if getal < 0 or getal > 255:
            raise ValueError("Ongeldig IP-adres, voer een getal tussen 0 en 255 per octet.")
    else:
        return True




# -------------------------
# Prefix validatie
# -------------------------
def valideer_prefix(prefix):
    try:
        getal = int(prefix)
    except ValueError:
        raise ValueError("Prefix ongeldig, voer een getal in.")

    if getal < 0 or getal > 32:
        raise ValueError("Prefix ongeldig, voer een getal tussen 0 en 32.")
    else:
        return True


# -------------------------
# VLAN validatie
# -------------------------
def valideer_vlan(vlan):
    try:
        getal = int(vlan)
    except ValueError:
        raise ValueError("Vlan ongeldig, voer een getal in.")

    if getal < 1 or getal > 4094:
        raise ValueError("Vlan ongeldig, voer een getal tussen 1 en 4094.")
    else :
        return True

def valideer_naam(naam):
    if not isinstance(naam, str):
        raise TypeError("Naam moet een string zijn.")

    if not naam.strip():
        raise ValueError("Naam mag niet leeg zijn.")

    if len(naam) > 100:
        raise ValueError("Naam mag maximaal 100 tekens bevatten.")