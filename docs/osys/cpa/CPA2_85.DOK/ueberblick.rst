.. index:: single: CP/A, Version 2
   seealso: CP/A, Version 2; CP/A

.. topic:: Beschreibung des Betriebssystems CP/A

   +-------------------------------------+------------------------+
   | | AdW der DDR                       | | NfD                  |
   | | Institut für Informatik           | | Berlin, den 11.06.85 |
   | | und Rechentechnik                 | | MS/SE/CPM-SB002      |
   | | Abt. Systementwicklung            | |                      |
   +-------------------------------------+------------------------+

.. index:: pair: CP/A, Version 2; Überblick

Überblick
#########

Das Betriebssystem |CP/A| wurde am Institut für Informatik und Rechentechnik
der |AdW der DDR| als Hilfsmittel zur Softwareentwicklung und zur Unterstützung
von Schreibarbeiten entwickelt. Es ist mit dem Betriebssystem |CP/M| kompatibel,
d.h. sämtliche für dieses Betriebssystem vorhandene Anwendersoftware kann
unverändert benutzt werden. |CP/A| ist auf Bürocomputern vom Typ |A5120| und
|A5130| bzw. hardwaremäßig äquivalenten Anlagen (z.B. |K8924|, |K8927|)
generierbar.

Folgende Konfigurationen werden unterstützt:

- 32 |...| 64 |kB| |RAM|,
- Bildschirm 24 |x| 80 oder 16 |x| 64, automatisch erkannt, Steuerzeichen |SCP|
  kompatibel
- Tastaturen |K7604/06| und |K7634/36|, automatisch erkannt,
- Disketten 5" (|K5600.10| DD, SS) und 8" (|MF3200| SD, SS) mit 2 Prozessor
  |CPU| Karte als Ansteuerung, mehrere Formate (u.a. |SCP| kompatibel),
- Drucker:

  - |SD1152|/|SD1157| (|PIO|\ 1, |PIO|\ 2, |IFSS|)
  - |SD1154| (|PIO|)

Sonstige Peripherie (Lochstreifen, Kassetten, |V.24|) wird durch spezielle
Dienstprogramme auf Anwenderniveau unterstützt.

|CP/A| zeichnet sich aus durch:

- leichte Anpassbarkeit an konkrete Hardwarekonfigurationen (Neuübersetzung
  des als Quelltext verfügbaren Betriebssystemteils |BIOS|, Linken gemeinsam
  mit den restlichen Systembestandteilen),
- einfache Struktur, die aufgrund weniger, fest definierter Schnittstellen
  sowohl eine einfache Bedienung als auch flexible Erweiterungen zulässt,
- Ausnutzung der Hardwaremöglichkeiten des Bürocomputers |A5120| und der
  angeschlossenen Peripherie,
- keinerlei Notwendigkeit zu Veränderungen am |A5120| (z.B. Lade-\ |PROM|,
  sowohl mit altem als auch mit neuem (|SCP|)Lade-\ |PROM| ladbar), womit der
  Rechner auch für andere Anwendungen einsetzbar bleibt.

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
