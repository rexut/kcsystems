.. index:: pair: PC/M; Steckverbinder

Steckverbinder
##############

.. index:: triple: PC/M; Steckverbinder; Tastatur

Tastatur X1
***********

39 poliger Steckverbinder

.. tabularcolumns:: p{0.05\linewidth}p{0.1\linewidth}p{0.1\linewidth}p{0.1\linewidth}p{0.15\linewidth}
.. table:: |PC/M| Steckverbinder - Tastatur :comp:`X1`
   :name: kcsystems-mach-pcm-tabelle-3
   :widths: 10, 20, 20, 20, 30
   :class: longtable
   :align: center
   :width: 50%

   +-----------+------------------------+-----------------+-----------------+----------------+
   |    Pin    |             A          |        B        |        C        |    Hinweise    |
   +===========+========================+=================+=================+================+
   | :pin:`1`  | :signal:`5P`           | :signal:`5P`    | :signal:`5P`    |                |
   +-----------+------------------------+-----------------+-----------------+----------------+
   | :pin:`2`  | n.b.                   | :signal:`A7`    | n.b.            |                |
   +-----------+------------------------+-----------------+-----------------+----------------+
   | :pin:`3`  | n.b.                   | :signal:`A6`    | n.b.            |                |
   +-----------+------------------------+-----------------+-----------------+----------------+
   | :pin:`4`  | n.b.                   | :signal:`A5`    | :signal:`B5`    |                |
   +-----------+------------------------+-----------------+-----------------+----------------+
   | :pin:`5`  | n.b.                   | :signal:`A4`    | :signal:`B4`    |                |
   +-----------+------------------------+-----------------+-----------------+----------------+
   | :pin:`6`  | n.b.                   | :signal:`A3`    | :signal:`B3`    |                |
   +-----------+------------------------+-----------------+-----------------+----------------+
   | :pin:`7`  | n.b.                   | :signal:`A2`    | :signal:`B2`    |                |
   +-----------+------------------------+-----------------+-----------------+----------------+
   | :pin:`8`  | n.b.                   | :signal:`A1`    | :signal:`B1`    |                |
   +-----------+------------------------+-----------------+-----------------+----------------+
   | :pin:`9`  | :signal:`/NMI` Taste   | :signal:`A0`    | :signal:`B0`    |                |
   +-----------+------------------------+-----------------+-----------------+----------------+
   | :pin:`10` | :signal:`/HALT`        | :signal:`/ASTB` | :signal:`/BSTB` |                |
   +-----------+------------------------+-----------------+-----------------+----------------+
   | :pin:`11` | :signal:`/RESET` Taste | :signal:`ARDY`  | :signal:`BRDY`  |                |
   +-----------+------------------------+-----------------+-----------------+----------------+
   | :pin:`12` | n.b.                   | n.b.            | n.b.            |                |
   +-----------+------------------------+-----------------+-----------------+----------------+
   | :pin:`13` | :signal:`GND`          | :signal:`GND`   | :signal:`GND`   |                |
   +-----------+------------------------+-----------------+-----------------+----------------+

.. tabularcolumns:: p{0.075\linewidth}p{0.075\linewidth}p{0.35\linewidth}
.. table:: |PC/M| Belegung der System PIO - Tastatur
   :name: kcsystems-mach-pcm-tabelle-2
   :widths: 15, 15, 70
   :class: longtable
   :align: center
   :width: 50%

   +-----------------+----------------+-----------------------------------+
   |       PIO       |    Tastatur    |             Verwendung            |
   +=================+================+===================================+
   | :signal:`A0`    | :signal:`TD0`  |                                   |
   +-----------------+----------------+                                   |
   | :signal:`A1`    | :signal:`TD1`  |                                   |
   +-----------------+----------------+                                   |
   | :signal:`A2`    | :signal:`TD2`  |                                   |
   +-----------------+----------------+                                   |
   | :signal:`A3`    | :signal:`TD3`  |   7 Bit |ASCII| - Zeichen         |
   +-----------------+----------------+                                   |
   | :signal:`A4`    | :signal:`TD4`  |                                   |
   +-----------------+----------------+                                   |
   | :signal:`A5`    | :signal:`TD5`  |                                   |
   +-----------------+----------------+                                   |
   | :signal:`A6`    | :signal:`TD6`  |                                   |
   +-----------------+----------------+-----------------------------------+
   | :signal:`A7`    | :signal:`TAST` | :level:`High` = Taste gedrückt    |
   +-----------------+----------------+-----------------------------------+
   | :signal:`/ASTB` | :signal:`GND`  |                                   |
   +-----------------+----------------+-----------------------------------+
   | :signal:`B0`    | :comp:`LED 0`  | Betriebsanzeige                   |
   +-----------------+----------------+-----------------------------------+
   | :signal:`B1`    | :comp:`LED 1`  | Run/Stop                          |
   +-----------------+----------------+-----------------------------------+
   | :signal:`B2`    | :comp:`LED 2`  | Ton Ein/Aus                       |
   +-----------------+----------------+-----------------------------------+
   | :signal:`B3`    | :comp:`LED 3`  | n.b.                              |
   +-----------------+----------------+-----------------------------------+
   | :signal:`B4`    | :comp:`LED 4`  | :level:`High` = **SAVE**,         |
   |                 |                | :level:`Low` = **LOAD**           |
   +-----------------+----------------+-----------------------------------+
   | :signal:`B5`    | :comp:`LED 5`  | :level:`High` = **Motor Ein**     |
   +-----------------+----------------+-----------------------------------+
   | :signal:`B6`    |                | **SAVE** = Eingang |KMBG|         |
   +-----------------+----------------+-----------------------------------+
   | :signal:`B7`    |                | **LOAD** = Ausgang |KMBG|         |
   +-----------------+----------------+-----------------------------------+
   |                 | :comp:`LED 6`  | Haltzustand der |CPU|             |
   +-----------------+----------------+-----------------------------------+

.. index:: triple: PC/M; Steckverbinder; Koppelbus

Koppelbusverbinder X2
*********************

Hinweise und Korrekturen, siehe |PC_M_TA2_N| in Abschnitt
:ref:`mach/pcm/PC_M4.DOC/hinweise-und-korrekturen:Zentrale Platine`.

58 poliger Steckverbinder

.. tabularcolumns:: p{0.05\linewidth}p{0.10\linewidth}p{0.10\linewidth}p{0.25\linewidth}
.. table:: |PC/M| Steckverbinder - Koppelbusverbinders :comp:`X2`
   :name: kcsystems-mach-pcm-tabelle-4
   :widths: 10, 20, 20, 50
   :class: longtable
   :align: center
   :width: 50%

   +-----------+---------------------+---------------------+----------------+
   |    Pin    |          A          |          B          |    Hinweise    |
   +===========+=====================+=====================+================+
   | :pin:`1`  | :signal:`GND`       | :signal:`GND`       |                |
   +-----------+---------------------+---------------------+----------------+
   | :pin:`2`  | n.b.                | :signal:`/IOSEL`    | **fehlerhaft** |
   +-----------+---------------------+---------------------+----------------+
   | :pin:`3`  | :signal:`ZC/TO 2`   | n.b.                |                |
   +-----------+---------------------+---------------------+----------------+
   | :pin:`4`  | :signal:`ZC/TO 0`   | :signal:`ZC/TO 1`   |                |
   +-----------+---------------------+---------------------+----------------+
   | :pin:`5`  | :signal:`C/TRG 1`   | :signal:`C/TRG 0`   |                |
   +-----------+---------------------+---------------------+----------------+
   | :pin:`6`  | :signal:`C/TRG 3`   | :signal:`C/TRG 2`   |                |
   +-----------+---------------------+---------------------+----------------+
   | :pin:`7`  | :signal:`B7`        | :signal:`A7`        |                |
   +-----------+---------------------+---------------------+----------------+
   | :pin:`8`  | :signal:`B6`        | :signal:`A6`        |                |
   +-----------+---------------------+---------------------+----------------+
   | :pin:`9`  | :signal:`B5`        | :signal:`A5`        |                |
   +-----------+---------------------+---------------------+----------------+
   | :pin:`10` | :signal:`B4`        | :signal:`A4`        |                |
   +-----------+---------------------+---------------------+----------------+
   | :pin:`11` | :signal:`B3`        | :signal:`GND`       |                |
   +-----------+---------------------+---------------------+----------------+
   | :pin:`12` | :signal:`B2`        | :signal:`A3`        |                |
   +-----------+---------------------+---------------------+----------------+
   | :pin:`13` | :signal:`B1`        | :signal:`A2`        |                |
   +-----------+---------------------+---------------------+----------------+
   | :pin:`14` | :signal:`B0`        | :signal:`A1`        |                |
   +-----------+---------------------+---------------------+----------------+
   | :pin:`15` | :signal:`5P`        | :signal:`A0`        |                |
   +-----------+---------------------+---------------------+----------------+
   | :pin:`16` | :signal:`/BSTB`     | :signal:`/ASTB`     |                |
   +-----------+---------------------+---------------------+----------------+
   | :pin:`17` | :signal:`BRDY`      | :signal:`ARDY`      |                |
   +-----------+---------------------+---------------------+----------------+
   | :pin:`18` | :signal:`IEI`       | :signal:`IEO`       | **fehlerhaft** |
   +-----------+---------------------+---------------------+----------------+
   | :pin:`19` | :signal:`/RTSA`     | :signal:`/DTRA`     |                |
   +-----------+---------------------+---------------------+----------------+
   | :pin:`20` | :signal:`/DTRB`     | :signal:`/RTSB`     |                |
   +-----------+---------------------+---------------------+----------------+
   | :pin:`21` | :signal:`TxDA 2`    | :signal:`TxDA 1`    |                |
   +-----------+---------------------+---------------------+----------------+
   | :pin:`22` | :signal:`TxDB 2`    | :signal:`TxDB 1`    |                |
   +-----------+---------------------+---------------------+----------------+
   | :pin:`23` | n.b.                | n.b.                | **fehlerhaft** |
   +-----------+---------------------+---------------------+----------------+
   | :pin:`24` | :signal:`RxDA 1`    | :signal:`RxDA 2`    |                |
   +-----------+---------------------+---------------------+----------------+
   | :pin:`25` | :signal:`RxDB 1`    | :signal:`RxDB 2`    |                |
   +-----------+---------------------+---------------------+----------------+
   | :pin:`26` | :signal:`5N`        | :signal:`5N`        |                |
   +-----------+---------------------+---------------------+----------------+
   | :pin:`27` | :signal:`12N`       | :signal:`12N`       |                |
   +-----------+---------------------+---------------------+----------------+
   | :pin:`28` | :signal:`12P`       | :signal:`12P`       |                |
   +-----------+---------------------+---------------------+----------------+
   | :pin:`29` | :signal:`5P`        | :signal:`5P`        |                |
   +-----------+---------------------+---------------------+----------------+

.. index:: triple: PC/M; Steckverbinder; Systembus

Systembusverbinder X3
*********************

Hinweise und Korrekturen, siehe |PC_M_TA3_N| in Abschnitt
:ref:`mach/pcm/PC_M4.DOC/hinweise-und-korrekturen:Zentrale Platine`.

58 poliger Steckverbinder

.. tabularcolumns:: p{0.05\linewidth}p{0.10\linewidth}p{0.10\linewidth}p{0.25\linewidth}
.. table:: |PC/M| Steckverbinder - Systembusverbinders :comp:`X3`
   :name: kcsystems-mach-pcm-tabelle-5
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
   | :pin:`10` | :signal:`/MSEL1`    | n.b.                | **fehlerhaft** |
   +-----------+---------------------+---------------------+----------------+
   | :pin:`11` | :signal:`/MSEL0`    | n.b.                | **fehlerhaft** |
   +-----------+---------------------+---------------------+----------------+
   | :pin:`12` | n.b.                | n.b.                | **fehlerhaft** |
   +-----------+---------------------+---------------------+----------------+
   | :pin:`13` | :signal:`A7`        | n.b.                | **fehlerhaft** |
   +-----------+---------------------+---------------------+----------------+
   | :pin:`14` | :signal:`A6`        | n.b.                | **fehlerhaft** |
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
   | :pin:`20` | :signal:`A0`        | n.b.                |                |
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

.. Local variables:
   coding: utf-8
   mode: text
   mode: rst
   End:
   vim: fileencoding=utf-8 filetype=rst :
