class AnalysisService:

    def analyseer(self, project):

        meldingen = []

        for component in project.componenten:
            gevonden = False

            for verbinding in project.verbindingen:
                if verbinding.component_a == component or verbinding.component_b == component:
                   gevonden = True
                break

            if not gevonden:
                meldingen.append(f"{component.naam} heeft geen verbinding.")

            if not component.ip_adres:
                meldingen.append(f"{component.naam} heeft nog geen IP-adres.")

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