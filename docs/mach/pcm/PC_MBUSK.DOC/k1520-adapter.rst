.. index:: pair: PC/M; K1520 Adapter

.. _kcsystems-mach-pcm-fa108901:

K1520 Adapter für den PC/M Computer
###################################

Die Vielzahl der existierenden |K1520| Baugruppen war der Ausgangspunkt für die Entwicklung einer Buskoppelbaugruppe vom |PC/M| zum |K1520| Bus. Damit werden für den |PC/M| Computer zahlreiche neue Anwendungsfälle erschlossen. Dies betrifft besonders die in verschiedenen Zeitschriften veröffentlichten Grafikzusätze und Baugruppen zur analogen sowie digitalen Ein- und Ausgabe.

.. index:: triple: PC/M; Stromlaufplan; FA 10/89-01 (BG)

.. list-table:: FA 10/89-01 (BG)
   :name: kcsystems-mach-pcm-fa108901-bg
   :class: longtable
   :align: center
   :width: 80 %
   :header-rows: 1

   * - FA 10/89-01 (BG)

   * - :raw-latex:`\begin{minipage}[c][][c]{0.65\textwidth}`

       .. figure:: bild-01.png
          :name: kcsystems-mach-pcm-busk-bild-01
          :figclass: align-center
          :align: center
          :width: 480 px
          :alt: Anordnung der Leiterplatte am |PC/M| Computer

          Anordnung der Leiterplatte am |PC/M| Computer

       :raw-latex:`\end{minipage}`

.. index:: triple: PC/M; K1520 Adapter; Aufgaben

Aufgaben des Busadapters
************************

Der |K1520| Busadapter dient der Umsetzung der Signale des |PC/M| Bus in die Steckverbinderbelegung des |K1520| Systembus. Dabei werden die Datenleitungen bidirektional getrieben (:comp:`D1`, DS8286). Die Umschaltung der Datenrichtung in Richtung |PC/M| Systembus erfolgt in folgenden Fällen:

1. Interruptzyklus:

   - :signal:`IEO` des |PC/M| hat :level:`High` Pegel
   - :signal:`M1` und :signal:`IORQ` sind aktiv

2. Lesen von peripheren I/O Bausteinen:

   - beim Lesen von peripheren I/O Bausteinen, die außerhalb des I/O Port Adressbereiches des |PC/M| liegen (:port:`00H` |...| :port:`7FH` und :port:`0A0H` |...| :port:`0FFH`)
   - :signal:`RD` und :signal:`IORQ` sind aktiv

3. Lesen von externen Speicherbaugruppen:

   - dabei muss eines der 5 :signal:`MSEL` Signale aktiv sein sowie aktiver Pegel von :signal:`MREQ` und :signal:`RD` vorliegen.

:comp:`D4.2` negiert den Ausgangspegel von :signal:`IEO` des |PC/M| Computers und steuert den IEI Eingang der |K1520| Peripherie. Die Interruptquellen des |PC/M| haben gegenüber der Peripherie die höchste Priorität.

.. index:: triple: PC/M; K1520 Adapter; Aufbau

Aufbau des Busadapters
**********************

Einen Vorschlag zur Anordnung des Busadapters zeigt |PC_MBUSK_B01_N|. Je nach mechanischem Aufbau des |PC/M| kann z.B. :comp:`X2` durch eine Stegleitung ersetzt und unmittelbar an einen |K1520| Steckeinheiteneinsatz angelötet bzw. gewickelt werden. Zu beachten ist, dass Zuleitungen über 200 mm vermieden werden. Längere Leitungen führen zu höherer Störanfälligkeit des Systems.

.. index:: triple: PC/M; K1520 Adapter; Inbetriebnahme

Inbetriebnahme
**************

Die Inbetriebnahme erfolgt nach dem kompletten Aufbau der Leiterplatte. |PC_MBUSK_B02_N| gibt den Stromlaufplan wieder. Es ist zu empfehlen die Stromeinspeisung für die |K1520| Peripherie unmittelbar am |K1520| Bus oder am Busadapter vorzunehmen. Dadurch werden Spannungsabfälle in der Verdrahtung, die zu unerwünschten Störungen führen könnten, vermieden. Werden die im Bestückungsplan (Bild 3) eingezeichneten Einlötkontakte vorgesehen ergibt sich eine einfache Möglichkeit der Testung des Systems auch im Betrieb. Die Test der Funktionen der Schaltung sollte statisch erfolgen. Dazu werden mit mit Widerständen von etwa 1 |kO| nach :signal:`5P` und von etwa 330 |Omega| nach Masse die jeweiligen Pegel an die Eingänge gelegt (siehe Punkt 1-3 oben). An Pin :pin:`11` des DS8286 (:comp:`D1`) kann mittels Multimeter, Logiktester o.ä. das Resultat beobachtet werden. Dieser Test ist unabhängig von speziellen Prüfprogrammen anwendbar. In Bild 4 und Bild 5 sind Leiterseite und Bestückungsseite der Leiterplatte abgebildet.

.. index:: triple: PC/M; Stromlaufplan; FA 10/89-01 (SP)

.. list-table:: FA 10/89-01 (SP)
   :name: kcsystems-mach-pcm-fa108901-sp
   :class: longtable
   :align: center
   :width: 80 %
   :header-rows: 1

   * - FA 10/89-01 (SP)

   * - :raw-latex:`\begin{minipage}[c][][c]{0.7\textwidth}`

       .. figure:: bild-02.png
          :name: kcsystems-mach-pcm-busk-bild-02
          :figclass: align-center
          :align: center
          :width: 560 px
          :alt: Stromlaufplan des |K1520| Busadapters

          Stromlaufplan des |K1520| Busadapters

       :raw-latex:`\end{minipage}`

.. index:: triple: PC/M; PCB Layouts; FA 10/89-01 (BP)

.. list-table:: FA 10/89-01 (BP)
   :name: kcsystems-mach-pcm-fa108901-bp
   :class: longtable
   :align: center
   :width: 80 %
   :header-rows: 1

   * - FA 10/89-01 (BP)

   * - .. figure:: bild-05.png
          :name: kcsystems-mach-pcm-busk-bild-05
          :figclass: align-center
          :align: center
          :width: 850 px
          :alt: Bestückungsplan der Adapterleiterplatte

          Bestückungsplan der Adapterleiterplatte

.. index:: triple: PC/M; PCB Layouts; FA 10/89-01 (LS)

.. list-table:: FA 10/89-01 (LS)
   :name: kcsystems-mach-pcm-fa108901-ls
   :class: longtable
   :align: center
   :width: 80 %
   :header-rows: 1

   * - FA 10/89-01 (LS)

   * - .. figure:: bild-03.png
          :name: kcsystems-mach-pcm-busk-bild-03
          :figclass: align-center
          :align: center
          :width: 850 px
          :alt: Layout der Leiterseite der Adapterleiterplatte

          Layout der Leiterseite der Adapterleiterplatte

.. index:: triple: PC/M; PCB Layouts; FA 10/89-01 (BS)

.. list-table:: FA 10/89-01 (BS)
   :name: kcsystems-mach-pcm-fa108901-bs
   :class: longtable
   :align: center
   :width: 80 %
   :header-rows: 1

   * - FA 10/89-01 (BS)

   * - .. figure:: bild-04.png
          :name: kcsystems-mach-pcm-busk-bild-04
          :figclass: align-center
          :align: center
          :width: 850 px
          :alt: Layout der Bestückungsseite der Adapterleiterplatte

          Layout der Bestückungsseite der Adapterleiterplatte

.. index:: triple: PC/M; K1520 Adapter; Abbildungsverzeichnis

Verzeichnis der Abbildungen
***************************

.. .. tabularcolumns:: cl
.. tabularcolumns:: p{0.12\linewidth}p{0.68\linewidth}
.. table:: |PC/M| |K1520| Bus Adapter - Verzeichnis der Bilder
   :widths: 15, 85
   :class: longtable
   :align: center
   :width: 80%

   +------------------+-------------------------------------------------------+
   | Bild             | Titel                                                 |
   +==================+=======================================================+
   | |PC_MBUSK_B01_N| | |PC_MBUSK_B01_T|                                      |
   +------------------+-------------------------------------------------------+
   | |PC_MBUSK_B02_N| | |PC_MBUSK_B02_T|                                      |
   +------------------+-------------------------------------------------------+
   | |PC_MBUSK_B03_N| | |PC_MBUSK_B03_T|                                      |
   +------------------+-------------------------------------------------------+
   | |PC_MBUSK_B04_N| | |PC_MBUSK_B04_T|                                      |
   +------------------+-------------------------------------------------------+
   | |PC_MBUSK_B05_N| | |PC_MBUSK_B05_T|                                      |
   +------------------+-------------------------------------------------------+

.. Local variables:
   coding: utf-8
   mode: text
   mode: rst
   End:
   vim: fileencoding=utf-8 filetype=rst :
