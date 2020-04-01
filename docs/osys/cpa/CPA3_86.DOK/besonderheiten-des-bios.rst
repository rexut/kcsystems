.. highlight:: none

.. index:: pair: CP/A, Version 3; BIOS

Besonderheiten des BIOS
#######################

Das |BIOS| kann entsprechend der Hardwarekonfiguration und der geplanten Betriebsweise in verschiedenen Varianten generiert werden. Sämtliche Angaben dazu befinden sich als kommentierte :z80:`EQU` Anweisungen am Anfang des |BIOS| Quelltextes. Es folgen daher nur Erläuterungen zu im |BIOS| enthaltenen Sonderfunktionen.

.. index:: triple: CP/A, Version 3; BIOS; I/O Byte

I/O Byte (nur PC1715)
*********************

Für die zeichenorientiert arbeitenden Geräte werden die Möglichkeiten des I/O Bytes von |CP/M| (Hauptspeicherplatz 3) in folgender Weise unterstützt:

.. tabularcolumns:: CC|CCCCCCCC
.. table:: |CP/A| V3(1986) |BIOS| - :z80:`IOBYTE` an :addr:`03H` (nur PC1715)
   :widths: 10, 10, 10, 10, 10, 10, 10, 10, 10, 10
   :width: 80%

   +-----------------+-------------+-------------+-------------+-------------+
   | Bitcode         | LST:        | PUN:        | RDR:        | CON:        |
   +--------+--------+------+------+------+------+------+------+------+------+
   | i(n+1) |  i(n)  |  i7  |  i6  |  i5  |  i4  |  i3  |  i2  |  i1  |  i0  |
   +========+========+======+======+======+======+======+======+======+======+
   |   0    |   0    | TTY:        | CRT:        | KBD:        | KBD: / CRT: |
   +--------+--------+-------------+-------------+-------------+-------------+
   |   0    |   1    | CRT:        | DUM:        | DUM:        | KBD: / DUM: |
   +--------+--------+-------------+-------------+-------------+-------------+
   |   1    |   0    | LPT:        | LST:        | DUM:        | RDR: / PUN: |
   +--------+--------+-------------+-------------+-------------+-------------+
   |   1    |   1    | DUM:        | UC1:        | UC1:        | UC1: / UC1: |
   +--------+--------+-------------+-------------+-------------+-------------+

:KBD: Tastatur
:CRT: Bildschirm
:DUM: Dummygerät, liefert :code:`1AH` (EOF) bei Eingabe, Hexadezimalausgabe
      auf :envvar:`CRT:` bei Ausgabe, Status (Ein- und Ausgabe) immer bereit
:TTY: Standarddrucker (wahlweise, sonst auf :envvar:`DUM:`)
:LPT: weiterer Drucker (wahlweise, sonst auf :envvar:`DUM:`)
:UC1: (|SIO|) Gerät zur Datenfernübertragung (wahlweise, sonst auf
      :envvar:`DUM:`) Abbildung auf die :envvar:`CON:` Schnittstelle, da
      diese eine Statusroutine für die Empfangsbereitschaft unterstützt.
      Die |BIOS| Funktionen :z80:`CONIN` / :z80:`CONOUT` bzw. READER / PUNCHER
      warten bis zur Empfangs- bzw. Sendebereitschaft eines Zeichens.
      Eine Statusabfrage für die Sendebereitschaft existiert für
      :envvar:`UC1:` nicht.

Die Standardbelegung des I/O Bytes nach Kaltstart ist :code:`00H`, davon abweichende Belegungen können direkt oder über die bekannten |CP/M| Programme wie :program:`STAT` gesetzt werden. Für den :envvar:`LST:` Kanal existiert außerdem im Stoppzustand eine besondere Taste zum Umschalten der
Gerätezuordnung.

Bildschirm, Tastatur
********************

.. index:: triple: CP/A, Version 3; BIOS; Bildschirm

Bildschirm
==========

Die Bildschirmsteuerzeichen sind |SCP| kompatibel, zusätzlich existieren einige Erweiterungen:

.. tabularcolumns:: cL
.. table:: |CP/A| V3(1986) |BIOS| - Bildschirmsteuerzeichen, |SCP| kompatibel
   :widths: 25, 75
   :width: 80%

   +----------------+-------------------------------------------------+
   | Steuerzeichen  | Wirkung                                         |
   +================+=================================================+
   | :code:`00H`    | :z80:`NOP` (keine Wirkung)                      |
   +----------------+-------------------------------------------------+
   | :code:`01H`    | Cursor links oben (home)                        |
   +----------------+-------------------------------------------------+
   | :code:`07H`    | akustisches Zeichen an Tastatur (i.a. nicht     |
   |                | vorhanden, dann Blinken der Lampen neben        |
   |                | :kbd:`STOP` Taste bzw. der Statuszeile beim     |
   |                | |PC1715|)                                       |
   +----------------+-------------------------------------------------+
   | :code:`08H`    | Cursor zurück                                   |
   +----------------+-------------------------------------------------+
   | :code:`0AH`    | Linefeed (neue Zeile)                           |
   +----------------+-------------------------------------------------+
   | :code:`0CH`    | Bildschirm löschen (verzögert zum Lesen der     |
   |                | zuletzt ausgegebenen Bildschirmzeilen), Cursor  |
   |                | links oben                                      |
   +----------------+-------------------------------------------------+
   | :code:`0DH`    | Carriage Return (an Zeilenanfang)               |
   +----------------+-------------------------------------------------+
   | :code:`0EH`    | Umschalten auf 2. Zeichensatz (nur |PC1715|)    |
   +----------------+-------------------------------------------------+
   | :code:`0FH`    | Umschalten auf 1. Zeichensatz (nur |PC1715|)    |
   +----------------+-------------------------------------------------+
   | :code:`14H`    | Rest des Bildschirms löschen                    |
   +----------------+-------------------------------------------------+
   | :code:`15H`    | Cursor nach rechts                              |
   +----------------+-------------------------------------------------+
   | :code:`16H`    | Rest der Zeile löschen                          |
   +----------------+-------------------------------------------------+
   | :code:`18H`    | Zeile löschen, Cursor an Zeilenanfang           |
   +----------------+-------------------------------------------------+
   | :code:`1AH`    | Cursor eine Zeile hoch                          |
   +----------------+-------------------------------------------------+
   | :code:`1BH`    | Einleitung Cursorpositionierfolge, die nächsten |
   |                | beiden Bytes beinhalten Zeile und Spalten,      |
   |                | Offset :code:`00H` oder :code:`80H`             |
   +----------------+-------------------------------------------------+
   | :code:`7FH`    | Delete (streichen Zeichen links vom Cursor)     |
   +----------------+-------------------------------------------------+
   | :code:`82H`    | Cursor an (Standard)                            |
   | (:code:`02H`)  |                                                 |
   +----------------+-------------------------------------------------+
   | :code:`83H`    | Cursor aus                                      |
   | (:code:`03H`)  |                                                 |
   +----------------+-------------------------------------------------+
   | :code:`84H`    | normal hell, nicht invers                       |
   | (:code:`04H`)  |                                                 |
   +----------------+-------------------------------------------------+
   | :code:`85H`    | normal hell, invers                             |
   | (:code:`05H`)  |                                                 |
   +----------------+-------------------------------------------------+
   | :code:`86H`    | intensiv hell, nicht invers                     |
   | (:code:`06H`)  |                                                 |
   +----------------+-------------------------------------------------+
   | :code:`87H`    | intensiv hell, invers                           |
   +----------------+-------------------------------------------------+

Wurde im |BIOS| die Variante mit dem international sehr verbreiteten Terminaltyp |ADM-3A|/|ADM-31| (und kompatiblen) generiert, so werden zusätzlich folgende Steuerzeichen akzeptiert:

.. tabularcolumns:: cL
.. table:: |CP/A| V3(1986) |BIOS| - Bildschirmsteuerzeichen, Terminaltyp ADM3a/ADM31
   :widths: 25, 75
   :width: 80%

   +----------------+-------------------------------------------------+
   | Steuerzeichen  | Wirkung                                         |
   +================+=================================================+
   | :code:`1BH`,   | Einleitung Cursorpositionierfolge, die nächsten |
   | :code:`3DH`    | beiden Bytes beinhalten Zeile und Spalte,       |
   +----------------+ Offset :code:`20H`, Gleichzeitig wird das       |
   | :code:`1BH`,   | Steuerzeichen :code:`1AH` in diesem Fall wie    |
   | :code:`59H`    | :code:`0CH` interpretiert (bis zum nächsten     |
   |                | Warmstart).                                     |
   +----------------+-------------------------------------------------+
   | :code:`1CH`    | Wirkung wie :code:`1AH`, Cursor eine Zeile hoch |
   +----------------+-------------------------------------------------+

Wurde im |BIOS| die Variante mit der Möglichkeit nutzereigener Tastendefinitionen generiert, so sind (neben der Tastendefinition im Stoppzustand) folgende Steuerzeichenfolgen hierfür möglich:

.. tabularcolumns:: cL
.. table:: |CP/A| V3(1986) |BIOS| - Steuerzeichen für Tastendefinitionen
   :widths: 25, 75
   :width: 80%

   +----------------+-------------------------------------------------+
   | Steuerzeichen  | Wirkung                                         |
   +================+=================================================+
   | :code:`1BH`,   | Einleitung der Tastendefinition, es folgt:      |
   | :code:`1BH`    | <Taste>,<zugehörige Zeichenfolge>,\ :code:`00H` |
   |                | für eine Tastendefinition bzw. nur :code:`00H`  |
   |                | für das Löschen aller bisherigen                |
   |                | Nutzertastendefinitionen. Für <Taste> gelten    |
   |                | die Codes, die unabhängig vom Tastaturtyp nach  |
   |                | der Abbildung auf den logischen Tastencode      |
   |                | vorliegen. Für die i.a. umzudefinierenden       |
   |                | Tasten :kbd:`S`, :kbd:`S1`, |...| bzw.          |
   |                | :kbd:`REC`/:kbd:`ENTER`, :kbd:`PF1`, |...|      |
   |                | sind dies die (tastaturunabhängigen!) Codes     |
   |                | :code:`E0H`, :code:`E1H`, |...|; der Code für   |
   |                | andere Tasten ist dem |BIOS| Listing            |
   |                | zu entnehmen.                                   |
   |                | Bei einem Überlauf der entsprechenden           |
   |                | |BIOS| Tabelle erfolgt die beim Steuerzeichen   |
   |                | :code:`07H` beschriebene Reaktion, die          |
   |                | restlichen Zeichen erscheinen dann als          |
   |                | direkte Bildschirmausgabe. Die definierten      |
   |                | Nutzertasten gelten auch über den nächsten      |
   |                | Warmstart hinaus bis zum expliziten Löschen.    |
   +----------------+-------------------------------------------------+

Nicht definierte Steuerzeichen für den Bildschirm (siehe |BIOS| Listing oder |SCP| Dokumentation) werden auf :console:`^` abgebildet (dies kann u.a. bei falsch installierten |CP/M| Programmen auftreten).

.. rubric:: Statuszeile (nur PC1715)

Unter Ausnutzung der Hardwaremöglichkeiten des |PC1715| lässt sich in |CP/A| beim "großen" Bildschirm (BAB2, 24 |x| 80) ohne Umbau und beim "kleinen" Bildschirm (BAB1, 16 |x| 24) durch Ändern der Brücke :comp:`X12` von :pin:`2:3` auf :pin:`2:1` auf dem Bildschirm eine zusätzliche Zeile darstellen. Diese wird zur Darstellung folgender Informationen angewendet:

- Normal- / Sonderzustand des Rechners (Fehlerlampe bei Bürocomputer) durch inverse / normal intensive Darstellung der gesamten Statuszeile. Insbesondere ist hierdurch ein optischer Ersatz des fehlenden akustischen Signals im Fehlerfall (Steuerzeichen :code:`07H`) möglich, indem die Zeile einmal blinkt.
- zur Zeit eingestellte Werte für Standardlaufwerk und Nutzer (z.B. :console:`A1>`), Pflege jede Sekunde entsprechend Hauptspeicherplatz 4,
- Speicherkapazität der zur Zeit |CP/A| bekannten Disketten als Orientierung für das Format der Diskette (z.B. :console:`A:800k B:800k`), Pflege bei jedem LOGIN durch das |BDOS|, gelöscht bei jedem Warmstart,
- Wert des I/O Bytes in hexadezimaler Form (z.B. :console:`i80`), Pflege jede Sekunde entsprechend Hauptspeicherplatz 3),
- Wert des Lampenpuffers in hexadezimaler Form (z.B. :console:`l80`), Pflege jede Sekunde entsprechend Hauptspeicherplatz :addr:`40H`,

  .. tabularcolumns:: lL
  .. table:: |CP/A| V3(1986) |BIOS| - Wert des Lampenpuffers
     :widths: 25, 75
     :width: 80%

     +----------+-------------------------------------------+
     |          | Bedeutung, wenn Bit =1:                   |
     +==========+===========================================+
     | Bit 7:   | alle Zeichen an :envvar:`CRT:` auch an    |
     |          | :envvar:`LST:` (Hardcopy)                 |
     +----------+-------------------------------------------+
     | Bit 6:   | Fehlerlampe                               |
     +----------+-------------------------------------------+
     | Bit 5:   | Druck nur auf rechter Druckerbahn         |
     +----------+-------------------------------------------+
     | Bit 4:   | Zeilenvorschub auf beiden Bahnen zugleich |
     +----------+-------------------------------------------+
     | Bit 3-0: | Selektor 3-0 (muss bei |PC1715| im        |
     |          | Lampenpufferbyte durch Anwender gesetzt   |
     |          | werden)                                   |
     +----------+-------------------------------------------+

- Meldungen des |BIOS|, werden nach 30 Sek. gelöscht,
- Uhrzeit,
- Kopf des Tastaturpuffers, nicht |ASCII| Zeichen als :console:`.`.

Die Anpassung des Bildschirmformats erfolgt beim Kaltstartvorgang automatisch. Beim Bürocomputer wird dabei Bit 6 vom Port :port:`0AH` abgefragt (16 |x| 64, wenn =1; 24 |x| 80, wenn =0). Da am |PC1715| eine solche Hardwareabfrage nicht möglich ist, erfolgt die Abfrage folgendermaßen:

1) Bei der Systemgenerierung wird ein Bildschirmformat als Anfangszustand
   vorgegeben (i.a. 24 |x| 80). Dies wird für die Kaltstartmeldungen zunächst
   angenommen.

2) Beginnt der Nutzer die Uhrzeiteingabe beim Kaltstart nicht innerhalb einer
   maximalen Zeitspanne von 20 s, so wird angenommen, dass der Bildschirm nicht
   lesbar ist und auf das andere Format umgeschaltet. Der gleiche Effekt ist
   durch Betätigen von :kbd:`ESC` statt einer Zifferntaste erreichbar.

3) Dies wiederholt sich solange, bis die Uhrzeit eingegeben ist.

Ein falsches Bildschirmformat führt am |PC1715| hardwarebedingt zu einem nicht synchronisiertem Monitorbild, beim richtigen Format wird es (wieder) stabil.

Um Software für den Bürocomputer, die sich durch Abfrage des Bits 6 im Port :port:`0AH` dem Bildschirmformat anpassen, unverändert auf dem |PC1715| einzusetzen, wird am |PC1715| der |CTC| Kanal 2 mit der Portadresse :port:`0AH` "missbraucht" und mit einer entsprechenden (und sich nicht verändernden) Zeitkonstante geladen.

.. index:: triple: CP/A, Version 3; BIOS; Tastatur

Tastatur
========

Bis zu 48 Tastaturzeichen (Länge modifizierbar) werden vom |BIOS| unabhängig von der Arbeit peripherer Geräte (z.B. Diskettenlaufwerke) gepuffert, i.a. gehen dadurch selbst bei versierten Schreibkräften keine Zeichen verloren, die Meldung :console:`WARTE` bei Textverarbeitungssystemen braucht nicht beachtet zu werden. Bei Programmen, die nicht ständig den Tastaturpuffer leeren (wie z.B. :program:`POWER`) kann bereits die Eingabe für den nächsten Programmschritt "im Voraus" erfolgen.

Beim |PC1715| sind die gepufferten Zeichen im rechten Teil der Statuszeile teilweise sichtbar, Sonderzeichen <:code:`20H` als Punkt.

Bei der Belegung der Tasten mussten bei der Vielfalt von Tastaturen eine Reihe von z.T. widersprüchlichen Forderungen erfüllt werden (die jedoch wesentlich für die Nutzerakzeptanz sind!):

- Anpassung an häufig benutzte Funktionen bei der Systembedienung, dem Textverarbeitungssystem :program:`WordStar` und anderer Standardsoftware (Datenbanktechnik, Tabellenkalkulation, |...|),
- möglichst gleiche Tasten für gleiche Funktionen bei verschiedenen Tastaturen,
- möglichst wenig :kbd:`SHIFT` oder :kbd:`CTRL` Umschaltungen,
- Wirkung der Tasten bei allen Anwendungen gleich (keine spezielle Tastenbelegung für :program:`WordStar` o.ä.),
- räumliche Gruppierung von logisch zusammengehörigen Tasten,
- Nutzung der LED Anzeigen für Systemzustände, die i.a. nicht auf dem Bildschirm sichtbar sind (z.B. Insert Modus bei :program:`WordStar` auf dem Bildschirm sichtbar, daher LED anderweitig nutzbar),
- Möglichkeit der Tastenumdefinition (auch Zeichenfolgen auf einer Taste) für spezielle Nutzeranwendungen.

In der folgenden Tabelle nicht aufgeführte Tasten werden ignoriert. Die Funktion der jeweiligen Taste hängt vom Systemzustand (|CCP| oder Anwendungsprogramm) ab und ist in den entsprechenden Dokumentationen nachzulesen.

.. .. tabularcolumns:: |p{2.2cm}|p{2.2cm}|p{2.2cm}|p{2.2cm}|p{5cm}|

.. tabularcolumns:: \X{15}{100}\X{15}{100}\X{15}{100}\X{15}{100}|\X{40}{100}
.. table:: |CP/A| V2(1985) |BIOS| - Testenbelegung verschiedener Tastauren
   :widths: 15, 15, 15, 15, 40
   :width: 80%

   +-----------+---------+-----------+--------+--------------------------------------+
   | K76x6     | ..x4    | ..37      | PC1715 | Code bzw. Funktion                   |
   +===========+=========+===========+========+======================================+
   | |CUP|     | |CUP|   | |CUP|     | |CUP|  | :kbd:`^E`                            |
   +-----------+---------+-----------+--------+--------------------------------------+
   | |CDN|,    | |CDN|,  | |CDN|,    | |CDN|, | :kbd:`^X`                            |
   | CE        | ERINP   | CE        | CE     |                                      |
   +-----------+---------+-----------+--------+--------------------------------------+
   | |CLT|     | |CLT|   | |CLT|     | |CLT|  | :kbd:`^H` (kann man auf :kbd:`^S`    |
   |           |         |           |        | umdefinieren)                        |
   +-----------+---------+-----------+--------+--------------------------------------+
   | |CRT|     | |CRT|   | |CRT|     | |CRT|  | :kbd:`^D`                            |
   +-----------+---------+-----------+--------+--------------------------------------+
   | |CLB|     | |CLB|   | |CLB|     | |CLB|  | :kbd:`^A`                            |
   +-----------+---------+-----------+--------+--------------------------------------+
   | |CRB|     | |CRB|   | |CRB|     | |CRB|  | :kbd:`^F`                            |
   +-----------+---------+-----------+--------+--------------------------------------+
   | |CDL|     | |CDL|   | |CDL|     | |CDL|  | :kbd:`^C`                            |
   +-----------+---------+-----------+--------+--------------------------------------+
   | |CHO|     | |CHO|   | |CHO|     | |CHO|  | :kbd:`^R`                            |
   +-----------+---------+-----------+--------+--------------------------------------+
   | |CLRB|    | |CLRB|  | |CLRB|    | |CLRB| | :kbd:`^I`                            |
   +-----------+---------+-----------+--------+--------------------------------------+
   | DEL       | DEL     | DELCH     | DEL    | :code:`7FH` (Löschen linkes Zeichen) |
   +-----------+---------+-----------+--------+--------------------------------------+
   | S         | REC     | ENTER     | S      | :kbd:`^B`                            |
   +-----------+---------+-----------+--------+--------------------------------------+
   | S1        | PF1     | PF1       | F1     | :kbd:`^G`                            |
   +-----------+---------+-----------+--------+--------------------------------------+
   | S2        | PF2     | PF2       | F2     | :kbd:`^Y`                            |
   +-----------+---------+-----------+--------+--------------------------------------+
   | S3        | PF3     | PF3       | F3     | :kbd:`^T`                            |
   +-----------+---------+-----------+--------+--------------------------------------+
   | S4        | PF4     | PF4       | F4     | :kbd:`^V`                            |
   +-----------+---------+-----------+--------+--------------------------------------+
   | S5        | PF5     | PF5       | F5     | :kbd:`^L`                            |
   +-----------+---------+-----------+--------+--------------------------------------+
   | S6        | PF6     | PF6       | F6     | :kbd:`^OD`                           |
   +-----------+---------+-----------+--------+--------------------------------------+
   | S7        | PF7     | PF7       | F7     | :kbd:`^OG`                           |
   +-----------+---------+-----------+--------+--------------------------------------+
   | S8        | PF8     | PF8       | F8     | :kbd:`^W`                            |
   +-----------+---------+-----------+--------+--------------------------------------+
   | S9        | PF9     | PF9       | F9     | :kbd:`^Z`                            |
   +-----------+---------+-----------+--------+--------------------------------------+
   | ex. n.    | PF10    | PF10      | F10    | :kbd:`^KS^QP`                        |
   +-----------+---------+-----------+--------+--------------------------------------+
   | ex. n.    | PF11    | PF11      | F11    | :kbd:`^KB`                           |
   +-----------+---------+-----------+--------+--------------------------------------+
   | ex. n     | PF12    | PF12      | F12    | :kbd:`^KK`                           |
   +-----------+---------+-----------+--------+--------------------------------------+
   | ex. n.    | ex. n.  | ex. n.    | F13    | :kbd:`^KV`                           |
   +-----------+---------+-----------+--------+--------------------------------------+
   | DELLINE   | DELLINE | DELL,     | ESC    | :kbd:`^[` (Escape)                   |
   |           |         | ESC       |        |                                      |
   +-----------+---------+-----------+--------+--------------------------------------+
   | ex. n.    | ex. n.  | HLT       | ex. n. | :kbd:`^S` (in |CP/A| STOP Taste)     |
   +-----------+---------+-----------+--------+--------------------------------------+
   | ex. n.    | ex. n.  | PRINT     | ex. n. | :kbd:`^P` (in |CP/A| HARDCOPY Taste) |
   +-----------+---------+-----------+--------+--------------------------------------+
   | ET1       | ENTER   | ET1       | ET     | :kbd:`^M` (CR)                       |
   +-----------+---------+-----------+--------+--------------------------------------+
   | ET2       | RESET   | ET2       | ex. n. | :kbd:`CTRL`, nochmaliges Drücken     |
   |           |         |           |        | hebt :kbd:`CTRL` Zustand auf;        |
   |           |         |           |        | :kbd:`^Q` Prefix für alle            |
   |           |         |           |        | Sondertasten (:program:`WordStar`    |
   |           |         |           |        | :kbd:`^Q` Funktionen) z.B.           |
   |           |         |           |        | :kbd:`^Q^F`, :kbd:`^Q^D` oder        |
   |           |         |           |        | :kbd:`^Q^Y`                          |
   +-----------+---------+-----------+--------+--------------------------------------+
   | Sel       | ex. n.  | 0 |...| 3 | ex. n. | Setzen von Bit i (0 |...| 3) in      |
   | 0 |...| 3 |         | unter     |        | Hauptspeicherplatz :code:`40H` und   |
   |           |         | LED       |        | einschalten LED daneben; Bit 0 wird  |
   |           |         |           |        | als CAPS Funktion benutzt            |
   |           |         |           |        | (groß |ALTRT| klein)                 |
   +-----------+---------+-----------+--------+--------------------------------------+
   | 00        | ex. n.  | 00        | 00     | 00                                   |
   +-----------+---------+-----------+--------+--------------------------------------+
   | 000       | Dzif    | ex. n.    | ex. n. | 000                                  |
   +-----------+---------+-----------+--------+--------------------------------------+
   | M         | EREOF   | M         | F14    | |BIOS| Monitor                       |
   +-----------+---------+-----------+--------+--------------------------------------+
   | CI        | OFF     | RESET     | F15    | Stopp des Rechners mit LED- und      |
   |           |         |           |        | Signalanzeige                        |
   +-----------+---------+-----------+--------+--------------------------------------+
   | INSMODE   | INSMODE | INSMD     | Minus  | Hardcopy Drucker ein/aus LED daneben |
   |           |         |           | (unter | an bei "ein"                         |
   |           |         |           | CE)    |                                      |
   +-----------+---------+-----------+--------+--------------------------------------+
   | INSLINE   | INS     | INSL      | INS    | Synchronisieren Drucker und          |
   |           |         |           |        | BIOS-Druckertreiber                  |
   +-----------+---------+-----------+--------+--------------------------------------+

.. rubric:: Erläuterungen

Hardcopy (:kbd:`INSMODE` Taste) schaltet den Drucker direkt parallel zur Bildschirmausgabe. Zur Kontrolle dieses Zustands wird die neben der Taste liegende Lampe angesteuert (bei |PC1715| siehe Statuszeile). Erneutes Drücken der Taste hebt den Zustand wieder auf. Der Zustand bleibt über den nächsten Warmstart hinaus erhalten.

Es ist zu beachten, dass nicht alle Bildschirmsteuerzeichen vom Drucker verstanden werden, i.a. betrifft dies jedoch nur die expliziten Steuerfolgen zur Cursorpositionierung. Diese Steuerzeichen werden bei der Druckausgabe auf :console:`^` abgebildet. Die :kbd:`^P` Funktion des |BDOS| ist weiterhin verfügbar, jedoch sollten nicht beide Funktionen zugleich aktiv sein.

Mit der Taste :kbd:`INSLINE` werden Druckertreiber und Drucker synchronisiert. Sie sollte nach jeder Neueinstellung des Blattanfangs nach Betätigung der :kbd:`SYN` Taste am Drucker gedrückt werden.

Beim Betätigen der :kbd:`STOP` Taste (:kbd:`CI`/:kbd:`OFF`/:kbd:`RESET`/:kbd:`F15` je nach Tastatur) wird der Tastaturpuffer geleert, das gesamte System bis zur Betätigung einer beliebigen anderen Taste bzw. bis zum Abbruch des laufenden Programms durch Warmstart (:kbd:`^C`) gestoppt (Warteschleife in Tastatureingabe) und die Fehlerlampe eingeschaltet. Diese Reaktionen werden ggf. bis zur Beendigung zeitkritischer Diskettentransfers oder des Bildneuaufbaus verzögert. Die Taste enthält die :kbd:`^S` Funktion des |BDOS| in verallgemeinerter Form und erlaubt auch dann das Stoppen der Anlage, wenn vom Programm keine Tastatureingabe oder Bildschirmausgabe gefordert wird.

Außerdem sind im Stoppzustand die Betätigungen folgender Tasten möglich (die während des Stoppzustandes damit eine andere Bedeutung haben):

.. rubric:: HARDCOPY Taste (:kbd:`INSMD`)

In diesem Fall wird der gesamte momentane Bildschirminhalt auf das LIST Gerät (i.a. Drucker) kopiert.

.. rubric:: Taste Drucker synchronisieren (nur PC1715)

Weiterschalten des :envvar:`LST:` Kanals im I/O Byte bei generierter Variante 2 Bahn Drucker (nur |PC1715|):

:Taste S (=^B):  Umschalten auf andere Druckerbahn, gleiche Wirkung haben
                 die |CP/A| Druckersteuerzeichen :code:`88H` und :code:`89H`;

:Taste F1 (=^G): Ein-/Ausschalten parallelen Vorschub auf beiden Druckerwalzen
                 (für breites Papier), gleiche Wirkung hat das |CP/A|
                 Druckersteuerzeichen :code:`8AH` (ausschalten durch
                 :code:`88H`/:code:`89H`)

.. rubric:: MONITOR Taste (:kbd:`M`), nur wenn mit BIOS Uhr generiert!

Die Uhranzeige auf dem Bildschirm wird aus- bzw. eingeschaltet. Dieser Zustand bleibt auch über einen Warmstart hinweg erhalten. Die Uhr läuft intern weiter, auch wenn die Anzeige ausgeschaltet (bzw. bei |PC1715| "eingefroren") ist.

.. rubric:: ESCAPE Taste (:kbd:`DELL` oder :kbd:`ESC`), wenn Nutzertastendefinition im BIOS generiert.

In diesem Fall sind anschließend folgende Handlungen für eine Tastendefinition notwendig:

- Betätigen der umzudefinierenden Taste,
- Eingabe der zugehörigen Zeichenfolge (einschl. :kbd:`CTRL` und anderen schon umdefinierten Tasten, die gerade neu zu definierende Taste enthält dabei die bis dahin definierte Zeichenfolge),
- Betätigen von Escape zum Abschluss.

Es können bis auf Begrenzungen des Speicherplatzes im |BIOS| (bei Generierung definierbar) beliebig viele Tasten während der Nutzerarbeit umdefiniert werden. Eine volle Tabelle wird durch Blinken der Fehlerlampe (und akustisches Signal, wenn vorhanden) angezeigt.

Soll eine schon umdefinierte Taste erneut umdefiniert werden, so müssen zuvor alle bis dahin erfolgten Umdefinitionen gelöscht werden (was sich auf Grund des begrenzten Tabellenplatzes ohnehin als notwendig erweisen wird). Dies geschieht im Stoppzustand durch zweimaliges Betätigen der ESCAPE Taste hintereinander. Eine Umdefinition von Tasten bzw. ein Löschen der Umdefinitionstabelle kann auch vom Anwenderprogramm erreicht werden (siehe Bildschirmsteuerzeichen).

Als Spezialfall einer Umdefinition sei auf die Neubelegung der Taste "|CLT|" mit :kbd:`^S` statt :kbd:`^H` hingewiesen, so dass auch die Softwarepakete, die als "Cursor nach links" nicht auch :kbd:`^H` sondern nur :kbd:`^S` verstehen, unverändert arbeiten können. Das |BDOS| von |CP/A| behandelt :kbd:`^H` und :kbd:`^S` bei der Stringeingabe gleichberechtigt (durch Wegfall der :kbd:`^S` Funktion zum Stoppen möglich geworden). POWER beispielsweise arbeitet jedoch nur mit :kbd:`^H` richtig, daher wurde als Kaltstartbelegung :kbd:`^H` gewählt.

Wurde die Monitorvariante des |BIOS| generiert, so wird beim Betätigen der MONITOR Taste :kbd:`M` der |BIOS| Monitor aufgerufen (siehe :ref:`osys/cpa/CPA3_86.DOK/besonderheiten-des-bios:BIOS Monitor`; ggf. ebenfalls verzögert); in der Variante ohne Monitor wird die Taste ignoriert.

Beim |PC1715| wird die Taste :kbd:`SI`/:kbd:`S0` unterstützt (Umschalten des Zeichensatzes, auch über Bildschirmsteuerzeichen - s.d.).

.. index:: triple: CP/A, Version 3; BIOS; Drucker

Drucker
*******

a) Bürocomputer

   Im |BIOS| wurde als Variante für |SD1152| Drucker ein Treiber integriert, der neben der normalen Betriebsart den Drucker |Diablo 1610/1620| simuliert. Dadurch konnten alle :program:`WordStar` Druckfunktionen auf der Basis von Microspaceschritten des Druckwerks (1\ |oneh| zeiliger Druck, Schattendruck zur Hervorhebung von Textteilen) sowie eine Farbbandumschaltung (bessere Ausnutzung einfarbiger Bänder) nutzbar gemacht werden. Hinweise zur Ansteuerung sind dem |BIOS| Quelltext bzw. entsprechenden :program:`WordStar` Unterlagen zu entnehmen.

   Folgende Besonderheiten bei der Nutzung von :program:`WordStar` ergeben sich aus der Tatsache, dass der obige Druckertyp eine Schrittweite von 1/120" für den Zeichenabstand besitzt, Drucker vom Typ |SD1152| aber nur 1/60", d.h. im Druckertreiber gerundet werden muss:

   :.CW n: n ungerade arbeitet nicht exakt

   :.UJ 1: Bei Microspace können durch Rundungen Zeichenabstandsänderungen
           auftreten, die das Druckbild negativ beeinflussen.

   Weiterhin ergibt sich als Einschränkung:

   :^P<CR>: nicht erlaubt (Überdrucken von Zeilen arbeitet nur bei zufälliger
            Druckrichtung vorwärts exakt, da kein Vor- und Rückwärtsdruck in
            diesem Fall).

   Die |Diablo 1610/1620| Simulation wird durch die Steuerzeichenfolge ':code:`1B 34`' aktiviert, alle anderen Steuerzeichenfolgen vor dieser Aktivierung werden normal an den Drucker gesendet, es sind also auch entsprechende Programme zur direkten Druckerbedienung nutzbar.

   Bei eingeschalteter Hardcopy erfolgt durch das |BIOS| nach 120 Zeichen ein automatischer Zeilenvorschub und nach 67 Zeilen ein automatischer Seitenvorschub (beide Werte sind im |BIOS| Quelltext und im unteren Hauptspeicher, siehe 5.7.2., modifizierbar). Bei Ausgabe von TAB Steuerzeichen realisiert der Druckertreiber die TAB Funktion in Schritten von 8 Zeichen.

   Zur besseren Farbbandausnutzung bewirkt beim |SD1152| jede zweite Betätigung der Taste "Drucker synchronisieren" (:kbd:`INSLINE`, siehe 5.1.) ein Vertauschen der oberen und der unteren Farbbandhälfte (schwarz und rot). Dieser Zustand bleibt bis zum nächsten Betätigen der Taste auch über den nächsten Warmstart hinaus erhalten.

   Sämtliche Funktionen sind für Drucker mit |PIO|\ 1, |PIO|\ 2 und |IFSS| Anschluss durch entsprechende Quelltextvarianten im |BIOS| verfügbar.

b) PC1715

   Für den |PC1715| sind die Anschlüsse "Printer", |V.24|, |IFSS| A und |IFSS| B (jeweils 9600 |bps|) unterstützt, ausgewählt wird vom |BIOS| der im I/O Byte (Hauptspeicherplatz 3, Bit 6 und 7) eingestellte Druckerausgang, siehe I/O Byte. Um ein Blockieren des Rechners bei versehentlich falsch gewähltem Druckerausgang, defektem oder nicht vorhandenem Drucker zu vermeiden, erfolgt im |BIOS| eine Timeout Überwachung von 30 Sekunden auf die Empfangsbereitschaft des Druckers. Wird diese Zeit überschritten (u.U. muss erst der Druckpuffer geleert werden ehe der Drucker wieder bereit ist), so werden nach einer |BIOS| Meldung bis zum nächsten Warmstart oder dem Betätigen der Taste "Drucker synchronisieren" alle Ausgaben an dieses Gerät ignoriert.

   Es erfolgt (außer bei generierter Variante 2 Bahn Drucker) keine Interpretation der ausgegebenen Zeichen, so dass statt eines Druckers auch andere Geräte mit entsprechender Schnittstelle (einschl. Datenfernübertragung, insbesondere bei :envvar:`UC1:` hier erfolgt grundsätzlich keine Interpretation der zu sendenden und zu empfangenen Zeichen und keine Timeout Überwachung) angeschlossen werden können.

   Es werden 2 Bahn Drucker mit der Schnittstelle 1 (z.B. |SD1152| |IFSS|) für beide Bahnen getrennt und parallel unterstützt. Dazu sind in |CP/A| (nicht gültig für |SCP|!) folgende Steuerzeichen definiert:

   :88H: Drucken auf linker Bahn (Standard)
   :89H: Drucken auf rechter Bahn (absolute Position 138)
   :8AH: Drucken auf linker und rechter Bahn (Linefeed auf beiden)

   Die gleiche Wirkung wie obige Steuerzeichen kann im Stoppzustand durch Betätigen der Tasten :kbd:`S` (:kbd:`^B`) bzw. :kbd:`F1` (:kbd:`^G`) erreicht werden (siehe Abschnitt Tastatur). Der eingestellte Zustand wird im Lampenpuffer, Bit 5 und 4 gespeichert und bleibt über den nächsten Warmstart hinaus erhalten.

.. index:: triple: CP/A, Version 3; BIOS; Zeitgeber

Zeitgeberdienste
****************

Überblick der Zeitgeberdienste
==============================

Unter Ausnutzung der beim Bürocomputer kaskadierten |CTC| Kanäle 2 und 3 wurden Zeittakte von 5 |ms| und 1 s bereitgestellt. Beim |PC1715| sind die freien |CTC| Kanäle nicht kaskadiert, hier wird als Kompromiss ein 25 |ms| Takt bereitgestellt, auf dessen Basis softwaremäßig ein 1 s Takt erzeugt wird. Auf Grund von zeitkritischen Abläufen am |PC1715| (nur ein Prozessor!) von länger als 25 |ms| (z.B. Diskettentransfer von 1 |kB| Sektorlänge ca. 40 |ms|) können 25 |ms| Takte verloren gehen, d.h. sowohl 25 |ms| als auch 1 s Takt können über längere Zeit hinweg "nachgehen". Im folgenden sind im Falle des |PC1715| alle "5 |ms|" sinngemäß (Faktor 5) durch "25 |ms|" zu ersetzen.

Der Zeittakt von 5 |ms| ist für Zeitmessungen vorgesehen. Die Einheit von 5 |ms| ist ein Kompromiss zwischen der zusätzlichen Interruptbelastung und dem maximal möglichen Faktor von 256 zur Erreichung des kaskadierten 1 s Taktes. Bei jedem Interrupt im Abstand von 5 |ms| wird ein 2 Byte Zähler auf dem Hauptspeicherplatz :z80:`TIM5CN` (siehe :ref:`osys/cpa/CPA3_86.DOK/besonderheiten-des-bios:Feste Adressen im unteren Hauptspeicher`) zyklisch um 1 erhöht. Der Anfangswert ist beliebig, d.h. es sind durch ständiges Aktivieren/Deaktivieren auch kumulative Zeitmessungen möglich. Die maximale Messdauer beträgt für eine Periode ca. 327 s bei einer Genauigkeit von 5 |ms|.

Der 5 |ms| Zeittakt ist standardmäßig aktiviert. Nach Rückkehr aus der Interruptreaktionsroutine des Taktes wird beim Bürocomputer :z80:`CONST` aufgerufen und damit ein (nicht existierender) Tastaturinterrupt simuliert und eine möglicherweise gedrückte Taste gelesen.

Der Zeittakt von 1 s ist zur Realisierung eines Timeout Apparats vorgesehen. Bei jedem Interrupt wird ein 2 Byte Zähler auf Hauptspeicherplatz :z80:`TIM1CN` (siehe :ref:`osys/cpa/CPA3_86.DOK/besonderheiten-des-bios:Feste Adressen im unteren Hauptspeicher`) um 1 vermindert. Der Nulldurchgang stellt i.a. das Timeout Ereignis dar, muss jedoch explizit abgefragt werden (keine Unterbrechung des gerade aktiven Programms!). Die maximale Timeout Größe beträgt hierbei ca. 9,1 Stunden. Außerdem wird jede Sekunde zu der durch :z80:`TIM1RT` (siehe :ref:`osys/cpa/CPA3_86.DOK/besonderheiten-des-bios:Feste Adressen im unteren Hauptspeicher`) definierten Routine gesprungen, wodurch beliebige Nutzerroutinen aktivierbar sind (alle Register frei, Rückkehr mit :z80:`RET`, Interruptverbot muss erhalten bleiben!). Standardmäßig wird bei jedem Warmstart die Adresse einer leeren Routine (nur :z80:`RET` Befehl) auf :z80:`TIM1RT` hinterlegt. Auch der 1 s Zeittakt ist standardmäßig aktiviert.

.. index:: triple: CP/A, Version 3; BIOS; Speicherschutz

Speicherschutzdienste (nur für Bürocomputer)
********************************************

Überblick der Speicherschutzdienste
===================================

Die Speicherschutzeinrichtung basiert auf einer Einteilung des verfügbaren Hauptspeichers von 64 |kB| in 64 Byte lange Abschnitte, die unabhängig voneinander als geschützt gekennzeichnet werden können. Schreibbefehle in diese Bereiche sind nur aus geschützten Bereichen selbst erlaubt, anderenfalls erfolgt eine Unterbrechung. Gekoppelt mit dem Speicherschutz ist ein Schutz gegen Ausführung von E/A Befehlen außerhalb von geschützten Bereichen (führt zu |NMI| Interrupt), d.h. geschützte Bereiche werden als privilegierte Systemprogramme betrachtet.

Bei Nutzung der Speicherschutzeinrichtung muss daher der |BIOS|/|BDOS| Bereich grundsätzlich mitgeschützt werden (vom |BDOS| aus wird in Diskettentabellen geschrieben, die im |BIOS| liegen). Alle sonstigen Programmbereiche, in denen E/A Befehle abgearbeitet werden können, müssen ebenfalls unabhängig von dem eigentlich gegen Überschreiben zu sichernden Bereich geschützt werden.

Routinen zur Realisierung der Speicherschutzdienste
===================================================

.. rubric:: :z80:`MPINIT`

Initialisierung der Speicherschutzeinrichtung und Definition des standardmäßig zu schützenden Bereichs von |BDOS|\+\ :addr:`40H` bis vor Bildschirmpuffer.

.. rubric:: :z80:`MPSET` (Integer Register :reg:`BC`: Anfangsadresse, Integer Register :reg:`DE`: Endadresse)

Definition eines zusätzlich zu schützenden Bereichs. Sind die Adressen nicht durch 64 teilbar, so wird die Anfangsadresse ab- und die Endadresse aufgerundet.

.. rubric:: :z80:`MPOFF`

Der gesamte Speicherschutz wird außer Kraft gesetzt. :z80:`MPOFF` wird bei jedem Warmstart aufgerufen, d.h. der normale |CP/A| Betrieb erfolgt ohne Speicherschutz.

Reaktion bei Verletzen des Speicherschutzes
===========================================

Der Schreibversuch wird unterdrückt. Auf dem Bildschirm erfolgt eine Ausschrift mit Angabe der Adresse des übernächsten Befehls (keine sofortige Unterbrechung auf Grund der Bearbeitungszeit der Hardware). Ist das System mit |BIOS| Monitor generiert, so wird anschließend zu diesem verzweigt, andernfalls wird das laufende Programm nicht gestoppt (eine Verlangsamung der Speicherschutzausschriften kann in diesem Fall z.B. durch Hardcopy auf den Drucker erreicht werden).

Reaktion bei Verletzen des E/A Schutzes
=======================================

Der E/A Befehl im ungeschützten Bereich wird ausgeführt. Anschließend erfolgt eine |NMI| Unterbrechung, d.h. es wird zur Adresse :addr:`66H` verzweigt. Da diese Zelle evtl. vom auszutestenden Programm benutzt wird (Standard :z80:`FCB` von :addr:`5CH` bis :addr:`7FH`), kann hier nicht standardmäßig ein Sprung zur entsprechenden Reaktionsroutine hinterlegt werden. Deshalb wurde innerhalb des |BIOS| Monitor die Möglichkeit geschaffen, auf Adresse :addr:`66H` wahlweise:

1) einen Sprungbefehl zur Reaktionsroutine (Reaktion dann analog zu Speicherschutz, jedoch ohne Aufruf |BIOS| Monitor), oder
2) einen Sprungbefehl zu einer leeren Reaktionsroutine (nur :z80:`RETN`) zum Ignorieren des Schutzes, oder
3) keinen Sprungbefehl

zu hinterlegen (siehe :ref:`osys/cpa/CPA3_86.DOK/besonderheiten-des-bios:\:command:\`PROTECT\` Kommando (nur für Bürocomputer)`). Ein hinterlegter Sprungbefehl muss bis nach dem Aufruf von :z80:`MPOFF` dort stehen bleiben!

.. index:: triple: CP/A, Version 3; BIOS; Console

Konsoleneingabe und Konsolenausgabe
***********************************

Die den alphanumerischen Tasten und den anderen Funktionstasten entsprechenden logischen Zeichenfolgen gelangen in einen Tastaturpuffer. Die Mehrzeicheneingaben (z.B. :kbd:`00` oder :kbd:`^KB`) werden vorher aufgelöst. :z80:`CONST` meldet zurück, ob der Puffer wenigstens ein Zeichen enthält.

:z80:`CONIN` übergibt - wenn vorhanden - das erste Zeichen aus dem Puffer. Anderenfalls wird auf die nächste Eingabe gewartet. Des Weiteren realisiert :z80:`CONIN` die Dauerfunktion für alle alphanumerischen Tasten der Tastatur |K7604/06|.

In :z80:`CONOUT` wird die Ausgabe des Zeichens :code:`07H` (BELL) durch einmaliges Blinken der Fehlerlampen realisiert.

.. index:: triple: CP/A, Version 3; BIOS; Monitor

BIOS Monitor
************

Der |BIOS| Monitor stellt - seine Generierung vorausgesetzt - einen Satz von residenten Funktionen bereit, die somit ohne Veränderung der Speicherplatzbelegung ständig, d.h. auch während der Arbeit eines Nutzerprogramms zur Verfügung stehen.

Die Aktivierung dieser Funktionen ist im Dialog durch Drücken der MONITOR Taste oder direkten Aufruf der Prozedur :z80:`MONCAL` möglich.

Der |BIOS| Monitor schützt sich gegen rekursiven Aufruf.

MONITOR Taste
=============

Die MONITOR Taste ist gegenüber anderen Tasten der Tastatur nicht ausgezeichnet. Insbesondere erzeugt auch sie bei ihrer Betätigung am Bürocomputer keinen Interrupt, d.h. sie muss abgefragt werden. Folgende zwei Methoden wurden am Bürocomputer implementiert:

1) Abfrage bei Eingabe eines Zeichens durch das |BIOS|, d.h. nur zu Zeitpunkten, wo auch eine Eingabe vom Programm gefordert wird und die Steuerung ohnehin im |BIOS| liegt;
2) Abfrage im 5 |ms| Zeitinterrupt, falls dieser aktiv ist.

Nach Drücken der MONITOR Taste erfolgt eine Ausschrift mit Angabe der Rückkehradresse (d.h. der Unterbrechungsstelle beim 5 |ms| Interrupt bzw. der Aufrufstelle bei normaler Zeicheneingabe). Danach können nacheinander beliebig viele Monitorfunktionen durch Eingabe ihres Anfangsbuchstabens (groß oder klein) aufgerufen werden.

Eine leere Eingabe oder die erneute Betätigung der MONITOR Taste führen zum Verlassen des |BIOS| Monitors.

Übersicht über die Monitorkommandos
===================================

Die Monitorkommandos sind:

.. tabularcolumns:: cL
.. table:: |CP/A| V3(1986) |BIOS| - Monitorkommandos
   :widths: 25, 75
   :width: 80%

   +----------+-----------------------------------------------------+
   | Zeichen  | Funktion                                            |
   +==========+=====================================================+
   | :kbd:`M` | Lesen/Modifizieren Speicher                         |
   +----------+-----------------------------------------------------+
   | :kbd:`C` | Aufruf Unterprogramm                                |
   +----------+-----------------------------------------------------+
   | :kbd:`P` | Ein-/Ausschalten Speicherschutz                     |
   +----------+-----------------------------------------------------+
   | :kbd:`R` | Anzeige der Registerstände beim Aufruf des Monitors |
   +----------+-----------------------------------------------------+
   | :kbd:`T` | Ein-/Ausschalten Zeittakt                           |
   +----------+-----------------------------------------------------+
   | :kbd:`H` | Help (Konvertieren Hex |CRT| Dez |CRT| |ASCII|)     |
   +----------+-----------------------------------------------------+

:command:`MEM` Kommando
=======================

Nach Eingabe von :kbd:`M` wird eine 2 Byte Adresse in hexadezimaler Form erwartet. Sie gibt die Anfangsadresse eines Speicherbereichs an.

Jeweils ein Byte wird aufsteigend in hexadezimaler Form angezeigt und eine Eingabe erwartet:

:keine Eing.:   keine Veränderung; nächstes Byte
:2 Hex-Ziffern: Überschreiben des Bytes; nächstes Byte
:"-" (Minus):   keine Veränderung; vorheriges Byte
:4 Hex-Ziffern: keine Veränderung; neuer Speicherbereich
:"." (Punkt):   Ende des :command:`MEM` Kommandos

:command:`CALL` Kommando
========================

Nach Eingabe von :kbd:`C` wird eine 2 Byte Adresse in hexadezimaler Form erwartet. Sie gibt die Startadresse eines Unterprogramms an. Als Rückkehradresse wird vor dem Ansprung dieses Programms eine Rückkehr zum |BIOS| Monitor in den Stack gebracht.

:command:`PROTECT` Kommando (nur für Bürocomputer)
==================================================

Nach Eingabe von :kbd:`P` (Aufruf :z80:`MPINIT` Definition des standardmäßig zu schützenden Bereichs) wird eine der folgenden Eingaben erwartet:

:"." (Punkt):   keine weitere Aktion
:2 Hex-Ziffern: ein Adresspaar: bezeichnet einen zu schützenden Bereich
:"-" (Minus):   Aufruf MPOFF: Aufhebung des gesamten Speicherschutzes
:"I":           Einstellung des Regimes "Ignorieren von E/A Schutzverletzungen", d.h. Hinterlegen von :z80:`RETN` auf :addr:`66H` (vgl. :ref:`osys/cpa/CPA3_86.DOK/besonderheiten-des-bios:Reaktion bei Verletzen des E/A Schutzes`)
:"L":           Einstellung des Regimes "Protokollieren von E/A Schutzverletzungen", d.h. Hinterlegen eines Sprungbefehls auf :addr:`66H` (vgl. :ref:`osys/cpa/CPA3_86.DOK/besonderheiten-des-bios:Reaktion bei Verletzen des E/A Schutzes`).

Wird keine Regimeeinstellung ("I" oder "L") vorgenommen, so bleibt die Zelle :addr:`66H` unverändert (Standard :z80:`FCB` von :addr:`5CH` bis :addr:`7FH`).

:command:`REG` Kommando
=======================

Nach Eingabe von :kbd:`R` werden die Stände der Registerpaare :reg:`AF`, :reg:`BC`, :reg:`DE`, :reg:`HL`, :reg:`IX`, :reg:`IY`, :reg:`SP` an der Aufrufstelle des Monitors sowie die Leitadresse des Rettungsbereich dieser Register (für eventuelle Modifizierung mittels :command:`MEM` Kommando) angezeigt.

:command:`TIME` Kommando
========================

Nach Eingabe von :kbd:`T` wird eine :kbd:`5` zur Aktivierung / Deaktivierung des 5 |ms| (bei |PC1715| 25 |ms|) Zeittakts oder eine :kbd:`1` zur Aktivierung / Deaktivierung des 1 s (bei |PC1715| wie 25 |ms|) Zeittakts erwartet. Folgt danach kein Zeichen, so wird der Takt aktiviert, ein anschließendes :kbd:`-` deaktiviert ihn.

:command:`HELP` Kommando
========================

Nach Eingabe von :kbd:`H` wird eine Hexadezimalzahl zwischen :code:`0` und :code:`FFFF` erwartet. Ihr Dezimalwert und ggf. das zugeordnete |ASCII| Zeichen (nur für Zahlen zwischen :code:`20H` und :code:`7EH`) werden ausgegeben.

.. index:: triple: CP/A, Version 3; BIOS; Erweiterungen

Einbindung der Erweiterungen in CP/A
************************************

Sprungvektor
============

Der Aufruf des Monitors, der Zeitgeber- und der Speicherschutzroutinen u.a. |BIOS| Unterprogramme ist von normalen Programmen aus ist über einen Sprungvektor möglich. Dieser besteht aus je 3 Byte langen Sprungbefehlen. Die Anfangsadresse des Sprungvektors befindet sich auf Hauptspeicherplatz :addr:`4EH` (beim Warmstart hinterlegt).

Folgende Entries sind vergeben (Funktion siehe |BIOS| Listing):

.. tabularcolumns:: clL
.. table:: |CP/A| V2(1985) |BIOS| - Sprungvektoren
   :widths: 10, 15, 75
   :width: 80%

   +------------+------------------+--------------------------------------+
   | Nummer     | Entry            | Parameter                            |
   +============+==================+======================================+
   | :code:`00` | :z80:`JP MONCAL` | \-                                   |
   +------------+------------------+--------------------------------------+
   | :code:`03` | :z80:`JP TIM5ON` | \-                                   |
   +------------+------------------+--------------------------------------+
   | :code:`06` | :z80:`JP TIM5OF` | \-                                   |
   +------------+------------------+--------------------------------------+
   | :code:`09` | :z80:`JP TIM1ON` | \-                                   |
   +------------+------------------+--------------------------------------+
   | :code:`0C` | :z80:`JP TIM1OF` | \-                                   |
   +------------+------------------+--------------------------------------+
   | :code:`0F` | :z80:`JP MPINIT` | \-                                   |
   +------------+------------------+--------------------------------------+
   | :code:`12` | :z80:`JP MPSET`  | Reg. :reg:`BC`, :reg:`DE`            |
   +------------+------------------+--------------------------------------+
   | :code:`15` | :z80:`JP MPOFF`  | \-                                   |
   +------------+------------------+--------------------------------------+
   | :code:`18` | :z80:`JP DELSPS` | \-                                   |
   +------------+------------------+--------------------------------------+
   | :code:`1B` | :z80:`JP DELSPR` | \-                                   |
   +------------+------------------+--------------------------------------+
   | :code:`1E` | :z80:`JP DISKIO` | Reg. :reg:`HL`, :reg:`IX`, :reg:`AF` |
   +------------+------------------+--------------------------------------+
   | :code:`21` | :z80:`JP UMLCON` | Reg. :reg:`A`                        |
   +------------+------------------+--------------------------------------+

Sind die betreffenden Funktionen nicht generiert, so steht auf dem Entry ein :z80:`RET` Befehl (und 2 :z80:`NOP` Befehle).

Der Aufruf ist z.B. über folgende Befehlsfolge möglich:

.. code-block:: nasm
   :linenos:

   	ld	a,<entry>
   	ld	hl,(4eh)
   	add	a,l
   	ld	l,a
   	ld	a,0		;kein XOR!
   	adc	a,h
   	ld	h,a
   	jp	(hl)

Feste Adressen im unteren Hauptspeicher
=======================================

.. tabularcolumns:: llL
.. table:: |CP/A| V3(1986) |BIOS| - Verständigungsbereich (|Zero Page|)
   :widths: 15, 15, 70
   :width: 80%

   +-------------+---------------------------------------------------------+
   | Bereich     | Inhalt                                                  |
   +=============+==================+======================================+
   | :addr:`00H` | :z80:`JP BIOS+3` | Warmstart                            |
   | |...|       |                  |                                      |
   | :addr:`02H` |                  |                                      |
   +-------------+------------------+--------------------------------------+
   | :addr:`03H` | :z80:`IOBYTE`                                           |
   +-------------+------------------+--------------------------------------+
   | :addr:`04H` |                  | User / Default Drive                 |
   +-------------+------------------+--------------------------------------+
   | :addr:`05H` | :z80:`JP BDOS`                                          |
   | |...|       |                                                         |
   | :addr:`07H` |                                                         |
   +-------------+------------------+--------------------------------------+
   | :addr:`08H` | frei             | für :z80:`RST` Routinen nutzbar      |
   | |...|       |                  |                                      |
   | :addr:`1FH` |                  |                                      |
   +-------------+------------------+--------------------------------------+
   | :addr:`20H` | (frei)           | bei |OSS| |RAM| Floppy belegt, sonst |
   | |...|       |                  | frei                                 |
   | :addr:`2CH` |                  |                                      |
   +-------------+------------------+--------------------------------------+
   | :addr:`2DH` | frei             | für :z80:`RST` Routinen nutzbar      |
   | |...|       |                  |                                      |
   | :addr:`37H` |                  |                                      |
   +-------------+------------------+--------------------------------------+
   | :addr:`38H` | :z80:`JP BREAK`  | Debugger                             |
   +-------------+------------------+--------------------------------------+
   | :addr:`3BH` |                  | reserviert                           |
   | |...|       |                  |                                      |
   | :addr:`3FH` |                  |                                      |
   +-------------+------------------+--------------------------------------+

Als Scratch Bereich des |BIOS| sind in |CP/M| die Zellen :addr:`40H` bis :addr:`4FH` freigehalten. Sie werden von |CP/A| wie folgt benutzt, bis auf :z80:`CPMEXT` können alle Werte auch vom Nutzer gesetzt werden:

.. tabularcolumns:: p{2cm}p{2cm}LL
.. table:: |CP/A| V2(1985) |BIOS| - Arbeitszellen
   :widths: 15, 15, 40, 30
   :width: 80%

   +-----------------+------------------------------------------------------------+
   | Bereich         | Inhalt                                                     |
   +=================+============================================================+
   | *Pufferspeicher für Tastaturlampen*                                          |
   +-----------------+----------------------------------+-------------------------+
   | :addr:`40H`     | (0 bei aus, 1 bei ein)           | bei |K7604/06| neben    |
   |                 +---------------+------------------+-------------------------+
   |                 |         Bit 7 | Hardcopylampe    | INSMODE                 |
   |                 +---------------+------------------+-------------------------+
   |                 |             6 | Fehlerlampe      | CI                      |
   |                 +---------------+------------------+-------------------------+
   |                 |     5 |...| 4 | reserviert (=0)                            |
   |                 +---------------+------------------+-------------------------+
   |                 |     5 |...| 4 | Selektor 3-0     | Sel-Tasten              |
   +-----------------+---------------+------------------+-------------------------+
   | *Zeitgeberdienste*                                                           |
   +-----------------+---------------+--------------------------------------------+
   | :addr:`41H`     | :z80:`TIM5CN` | Zähler 5 |ms| Zeittakt                     |
   | |...|           |               |                                            |
   | :addr:`42H`     |               |                                            |
   +-----------------+---------------+--------------------------------------------+
   | :addr:`43H`     | :z80:`TIM1CN` | Zähler 1 s Zeittakt                        |
   | |...|           |               |                                            |
   | :addr:`44H`     |               |                                            |
   +-----------------+---------------+--------------------------------------------+
   | :addr:`45H`     | :z80:`TIM1RT` | Adresse der 1 s Nutzerroutine              |
   | |...|           |               |                                            |
   | :addr:`46H`     |               |                                            |
   +-----------------+---------------+--------------------------------------------+
   | *Hardcopy Bildschirm* |CRT| *Drucker*                                        |
   +-----------------+---------------+--------------------------------------------+
   | :addr:`47H`     | :z80:`LMAXP`  | max. Anzahl Druckpositionen bei            |
   +-----------------+---------------+--------------------------------------------+
   | :addr:`48H`     | :z80:`LMAXN`  | max. Anzahl Druckzeilen bei                |
   +-----------------+---------------+--------------------------------------------+
   | :addr:`49H`     |               | reserviert                                 |
   | |...|           |               |                                            |
   | :addr:`4DH`     |               |                                            |
   +-----------------+---------------+--------------------------------------------+
   | :addr:`4EH`     | :z80:`CPMEXT` | Sprungvektoradresse für |CP/A| Erweiterung |
   | |...|           |               |                                            |
   | :addr:`4FH`     |               |                                            |
   +-----------------+---------------+--------------------------------------------+
   | *BIOS Uhr*                                                                   |
   +-----------------+---------------+--------------------------------------------+
   | :addr:`50H`     | :z80:`TIME`   | |BIOS| BCD Uhr in der Form HHMMSS          |
   | |...|           |               |                                            |
   | :addr:`52H`     |               |                                            |
   +-----------------+---------------+--------------------------------------------+
   | :addr:`53H`     | :z80:`DATE`   | von :program:`ACCOUNT` hinterlegtes        |
   | |...|           |               | BCD Datum TTMMJJ                           |
   | :addr:`55H`     |               |                                            |
   +-----------------+---------------+--------------------------------------------+
   | :addr:`56H`     |               | reserviert                                 |
   | |...|           |               |                                            |
   | :addr:`5BH`     |               |                                            |
   +-----------------+---------------+--------------------------------------------+
   | *Floppy Disk Operationen*                                                    |
   +-----------------+---------------+--------------------------------------------+
   | :addr:`5CH`     | :z80:`FCB`    | Standard |FCB|                             |
   | |...|           |               |                                            |
   | :addr:`7FH`     |               |                                            |
   +-----------------+---------------+--------------------------------------------+
   | :addr:`80H`     | :z80:`DMA`    | Standard |DMA|                             |
   | |...|           |               |                                            |
   | :addr:`0FFH`    |               |                                            |
   +-----------------+---------------+--------------------------------------------+
   | *Anwenderbereich*                                                            |
   +-----------------+---------------+--------------------------------------------+
   | ab :addr:`100H` |               | Beginn |TPA|                               |
   +-----------------+---------------+--------------------------------------------+

Belegung der Interruptsäule
===========================

Die Interruptsäule befindet sich i.a. :addr:`40H` Bytes vor dem Beginn des Bildschirmpuffers, d.h. auf :addr:`0F7C0H`. Die genaue Lage sollte über das :reg:`I` Register ermittelt werden, im folgenden wird hierfür ':code:`ii`' verwendet:

.. tabularcolumns:: cL
.. table:: |CP/A| V3(1986) |BIOS| - Interruptsäule
   :widths: 25, 75
   :width: 80%

   +--------------------+--------------------------------------------+
   | Bereich            | Zugehörigkeit                              |
   +====================+============================================+
   | vor :addr:`0iiC0H` | |BIOS|, d.h. Interruptsäule ohne           |
   |                    | Systemmodifikation nicht nach vorn         |
   |                    | "verlängerbar"                             |
   +--------------------+--------------------------------------------+
   | :addr:`0iiC0H`     | Kassettenanschluss, frei wenn nicht vorher |
   | |...|              |                                            |
   | :addr:`0iiCFH`     |                                            |
   +--------------------+--------------------------------------------+
   | :addr:`0iiD0H`     | |SIO| (|V.24| o.ä.)                        |
   | |...|              |                                            |
   | :addr:`0iiDFH`     |                                            |
   +--------------------+--------------------------------------------+
   | :addr:`0iiE0H`     | frei                                       |
   | |...|              |                                            |
   | :addr:`0iiE5H`     |                                            |
   +--------------------+--------------------------------------------+
   | :addr:`0iiE6H`     | Speicherschutz                             |
   | |...|              |                                            |
   | :addr:`0iiE7H`     |                                            |
   +--------------------+--------------------------------------------+
   | :addr:`0iiE8H`     | Disketten                                  |
   | |...|              |                                            |
   | :addr:`0iiEBH`     |                                            |
   +--------------------+--------------------------------------------+
   | :addr:`0iiECH`     | frei                                       |
   | |...|              |                                            |
   | :addr:`0iiEFH`     |                                            |
   +--------------------+--------------------------------------------+
   | :addr:`0iiF0H`     | Lochstreifen Leser/Stanzer                 |
   | |...|              |                                            |
   | :addr:`0iiF7H`     |                                            |
   +--------------------+--------------------------------------------+
   | :addr:`0iiF8H`     | System |CTC| Kanal 0, 1 (frei)             |
   | |...|              |                                            |
   | :addr:`0iiFBH`     |                                            |
   +--------------------+--------------------------------------------+
   | :addr:`0iiFCH`     | System |CTC| Kanal 2, 3 (5 |ms|, 1 s)      |
   | |...|              |                                            |
   | :addr:`0iiFFH`     |                                            |
   +--------------------+--------------------------------------------+

.. spelling::

   Dzif
   Sel

.. Local variables:
   coding: utf-8
   mode: text
   mode: rst
   End:
   vim: fileencoding=utf-8 filetype=rst :
