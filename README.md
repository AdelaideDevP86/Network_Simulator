Roadmap: Network Validator
Einddoel

Een netwerkontwerp-validator: je beschrijft een netwerk in een JSON-bestand en de tool rapporteert fouten en risico's, vóórdat er iets geïmplementeerd wordt.

Versie 1.0 is af als:

een netwerk ingeladen kan worden uit een JSON-bestand;
zes checks werken en heldere meldingen geven;
de tool met één commando te draaien is;
de README uitlegt wat het doet, met voorbeeldinvoer en -uitvoer;
de checks echte pytest-tests hebben.
Fase 0: Opschonen
 Roadmap vervangen door dit bestand
 PyCharm-voorbeeldcode uit main.py verwijderen
 README.md aanmaken met titel en einddoel

Klaar als: iemand die de repo opent binnen 10 seconden ziet wat het project is.

Fase 1: Domeinmodel repareren
 valideer_ipv4 laten werken met de ipaddress-module
 Prefix opslaan als int
 Naam valideren in de constructor van Component
 Bij toevoegen_component controleren of het VLAN bestaat
 Verbinding van een component met zichzelf weigeren
 print verwijderen uit component_zoeken

Klaar als: ongeldige IP-adressen, lege namen, onbekende VLAN's en verbindingen met zichzelf niet meer geaccepteerd worden.

Fase 2: Inladen uit JSON
 JSON-formaat vastleggen (VLAN's, componenten, verbindingen)
 Functie laad_project(pad) in map opslag/
 Voorbeeldbestand voorbeelden/kantoor.json met opzettelijke fouten

Klaar als: een JSON-bestand een volledig NetworkProject oplevert.

Fase 3: Checks
 Melding-object met ernst (FOUT of WAARSCHUWING), check en tekst
 Dubbel IP-adres (bestaat al, omzetten naar Melding)
 Component zonder verbinding (bestaat al, omzetten naar Melding)
 Netwerk- of broadcastadres gebruikt als host-IP
 Gateway buiten het subnet
 Overlappende subnetten
 Component verwijst naar onbekend VLAN

Klaar als: het voorbeeldbestand alle opzettelijke fouten meldt, zonder valse meldingen.

Fase 4: Opdrachtregel-tool
 main.py leest een bestandspad in met argparse
 Rapport tonen: eerst fouten, dan waarschuwingen, dan een samenvatting

Klaar als: python main.py voorbeelden/kantoor.json een volledig rapport geeft.

Fase 5: Afronden
 README uitwerken: installatie, gebruik, voorbeeld, lijst met checks
 Bestaande testbestanden omzetten naar echte pytest-tests
 Tests schrijven voor de checks uit fase 3
 Release-tag v1.0

Klaar als: de repolink zonder uitleg naar een stagebedrijf kan.

Ideeën voor na 1.0

Pas oppakken als versie 1.0 af is.

Grafische interface (PySide6)
Topologie tekenen
Single points of failure vinden (articulatiepunten en bruggen)
PoE-budget per switch controleren
Subnet bijna vol
Automatisch vrij IP-adres voorstellen
Rapport exporteren naar HTML of PDF
Uitvalsimulatie: wat gebeurt er als deze switch uitvalt?
