.. highlight:: none
   :linenothreshold: 1

.. index:: pair: PC/M; K7659 Tastaturanschluss

.. _kcsystems-mach-pcm-fa059001:

K7659 - Tastaturanschluss für den PC/M Computer
###############################################

Arbeitsstand: 09.01.1989

.. index:: triple: PC/M; K7659 Tastaturanschluss; Einleitung

Einleitung
**********

Die Tastaturschnittstelle des |PC/M| Computers gestattet den Anschluss unterschiedlicher Tastaturtypen. Es ist lediglich ein 7 Bit Datenwort mit dem Code der gedrückten Taste im |ASCII| Format und eine Information über den Status der Tastatur erforderlich. Dieser Status zeigt mit :Level:`High` Pegel an, dass eine Taste betätigt wird. Neben vielen anderen Möglichkeiten der Realisierung eines Tastaturinterfaces soll eine relativ universelle Schaltung vorgestellt werden, die ohne Mikrorechner auskommt und sich durch Austausch eines Zeichengenerator |EPROM|'s leicht an die individuellen Bedürfnisse anpassen lässt.

.. index:: triple: PC/M; K7659 Tastaturanschluss; Schaltung

Die Schaltung der Tastaturansteuerung
*************************************

Die Schaltung der Ansteuerung für |K7659| Tastaturen (|PC_M7659_B02_N|) arbeitet auf Grundlage der Erkennung einer gedrückten Taste der Tastaturmatrix (|PC_M7659_B01_N|) :cite:`pcm:website:elektroschaltgeraete1985bedienungsanleitungk7659`.

.. index:: triple: PC/M; Stromlaufplan; FA 5/90-01 (TM)

.. list-table:: FA 5/90-01 (TM)
   :name: kcsystems-mach-pcm-fa059001-tm
   :class: longtable
   :align: center
   :width: 80 %
   :header-rows: 1

   * - FA 5/90-01 (TM)

   * - .. figure:: bild-01.png
          :name: kcsystems-mach-pcm-7659-bild-01
          :figclass: align-center
          :align: center
          :width: 640 px
          :alt: Matrix der |K7659| Tastatur und deren Belegung

          Matrix der |K7659| Tastatur und deren Belegung

.. index:: triple: PC/M; Stromlaufplan; FA 5/90-01 (SP)

.. list-table:: FA 5/90-01 (SP)
   :name: kcsystems-mach-pcm-fa059001-sp
   :class: longtable
   :align: center
   :width: 80 %
   :header-rows: 1

   * - FA 5/90-01 (SP)

   * - .. figure:: bild-02.png
          :name: kcsystems-mach-pcm-7659-bild-02
          :figclass: align-center
          :align: center
          :width: 850 px
          :alt: Stromlaufplan der Tastaturansteuerung

          Stromlaufplan der Tastaturansteuerung

Über die zugehörigen Treiber (:comp:`VT1` |...| :comp:`VT7`; :comp:`D12`, :comp:`D16`) werden je nach gedrückter Taste die Adressen für den Zeichengenerator |EPROM| (:comp:`D8`) erzeugt, der dann entsprechend seiner Programmierung den Tastencode an den Datenausgängen bereitstellt. Die Ausgänge :signal:`D0` bis :signal:`D6` werden unmittelbar mit dem Tastatursteckverbinder der zentralen Platine verbunden (:comp:`X1` auf der zentralen Platine). Mittels :comp:`D2`, :comp:`D3`, :comp:`D5`, :comp:`D6` und :comp:`D14` wird bei einer gedrückten Taste über :comp:`VT2` und :comp:`D10` das Statussignal :signal:`TAST` erzeugt und ebenfalls an den Steckverbinder geführt. :comp:`R1` dient dabei der Einstellung einer sicheren Triggerung des Eingangssignals an :comp:`D10`.

Die IS :comp:`D15` dekodiert unmittelbar aus der Matrix die Tasten :signal:`NMI` und :signal:`RESET`, die über :comp:`VT9` und :comp:`VT10` mit offenem Kollektor ebenfalls an den Steckverbinder :comp:`X2` der Tastatursteuerung geführt werden.

Ist keine der Funktionstasten (:kbd:`SHIFT` oder :kbd:`CTRL` usw.) gedrückt, wird im |EPROM| der Adressbereich :addr:`000H` |...| :addr:`0FFH` ausgewählt. Das Betätigen der Taste :kbd:`SHIFT` wird unmittelbar in der Matrix erkannt und zum Einstellen der Adressen des Zeichengenerators verwendet. Als Adressbereich kommt :addr:`0100H` |...| :addr:`01FFH` im |EPROM| zur Anwendung. Zusätzlich ist die Funktion des "Feststellers" der :kbd:`SHIFT` Taste mit der Schaltung aus :comp:`D7`, :comp:`D9`, :comp:`D11` und :comp:`D13` realisiert. Eine Anzeige der gedrückten :kbd:`SHIFT` Taste ist mit :comp:`VD1` vorgesehen. :comp:`VD2` bis :comp:`VD5` der |K7659| stehen einer beliebigen Verwendung zur Verfügung (z.B. Anzeige der Funktionen der :signal:`LED0` |...| :signal:`LED6` der zentralen Platine).

Die :kbd:`CTRL` Steuerzeichen können über die zugehörige, gleichfalls hardwareseitig festgelegte, Taste erzeugt werden. Im |EPROM| wird dazu der Bereich :addr:`0200H` |...| :addr:`02FFH` ausgewählt.

Den Inhalt des Zeichengenerator |EPROM| und die daraus resultierenden Tastencodierungen zeigen |PC_M7659_LHD_N| und |PC_M7659_T1_N|. In der Spalte "Adresse" wird für :option:`T` eingesetzt:

.. option:: T

   .. option:: 0

      normaler Tastencode (ohne :kbd:`SHIFT` oder :kbd:`CTRL`)

   .. option:: 1
   
         bei gedrückter :kbd:`SHIFT` Taste

   .. option:: 2
   
         bei gedrückter :kbd:`CTRL` Taste.

Bild D:

.. index:: triple: PC/M; Software; FA 5/90-01 (SW/ZG) :comp:`D8`

.. list-table:: FA 5/90-01 (SW/ZG) :comp:`D8`
   :name: kcsystems-mach-pcm-fa059001-sw
   :class: longtable
   :align: center
   :width: 80 %
   :header-rows: 1

   * - FA 5/90-01 (SW/ZG)

   * - :raw-latex:`\begin{minipage}[c][][c]{0.8\textwidth}`

       .. figure:: bild-hd.png
          :name: kcsystems-mach-pcm-7659-bild-hd
          :figclass: align-center
          :align: center
          :width: 850 px
          :alt: Inhalt des Zeichengenerator |EPROM|

          Inhalt des Zeichengenerator |EPROM|

       :raw-latex:`\end{minipage}`

   * - .. code-block:: hexdump
          :caption: Inhalt des Zeichengenerator |EPROM|
          :name: kcsystems-mach-pcm-7659-listing-bild-hd

          0000    00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00
          0010    00 31 71 61  79 32 77 73  78 00 00 00  00 00 00 00
          0020    00 33 65 64  63 34 72 66  76 00 00 00  00 00 00 00
          0030    00 35 74 67  62 36 7A 68  6E 00 00 00  00 00 00 00
          0040    00 37 75 6A  6D 38 69 6B  2C 00 00 00  00 00 00 00
          0050    00 39 6F 6C  2E 30 70 7C  2D 00 00 00  00 00 00 00
          0060    00 7E 7D 7B  3C 2B 23 5E  09 00 00 00  00 00 00 00
          0070    00 3E 0D 04  01 20 1B 13  06 00 00 00  00 00 00 00
          0080    00 00 0C 7F  05 18 13 04  03 00 00 00  00 00 00 00
          0090    00 1A 17 07  14 19 02 0B  11 00 00 00  00 00 00 00
          00A0    00 12 00 1A  0A 15 08 00  FF 00 00 00  00 00 00 00
          00B0    00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00
          00C0    00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00
          00D0    00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00
          00E0    00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00
          00F0    00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00
          0100    00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00
          0110    00 21 51 41  59 22 57 53  58 00 00 00  00 00 00 00
          0120    00 FF 45 44  43 24 52 46  56 00 00 00  00 00 00 00
          0130    00 25 54 47  42 26 5A 48  4E 00 00 00  00 00 00 00
          0140    00 2F 55 4A  4D 28 49 4B  3B 00 00 00  00 00 00 00
          0150    00 29 4F 4C  3A 3D 50 5C  5F 00 00 00  00 00 00 00
          0160    00 3F 5D 5B  3C 2A 27 7E  09 00 00 00  00 00 00 00
          0170    00 3E 0D 04  01 20 1B 13  06 00 00 00  00 00 00 00
          0180    00 00 0C 1E  05 18 13 04  03 00 00 00  00 00 00 00
          0190    00 1A 17 07  14 19 02 0B  11 00 00 00  00 00 00 00
          01A0    00 12 00 1A  0A 15 08 00  FF 00 00 00  00 00 00 00
          01B0    00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00
          01C0    00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00
          01D0    00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00
          01E0    00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00
          01F0    00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00
          0200    00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00
          0210    00 31 11 01  19 32 17 13  18 00 00 00  00 00 00 00
          0220    00 33 05 04  03 34 12 06  16 00 00 00  00 00 00 00
          0230    00 35 14 07  02 36 1A 08  0E 00 00 00  00 00 00 00
          0240    00 37 15 0A  0D 38 09 0B  2C 00 00 00  00 00 00 00
          0250    00 39 0F 0C  2E 30 10 1C  2D 00 00 00  00 00 00 00
          0260    00 1E 1D 1B  3C 2B 1F 1E  09 00 00 00  00 00 00 00
          0270    00 3E 0D 04  01 60 1F 13  06 00 00 00  00 00 00 00
          0280    00 00 0C 1F  05 18 13 04  03 00 00 00  00 00 00 00
          0290    00 1A 17 07  14 19 02 0B  11 00 00 00  00 00 00 00
          02A0    00 12 FF 1A  0A 15 08 FF  FF FF FF FF  FF FF FF FF
          02B0    FF FF FF FF  FF FF FF FF  FF FF FF FF  FF FF FF FF
          02C0    FF FF FF FF  FF FF FF FF  FF FF FF FF  FF FF FF FF
          02D0    FF FF FF FF  FF FF FF FF  FF FF FF FF  FF FF FF FF
          02E0    FF FF FF FF  FF FF FF FF  FF FF FF FF  FF FF FF FF
          02F0    FF FF FF FF  FF FF FF FF  FF FF FF FF  FF FF FF FF

Bild E:

.. tabularcolumns:: \X{12}{100}\X{16}{100}|\X{12}{100}\X{12}{100}|\X{12}{100}\X{12}{100}|\X{12}{100}\X{12}{100}
.. table:: |PC/M| |K7659| Tastaturanschluss - Tastencodebelegung mit |EPROM| nach Bild D
   :name: kcsystems-mach-pcm-7659-tabelle-1
   :widths: 12, 16, 12, 12, 12, 12, 12, 12
   :class: longtable
   :align: center
   :width: 80%

   +------------------------------+-----------------------------------------------------------------------------------+
   | Tastatursteuerung            | Code Hexadezimal und |ASCII|                                                      |
   +--------------+---------------+---------------------------+---------------------------+---------------------------+
   |   |K7659|    |    Adresse    | normal                    | :kbd:`SHIFT`              | :kbd:`CTRL`               |
   +==============+===============+============+==============+============+==============+============+==============+
   | :kbd:`A00`   | :addr:`0T77H` | :code:`13` | :kbd:`^S`    | :code:`13` | :kbd:`^S`    | :code:`13` | :kbd:`^S`    |
   +--------------+---------------+------------+--------------+------------+--------------+------------+--------------+
   | :kbd:`A01`   | :addr:`0T73H` | :code:`04` | :kbd:`^D`    | :code:`04` | :kbd:`^D`    | :code:`04` | :kbd:`^D`    |
   +--------------+---------------+------------+--------------+------------+--------------+------------+--------------+
   | :kbd:`A05`   | :addr:`0T75H` | :code:`20` | :kbd:`SPACE` | :code:`20` | :kbd:`SPACE` | :code:`60` | :kbd:`\``    |
   +--------------+---------------+------------+--------------+------------+--------------+------------+--------------+
   | :kbd:`A10`   | :addr:`0T74H` | :code:`01` | :kbd:`^A`    | :code:`01` | :kbd:`^A`    | :code:`01` | :kbd:`^A`    |
   +--------------+---------------+------------+--------------+------------+--------------+------------+--------------+
   | :kbd:`A11`   | :addr:`0T78H` | :code:`06` | :kbd:`^F`    | :code:`06` | :kbd:`^F`    | :code:`06` | :kbd:`^F`    |
   +--------------+---------------+------------+--------------+------------+--------------+------------+--------------+
   +--------------+---------------+------------+--------------+------------+--------------+------------+--------------+
   | :kbd:`B00`   | :addr:`0T68H` | :code:`09` | :kbd:`HT`    | :code:`09` | :kbd:`HT`    | :code:`09` | :kbd:`HT`    |
   +--------------+---------------+------------+--------------+------------+--------------+------------+--------------+
   | :kbd:`B01`   | :addr:`0T14H` | :code:`79` | :kbd:`y`     | :code:`59` | :kbd:`Y`     | :code:`19` | :kbd:`^Y`    |
   +--------------+---------------+------------+--------------+------------+--------------+------------+--------------+
   | :kbd:`B02`   | :addr:`0T18H` | :code:`78` | :kbd:`x`     | :code:`58` | :kbd:`X`     | :code:`18` | :kbd:`^X`    |
   +--------------+---------------+------------+--------------+------------+--------------+------------+--------------+
   | :kbd:`B03`   | :addr:`0T24H` | :code:`63` | :kbd:`c`     | :code:`43` | :kbd:`C`     | :code:`03` | :kbd:`^C`    |
   +--------------+---------------+------------+--------------+------------+--------------+------------+--------------+
   | :kbd:`B04`   | :addr:`0T28H` | :code:`76` | :kbd:`v`     | :code:`56` | :kbd:`V`     | :code:`16` | :kbd:`^V`    |
   +--------------+---------------+------------+--------------+------------+--------------+------------+--------------+
   | :kbd:`B05`   | :addr:`0T34H` | :code:`62` | :kbd:`b`     | :code:`42` | :kbd:`B`     | :code:`02` | :kbd:`^B`    |
   +--------------+---------------+------------+--------------+------------+--------------+------------+--------------+
   | :kbd:`B06`   | :addr:`0T38H` | :code:`6E` | :kbd:`n`     | :code:`4E` | :kbd:`N`     | :code:`0E` | :kbd:`^N`    |
   +--------------+---------------+------------+--------------+------------+--------------+------------+--------------+
   | :kbd:`B07`   | :addr:`0T44H` | :code:`6D` | :kbd:`m`     | :code:`4D` | :kbd:`M`     | :code:`0D` | :kbd:`^M`    |
   +--------------+---------------+------------+--------------+------------+--------------+------------+--------------+
   | :kbd:`B08`   | :addr:`0T48H` | :code:`2C` | :kbd:`,`     | :code:`3B` | :kbd:`;`     | :code:`2C` | :kbd:`,`     |
   +--------------+---------------+------------+--------------+------------+--------------+------------+--------------+
   | :kbd:`B09`   | :addr:`0T54H` | :code:`2E` | :kbd:`.`     | :code:`3A` | :kbd:`:`     | :code:`2E` | :kbd:`.`     |
   +--------------+---------------+------------+--------------+------------+--------------+------------+--------------+
   | :kbd:`B10`   | :addr:`0T58H` | :code:`2D` | :kbd:`\-`    | :code:`5F` | :kbd:`_`     | :code:`2D` | :kbd:`\-`    |
   +--------------+---------------+------------+--------------+------------+--------------+------------+--------------+
   | :kbd:`B11`   |               |              :kbd:`SHIFT`                                                         |
   +--------------+---------------+-----------------------------------------------------------------------------------+
   | :kbd:`B95`   |               |              :kbd:`CTRL`                                                          |
   +--------------+---------------+-----------------------------------------------------------------------------------+
   +--------------+---------------+-----------------------------------------------------------------------------------+
   | :kbd:`C00`   |               |              :kbd:`SHIFT-F`                                                       |
   +--------------+---------------+------------+--------------+------------+--------------+------------+--------------+
   | :kbd:`C01`   | :addr:`0T13H` | :code:`61` | :kbd:`a`     | :code:`41` | :kbd:`A`     | :code:`01` | :kbd:`^A`    |
   +--------------+---------------+------------+--------------+------------+--------------+------------+--------------+
   | :kbd:`C02`   | :addr:`0T17H` | :code:`73` | :kbd:`s`     | :code:`53` | :kbd:`S`     | :code:`13` | :kbd:`^S`    |
   +--------------+---------------+------------+--------------+------------+--------------+------------+--------------+
   | :kbd:`C03`   | :addr:`0T23H` | :code:`64` | :kbd:`d`     | :code:`44` | :kbd:`D`     | :code:`04` | :kbd:`^D`    |
   +--------------+---------------+------------+--------------+------------+--------------+------------+--------------+
   | :kbd:`C04`   | :addr:`0T27H` | :code:`66` | :kbd:`f`     | :code:`46` | :kbd:`F`     | :code:`06` | :kbd:`^F`    |
   +--------------+---------------+------------+--------------+------------+--------------+------------+--------------+
   | :kbd:`C05`   | :addr:`0T33H` | :code:`67` | :kbd:`g`     | :code:`47` | :kbd:`G`     | :code:`07` | :kbd:`^G`    |
   +--------------+---------------+------------+--------------+------------+--------------+------------+--------------+
   | :kbd:`C06`   | :addr:`0T37H` | :code:`68` | :kbd:`h`     | :code:`48` | :kbd:`H`     | :code:`08` | :kbd:`^H`    |
   +--------------+---------------+------------+--------------+------------+--------------+------------+--------------+
   | :kbd:`C07`   | :addr:`0T43H` | :code:`6A` | :kbd:`j`     | :code:`4A` | :kbd:`J`     | :code:`0A` | :kbd:`^J`    |
   +--------------+---------------+------------+--------------+------------+--------------+------------+--------------+
   | :kbd:`C08`   | :addr:`0T47H` | :code:`6B` | :kbd:`k`     | :code:`4B` | :kbd:`K`     | :code:`0B` | :kbd:`^K`    |
   +--------------+---------------+------------+--------------+------------+--------------+------------+--------------+
   | :kbd:`C09`   | :addr:`0T53H` | :code:`6C` | :kbd:`l`     | :code:`4C` | :kbd:`L`     | :code:`0C` | :kbd:`^L`    |
   +--------------+---------------+------------+--------------+------------+--------------+------------+--------------+
   | :kbd:`C10`   | :addr:`0T57H` | :code:`7C` | :kbd:`\|`    | :code:`5C` | :kbd:`\\`    | :code:`1C` | :kbd:`^\\`   |
   +--------------+---------------+------------+--------------+------------+--------------+------------+--------------+
   | :kbd:`C11`   | :addr:`0T63H` | :code:`7B` | :kbd:`{`     | :code:`5B` | :kbd:`[`     | :code:`1B` | :kbd:`^[`    |
   +--------------+---------------+------------+--------------+------------+--------------+------------+--------------+
   | :kbd:`C12`   | :addr:`0T66H` | :code:`23` | :kbd:`#`     | :code:`27` | :kbd:`'`     | :code:`1F` | :kbd:`^_`    |
   +--------------+---------------+------------+--------------+------------+--------------+------------+--------------+
   | :kbd:`C/B13` | :addr:`0T72H` | :code:`0D` | :kbd:`^M`    | :code:`0D` | :kbd:`^M`    | :code:`0D` | :kbd:`^M`    |
   +--------------+---------------+------------+--------------+------------+--------------+------------+--------------+
   | :kbd:`C53`   | :addr:`0TA6H` | :code:`08` | :kbd:`^H`    | :code:`08` | :kbd:`^H`    | :code:`08` | :kbd:`^H`    |
   +--------------+---------------+------------+--------------+------------+--------------+------------+--------------+
   +--------------+---------------+------------+--------------+------------+--------------+------------+--------------+
   | :kbd:`D00`   | :addr:`0T76H` | :code:`1B` | :kbd:`ESC`   | :code:`1B` | :kbd:`ESC`   | :code:`1F` | :kbd:`^_`    |
   +--------------+---------------+------------+--------------+------------+--------------+------------+--------------+
   | :kbd:`D01`   | :addr:`0T12H` | :code:`71` | :kbd:`q`     | :code:`51` | :kbd:`Q`     | :code:`11` | :kbd:`^Q`    |
   +--------------+---------------+------------+--------------+------------+--------------+------------+--------------+
   | :kbd:`D02`   | :addr:`0T16H` | :code:`77` | :kbd:`w`     | :code:`57` | :kbd:`W`     | :code:`17` | :kbd:`^W`    |
   +--------------+---------------+------------+--------------+------------+--------------+------------+--------------+
   | :kbd:`D03`   | :addr:`0T22H` | :code:`65` | :kbd:`e`     | :code:`45` | :kbd:`E`     | :code:`05` | :kbd:`^E`    |
   +--------------+---------------+------------+--------------+------------+--------------+------------+--------------+
   | :kbd:`D04`   | :addr:`0T26H` | :code:`72` | :kbd:`r`     | :code:`52` | :kbd:`R`     | :code:`12` | :kbd:`^R`    |
   +--------------+---------------+------------+--------------+------------+--------------+------------+--------------+
   | :kbd:`D05`   | :addr:`0T32H` | :code:`74` | :kbd:`t`     | :code:`54` | :kbd:`T`     | :code:`14` | :kbd:`^T`    |
   +--------------+---------------+------------+--------------+------------+--------------+------------+--------------+
   | :kbd:`D06`   | :addr:`0T36H` | :code:`7A` | :kbd:`z`     | :code:`5A` | :kbd:`Z`     | :code:`1A` | :kbd:`^Z`    |
   +--------------+---------------+------------+--------------+------------+--------------+------------+--------------+
   | :kbd:`D07`   | :addr:`0T42H` | :code:`75` | :kbd:`u`     | :code:`55` | :kbd:`U`     | :code:`15` | :kbd:`^U`    |
   +--------------+---------------+------------+--------------+------------+--------------+------------+--------------+
   | :kbd:`D08`   | :addr:`0T46H` | :code:`69` | :kbd:`i`     | :code:`49` | :kbd:`I`     | :code:`09` | :kbd:`^I`    |
   +--------------+---------------+------------+--------------+------------+--------------+------------+--------------+
   | :kbd:`D09`   | :addr:`0T52H` | :code:`6F` | :kbd:`o`     | :code:`4F` | :kbd:`O`     | :code:`0F` | :kbd:`^O`    |
   +--------------+---------------+------------+--------------+------------+--------------+------------+--------------+
   | :kbd:`D10`   | :addr:`0T56H` | :code:`70` | :kbd:`p`     | :code:`50` | :kbd:`P`     | :code:`10` | :kbd:`^P`    |
   +--------------+---------------+------------+--------------+------------+--------------+------------+--------------+
   | :kbd:`D11`   | :addr:`0T62H` | :code:`7D` | :kbd:`}`     | :code:`5D` | :kbd:`]`     | :code:`1D` | :kbd:`^]`    |
   +--------------+---------------+------------+--------------+------------+--------------+------------+--------------+
   | :kbd:`D12`   | :addr:`0T65H` | :code:`2B` | :kbd:`\+`    | :code:`2A` | :kbd:`\*`    | :code:`2B` | :kbd:`\+`    |
   +--------------+---------------+------------+--------------+------------+--------------+------------+--------------+
   | :kbd:`D13`   | :addr:`0T82H` | :code:`0C` | :kbd:`^L`    | :code:`0C` | :kbd:`^L`    | :code:`0C` | :kbd:`^L`    |
   +--------------+---------------+------------+--------------+------------+--------------+------------+--------------+
   | :kbd:`D53`   | :addr:`0TA5H` | :code:`15` | :kbd:`^U`    | :code:`15` | :kbd:`^U`    | :code:`15` | :kbd:`^U`    |
   +--------------+---------------+------------+--------------+------------+--------------+------------+--------------+
   | :kbd:`D/C95` |               |              :signal:`NMI`                                                        |
   +--------------+---------------+-----------------------------------------------------------------------------------+
   +--------------+---------------+------------+--------------+------------+--------------+------------+--------------+
   | :kbd:`E00`   | :addr:`0T67H` | :code:`5E` | :kbd:`^`     | :code:`7E` | :kbd:`~`     | :code:`1E` | :kbd:`^^`    |
   +--------------+---------------+------------+--------------+------------+--------------+------------+--------------+
   | :kbd:`E01`   | :addr:`0T11H` | :code:`31` | :kbd:`1`     | :code:`21` | :kbd:`!`     | :code:`31` | :kbd:`1`     |
   +--------------+---------------+------------+--------------+------------+--------------+------------+--------------+
   | :kbd:`E02`   | :addr:`0T15H` | :code:`32` | :kbd:`2`     | :code:`22` | :kbd:`"`     | :code:`32` | :kbd:`2`     |
   +--------------+---------------+------------+--------------+------------+--------------+------------+--------------+
   | :kbd:`E03`   | :addr:`0T21H` | :code:`33` | :kbd:`3`     | :code:`40` | :kbd:`@`     | :code:`33` | :kbd:`3`     |
   +--------------+---------------+------------+--------------+------------+--------------+------------+--------------+
   | :kbd:`E04`   | :addr:`0T25H` | :code:`34` | :kbd:`4`     | :code:`24` | :kbd:`$`     | :code:`34` | :kbd:`4`     |
   +--------------+---------------+------------+--------------+------------+--------------+------------+--------------+
   | :kbd:`E05`   | :addr:`0T31H` | :code:`35` | :kbd:`5`     | :code:`25` | :kbd:`%`     | :code:`35` | :kbd:`5`     |
   +--------------+---------------+------------+--------------+------------+--------------+------------+--------------+
   | :kbd:`E06`   | :addr:`0T35H` | :code:`36` | :kbd:`6`     | :code:`26` | :kbd:`&`     | :code:`36` | :kbd:`6`     |
   +--------------+---------------+------------+--------------+------------+--------------+------------+--------------+
   | :kbd:`E07`   | :addr:`0T41H` | :code:`37` | :kbd:`7`     | :code:`2F` | :kbd:`/`     | :code:`37` | :kbd:`7`     |
   +--------------+---------------+------------+--------------+------------+--------------+------------+--------------+
   | :kbd:`E08`   | :addr:`0T45H` | :code:`38` | :kbd:`8`     | :code:`28` | :kbd:`(`     | :code:`38` | :kbd:`8`     |
   +--------------+---------------+------------+--------------+------------+--------------+------------+--------------+
   | :kbd:`E09`   | :addr:`0T51H` | :code:`39` | :kbd:`9`     | :code:`29` | :kbd:`)`     | :code:`39` | :kbd:`9`     |
   +--------------+---------------+------------+--------------+------------+--------------+------------+--------------+
   | :kbd:`E10`   | :addr:`0T55H` | :code:`30` | :kbd:`0`     | :code:`3D` | :kbd:`=`     | :code:`30` | :kbd:`0`     |
   +--------------+---------------+------------+--------------+------------+--------------+------------+--------------+
   | :kbd:`E11`   | :addr:`0T61H` | :code:`7E` | :kbd:`~`     | :code:`3F` | :kbd:`?`     | :code:`1E` | :kbd:`^^`    |
   +--------------+---------------+------------+--------------+------------+--------------+------------+--------------+
   | :kbd:`E12`   | :addr:`0T64H` | :code:`3C` | :kbd:`<`     | :code:`3C` | :kbd:`<`     | :code:`3C` | :kbd:`<`     |
   +--------------+---------------+------------+--------------+------------+--------------+------------+--------------+
   | :kbd:`E13`   | :addr:`0T71H` | :code:`3E` | :kbd:`>`     | :code:`3E` | :kbd:`>`     | :code:`3E` | :kbd:`>`     |
   +--------------+---------------+------------+--------------+------------+--------------+------------+--------------+
   | :kbd:`E14`   | :addr:`0T83H` | :code:`7F` | :kbd:`DEL`   | :code:`1E` | :kbd:`^^`    | :code:`1F` | :kbd:`^_`    |
   +--------------+---------------+------------+--------------+------------+--------------+------------+--------------+
   | :kbd:`E53`   | :addr:`0TA4H` | :code:`0A` | :kbd:`^J`    | :code:`0A` | :kbd:`^J`    | :code:`0A` | :kbd:`^J`    |
   +--------------+---------------+------------+--------------+------------+--------------+------------+--------------+
   | :kbd:`E95`   | :addr:`0TA5H` |              nicht belegt (:code:`FF`)                                            |
   +--------------+---------------+-----------------------------------------------------------------------------------+
   +--------------+---------------+------------+--------------+------------+--------------+------------+--------------+
   | :kbd:`F01`   | :addr:`0T84H` | :code:`05` | :kbd:`^E`    | :code:`05` | :kbd:`^E`    | :code:`05` | :kbd:`^E`    |
   +--------------+---------------+------------+--------------+------------+--------------+------------+--------------+
   | :kbd:`F02`   | :addr:`0T85H` | :code:`18` | :kbd:`^X`    | :code:`18` | :kbd:`^X`    | :code:`18` | :kbd:`^X`    |
   +--------------+---------------+------------+--------------+------------+--------------+------------+--------------+
   | :kbd:`F03`   | :addr:`0T86H` | :code:`13` | :kbd:`^S`    | :code:`13` | :kbd:`^S`    | :code:`13` | :kbd:`^S`    |
   +--------------+---------------+------------+--------------+------------+--------------+------------+--------------+
   | :kbd:`F04`   | :addr:`0T87H` | :code:`04` | :kbd:`^D`    | :code:`04` | :kbd:`^D`    | :code:`04` | :kbd:`^D`    |
   +--------------+---------------+------------+--------------+------------+--------------+------------+--------------+
   | :kbd:`F05`   | :addr:`0TA1H` | :code:`12` | :kbd:`^R`    | :code:`12` | :kbd:`^R`    | :code:`12` | :kbd:`^R`    |
   +--------------+---------------+------------+--------------+------------+--------------+------------+--------------+
   | :kbd:`F06`   | :addr:`0T88H` | :code:`03` | :kbd:`^C`    | :code:`03` | :kbd:`^C`    | :code:`03` | :kbd:`^C`    |
   +--------------+---------------+------------+--------------+------------+--------------+------------+--------------+
   | :kbd:`F07`   | :addr:`0T91H` | :code:`1A` | :kbd:`^Z`    | :code:`1A` | :kbd:`^Z`    | :code:`1A` | :kbd:`^A`    |
   +--------------+---------------+------------+--------------+------------+--------------+------------+--------------+
   | :kbd:`F08`   | :addr:`0T92H` | :code:`17` | :kbd:`^W`    | :code:`17` | :kbd:`^W`    | :code:`17` | :kbd:`^W`    |
   +--------------+---------------+------------+--------------+------------+--------------+------------+--------------+
   | :kbd:`F09`   | :addr:`0T93H` | :code:`07` | :kbd:`^G`    | :code:`07` | :kbd:`^G`    | :code:`07` | :kbd:`^G`    |
   +--------------+---------------+------------+--------------+------------+--------------+------------+--------------+
   | :kbd:`F10`   | :addr:`0T94H` | :code:`14` | :kbd:`^T`    | :code:`14` | :kbd:`^T`    | :code:`14` | :kbd:`^T`    |
   +--------------+---------------+------------+--------------+------------+--------------+------------+--------------+
   | :kbd:`F11`   | :addr:`0T95H` | :code:`19` | :kbd:`^Y`    | :code:`19` | :kbd:`^Y`    | :code:`19` | :kbd:`^Y`    |
   +--------------+---------------+------------+--------------+------------+--------------+------------+--------------+
   | :kbd:`F12`   | :addr:`0T96H` | :code:`02` | :kbd:`^B`    | :code:`02` | :kbd:`^B`    | :code:`02` | :kbd:`^B`    |
   +--------------+---------------+------------+--------------+------------+--------------+------------+--------------+
   | :kbd:`F13`   | :addr:`0T97H` | :code:`0B` | :kbd:`^K`    | :code:`0B` | :kbd:`^K`    | :code:`0B` | :kbd:`^K`    |
   +--------------+---------------+------------+--------------+------------+--------------+------------+--------------+
   | :kbd:`F14`   | :addr:`0T98H` | :code:`11` | :kbd:`^Q`    | :code:`11` | :kbd:`^Q`    | :code:`11` | :kbd:`^Q`    |
   +--------------+---------------+------------+--------------+------------+--------------+------------+--------------+
   | :kbd:`F53`   | :addr:`0TA3H` | :code:`1A` | :kbd:`^Z`    | :code:`1A` | :kbd:`^Z`    | :code:`1A` | :kbd:`^Z`    |
   +--------------+---------------+------------+--------------+------------+--------------+------------+--------------+
   | :kbd:`F95`   |               |              :signal:`RESET`                                                      |
   +--------------+---------------+-----------------------------------------------------------------------------------+

.. index:: triple: PC/M; K7659 Tastaturanschluss; Inbetriebnahme

Aufbau und Inbetriebnahme
*************************

Die Leiterplatte der Tastaturansteuerung für |K7659| ist auf zweiseitigem Basismaterial zu realisieren. |PC_M7659_B03_N| und |PC_M7659_B04_N| zeigen die zugehörige Leiterzugführung. |PC_M7659_B05_N| gibt den Bestückungsplan wieder. Die Inbetriebnahme der Tastatursteuerung ist nach kompletter Bestückung möglich. Es ist zu empfehlen, den Zeichengenerator dabei auf einer |EPROM| Fassung steckbar anzuordnen, um bei Bedarf die Belegung der Tastatur ändern zu können. Zuerst sollte die Funktion der :kbd:`SHIFT` und :kbd:`CTRL` Tasten durch Messen der Pegel mit einem Multimeter überprüft werden. Danach werden alle weiteren Tasten auf Funktionsfähigkeit getestet und gegebenenfalls die zugehörigen Spaltendekoder und Zeilendekoder bzw. Spaltentreiber und Zeilentreiber überprüft. Zuletzt kann der |EPROM| eingesetzt werden und die Tastatur wird an den |PC/M| Computer angeschlossen. |EPROM| Inhalt und weitere Informationen können über die im |Funkamateur| Heft 11/1988 angegebenen Quellen auf gleiche Art und Weise bereitgestellt werden.

:raw-latex:`\begin{turn}{90}`
:raw-latex:`\begin{minipage}[c][\textwidth][c]{\textheight}`

.. index:: triple: PC/M; PCB Layouts; FA 5/90-01 (BP)
.. index:: triple: PC/M; PCB Layouts; FA 5/90-01 (LS)
.. index:: triple: PC/M; PCB Layouts; FA 5/90-01 (BS)

.. list-table:: FA 5/90-01 (BP) (LS) (BS)
   :name: kcsystems-mach-pcm-fa059001-lsbsbp
   :class: longtable
   :align: center
   :width: 80 %
   :header-rows: 1

   * - FA 5/90-01 (BS)
     - FA 5/90-01 (LS)
     - FA 5/90-01 (BP)

   * - :raw-latex:`\begin{turn}{270}`
       :raw-latex:`\begin{minipage}[c][][c]{0.6\textwidth}`

       .. figure:: bild-04.png
          :name: kcsystems-mach-pcm-7659-bild-04
          :figclass: align-center
          :align: center
          :width: 560 px
          :alt: Bestückungsseite der Tastaturansteuerung

          Bestückungsseite der Tastaturansteuerung

       :raw-latex:`\end{minipage}`
       :raw-latex:`\end{turn}`

     - :raw-latex:`\begin{turn}{270}`
       :raw-latex:`\begin{minipage}[c][][c]{0.6\textwidth}`

       .. figure:: bild-03.png
          :name: kcsystems-mach-pcm-7659-bild-03
          :figclass: align-center
          :align: center
          :width: 560 px
          :alt: Leiterseite der Tastaturansteuerung

          Leiterseite der Tastaturansteuerung

       :raw-latex:`\end{minipage}`
       :raw-latex:`\end{turn}`

     - :raw-latex:`\begin{turn}{270}`
       :raw-latex:`\begin{minipage}[c][][c]{0.6\textwidth}`

       .. figure:: bild-05.png
          :name: kcsystems-mach-pcm-7659-bild-05
          :figclass: align-center
          :align: center
          :width: 560 px
          :alt: Bestückungsplan der |K7659| Tastaturansteuerung

          Bestückungsplan der |K7659| Tastaturansteuerung

       :raw-latex:`\end{minipage}`
       :raw-latex:`\end{turn}`

:raw-latex:`\end{minipage}`
:raw-latex:`\end{turn}`
:raw-latex:`\FloatBarrier`

.. index:: triple: PC/M; K7659 Tastaturanschluss; Abbildungsverzeichnis

Bildunterschriften
******************

.. .. tabularcolumns:: cl
.. tabularcolumns:: p{0.12\linewidth}p{0.68\linewidth}
.. table:: |PC/M| |K7659| Tastaturanschluss - Verzeichnis der Bilder
   :widths: 15, 85
   :class: longtable
   :align: center
   :width: 80%

   +------------------+-------------------------------------------------------+
   | Bild             | Titel                                                 |
   +==================+=======================================================+
   | |PC_M7659_B01_N| | |PC_M7659_B01_T|                                      |
   +------------------+-------------------------------------------------------+
   | |PC_M7659_B02_N| | |PC_M7659_B02_T|                                      |
   +------------------+-------------------------------------------------------+
   | |PC_M7659_B03_N| | |PC_M7659_B03_T|                                      |
   +------------------+-------------------------------------------------------+
   | |PC_M7659_B04_N| | |PC_M7659_B04_T|                                      |
   +------------------+-------------------------------------------------------+
   | |PC_M7659_B05_N| | |PC_M7659_B05_T|                                      |
   +------------------+-------------------------------------------------------+
   | |PC_M7659_BHD_N| | |PC_M7659_BHD_T|                                      |
   +------------------+-------------------------------------------------------+

.. index:: triple: PC/M; K7659 Tastaturanschluss; Literaturverzeichnis

Literatur
*********

Verschoben, siehe :ref:`bibliography:Bibliography`.

.. Local variables:
   coding: utf-8
   mode: text
   mode: rst
   End:
   vim: fileencoding=utf-8 filetype=rst :
