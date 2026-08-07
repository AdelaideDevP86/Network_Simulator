Analyse
│
├── IP-adressen
│   ├── ☐ Dubbel IP
│   ├── ☐ Ontbrekend IP
│   ├── ☐ Gateway ontbreekt
│   └── ☐ Gateway buiten subnet
│
├── VLAN
│   ├── ☐ Component zonder VLAN
│   ├── ☐ VLAN bestaat niet
│   └── ☐ Ongebruikte VLAN
│
├── Subnet
│   ├── ☐ Zelfde VLAN, ander subnet
│   ├── ☐ Overlappende subnetten
│   └── ☐ Subnet bijna vol
│
├── Verbindingen
│   ├── ☑ Geen verbinding
│   ├── ☐ Router zonder verbinding
│   ├── ☐ Switch zonder apparaten
│   └── ☐ Dubbele verbinding
│
└── Algemeen
    ├── ☑ Component zonder IP
    └── ☐ Dubbele hostnaam


Hahaha, ik ga los. 😄

Ik ga hem schrijven alsof dit een project is waar je **2 jaar** aan werkt. Niet omdat je alles gaat bouwen, maar zodat je altijd inspiratie hebt.

---

# 🌍 Network Planner - Complete Roadmap

# Version 0.1 - Fundament

## Project

* ☑ NetworkProject
* ☑ Component
* ☑ Verbinding
* ☑ VLAN
* ☑ Validators
* ☑ Analyse
* ☐ Logging
* ☐ Configuratiebestand
* ☐ Settings

---

# Version 0.2 - Componenten

## Algemene eigenschappen

* ☑ Naam
* ☑ Type
* ☑ Beschrijving
* ☑ IPv4
* ☑ Prefix
* ☑ Gateway
* ☑ VLAN

---

## Uitbreiding

* ☐ MAC-adres
* ☐ Fabrikant
* ☐ Model
* ☐ Serienummer
* ☐ Locatie
* ☐ Rackpositie
* ☐ OS
* ☐ Firmware
* ☐ Management IP
* ☐ DNS
* ☐ DHCP
* ☐ Online status

---

## Componenttypen

* ☐ Router
* ☐ Switch
* ☐ Layer 3 Switch
* ☐ Firewall
* ☐ Server
* ☐ NAS
* ☐ Printer
* ☐ Laptop
* ☐ Desktop
* ☐ Telefoon
* ☐ Camera
* ☐ Access Point
* ☐ IoT Device
* ☐ PLC
* ☐ Raspberry Pi

---

# Version 0.3 - Verbindingen

## Eigenschappen

* ☑ Status
* ☐ Kabeltype
* ☐ Poort
* ☐ Interface
* ☐ Bandbreedte
* ☐ Duplex
* ☐ MTU
* ☐ Lengte
* ☐ Latency

---

## Kabeltypen

* ☐ UTP
* ☐ STP
* ☐ Glasvezel
* ☐ DAC
* ☐ Wireless

---

# Version 0.4 - VLAN

* ☑ Nummer
* ☑ Naam
* ☑ Beschrijving

---

## Uitbreiden

* ☐ Native VLAN
* ☐ Management VLAN
* ☐ Voice VLAN
* ☐ Gast VLAN
* ☐ Trunk VLAN
* ☐ Allowed VLANs
* ☐ Default Gateway
* ☐ DHCP Scope

---

# Version 0.5 - Subnet

* ☐ Subnet-object
* ☐ Netwerkadres
* ☐ Broadcast
* ☐ Eerste host
* ☐ Laatste host
* ☐ Aantal hosts
* ☐ Vrije hosts
* ☐ Gebruikte hosts

---

# Version 0.6 - Analyse

## IP

* ☑ Geen IP
* ☑ Dubbel IP
* ☐ Ongeldig subnet
* ☐ Gateway ontbreekt
* ☐ Gateway buiten subnet
* ☐ Broadcast gebruikt
* ☐ Netwerkadres gebruikt
* ☐ Dubbele gateway

---

## VLAN

* ☐ VLAN bestaat niet
* ☐ Geen VLAN
* ☐ Lege VLAN
* ☐ Ongebruikte VLAN
* ☐ Te veel apparaten
* ☐ Management VLAN ontbreekt

---

## Verbindingen

* ☑ Geen verbinding
* ☐ Router zonder verbinding
* ☐ Switch zonder apparaten
* ☐ Server zonder verbinding
* ☐ Printer zonder verbinding
* ☐ Dubbele verbinding
* ☐ Ringdetectie
* ☐ Los eiland

---

## Subnet

* ☐ Zelfde VLAN ander subnet
* ☐ Verschillende VLAN zelfde subnet
* ☐ Overlappende subnetten
* ☐ Subnet bijna vol
* ☐ Onlogische prefix

---

## Apparaten

* ☐ Dubbele naam
* ☐ Naam leeg
* ☐ Naamconventie

---

## Netwerk

* ☐ Geen router
* ☐ Geen gateway
* ☐ Geen internetpad
* ☐ Geen DNS
* ☐ Bottleneck

---

# Version 0.7 - Berekeningen

* ☐ Netwerkadres
* ☐ Broadcast
* ☐ Wildcard
* ☐ Hostrange
* ☐ CIDR
* ☐ Masker
* ☐ Prefix converter
* ☐ Binair tonen
* ☐ Hex tonen

---

# Version 0.8 - Automatiseren

* ☐ Automatisch IP uitdelen
* ☐ Vrij IP zoeken
* ☐ Gateway voorstellen
* ☐ VLAN voorstellen
* ☐ Naam genereren
* ☐ Racknummer genereren

---

# Version 0.9 - Opslag

* ☐ JSON
* ☐ XML
* ☐ YAML
* ☐ SQLite
* ☐ PostgreSQL

---

# Version 1.0 - GUI

## Componentbeheer

* ☐ Toevoegen
* ☐ Bewerken
* ☐ Verwijderen
* ☐ Zoeken
* ☐ Filteren

---

## Visualisatie

* ☐ Apparaten tekenen
* ☐ Verbinding tekenen
* ☐ Kleuren
* ☐ Zoom
* ☐ Drag & Drop

---

## Analyse

* ☐ Analyse starten
* ☐ Fouten tonen
* ☐ Waarschuwingen tonen
* ☐ Export

---

# Version 1.1 - Rapportage

* ☐ PDF
* ☐ CSV
* ☐ Excel
* ☐ HTML
* ☐ Print

---

# Version 1.2 - Simulatie

* ☐ Ping
* ☐ Kabel eruit trekken
* ☐ Switch uitzetten
* ☐ Router uitzetten
* ☐ Gateway uitzetten
* ☐ Latency simuleren
* ☐ Packet loss
* ☐ Bandbreedte simuleren

---

# Version 1.3 - Security

* ☐ ACL
* ☐ Firewall
* ☐ DMZ
* ☐ Gastnetwerk
* ☐ Port Security
* ☐ MAC filtering
* ☐ Rogue DHCP
* ☐ VLAN hopping waarschuwing

---

# Version 1.4 - Enterprise

* ☐ STP
* ☐ RSTP
* ☐ EtherChannel
* ☐ OSPF
* ☐ BGP
* ☐ VRRP
* ☐ HSRP
* ☐ QoS

---

# Version 1.5 - Monitoring

* ☐ CPU
* ☐ RAM
* ☐ Uptime
* ☐ Poortstatus
* ☐ Temperatuur
* ☐ SNMP
* ☐ Syslog

---

# Version 2.0 - Datacenter

* ☐ Racks
* ☐ Patchpanelen
* ☐ Glasvezel
* ☐ UPS
* ☐ Redundantie
* ☐ Core-distribution-access model
* ☐ Storage-netwerk

---

# Version 3.0 - Droomversie

* ☐ Cisco-config importeren.
* ☐ Cisco-config genereren.
* ☐ Packet Tracer import.
* ☐ Visio import.
* ☐ Topologie automatisch tekenen.
* ☐ AI die netwerk verbetervoorstellen doet.
* ☐ Netwerkscore (0–100).
* ☐ Kostenraming van hardware.
* ☐ Capaciteitsplanning.
* ☐ Impactanalyse ("Wat gebeurt er als deze switch uitvalt?").

---

## 🎯 Mijn advies

Ik zou dit bestand letterlijk `ROADMAP.md` noemen en er **niets aan schrappen**. Zie het niet als een to-do voor volgende week, maar als een ideeënboek. Elke keer als je iets nieuws leert op school of in de praktijk, kun je denken:

> "Hé... dat past in mijn netwerkplanner."

En dan voeg je het toe. Zo groeit je project met jouw kennis, in plaats van dat je eerst alles moet weten voordat je iets kunt bouwen. Ik denk dat dat heel goed past bij de manier waarop jij dit project benadert. 🚀
