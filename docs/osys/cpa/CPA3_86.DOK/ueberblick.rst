.. index:: single: CP/A, Version 3
   seealso: CP/A, Version 3; CP/A

.. topic:: Beschreibung des Betriebssystems CP/A für Bürocomputer und PC1715

   +-------------------------------------+------------------------+
   | | AdW der DDR                       | |                      |
   | | Institut für Informatik           | | Berlin, den 11.09.86 |
   | | und Rechentechnik                 | | RN/SE/IMPL-SB/001    |
   | | Abt.Systementwicklung             | |                      |
   +-------------------------------------+------------------------+

.. index:: pair: CP/A, Version 3; Überblick

Überblick
#########

Das Betriebssystem |CP/A| wurde am Institut für Informatik und Rechentechnik
der |AdW der DDR| als Hilfsmittel zur SoftwareEntwicklung und zur Unterstützung
von Schreibarbeiten entwickelt. Es ist mit dem Betriebssystem |CP/M| kompatibel,
d.h. sämtliche für dieses Betriebssystem vorhandene AnwenderSoftware kann
unverändert benutzt werden. |CP/A| ist für Bürocomputer vom Typ |A5120| und
|A5130| bzw. hardwaremäßig äquivalenten Anlagen (z.B. |K8924|, |K8927|)
sowie für |PC1715| generierbar.

Folgende Konfigurationen werden unterstützt:

- 32 |...| 64 |kB| |RAM|,
- evtl. vorhandene |OSS| Speichererweiterung (48K) als |RAM| Floppy
  ':file:`M:`', Nichtexistenz bei Kaltstart automatisch erkannt
- Bildschirm 24 |x| 80 oder 16 |x| 64, bei Kaltstart auf Bürocomputer
  automatisch, auf |PC1715| halbautomatisch erkannt, Steuerzeichen
  |SCP| kompatibel
- Tastaturen |K7604/06|, |K7634|, |K7636| und |K7637| bzw. |PC1715 Tastatur|,
  unterschiedliche Tastaturen bei |A51xx| bei Kaltstart automatisch erkannt
- Disketten 5" (40 und 80 Track; DD, SS) sowie 8" (SD, SS) mit 2 Prozessor
  |CPU| Karte |K2526| als Ansteuerung, bzw. |PC1715| 5" (40 und 80 Track; DD;
  SS und DS), mehrere physische Formate
  (u.a. |SCP| kompatibel), die bei LOGIN automatisch erkannt werden
- Drucker:

  - |SD1152|, |SD1157|, |K631x| (|PIO|\ 1, |PIO|\ 2, |IFSS|, |AFS| Anschluss)
  - |SD1154| (|PIO|-Spezialanschluss)
  - |SD1156| (|PIO|-Spezialanschluss |FZB| Müncheberg)
  - bei |PC1715| serielle Drucker an Printer/|V.24|/|IFSS| A/|IFSS| B

Sonstige Peripherie (z.B. Lochstreifen, Kassetten) wird durch spezielle
Dienstprogramme auf Anwenderniveau unterstützt, da ihre Nutzung i.a. nicht
ständig erfolgt.

|CP/A| zeichnet sich aus durch:

- einheitliche Nutzeroberfläche für die verschiedenen Bürocomputertypen
  und |PC1715|, so dass ein Wechsel zwischen diesen Geräten relativ problemlos
  möglich ist
- leichte Anpassbarkeit an gewünschte Hardware- und Softwarekonfigurationen
  (Neuübersetzung des als Quelltext verfügbaren Betriebssystemteils |BIOS|,
  der entsprechend dem Leistungsumfang in seiner Größe verschieden sein
  kann!; Linken gemeinsam mit den restlichen Systembestandteilen)
- Ausnutzung der Hardwaremöglichkeiten des Rechners und der angeschlossenen
  Peripherie, automatische Anpassung an wichtige Hardwarekomponenten (Tastatur,
  Bildschirm) beim Laden des Systems
- keinerlei Notwendigkeit zu Veränderungen am Bürocomputer (z.B. Lade-\ |PROM|,
  sowohl mit altem als auch mit neuem (|SCP|)Lade-\ |PROM| ladbar), womit der
  Rechner auch für andere Anwendungen einsetzbar bleibt
- einfache Struktur, die aufgrund weniger, fest definierter Schnittstellen
  sowohl eine einfache Bedienung als auch flexible Erweiterungen zulässt

Das Betriebssystem |CP/A| besteht aus den drei Hauptteilen |BIOS| (Basic
Input/Output System), |BDOS| (Basic Disk Operating System) und |CCP| (Console
Command Processor), die dem Anwender als Quelltext (|BIOS|) bzw. als
Link-Eingaben (|BDOS|, |CCP|) für die Systemgenerierung zur Verfügung stehen.

.. Local variables:
   coding: utf-8
   mode: text
   mode: rst
   End:
   vim: fileencoding=utf-8 filetype=rst :
