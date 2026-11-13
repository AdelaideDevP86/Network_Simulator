from domain.network_project import NetworkProject

def analyseer(project):
    meldingen = []
    meldingen.extend(check_verbindingen(project))
    meldingen.extend(check_ipadres(project))
    meldingen.extend(check_dubbele_ipadressen(project))

    return meldingen

def check_dubbele_ipadressen(project):
    meldingen = []
    for i, component in enumerate(project.componenten):

        if not component.ip_adres:
            continue

        for ander_component in project.componenten[i + 1:]:

            if not ander_component.ip_adres:
                continue

            if component.ip_adres == ander_component.ip_adres:
                meldingen.append(
                    f"{component.naam} en {ander_component.naam} gebruiken hetzelfde IP-adres."
                )

    return meldingen

def check_verbindingen(project):
    meldingen = []
    actieve_verbindingen, inactieve_verbindingen = project.scheid_actieve_en_inactieve_verbindingen()

    for component in project.componenten:
        gevonden = False

        for verbinding in actieve_verbindingen:
            if verbinding.component_a == component or verbinding.component_b == component:
                gevonden = True
                break

        if not gevonden:
            meldingen.append(f"{component.naam} heeft geen actieve verbinding.")

    for verbinding in inactieve_verbindingen:
        meldingen.append(f"Verbinding tussen {verbinding.component_a.naam} en {verbinding.component_b.naam} is DOWN.")
    
    return meldingen

def check_ipadres(project):
    meldingen = []

    for component in project.componenten:

        if not component.ip_adres:
            meldingen.append(f"{component.naam} heeft nog geen IP-adres.")

    return meldingen
