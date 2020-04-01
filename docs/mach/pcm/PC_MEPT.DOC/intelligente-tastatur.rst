.. index:: pair: PC/M; Intelligente Tastatur

Intelligente Tastatur am PC/M
#############################

Bearbeitungsstand: 17.09.1988 

Das File :file:`PC/MEPT.DOC` enthält einige Informationen für die Nutzung des |EPR2TUK| als Tastaturrechner für den |PC/M| Computer. Die Tastatur ist Hardwareseitig voll kompatibel zur im |Funkamateur| vorgestellten Variante. Die Belegung der Tasten weicht jedoch zum Teil ab. Wesentlicher Unterschied ist die schreibmaschinenkompatible Ausgabe von Groß- und Kleinschreibung (Großschreibung bei gedrückter :kbd:`SHIFT` Taste), die im Betriebssystem nicht mehr korrigiert werden muss. Dies sollte bei der Anpassen bzw. Übersetzen des Files :file:`PCM.MAC` (|PC/M| |BIOS| **Version 2.XX**) und der nachfolgenden Version mit dem Definitionsfile :file:`PCMDEF.MAC` (|PC/M| |BIOS| **Version 3.XX**) beachtet werden. Die Tastatur verfügt über eine eigenständige Autorepeatfunktion.

Die LED Steuerung wurden in der vorliegenden Version nicht übernommen.

.. index:: triple: PC/M; Intelligente Tastatur; Anschlüsse

Anschlüsse zur Zentralen Platine des PC/M
*****************************************

.. tabularcolumns:: p{0.175\linewidth}p{0.075\linewidth}|p{0.175\linewidth}p{0.075\linewidth}
.. table:: |PC/M| |EPR2TUK| Tastatur - Anschlüsse zur Zentralen Platine
   :name: kcsystems-mach-pcm-ept-tabelle-1
   :widths: 35, 15, 35, 15
   :class: longtable
   :align: center
   :width: 50%

   +-----------------+------------+----------------+--------------+
   |                 |            |    Zentrale    |              |
   |    |EPR2TUK|    | :comp:`X2` |    Platine     | :comp:`X1`   |
   +=================+============+================+==============+
   | :signal:`OT0`   | :pin:`A13` | :signal:`TD0`  | :pin:`B9`    |
   +-----------------+------------+----------------+--------------+
   | :signal:`OT1`   | :pin:`A12` | :signal:`TD1`  | :pin:`B8`    |
   +-----------------+------------+----------------+--------------+
   | :signal:`OT2`   | :pin:`C11` | :signal:`TD2`  | :pin:`B7`    |
   +-----------------+------------+----------------+--------------+
   | :signal:`OT3`   | :pin:`C12` | :signal:`TD3`  | :pin:`B6`    |
   +-----------------+------------+----------------+--------------+
   | :signal:`OT4`   | :pin:`C14` | :signal:`TD4`  | :pin:`B5`    |
   +-----------------+------------+----------------+--------------+
   | :signal:`OT5`   | :pin:`A11` | :signal:`TD5`  | :pin:`B4`    |
   +-----------------+------------+----------------+--------------+
   | :signal:`OT6`   | :pin:`C10` | :signal:`TD6`  | :pin:`B3`    |
   +-----------------+------------+----------------+--------------+
   | :signal:`OT7`   | :pin:`A10` | :signal:`TAST` | :pin:`B2`    |
   +-----------------+------------+----------------+--------------+
   | :signal:`BAT3`  | :pin:`A3`  | :signal:`5P`   | :pin:`ABC1`  |
   +-----------------+------------+----------------+--------------+
   | :signal:`GND`   | :pin:`A4`  | :signal:`GND`  | :pin:`ABC13` |
   +-----------------+------------+----------------+--------------+

.. index:: triple: PC/M; Intelligente Tastatur; Commodore Tastatur

Tastaturbelegung für Commodore Tastatur
***************************************

Tastaturbelegung und |EPR2TUK| - Anschlüsse bei Commodore Tastatur (CBM-II Modell B etc.):

.. tabularcolumns:: \X{12}{100}\X{12}{100}\X{12}{100}|cccccc
.. table:: |PC/M| |EPR2TUK| Tastatur - Anschlüsse bei Commodore Tastatur
   :name: kcsystems-mach-pcm-ept-tabelle-2
   :widths: 12, 11, 11, 11, 11, 11, 11, 11, 11
   :class: longtable
   :align: center
   :width: 80%

   +--------------------------------+--------------+---------------+------------+--------------+-----------+-------------+
   | Farbe     [#f1]_               | **dkbl**     | **dkgn**      | **ge**     | **or**       | **rt**    | **br**      |
   +-----------+--------------------+--------------+---------------+------------+--------------+-----------+-------------+
   |           | |EPR2TUK|          | :pin:`C3`    | :pin:`C6`     | :pin:`C7`  | :pin:`C8`    | :pin:`A15`| :pin:`C10`  |
   +-----------+------------+-------+--------------+---------------+------------+--------------+-----------+-------------+
   |                        | |PIO| | Ab0          | Ab1           | Ab2        | Ab3          | Ab4       | Ab5         |
   +===========+============+=======+==============+===============+============+==============+===========+=============+
   | **sw-ws** | :pin:`C24` | Aa0   | :kbd:`?`     | :kbd:`:`      | :kbd:`L`   | :kbd:`O`     | :kbd:`(`  | :kbd:`F9`   |
   |           +------------+-------+--------------+---------------+------------+--------------+-----------+-------------+
   |           |            |       | :kbd:`/`     | :kbd:`;`      |            |              | :kbd:`9`  |             |
   +-----------+------------+-------+--------------+---------------+------------+--------------+-----------+-------------+
   | **gr-ws** | :pin:`C23` | Aa1   | :kbd:`"`     | :kbd:`[`      | :kbd:`P`   | :kbd:`\_`    | :kbd:`)`  | :kbd:`F10`  |
   |           +------------+-------+--------------+---------------+------------+--------------+-----------+-------------+
   |           |            |       | :kbd:`,`     |               |            |              | :kbd:`0`  |             |
   +-----------+------------+-------+--------------+---------------+------------+--------------+-----------+-------------+
   | **vi-ws** | :pin:`C22` | Aa2   | :kbd:`π`     | :kbd:`RETURN` | :kbd:`]`   |              | :kbd:`\+` | :kbd:`LF`   |
   |           +------------+-------+--------------+---------------+------------+--------------+-----------+-------------+
   |           |            |       |              |               |            | :kbd:`←`     |           |             |
   +-----------+------------+-------+--------------+---------------+------------+--------------+-----------+-------------+
   | **bl-ws** | :pin:`C21` | Aa3   |              | :kbd:`C=`     | :kbd:`INS` | :kbd:`→`     | :kbd:`←`  | :kbd:`LB`   |
   |           +------------+-------+--------------+---------------+------------+--------------+-----------+-------------+
   |           |            |       |              |               | :kbd:`DEL` |              |           |             |
   +-----------+------------+-------+--------------+---------------+------------+--------------+-----------+-------------+
   | **gn-ws** | :pin:`C19` | Aa4   | :kbd:`0`     | :kbd:`1`      | :kbd:`4`   | :kbd:`7`     | :kbd:`?`  | :kbd:`CLR`  |
   |           +------------+-------+--------------+---------------+------------+--------------+-----------+-------------+
   |           |            |       |              |               |            |              |           | :kbd:`HOME` |
   +-----------+------------+-------+--------------+---------------+------------+--------------+-----------+-------------+
   | **ge-ws** | :pin:`C18` | Aa5   | :kbd:`.`     | :kbd:`2`      | :kbd:`5`   | :kbd:`8`     | :kbd:`CE` | :kbd:`OFF`  |
   |           +------------+-------+--------------+---------------+------------+--------------+-----------+-------------+
   |           |            |       |              |               |            |              |           | :kbd:`RSV`  |
   +-----------+------------+-------+--------------+---------------+------------+--------------+-----------+-------------+
   | **or-ws** | :pin:`C17` | Aa6   | :kbd:`00`    | :kbd:`3`      | :kbd:`6`   | :kbd:`9`     | :kbd:`\*` | :kbd:`NORM` |
   |           +------------+-------+--------------+---------------+------------+--------------+-----------+-------------+
   |           |            |       |              |               |            |              |           | :kbd:`GRAPH`|
   +-----------+------------+-------+--------------+---------------+------------+--------------+-----------+-------------+
   | **rs-ws** | :pin:`C16` | Aa7   |              | :kbd:`ENTER`  | :kbd:`\+`  | :kbd:`\-`    | :kbd:`/`  | :kbd:`RUN`  |
   |           +------------+-------+--------------+---------------+------------+--------------+-----------+-------------+
   |           |            |       |              |               |            |              |           | :kbd:`STOP` |
   +-----------+------------+-------+--------------+---------------+------------+--------------+-----------+-------------+
   | **br-ws** | :pin:`A23` | Ba0   | :kbd:`CTRL`  | :kbd:`SHFT`   |            | :kbd:`TAB`   | :kbd:`ESC`| :kbd:`F1`   |
   |           +------------+-------+--------------+---------------+------------+--------------+-----------+-------------+
   |           |            |       |              |               |            |              |           |             |
   +-----------+------------+-------+--------------+---------------+------------+--------------+-----------+-------------+
   | **hlgn**  | :pin:`A22` | Ba1   |              | :kbd:`Z`      | :kbd:`A`   | :kbd:`Q`     | :kbd:`!`  | :kbd:`F2`   |
   |           +------------+-------+--------------+---------------+------------+--------------+-----------+-------------+
   |           |            |       |              |               |            |              | :kbd:`1`  |             |
   +-----------+------------+-------+--------------+---------------+------------+--------------+-----------+-------------+
   | **hlbl**  | :pin:`A21` | Ba2   | :kbd:`C`     | :kbd:`X`      | :kbd:`S`   | :kbd:`W`     | :kbd:`@`  | :kbd:`F3`   |
   |           +------------+-------+--------------+---------------+------------+--------------+-----------+-------------+
   |           |            |       |              |               |            |              | :kbd:`2`  |             |
   +-----------+------------+-------+--------------+---------------+------------+--------------+-----------+-------------+
   | **rs**    | :pin:`A20` | Ba3   | :kbd:`V`     | :kbd:`F`      | :kbd:`D`   | :kbd:`E`     | :kbd:`#`  | :kbd:`F4`   |
   |           +------------+-------+--------------+---------------+------------+--------------+-----------+-------------+
   |           |            |       |              |               |            |              | :kbd:`3`  |             |
   +-----------+------------+-------+--------------+---------------+------------+--------------+-----------+-------------+
   | **sw**    | :pin:`A19` | Ba4   | :kbd:`B`     | :kbd:`G`      | :kbd:`T`   | :kbd:`R`     | :kbd:`$`  | :kbd:`F5`   |
   |           +------------+-------+--------------+---------------+------------+--------------+-----------+-------------+
   |           |            |       |              |               |            |              | :kbd:`4`  |             |
   +-----------+------------+-------+--------------+---------------+------------+--------------+-----------+-------------+
   | **ws**    | :pin:`A18` | Ba5   | :kbd:`N`     | :kbd:`H`      | :kbd:`Y`   |              | :kbd:`%`  | :kbd:`F6`   |
   |           +------------+-------+--------------+---------------+------------+--------------+-----------+-------------+
   |           |            |       |              |               |            | :kbd:`6`     | :kbd:`5`  |             |
   +-----------+------------+-------+--------------+---------------+------------+--------------+-----------+-------------+
   | **gr**    | :pin:`A17` | Ba6   | :kbd:`Space` | :kbd:`M`      | :kbd:`J`   | :kbd:`U`     | :kbd:`&`  | :kbd:`F7`   |
   |           +------------+-------+--------------+---------------+------------+--------------+-----------+-------------+
   |           |            |       |              |               |            |              | :kbd:`7`  |             |
   +-----------+------------+-------+--------------+---------------+------------+--------------+-----------+-------------+
   | **vi**    | :pin:`A16` | Ba7   | :kbd:`>`     | :kbd:`<`      | :kbd:`K`   | :kbd:`I`     | :kbd:`\*` | :kbd:`F8`   |
   |           +------------+-------+--------------+---------------+------------+--------------+-----------+-------------+
   |           |            |       | :kbd:`.`     | :kbd:`,`      |            |              | :kbd:`8`  |             |
   +-----------+------------+-------+--------------+---------------+------------+--------------+-----------+-------------+

.. rubric:: |ASCII| Codes der Commodore Tastatur (Angaben hexadezimal!)

* :ref:`kcsystems-mach-pcm-epr3tuk-cbm2-kbd-ascii-1`
* :ref:`kcsystems-mach-pcm-epr3tuk-cbm2-kbd-ascii-2`

.. _kcsystems-mach-pcm-epr3tuk-cbm2-kbd-ascii-1:
.. tikz:: PC/M EPR2TUK Tastatur - Commodore Tastatur Teil 1
   :include: commodore-tastatur-belegung-1.tikz
   :libs: matrix

.. _kcsystems-mach-pcm-epr3tuk-cbm2-kbd-ascii-2:
.. tikz:: PC/M EPR2TUK Tastatur - Commodore Tastatur Teil 2
   :include: commodore-tastatur-belegung-2.tikz
   :libs: matrix


.. index:: triple: PC/M; Intelligente Tastatur; Hinweise zur Bestückung

Hinweise zur Bestückung und Tastatur 
************************************
 
:comp:`D11` (|U2716|), :comp:`D7` (|U857|, |UB 857 D|), :comp:`D16` (V40098), :comp:`D15` (74154), :comp:`D5` (DL123) sowie :comp:`V2`, :comp:`V3`, :comp:`V4`, :comp:`V5`, :comp:`C5`, :comp:`R7`, :comp:`R8`, :comp:`R13`, :comp:`R15` |...| :comp:`R23` und :comp:`Q` sind nicht zu bestücken. 

Für :comp:`Q` wird ein Kondensator mit 1 |nF| eingesetzt. :comp:`V5` wird durch eine Brücke zwischen :pin:`C` und :pin:`E` ersetzt. :comp:`V3` wird gebrückt. :comp:`D5` wird durch eine Brücke von Pin :pin:`11` zu Pin :pin:`5` ersetzt. :comp:`D8` muss an :signal:`IEI` Pin :pin:`24` zusätzlich mit einem Pull Up Widerstand von ca. 3 |kO| versehen werden.

Die Datenleitungen für |PIO| :comp:`D9` Kanal :signal:`A0` |...| :signal:`A5` werden mit ca. 5 |kO| nach Masse geschaltet.

Bitte die Brücke für |Vpp| am |EPROM| zu :signal:`5P` nicht vergessen und Pin :pin:`6` des DS8205 (:comp:`IS12`) auf :signal:`5P` legen.

Weiterhin sollte die :signal:`RESET` Leitung für die Tastatur und die zentrale Platine parallelgeschaltet werden.

Die |EPROM| Version **TAST8282.002** wird bei Einsatz eines DS8282 als :comp:`D17` und die Version **TAST8283.002** bei Einsatz eines DS8283 verwendet. Beide sind Versionen die auf die Arbeit mit WordStar (:program:`TP`) zugeschnitten wurden. 

.. ...........................................................................

.. _kcsystems-mach-pcm-ept-epr2tuk:

.. rubric:: |EPR2TUK| Unterlagen

.. .. tabularcolumns:: cl
.. tabularcolumns:: p{0.12\linewidth}p{0.68\linewidth}
.. table:: |EPR2TUK| - Verzeichnis der Bilder
   :widths: 15, 85
   :class: longtable
   :align: center
   :width: 80%

   +------------------+-------------------------------------------------------+
   | Bild             | Titel                                                 |
   +==================+=======================================================+
   | |PC_MEPT_SCH_N|  | |PC_MEPT_SCH_T|                                       |
   +------------------+-------------------------------------------------------+
   | |PC_MEPT_ZUS_N|  | |PC_MEPT_ZUS_T|                                       |
   +------------------+-------------------------------------------------------+
   | |PC_MEPT_SOLD_N| | |PC_MEPT_SOLD_T|                                      |
   +------------------+-------------------------------------------------------+
   | |PC_MEPT_COMP_N| | |PC_MEPT_COMP_T|                                      |
   +------------------+-------------------------------------------------------+

.. index:: triple: PC/M; Stromlaufplan; EPT/EPR2TUK (SP)

.. list-table:: EPT/EPR2TUK (SP)
   :name: kcsystems-mach-pcm-ept-epr2tuk-sp
   :class: longtable
   :align: center
   :width: 80 %
   :header-rows: 1

   * - EPT/EPR2TUK (SP)

   * - :raw-latex:`\begin{turn}{90}`
       :raw-latex:`\begin{minipage}[c][][c]{0.9\textheight}`

       .. figure:: epr2tuk-sch.png
          :name: kcsystems-mach-pcm-ept-epr2tuk-sch
          :figclass: align-center
          :align: center
          :width: 850 px
          :alt: |EPR2TUK| Stromlaufplan

          |EPR2TUK| Stromlaufplan

       :raw-latex:`\end{minipage}`
       :raw-latex:`\end{turn}`

:raw-latex:`\begin{turn}{90}`
:raw-latex:`\begin{minipage}[c][\textwidth][c]{\textheight}`

.. index:: triple: PC/M; PCB Layouts; EPT/EPR2TUK (BP)
.. index:: triple: PC/M; PCB Layouts; EPT/EPR2TUK (LS)
.. index:: triple: PC/M; PCB Layouts; EPT/EPR2TUK (BS)

.. list-table:: EPT/EPR2TUK (BP) (LS) (BS)
   :name: kcsystems-mach-pcm-ept-epr2tuk-lsbsbp
   :class: longtable
   :align: center
   :width: 80 %
   :header-rows: 1

   * - EPT/EPR2TUK (BS)
     - EPT/EPR2TUK (LS)
     - EPT/EPR2TUK (BP)

   * - :raw-latex:`\begin{turn}{270}`
       :raw-latex:`\begin{minipage}[c][][c]{0.6\textwidth}`

       .. figure:: epr2tuk-comp.png
          :name: kcsystems-mach-pcm-ept-epr2tuk-comp
          :figclass: align-center
          :align: center
          :width: 420 px
          :alt: |EPR2TUK| Bestückungsseite

          |EPR2TUK| Bestückungsseite

       :raw-latex:`\end{minipage}`
       :raw-latex:`\end{turn}`

     - :raw-latex:`\begin{turn}{270}`
       :raw-latex:`\begin{minipage}[c][][c]{0.6\textwidth}`

       .. figure:: epr2tuk-sold.png
          :name: kcsystems-mach-pcm-ept-epr2tuk-sold
          :figclass: align-center
          :align: center
          :width: 420 px
          :alt: |EPR2TUK| Leiterseite

          |EPR2TUK| Leiterseite

       :raw-latex:`\end{minipage}`
       :raw-latex:`\end{turn}`

     - :raw-latex:`\begin{turn}{270}`
       :raw-latex:`\begin{minipage}[c][][c]{0.6\textwidth}`

       .. figure:: epr2tuk-zus.png
          :name: kcsystems-mach-pcm-ept-epr2tuk-zus
          :figclass: align-center
          :align: center
          :width: 420 px
          :alt: |EPR2TUK| Bestückungsplan

          |EPR2TUK| Bestückungsplan

       :raw-latex:`\end{minipage}`
       :raw-latex:`\end{turn}`

:raw-latex:`\end{minipage}`
:raw-latex:`\end{turn}`
:raw-latex:`\FloatBarrier`

.. ...........................................................................

.. rubric:: Footnotes

.. [#f1] :wikide:`Farb-Kurzzeichen` nach DIN 47002, IEC 60757 und IEC 62

   **sw**:	schwarz		**br**: braun		**rt**: rot
   **or**:	orange		**ge**: gelb		**gn**: grün
   **bl**:	blau		**vi**: violett		**gr**: grau
   **ws**:	weiß		**rs**: rosa		**tk**: türkis
   **gnge**:	grün-gelb
   **dk**:	dunkel
   **hl**:	hell

.. spelling::

   Aa
   Ba

.. Local variables:
   coding: utf-8
   mode: text
   mode: rst
   End:
   vim: fileencoding=utf-8 filetype=rst :
