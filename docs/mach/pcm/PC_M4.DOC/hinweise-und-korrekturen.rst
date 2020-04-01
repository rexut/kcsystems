.. index:: pair: PC/M; Hinweise und Korrekturen

Hinweise und Korrekturen
########################

.. index:: triple: PC/M; Hinweise und Korrekturen; Zentrale Platine

.. _kcsystems-mach-pcm-fa1188v24io:

Zentrale Platine
****************

Die Leiterplatten des |PC/M| Computers wurden digitalisiert und der Fa. Kolbe in Berlin zur Verfügung gestellt. Der Arbeitsstand |PC/M| **- 230388 - L** (Leiterseite Zentrale Platine) enthält zwei Fehler, die einfach zu korrigieren sind:

- Pin :pin:`4` und Pin :pin:`5` von :comp:`D52.3` (DL000; 1. Reihe rechts neben |U2164|) müssen verbunden werden.
- Die Verbindung von :comp:`D50` (DL074) Pin :pin:`2` an :comp:`D47.3` (DL004) Pin :pin:`1` ist aufzutrennen und durch eine Verbindung von :comp:`D50` Pin :pin:`3` an :comp:`D47.3` Pin :pin:`2` zu ersetzen (2. Reihe rechts neben |U2164|).

Mit dem Stand |PC/M| **- 280888 - L** sind diese Fehler korrigiert. Die im |Funkamateur| abgebildeten Leiterplatten sind fehlerfrei.

Abhängig vom eingesetzten |DRAM| Typ kann es erforderlich sein, :comp:`D49` und :comp:`D50` (im Original LS-TTL) durch TTL Typen zu ersetzen (D100, D104). Diese IS verfügen über einen höheren Lastfaktor.

Werden mehrere Module am Systembus (über :comp:`X3`) angesteckt, ist zur Vermeidung größerer Spannungsabfälle eine Einspeisung der Betriebsspannungen unmittelbar an der Busplatine zu empfehlen.

Die zentrale Platine verfügt im Urzustand über zwei |IFSS|. Bei Verwendung von |IFSS| sollten die Optokoppler :comp:`A2` und :comp:`A3` (MB104) vom Typ der Stromgruppe B oder besser sein.

Für eine hardwareseitige Umrüstung auf |V.24| sind die Verbindungen von :comp:`D61` (DL003) zur |SIO| aufzutrennen bzw. :comp:`D61` und die zugehörigen Bauelemente sowie Optokoppler werden nicht bestückt. Die Hardware eines mit Standardbauteilen auskommenden |V.24| Moduls ist in |PC_M_BC2_N| dargestellt. Die |SIO| Ausgänge :signal:`TxDB`, :signal:`RTSB` und :signal:`DTRB` werden mit einem |B084| (3 |OPV| werden genutzt) und die |SIO| Eingänge :signal:`RxDB`, :signal:`CTSB` und :signal:`DCDB` mit 3 Stück |B 611 D| ausgerüstet. Die zugehörige Software und die anzuschließenden Leitungen sind abhängig vom angeschlossenen Gerät und dessen speziellen Bedingungen.

.. index:: triple: PC/M; Stromlaufplan; FA 11/88-V24IO (SP)

.. list-table:: FA 11/88-V24IO (SP)
   :name: kcsystems-mach-pcm-fa1188v24io-sp
   :class: longtable
   :align: center
   :width: 80 %
   :header-rows: 1

   * - FA 11/88-V24IO (SP)

   * - .. figure:: bild-c2.png
          :name: kcsystems-mach-pcm-bild-c2
          :figclass: align-center
          :align: center
          :width: 240 px
          :alt: |V.24| Hardware

          |V.24| Hardware

Die Schaltung wurde auf einer Rasterplatine realisiert und an :comp:`X2` angesteckt, an den auf der zentralen Platine die |SIO| Leitungen mit TTL Pegel geführt wurden. Die Belegung des Koppelbusverbinders :comp:`X2` ist dann wie folgt vorzusehen (|SIO| Kanal B als |V.24|):

.. tabularcolumns:: p{0.05\linewidth}p{0.10\linewidth}p{0.10\linewidth}p{0.25\linewidth}
.. table:: |PC/M| Steckverbinder - Koppelbusverbinders :comp:`X2` (korrigiert)
   :name: kcsystems-mach-pcm-tabelle-a2
   :widths: 10, 20, 20, 50
   :class: longtable
   :align: center
   :width: 50%

   +-----------+---------------------+---------------------+--------------------------+
   |    Pin    |          A          |          B          |         Hinweise         |
   +===========+=====================+=====================+==========================+
   | :pin:`1`  | :signal:`GND`       | :signal:`GND`       |                          |
   +-----------+---------------------+---------------------+--------------------------+
   | :pin:`2`  | :signal:`CTSB`      | :signal:`DCDB`      | **korrigiert**           |
   +-----------+---------------------+---------------------+--------------------------+
   | :pin:`3`  | :signal:`ZC/TO 2`   | (:signal:`/RESET`)  | **erweitert**            |
   +-----------+---------------------+---------------------+--------------------------+
   | :pin:`4`  | :signal:`ZC/TO 0`   | :signal:`ZC/TO 1`   |                          |
   +-----------+---------------------+---------------------+--------------------------+
   | :pin:`5`  | :signal:`C/TRG 1`   | :signal:`C/TRG 0`   |                          |
   +-----------+---------------------+---------------------+--------------------------+
   | :pin:`6`  | :signal:`C/TRG 3`   | :signal:`C/TRG 2`   |                          |
   +-----------+---------------------+---------------------+--------------------------+
   | :pin:`7`  | :signal:`B7`        | :signal:`A7`        |                          |
   +-----------+---------------------+---------------------+--------------------------+
   | :pin:`8`  | :signal:`B6`        | :signal:`A6`        |                          |
   +-----------+---------------------+---------------------+--------------------------+
   | :pin:`9`  | :signal:`B5`        | :signal:`A5`        |                          |
   +-----------+---------------------+---------------------+--------------------------+
   | :pin:`10` | :signal:`B4`        | :signal:`A4`        |                          |
   +-----------+---------------------+---------------------+--------------------------+
   | :pin:`11` | :signal:`B3`        | :signal:`GND`       |                          |
   +-----------+---------------------+---------------------+--------------------------+
   | :pin:`12` | :signal:`B2`        | :signal:`A3`        |                          |
   +-----------+---------------------+---------------------+--------------------------+
   | :pin:`13` | :signal:`B1`        | :signal:`A2`        |                          |
   +-----------+---------------------+---------------------+--------------------------+
   | :pin:`14` | :signal:`B0`        | :signal:`A1`        |                          |
   +-----------+---------------------+---------------------+--------------------------+
   | :pin:`15` | :signal:`5P`        | :signal:`A0`        |                          |
   +-----------+---------------------+---------------------+--------------------------+
   | :pin:`16` | :signal:`/BSTB`     | :signal:`/ASTB`     |                          |
   +-----------+---------------------+---------------------+--------------------------+
   | :pin:`17` | :signal:`BRDY`      | :signal:`ARDY`      |                          |
   +-----------+---------------------+---------------------+--------------------------+
   | :pin:`18` | :signal:`TxDB`      | (:signal:`TD-IFSS`) | **korrigiert/erweitert** |
   +-----------+---------------------+---------------------+--------------------------+
   | :pin:`19` | :signal:`/RTSA`     | :signal:`/DTRA`     |                          |
   +-----------+---------------------+---------------------+--------------------------+
   | :pin:`20` | :signal:`/DTRB`     | :signal:`/RTSB`     |                          |
   +-----------+---------------------+---------------------+--------------------------+
   | :pin:`21` | :signal:`TxDA 2`    | :signal:`TxDA 1`    |                          |
   +-----------+---------------------+---------------------+--------------------------+
   | :pin:`22` | :signal:`TxDB 2`    | :signal:`TxDB 1`    |                          |
   +-----------+---------------------+---------------------+--------------------------+
   | :pin:`23` | (:signal:`RD-IFSS`) | :signal:`RxDB`      | **korrigiert/erweitert** |
   +-----------+---------------------+---------------------+--------------------------+
   | :pin:`24` | :signal:`RxDA 1`    | :signal:`RxDA 2`    |                          |
   +-----------+---------------------+---------------------+--------------------------+
   | :pin:`25` | :signal:`RxDB 1`    | :signal:`RxDB 2`    |                          |
   +-----------+---------------------+---------------------+--------------------------+
   | :pin:`26` | :signal:`5N`        | :signal:`5N`        |                          |
   +-----------+---------------------+---------------------+--------------------------+
   | :pin:`27` | :signal:`12N`       | :signal:`12N`       |                          |
   +-----------+---------------------+---------------------+--------------------------+
   | :pin:`28` | :signal:`12P`       | :signal:`12P`       |                          |
   +-----------+---------------------+---------------------+--------------------------+
   | :pin:`29` | :signal:`5P`        | :signal:`5P`        |                          |
   +-----------+---------------------+---------------------+--------------------------+

Für Erweiterungsplatinen (|AD|/|DA| Wandler, Tonausgabe) wird der Systemsteckverbinder :comp:`X3` hinsichtlich weiterer Betriebsspannungen wie folgt belegt:

.. tabularcolumns:: p{0.05\linewidth}p{0.10\linewidth}p{0.10\linewidth}p{0.25\linewidth}
.. table:: |PC/M| Steckverbinder - Systembusverbinders :comp:`X3` (korrigiert)
   :name: kcsystems-mach-pcm-tabelle-a3
   :widths: 10, 20, 20, 50
   :class: longtable
   :align: center
   :width: 50%

   +-----------+---------------------+---------------------+----------------+
   |    Pin    |          A          |          B          |    Hinweise    |
   +===========+=====================+=====================+================+
   | :pin:`1`  | :signal:`GND`       | :signal:`GND`       |                |
   +-----------+---------------------+---------------------+----------------+
   | :pin:`2`  | :signal:`GND`       | :signal:`GND`       |                |
   +-----------+---------------------+---------------------+----------------+
   | :pin:`3`  | :signal:`A15`       | :signal:`A14`       |                |
   +-----------+---------------------+---------------------+----------------+
   | :pin:`4`  | :signal:`A13`       | :signal:`A12`       |                |
   +-----------+---------------------+---------------------+----------------+
   | :pin:`5`  | :signal:`A11`       | :signal:`A10`       |                |
   +-----------+---------------------+---------------------+----------------+
   | :pin:`6`  | :signal:`A9`        | :signal:`A8`        |                |
   +-----------+---------------------+---------------------+----------------+
   | :pin:`7`  | :signal:`/MSEL4`    | :signal:`SEL2`      |                |
   +-----------+---------------------+---------------------+----------------+
   | :pin:`8`  | :signal:`/MSEL3`    | :signal:`SEL1`      |                |
   +-----------+---------------------+---------------------+----------------+
   | :pin:`9`  | :signal:`/MSEL2`    | :signal:`SEL0`      |                |
   +-----------+---------------------+---------------------+----------------+
   | :pin:`10` | :signal:`/MSEL1`    | :signal:`12P`       | **korrigiert** |
   +-----------+---------------------+---------------------+----------------+
   | :pin:`11` | :signal:`/MSEL0`    | :signal:`IOSEL0`    | **korrigiert** |
   +-----------+---------------------+---------------------+----------------+
   | :pin:`12` | :signal:`IEO`       | :signal:`IEI`       | **korrigiert** |
   +-----------+---------------------+---------------------+----------------+
   | :pin:`13` | :signal:`A7`        | :signal:`5N`        | **korrigiert** |
   +-----------+---------------------+---------------------+----------------+
   | :pin:`14` | :signal:`A6`        | :signal:`12N`       | **korrigiert** |
   +-----------+---------------------+---------------------+----------------+
   | :pin:`15` | :signal:`A5`        | :signal:`CP`        |                |
   +-----------+---------------------+---------------------+----------------+
   | :pin:`16` | :signal:`A4`        | :signal:`D4`        |                |
   +-----------+---------------------+---------------------+----------------+
   | :pin:`17` | :signal:`A3`        | :signal:`D3`        |                |
   +-----------+---------------------+---------------------+----------------+
   | :pin:`18` | :signal:`A2`        | :signal:`D5`        |                |
   +-----------+---------------------+---------------------+----------------+
   | :pin:`19` | :signal:`A1`        | :signal:`D6`        |                |
   +-----------+---------------------+---------------------+----------------+
   | :pin:`20` | :signal:`A0`        | (:signal:`/BUSAK`)  | **erweitert**  |
   +-----------+---------------------+---------------------+----------------+
   | :pin:`21` | :signal:`/M1`       | :signal:`D2`        |                |
   +-----------+---------------------+---------------------+----------------+
   | :pin:`22` | :signal:`/RFSH`     | :signal:`D7`        |                |
   +-----------+---------------------+---------------------+----------------+
   | :pin:`23` | :signal:`/RESET`    | :signal:`D0`        |                |
   +-----------+---------------------+---------------------+----------------+
   | :pin:`24` | :signal:`/BUSRQ`    | :signal:`D1`        |                |
   +-----------+---------------------+---------------------+----------------+
   | :pin:`25` | :signal:`/WAIT`     | :signal:`/INT`      |                |
   +-----------+---------------------+---------------------+----------------+
   | :pin:`26` | :signal:`/HALT`     | :signal:`/NMI`      |                |
   +-----------+---------------------+---------------------+----------------+
   | :pin:`27` | :signal:`/WR`       | :signal:`/MREQ`     |                |
   +-----------+---------------------+---------------------+----------------+
   | :pin:`28` | :signal:`/RD`       | :signal:`/IORQ`     |                |
   +-----------+---------------------+---------------------+----------------+
   | :pin:`29` | :signal:`5P`        | :signal:`5P`        |                |
   +-----------+---------------------+---------------------+----------------+

.. rubric:: |PC_M_B02_N| (|FA| 1/88):

- die SEL Leitungen an :comp:`X3` (:pin:`B7`, :pin:`B8`, :pin:`B9`) sind High aktiv und werden bezeichnet:

  - :comp:`X3`/:pin:`B7`  =  :signal:`SEL2`
  - :comp:`X3`/:pin:`B8`  =  :signal:`SEL1`
  - :comp:`X3`/:pin:`B9`  =  :signal:`SEL0`

- der nicht bezeichnete Eingang von :comp:`D51.1` (DL008) trägt die Pin Nummer :pin:`5`

.. rubric:: |PC_M_B03_N| (|FA| 2/88):

- die |SIO| (:comp:`D57`) entspricht der Bondvariante 0 (|U8560|).
- die Bezeichnung der Eingänge von :comp:`D54` ist:

  - Pin :pin:`4` = :signal:`E1`
  - Pin :pin:`5` = :signal:`E2`
  - Pin :pin:`6` = :signal:`E3`

- an Pin :pin:`4` von :comp:`A1` (|B082|) muss es heißen :signal:`5N` (-5V) statt 5!
- die Basis von :comp:`A2` und :comp:`A3` ist jeweils Pin :pin:`6`
- an :comp:`D61` (DL003) sind Pin :pin:`1` und :pin:`2` sowie Pin :pin:`4` und :pin:`5` im Stromlaufplan zu verbinden (fehlender Punkt)
- der Kondensator 47 |nF| (Abgleichwert) an :comp:`X4`::pin:`3` ist im Bestückungsplan
  mit 100 |nF| angegeben

.. rubric:: |PC_M_B04D_N| (|FA| 4/88):

- die im Bestückungsplan rechts oben eingezeichnete Brücke um den 22 |nF| Kondensator ist falsch; sie besteht aus zwei Brücken, eine oberhalb des Kondensators und eine weitere unterhalb des Kondensators
- der an gleicher Stelle befindliche Elko 22 |uF| hat seinen Pluspol bei Pin :pin:`1` des DL004
- der 33 |nF| Kondensator unterhalb des Quarzes ist zu streichen; an diese Stelle kann ein zweiter Kondensator parallel zu :comp:`C1` geschaltet werden, um den Abgleich des Oszillators auf 10 |MHz| zu ermöglichen
- der Elko 470 |uF| links des |DRAM| Blockes hat seinen Pluspol auf der unteren Seite (zu :comp:`X2` hin)
- die |DRAM| Blöcke sind von rechts nach links :comp:`B0`, :comp:`B1` und :comp:`B2`; die Daten von unten nach oben in allen drei Blöcken :comp:`D6`, :comp:`D1`, :comp:`D3`, :comp:`D2`, :comp:`D5`, :comp:`D7`, :comp:`D4` und :comp:`D0`
- der Widerstand 2.2 |kO| links oben über den DL074 sollte mit 4.7 |kO| bestückt werden (s. Stromlaufplan)

.. rubric:: |PC_M_B05_N| (|FA| 4/88):

- der |TPA| umfasst den Bereich von :addr:`0100H` bis :addr:`0C7FFH` in Bank 0
- bei nur einem definierten |RAM| Floppy Laufwerk hat dieses die Bezeichnung A mit Beginn in der Bank 1

.. index:: triple: PC/M; Hinweise und Korrekturen; Bildschirmansteuerung

.. _kcsystems-mach-pcm-fa058804-k1:

Bildschirmansteuerung
*********************

Beim Betrieb der Bildschirmansteuerung wurden in Abhängigkeit von den eingesetzten Exemplaren der |SRAM|'s einzelne Fehler im Bildaufbau festgestellt. Dabei können am linken Bildrand z.B. senkrechte Linien mit der Höhe eines Zeichens in Abhängigkeit von der Kursorposition auftreten. Die Schaltung nach |PC_M_BD3_N| (s.a. |PC_M_B07_N|, |FA| 4/88) verhindert diesen exemplarabhängigen Effekt durch veränderte :signal:`STB` Steuerung von :comp:`D112` und vermeidet zusätzlich Flimmererscheinungen beim Zugriff auf die Bildschirmansteuerung durch den Mikroprozessor mittels veränderter :signal:`OE` Steuerung.

.. index:: triple: PC/M; Stromlaufplan; FA 5/88-04 (SP/K1)

.. list-table:: FA 5/88-04 (SP/K1)
   :name: kcsystems-mach-pcm-fa058804-spk1
   :class: longtable
   :align: center
   :width: 80 %
   :header-rows: 1

   * - FA 5/88-04 (SP/K1)

   * - .. figure:: bild-d3.png
          :name: kcsystems-mach-pcm-bild-d3
          :figclass: align-center
          :align: center
          :width: 320 px
          :alt: Änderung der Bildschirmansteuerung

          Änderung der Bildschirmansteuerung

Die in |PC_M_B07_N| (|FA| 4/88) dargestellte Schaltung zeigt die Bildschirmsteuerung für 32 Zeilen und 64 Zeichen je Zeile ab Adresse :addr:`0F800H` dar. Die Kompatibilität zu Programmen mit einem Bildschirmbereich ab Adresse :addr:`0FC00H` mit 16 Zeilen zu 64 Zeichen wurde durch Einfügen eines Negators (:comp:`D115.6`) in die Leitung 11 des :comp:`D126` zum Multiplexer :comp:`D105` erreicht. Damit ergibt sich folgende Leitungsführung, die in der Leiterplatte nach |PC_M_B08A_N| bis |PC_M_B08B_N| realisiert ist und durch das Betriebssystem unterstützt wird:

- :comp:`D126` Pin :pin:`3`  über :signal:`Leitung 11`  an :comp:`D115.6` Pin :pin:`12`
- :comp:`D115` Pin :pin:`13` über :signal:`Leitung 11a` an :comp:`D105`   Pin :pin:`13`
- :comp:`D126` Pin :pin:`2`  über :signal:`Leitung 12`  an :comp:`D106`   Pin :pin:`3`
- :comp:`D126` Pin :pin:`6`  über :signal:`Leitung 13`  an :comp:`D105`   Pin :pin:`10`
- :comp:`D126` Pin :pin:`7`  über :signal:`Leitung 14`  an :comp:`D105`   Pin :pin:`6`
- :comp:`D127` Pin :pin:`3`  über :signal:`Leitung 15`  an :comp:`D105`   Pin :pin:`3`.

.. rubric:: |PC_M_B06_N| (|FA| 4/88):

- die Leitungen zwischen Zeichenlatch und Zeichengenerator sind :signal:`A3` |...| :signal:`A10`
- die Leitungen zwischen Zeichengenerator und Parallelserienwandler sind :signal:`D0` |...| :signal:`D7`

.. rubric:: |PC_M_B07_N| (|FA| 4/88):

- der Ausgang 7 des :comp:`D114` trägt die Pin Nummer 7
- die Verbindung zwischen Primärkreis und Sekundärkreis des Modulators im Stromlaufplan ist im Stromlaufplan zu unterbrechen (auf Leiterplatte i.O.)
- der Eingang 1B des Multiplexers D104 (DL257) hat die Pin Nummer 3

.. rubric:: |PC_M_B08C_N| (|FA| 5/88):

- Pin 1 des DS8282 in der Mitte der Leiterplatte ist rechts unten
- der Ausgang :signal:`B` über dem SF137 muss die Bezeichnung :signal:`/B` tragen; :signal:`B` und :signal:`/B` sind die gegenphasigen Videoausgangssignale; :signal:`A` kennzeichnet die Verbindung zum HF Modulator
- die Anschlüsse der Brücken :comp:`10` und :comp:`E3` befinden sich (v.l.n.r.) bei Pin :pin:`1` des DL192 in der rechten oberen Ecke
- die Reihe A von :comp:`X103` ist außen

.. index:: triple: PC/M; Hinweise und Korrekturen; Tastatur

Tastatur
********

.. rubric:: |PC_M_B14_N| (|FA| 6/88):

- die Bezeichnung am Spaltendekoder heißt richtig :signal:`TD0` |...| :signal:`TD2`
- unter der Zeile :signal:`SP` der Tastaturmatrix sind die Zeilen mit :signal:`Z1` |...| :signal:`Z8`, :signal:`Z1A` und :signal:`Z2A` benannt
- die Bezeichnung :signal:`ZA` an der Tastaturmatrix heißt richtig :signal:`Z8`

.. rubric:: |PC_M_B18_N| (|FA| 6/88):

- die Tasten :signal:`NMI` und :signal:`RESET` sollten abgesetzt von den übrigen Tasten angeordnet werden, um eine unbeabsichtigte Betätigung zu vermeiden

An dieser Stelle möchten wir denjenigen danken, die mit konstruktiven Beiträgen zur Weiterentwicklung des |PC/M| Computers beigetragen haben. Die aktuelle Betriebssystemversion und weitere System- und Anwenderprogramme und Dokumentationen können gegen Einsendung einer Diskette mit 624 |kB| |SCP| Format in einem Umschlag A5 (keine Pakete oder Päckchen!) und Erstattung der Unkosten zur Verfügung gestellt werden.

.. topic:: Klubstation Y56ZN - PC/M Computer -

   +-----------------------------------------------------------+
   | | Klubstation Y56ZN                                       |
   | | - PC/M Computer -                                       |
   +-----------------------------------------------------------+
   | **Anmerkung:** *Anschriften aus datenschutzrechtlichen*   |
   | *Gründen entfernt!*                                       |
   +-----------------------------------------------------------+

.. | | PF24                                                    |
.. | | 9273 Oberlungwitz                                       |
.. +-----------------------------------------------------------+

.. Local variables:
   coding: utf-8
   mode: text
   mode: rst
   End:
   vim: fileencoding=utf-8 filetype=rst :
