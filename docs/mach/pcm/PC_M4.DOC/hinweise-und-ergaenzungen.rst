.. highlight:: none
   :linenothreshold: 1

.. index:: pair: PC/M; Hinweise und Ergänzungen

Hinweise und Ergänzungen
########################

Der |PC/M| Computer ist aufgrund seiner modularen Struktur ein erweiterbares System. Je nach Wunsch des Anwenders sind dazu unterschiedlichste Hardwaremodule nachrüstbar. Um die Anzahl systemspezifischer Modulen zu begrenzen, wurde eine |K1520| Buskoppelplatine entwickelt, die den Anschluss von |K1520| Baugruppen über den dort definierten Systembus ermöglicht. Darüber hinaus wurden durch uns und durch andere Anwender des |PC/M| unterschiedliche Leiterplatten zur |AD|/|DA| Wandlung, zur Tonausgabe, |RAM| Erweiterung bis zu 512 |kB| (Zusatz |RAM| Floppy), zur |EPROM| Erweiterung (als |EPROM| Floppy), als |EPROM| Emulator und Programmierzusatz sowie eine Floppy Disk Steuerung entwickelt. Zusätzlich existieren Varianten der Tastatursteuerung, die zu gegebenem Zeitpunkt veröffentlicht werden.

Als Grafikzusatz empfehlen wir den Einsatz einer der bereits zahlreichen veröffentlichten Versionen (|rfe|, |MP| u.a.) für |K1520| Systeme.

Das Betriebssystem wurde weiterentwickelt und steht momentan (08/88) in der Version 2.02 bei voller Kompatibilität zum veröffentlichten System zur Verfügung.

.. index:: triple: PC/M; Hinweise und Ergänzungen; K1520 V-Tape

.. _kcsystems-mach-pcm-fa1188k1520vtcp:

V-Tape für K1520 Systeme
************************

Die Kompatibilität des |PC/M| Computers zu anderen |CP/M| kompatiblen Systemen kann erst dann voll ausgeschöpft werden, wenn eine Konvertierungsmöglichkeit von Kassette auf Magnetband und umgekehrt besteht. Dazu ist beispielsweise eine direkte Datenübertragung zwischen unterschiedlichen Computern mittels |IFSS| oder |V.24| möglich (:Program:`MOVE-IT` für |PC/M| u.a. Programme).

.. index:: triple: PC/M; Stromlaufplan; FA 11/88-K1520VTCP (SP)

.. list-table:: FA 11/88-K1520VTCP (SP)
   :name: kcsystems-mach-pcm-fa1188k1520vtcp-sp
   :class: longtable
   :align: center
   :width: 80 %
   :header-rows: 1

   * - FA 11/88-K1520VTCP (SP)

   * - .. figure:: bild-a1.png
          :name: kcsystems-mach-pcm-bild-a1
          :figclass: align-center
          :align: center
          :width: 560 px
          :alt: Kassettenmodul für |K1520| Systeme

          Kassettenmodul für |K1520| Systeme

|PC_M_BA1_N| zeigt eine Schaltung, die bei geringem Hardwareaufwand einen Programmaustausch mit |K1520| Computersystemen ermöglicht. Solche Computer sind z.B. der |A5120| und |A5130|. Die Schaltung entspricht weitgehend der im |PC/M| Computer realisierten. Über das V-Tape Kopierprogramm :program:`VTCP` können damit Programme und Dateien von Kassette auf Diskette (auch auf das |RAM| Floppy des |PC/M|) und umgekehrt übertragen werden. In |PC_M_BB1_N| ist das HEX-Listing abgebildet. Durch das Programm wird der Adressbereich von :addr:`0100H` bis :addr:`0AFFH` des Computers belegt. Da die |CP/M| Schnittstellen genutzt werden, ist eine Verwendung in anderen Computern erreichbar. Der Programmstart erfolgt (nach geladenem |BDOS| beim |PC/M|) auf Adresse :addr:`0100H`. Befindet sich das :file:`VTCP.COM` bereits auf Diskette (|RAM| Floppy), wird es wie üblich nur mit dem Namen (:command:`VTCP`) aufgerufen und gestartet. Das Abspeichern auf Kassette erfolgt im Betriebssystem |CP/V| oder mit dem residenten Kommando :command:`SAVE` oder einem anderen Dienstprogramm auf das Floppy Disk Laufwerk bzw. das |RAM| Floppy des |PC/M| Computers. Das Programm meldet sich mit seiner Überschrift und dem Prompt :console:`VTC>`. Die Anpassung an den Bürocomputer |A5120| gemäß Stromlaufplan nach |PC_M_BA1_N| und an den |PC/M| Computer erfolgt durch Austausch folgender Bytes im Listing:

.. tabularcolumns:: p{0.32\linewidth}p{0.12\linewidth}p{0.12\linewidth}p{0.24\linewidth}
.. table:: |PC/M| |V-Tape| für |K1520| Systeme - Anpassung an den Bürocomputer |A5120| / |A5130|
   :name: kcsystems-mach-pcm-tabelle-a1
   :widths: 40, 15, 15, 30
   :class: longtable
   :align: center
   :width: 80%

   +----------------+--------------+--------------+----------------------------+
   | Adresse        | |A51xx|      | |PC/M|       |                            |
   +================+==============+==============+============================+
   | :addr:`0508H`, | :code:`035H` | :code:`085H` | |PIO| Daten                |
   | :addr:`0510H`, |              |              |                            |
   | :addr:`0518H`, |              |              |                            |
   | :addr:`051CH`, |              |              |                            |
   | :addr:`0985H`, |              |              |                            |
   | :addr:`098AH`, |              |              |                            |
   | :addr:`09ABH`, |              |              |                            |
   | :addr:`09AFH`, |              |              |                            |
   | :addr:`09B2H`, |              |              |                            |
   | :addr:`09B9H`  |              |              |                            |
   +----------------+--------------+--------------+----------------------------+
   | :addr:`099CH`, | :code:`037H` | :code:`087H` | |PIO| Control              |
   | :addr:`09A0H`, |              |              |                            |
   | :addr:`09A4H`, |              |              |                            |
   | :addr:`09A7H`  |              |              |                            |
   +----------------+--------------+--------------+----------------------------+
   | :addr:`0530H`  | :code:`006H` | :code:`084H` | Tastatur Port              |
   +----------------+--------------+--------------+----------------------------+
   | :addr:`0532H`  | :code:`00AH` | :code:`083H` | Break Code (:kbd:`CTRL-C`) |
   +----------------+--------------+--------------+----------------------------+

.. rubric:: Verwendete Symbole:

Ein :console:`?` im Namen oder im Typ führen zum Ignorieren des jeweiligen Zeichens beim Suchen der Datei. Ein :console:`*` hat das Überlesen aller Zeichen ab der Position von :console:`*` zur Folge.

.. option:: name

   Ist ein |ASCII| String mit 0 |...| 8 Zeichen.

.. option:: typ

   Ist ein |ASCII| String mit 0 |...| 3 Zeichen.

.. option:: name.typ

   Ist ein |ASCII| String zusammengesetzt aus :option:`name` und :option:`typ`.

.. option:: o

   Ist eine Option.

.. option:: aaaa, bbbb, cccc, dddd

   Sind Parameter in hexadezimaler Angabe.

.. option:: <....>

   Diese Angaben können zur genauen Festlegung der Kommandos verwendet werden.

.. rubric:: Die Kommandos

Die Kommandos bestehen aus einem Zeichen, gefolgt von verschiedenen Optionen und Parametern.

.. rubric:: :command:`name`

Eine Datei vom Type :mimetype:`.COM` wird auf die ursprüngliche Adresse geladen und auf der beim Speichern vereinbarten Adresse sofort gestartet.

.. rubric:: :command:`G` <:option:`aaaa`>

**Go**: Sprung zur Adresse 0 oder :option:`aaaa`.

.. rubric:: :command:`I` .

**Inhaltsverzeichnis**: Auflisten der Dateien des Magnetbandes.

.. rubric:: :command:`L` :option:`name.typ` <:option:`aaaa`> /<:option:`bbbb` <:option:`cccc`>\ >

**Laden**: Laden der Datei :file:`name.typ` ab Adresse :option:`aaaa` von Blocknummer :option:`bbbb` bis Blocknummer :option:`cccc`.

.. rubric:: :command:`Q`

**Quit**: Verlassen des :program:`VTCP`

.. rubric:: :command:`S` :option:`name.typ` :option:`aaaa` :option:`bbbb` <:option:`cccc`> </<:option:`o`> :option:`dddd`>

**Speichern**: Speichern der Datei :file:`name.typ` von Adresse :option:`aaaa` bis Adresse :option:`bbbb` mit Startadresse 0 oder :option:`cccc` auf Band ab Blocknummer 0 oder :option:`dddd`.

Für :option:`o` ist zulässig:

.. option:: D

   :Distance: Mit vergrößertem Abstand zwischen zwei Blöcken.

.. option:: F

   :Following: Datei besteht aus mehreren Teilen; letzter Teil der Datei
               ohne "F"! (Datei wird beim Laden insgesamt eingelesen).

.. rubric:: :command:`V` .....

**Vergleichen**: Wie Laden, aber Vergleichen mit dem Speicherinhalt im Arbeitsspeicher des Rechners.

.. rubric:: :command:`X` .....

**Starten**: Wie Laden, aber mit Starten des Programmes auf der beim Speichern vereinbarten Adresse (:option:`cccc`).

.. rubric:: :command:`Z` :option:`aaaa`

Aufzeichnungsgeschwindigkeit wählen:

.. .. tabularcolumns:: lL
.. tabularcolumns:: p{0.2\linewidth}p{0.6\linewidth}
.. table:: |PC/M| |V-Tape| für |K1520| Systeme - Bitraten für Kommando :command:`Z`
   :name: kcsystems-mach-pcm-tabelle-az
   :widths: 25, 75
   :class: longtable
   :align: center
   :width: 80%

   +----------------+------------------------------------+
   | :option:`aaaa` |  Bitrate bei 2.5 MHz Taktfrequenz  |
   +================+====================================+
   | 1200           |  1200 Bit/s                        |
   +----------------+------------------------------------+
   | 2400           |  2400 Bit/s                        |
   +----------------+------------------------------------+
   | 3600           |  3600 Bit/s                        |
   +----------------+------------------------------------+
   | 4800           |  4800 Bit/s                        |
   +----------------+------------------------------------+

.. rubric:: :command:`D` :option:`name.typ`

**Diskette**: Die Datei :file:`name.typ` wird von Diskette im Laufwerk :file:`A` (Kaltstartlaufwerk) gelesen. Es werden alle Dateien, die :file:`name.typ` entsprechen kopiert. :samp:`D *.*` kopiert alle Dateien von Diskette auf Magnetband.

.. rubric:: :command:`J`

**Inhaltsverzeichnis Diskette**: Anzeigen des Inhaltsverzeichnisses der Diskette.

.. rubric:: :command:`T` :option:`name.typ`

**Tape**: Die Datei :file:`name.typ` wird auf dem Magnetband gesucht, eingelesen und auf Diskette im Laufwerk :file:`A` (Kaltstartlaufwerk) gespeichert.

.. index:: triple: PC/M; Software; FA 11/88-K1520VTCP (SW/VTCP)

.. list-table:: FA 11/88-K1520VTCP (SW/VTCP)
   :name: kcsystems-mach-pcm-fa1188k1520vtcp-sw
   :class: longtable
   :align: center
   :width: 80 %
   :header-rows: 1

   * - FA 11/88-K1520VTCP (SW/VTCP)

   * - :raw-latex:`\begin{minipage}[c][][c]{0.8\textwidth}`

       .. figure:: bild-b1.png
          :name: kcsystems-mach-pcm-bild-b1
          :figclass: align-center
          :align: center
          :width: 850 px
          :alt: HEX-Listing für das Kassettenmodul

          HEX-Listing für das Kassettenmodul

       :raw-latex:`\end{minipage}`

   * - .. code-block:: hexdump
          :caption: HEX-Listing für das Kassettenmodul
          :name: kcsystems-mach-pcm-listing-bild-b1

          0100  C3 3D 02 11 09 00 2A 01-00 19 CB B9 E9 FB C5 D5
          0110  E5 CD 03 01 E1 D1 C1 F3-C9 E3 4E 23 CD 0D 01 CB
          0120  79 28 F7 E3 C9 1A FE 7E-D0 FE 61 D8 CB AF C9 AF
          0130  21 40 0A 77 23 77 23 77-06 3C 1A FE 20 13 20 04
          0140  10 F8 18 04 1B CD 25 01-2B 2B D6 30 F8 FE 0A 38
          0150  08 D6 07 FE 0A F8 FE 10-F0 13 34 23 ED 6F 23 ED
          0160  6F 18 E2 CD 2F 01 23 44-4D 6E 03 0A 67 C9 7C CD
          0170  73 01 7D F5 1F 1F 1F 1F-CD 7C 01 F1 E6 0F C6 30
          0180  FE 3A 38 02 C6 07 4F 18-84 CD 19 01 56 54 43 BE
          0190  21 80 00 36 3E 06 40 23-36 20 10 FB 36 3F 11 80
          01A0  00 0E 0A FB CD 05 00 F3-11 82 00 CD E0 08 CD 25
          01B0  01 13 08 1A FE 20 28 09-1B 3E FF 32 9E 0A C3 50
          01C0  05 08 13 32 9E 0A FE 44-CA 24 03 FE 54 CA A5 06
          01D0  FE 53 CA 3C 04 FE 4C CA-62 07 FE 58 CA 50 05 FE
          01E0  56 CA 47 05 FE 5A CA BF-09 FE 51 CA 00 00 FE 4A
          01F0  CA 0B 06 FE 49 CA 02 0A-FE 20 28 8D FE 47 C2 0B
          0200  0A CD 63 01 E9 CD 19 01-20 20 20 42 4F 46 BA 2A
          0210  3E 0A CD 6E 01 CD 19 01-20 20 20 45 4F 46 BA 2A
          0220  3C 0A CD 6E 01 CD 19 01-20 20 20 53 4F 46 BA 2A
          0230  95 0A C3 6E 01 1A BE C0-23 13 10 F9 C9 C3 40 02
          0240  31 FF 0A AF 32 9F 0A 0E-0D CD 05 00 CD 19 01 0C
          0250  56 2D 54 61 70 65 20 4B-6F 70 69 65 72 70 72 6F
          0260  67 72 61 6D 6D 20 20 56-33 2E 33 30 0D 0A 2A 2A
          0270  2A 2A 2A 2A 2A 20 2B 2B-2B 20 41 4D 38 38 20 2B
          0280  2B 2B 20 2A 2A 2A 2A 2A-2A 2A 0D 0A 20 20 20 20
          0290  20 28 50 75 66 66 65 72-20 61 62 20 31 30 30 30
          02A0  48 29 0D 0A 8A CD 99 09-31 FF 0A FB CD 89 01 18
          02B0  F7 06 3C 1A 13 FE 2F C8-10 F9 37 C9 01 00 02 18
          02C0  03 01 00 04 3E E6 CD 02-05 0B 79 B0 20 F6 C9 0E
          02D0  19 CD 05 00 3C 21 45 0A-77 23 06 08 11 A3 0A CD
          02E0  25 01 77 13 23 10 F8 13-06 03 CD 25 01 77 13 23
          02F0  10 F8 36 00 21 65 0A 36-00 C9 CD 19 01 0D 0A 44
          0300  61 74 65 69 20 6E 69 63-68 74 20 67 65 66 75 6E
          0310  64 65 6E 21 0D 8A 18 90-21 6B 0A 11 A3 0A 01 0C
          0320  00 ED B0 C9 CD 57 05 CD-18 03 3E 00 32 3A 0A CD
          0330  CF 02 3A 3A 0A B7 20 13-3E 01 32 3A 0A 0E 11 11
          0340  45 0A CD 05 00 FE FF 28-B1 18 1D F5 0E 11 11 45
          0350  0A CD 05 00 F1 47 3C 32-3A 0A C5 0E 12 CD 05 00
          0360  C1 FE FF CA A8 02 10 F2-CD E2 03 3C 28 71 AF 32
          0370  51 0A 32 54 0A 32 65 0A-11 45 0A 0E 0F CD 05 00
          0380  21 00 00 22 77 0A 3E 46-32 9D 0A 21 00 01 22 7D
          0390  0A 11 00 10 D5 11 45 0A-0E 14 CD 05 00 B7 20 24
          03A0  21 80 00 01 80 00 D1 ED-B0 7A FE 8F 38 E6 ED 53
          03B0  81 0A 21 00 10 22 7F 0A-CD 74 04 2A 77 0A 23 22
          03C0  77 0A 18 C2 11 45 0A 0E-10 CD 05 00 D1 ED 53 81
          03D0  0A 21 00 10 22 7F 0A 3E-AA 32 9D 0A CD 74 04 C3
          03E0  2F 03 21 80 00 FE 00 28-15 21 A0 00 FE 01 28 0E
          03F0  21 C0 00 FE 02 28 07 21-E0 00 FE 03 20 3B CB 7E

   * - .. code-block:: hexdump
          :lineno-start: 49

          0400  20 37 11 45 0A 01 20 00-ED B0 06 08 21 46 0A 11
          0410  6B 0A 4E 79 E6 7F 12 CD-0D 01 13 23 10 F4 3E 2E
          0420  4F 12 13 CD 0D 01 06 03-4E 79 E6 7F 12 CD 0D 01
          0430  13 23 10 F4 CD E0 08 AF-C9 3E FF C9 3E AA 32 9D
          0440  0A AF 6F 67 22 77 0A CD-57 05 CD 63 01 22 7F 0A
          0450  CD 63 01 22 81 0A CD 63-01 22 7D 0A CD B1 02 38
          0460  13 1A FE 44 28 04 FE 46-20 04 32 9D 0A 13 CD 63
          0470  01 22 77 0A 2A 77 0A CD-6E 01 2A 7F 0A ED 5B 81
          0480  0A CD B8 09 CD C1 02 D5-EB B7 ED 52 7C B7 23 28
          0490  11 AF 32 7A 0A 32 79 0A-3A 9D 0A FE 44 CC BC 02
          04A0  18 0A 7D 32 7A 0A 3A 9D-0A 32 79 0A EB 22 7B 0A
          04B0  CD D1 04 D1 3A 79 0A FE-40 D2 E0 08 E5 2A 77 0A
          04C0  23 E5 D5 CD 3B 09 D1 E1-CD 6E 01 22 77 0A E1 18
          04D0  B6 11 6B 0A 0E 00 EB CD-3A 05 3E B4 CD 02 05 06
          04E0  14 CD F4 04 EB 0E 00 CD-3A 05 3E 6B CD 02 05 3A
          04F0  7A 0A 47 A6 79 86 4F 7E-CD 02 05 23 A6 10 F5 79
          0500  E3 E3 C5 4F 37 CB 11 DB-35 CB F7 30 02 E6 BF D3
          0510  35 3E 13 3D 20 FD A6 DB-35 EE 40 D3 35 CB 11 28
          0520  07 3E 11 3D 20 FD 18 DF-3E 09 3D 20 FD A6 C1 DB
          0530  06 FE 0A C0 CD E0 08 C3-A8 02 06 0A 3E E6 B7 CD
          0540  02 05 34 35 10 F6 C9 AF-32 9F 0A 06 FF C3 67 07
          0550  CD 62 07 2A 95 0A E9 21-6B 0A E5 06 0C 36 20 23
          0560  10 FB 06 09 E1 3A 9E 0A-3C 20 15 05 CD 25 01 77
          0570  23 13 10 F8 36 2E 23 36-43 23 36 4F 23 36 4D C9
          0580  CD 25 01 FE 2A 28 0C FE-2E 28 11 77 23 13 10 F0
          0590  C3 0B 0A 3E 3F 77 23 10-FC 3E 2E 13 21 73 0A 77
          05A0  06 04 13 23 CD 25 01 FE-2A 28 08 FE 20 C8 77 10
          05B0  F1 18 DD 05 3E 3F 77 23-10 FC 13 1A FE 20 20 FA
          05C0  C9 AF 32 A1 0A FD E5 06-1A 10 FE CD 83 09 FE E6
          05D0  28 09 FE 19 20 F1 3E FF-32 A1 0A C1 E3 E3 A6 A6
          05E0  CD 68 09 FE E6 20 DA 10-F3 B7 E3 E3 A6 A6 CD 68
          05F0  09 B9 C8 FE E6 28 F7 18-C8 21 A2 0A 3E 3F 06 0B
          0600  23 BE 28 03 10 FA C9 36-20 18 F9 21 3B 0A 36 04
          0610  11 45 0A 3E 3F 12 21 51-0A 36 00 0E 11 CD 05 00
          0620  FE FF 20 1C CD 19 01 44-69 73 6B 65 74 74 65 20
          0630  6C 65 65 72 21 0D 8A C9-11 45 0A 0E 12 CD 05 00
          0640  21 80 00 B7 28 1A 21 A0-00 FE 01 28 13 21 C0 00
          0650  FE 02 28 0C 21 E0 00 FE-03 28 05 FE FF CA E0 08
          0660  7E FE 3F 28 D3 CB 7F 20-CF E5 DD E1 DD 7E 0C E6
          0670  1F FE 01 28 03 B7 20 C0-23 06 08 4E 23 CD 0D 01
          0680  10 F9 06 03 0E 2E CD 0D-01 4E 23 CD 0D 01 10 F9
          0690  21 3B 0A 35 20 07 36 04-CD E0 08 18 9B CD 19 01
          06A0  20 49 A0 18 93 D5 0E 0D-CD 05 00 D1 AF 32 38 0A
          06B0  6F 67 DD 21 A0 0A DD 77-00 22 77 0A 2B 22 7F 0A
          06C0  3E 44 32 39 0A 21 00 10-22 99 0A CD 57 05 CD 99
          06D0  07 CD AA 09 CD DF 06 0E-10 11 45 0A C3 05 00 3A
          06E0  38 0A B7 20 23 3E FF 32-38 0A 21 83 0A 11 A3 0A
          06F0  01 0C 00 ED B0 CD CF 02-0E 13 11 45 0A CD 05 00

   * - .. code-block:: hexdump
          :lineno-start: 97

          0700  0E 16 11 45 0A CD 05 00-ED 5B 3C 0A 21 00 10 E5
          0710  B7 ED 52 30 1A 01 80 00-E1 D5 11 80 00 ED B0 E5
          0720  11 45 0A 0E 15 CD 05 00-E1 D1 B7 20 0F 18 E0 21
          0730  00 10 22 99 0A 3E FF 32-A2 0A E1 C9 CD 19 01 0D
          0740  0A 44 69 73 6B 65 74 74-65 20 76 6F 6C 6C 21 0D
          0750  8A C9 2A 93 0A ED 5B 92-0A 1D 16 00 19 2A 99 0A
          0760  19 C9 AF 47 32 9F 0A 67-6F 32 39 0A 22 77 0A 2B
          0770  22 7F 0A DD 21 A0 0A DD-70 00 CD 57 05 CD 63 01
          0780  22 99 0A CD B1 02 38 11-CD 63 01 22 77 0A CD 63
          0790  01 7C B5 28 04 23 22 7F-0A CD B1 09 3E FF 32 A2
          07A0  0A FD 21 B4 06 CD C1 05-01 00 14 21 83 0A FD E3
          07B0  FD E3 CD 68 09 77 81 4F-23 10 F3 B7 CD 68 09 B9
          07C0  28 05 CD 1F 09 18 DA 21-83 0A E5 06 0C 4E 23 CD
          07D0  0D 01 10 F9 CD 19 01 20-A0 2A 8F 0A CD 6E 01 D1
          07E0  21 6B 0A 06 0C 7E FE 2A-28 26 FE 3F 28 21 CD 25
          07F0  01 BE 28 1B CD 3B 09 18-A8 0E 3C 30 02 0E 3E CD
          0800  0D 01 2A 9B 0A CD 6E 01-0E 07 CD 0D 01 18 E5 23
          0810  13 3E 04 B8 20 03 21 74-0A 10 CA 2A 77 0A 22 9B
          0820  0A ED 5B 8F 0A B7 ED 52-20 CF 06 05 0E 20 CD 0D
          0830  01 10 F9 2A 7F 0A ED 52-CA E0 08 2A 93 0A D5 3A
          0840  A2 0A FE FF 20 1D 22 3E-0A AF 32 A2 0A ED 5B 99
          0850  0A BA 20 03 BB 28 0C EB-22 3E 0A B7 ED 52 EB ED
          0860  53 99 0A ED 5B 99 0A 19-D1 FD 21 6B 05 CD C1 05
          0870  0E 00 3A 92 0A 47 E3 E3-CD 68 09 DD CB 00 46 20
          0880  01 77 BE 20 64 23 81 4F-10 EE B7 CD 68 09 2B 22
          0890  3C 0A 2A 77 0A 22 9B 0A-B9 C2 C2 07 23 22 77 0A
          08A0  3A 39 0A B7 28 2F 7D E6-7F 20 2A CD AA 09 CD 19
          08B0  01 0D 0A 53 74 6F 70 20-54 61 70 65 21 87 CD DF
          08C0  06 CD B1 09 CD 19 01 0D-53 74 61 72 74 20 54 61
          08D0  70 65 21 07 8D 3A 91 0A-FE AA C2 F4 07 CD 05 02
          08E0  CD AA 09 CD 19 01 0D 8A-C9 F5 CD 19 01 20 20 20
          08F0  20 20 20 20 20 20 41 44-44 52 3A A0 CD 6E 01 CD
          0900  19 01 20 20 54 61 70 65-3A A0 F1 CD 73 01 CD 19
          0910  01 20 20 52 41 4D 3A A0-7E CD 73 01 C3 C2 07 CD
          0920  19 01 0D 45 52 52 4F 52-20 3E 20 50 72 75 65 66
          0930  73 75 6D 6D 65 20 20 20-20 20 87 0E 0D CD 0D 01
          0940  21 9F 0A 7E FE 55 C0 21-83 0A 11 A3 0A 01 0C 00
          0950  1A 13 ED A1 E0 28 F9 0E-0A CD 0D 01 01 0C 00 11
          0960  A3 0A 21 83 0A ED B0 C9-C5 06 08 0E 0D 0D 20 FD
          0970  18 05 0E 17 0D 20 FD CD-83 09 10 F6 4F 3A A1 0A
          0980  A9 C1 C9 F5 DB 35 E6 80-4F DB 35 E6 80 B9 28 F9
          0990  4F CD 2F 05 F1 CB 11 17-C9 3E 00 D3 37 3E CF D3
          09A0  37 3E 8F D3 37 3E 07 D3-37 C9 DB 35 E6 CF D3 35
          09B0  C9 DB 35 F6 20 F3 18 F6-DB 35 F6 30 F3 18 EF CD
          09C0  63 01 7C 0E 00 FE 12 28-0F 0C FE 24 28 0A 0C FE
          09D0  36 28 05 0C FE 48 20 33-21 18 0A 06 00 79 87 87
          09E0  87 4F 09 7E 23 32 C8 05-7E 23 32 6C 09 7E 23 32
          09F0  73 09 7E 23 32 12 05 7E-23 32 22 05 7E 23 32 29

   * - .. code-block:: hexdump
          :lineno-start: 145

          0A00  05 C9 21 9F 0A 36 55 E5-C3 4B 05 CD 19 01 45 52
          0A10  52 4F 52 0D 8A C3 A8 02-50 50 5A 3F 3C 34 00 00
          0A20  28 1E 28 1E 1C 14 00 00-1A 0D 17 13 11 09 00 00
          0A30  14 04 0E 0E 0B 04 00 00-00 00 00 00 00 00 00 00
          0A40  00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00
          0A50  00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00
          0A60  00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00
          0A70  00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00
          0A80  00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00
          0A90  00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00
          0AA0  00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00
          0AB0  00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00
          0AC0  00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00
          0AD0  00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00
          0AE0  00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00
          0AF0  00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00

.. Local variables:
   coding: utf-8
   mode: text
   mode: rst
   End:
   vim: fileencoding=utf-8 filetype=rst :
