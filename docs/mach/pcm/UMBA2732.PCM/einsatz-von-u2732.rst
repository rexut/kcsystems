.. index:: pair: PC/M; Umbau U2732

.. _kcsystems-mach-pcm-fa038805-k2:

Einsatz von U2732
#################

.. topic:: Werter PC/M User!

   +-----------------------------------------------------------+
   | | Dr. Albrecht Mugler                                     |
   +-----------------------------------------------------------+
   | **Anmerkung:** *Anschriften aus datenschutzrechtlichen*   |
   | *Gründen entfernt!*                                       |
   +-----------------------------------------------------------+

.. | | PSF 24                                                  |
.. | | 9273 Oberlungwitz                                       |
.. +-----------------------------------------------------------+

Beim Einsatz von |U2732| (4096 |*| 8 Bit |EPROM|'s) im |PC/M| Computer sind folgende Änderungen auf der zentralen Platine erforderlich:

1. Auftrennen der Verbindung Pin :pin:`21` von :comp:`D14` |...| :comp:`D17` (|EPROM| Fassung) an +5 V (:signal:`5P`)
2. Verbindung zwischen Pin :pin:`21` von :comp:`D14` |...| :comp:`D17` mit Pin :pin:`17` von :comp:`D7` (DS8282) herstellen (Adresse :signal:`A13`)
3. Verbindung von Pin :pin:`9/10` von :comp:`D12` (D154) an Pin :pin:`17` von :comp:`D7` Auftrennen und Pin :pin:`9/10` von :comp:`D12` an Masse legen
4. |U2732| einsetzen

Die Aufteilung der Speicherbereiche ist wie folgt damit festgelegt:

.. .. tabularcolumns:: lcl
.. tabularcolumns:: p{0.2\linewidth}p{0.08\linewidth}p{0.52\linewidth}
.. table:: |PC/M| |U2732| Umbau - Aufteilung der Speicherbereiche
   :name: kcsystems-mach-pcm-tabelle-1-k2
   :widths: 25, 10, 65
   :class: longtable
   :align: center
   :width: 80%

   +-----------------------------------+-------------+----------------------+
   | Speicherbereich                   | IS          | Inhalt               |
   +===================================+=============+======================+
   | :addr:`0000H` |...| :addr:`07FFH` | :comp:`D14` | niederwertige 2 |kB| |
   +-----------------------------------+-------------+----------------------+
   | :addr:`0800H` |...| :addr:`0FFFH` | :comp:`D15` | niederwertige 2 |kB| |
   +-----------------------------------+-------------+----------------------+
   | :addr:`1000H` |...| :addr:`17FFH` | :comp:`D16` | niederwertige 2 |kB| |
   +-----------------------------------+-------------+----------------------+
   | :addr:`1800H` |...| :addr:`1FFFH` | :comp:`D17` | niederwertige 2 |kB| |
   +-----------------------------------+-------------+----------------------+
   | :addr:`2000H` |...| :addr:`27FFH` | :comp:`D14` | höherwertige 2 |kB|  |
   +-----------------------------------+-------------+----------------------+
   | :addr:`2800H` |...| :addr:`2FFFH` | :comp:`D15` | höherwertige 2 |kB|  |
   +-----------------------------------+-------------+----------------------+
   | :addr:`3000H` |...| :addr:`37FFH` | :comp:`D16` | höherwertige 2 |kB|  |
   +-----------------------------------+-------------+----------------------+
   | :addr:`3800H` |...| :addr:`3FFFH` | :comp:`D17` | höherwertige 2 |kB|  |
   +-----------------------------------+-------------+----------------------+

Die logische Aufteilung erfolgt je nach Betriebssystem und ist zur Zeit wie folgt festgelegt:

.. .. tabularcolumns:: cL
.. tabularcolumns:: p{0.2\linewidth}p{0.6\linewidth}
.. table:: |PC/M| |U2732| Umbau - Speicherstruktur des Betriebssystems
   :name: kcsystems-mach-pcm-tabelle-2-k2
   :widths: 25, 75
   :class: longtable
   :align: center
   :width: 80%

   +-----------------------------------+---------------------------------------------+
   | Speicherbereich                   | Teil des Betriebssystems                    |
   +===================================+=============================================+
   | :addr:`0000H` |...| :addr:`1FFFH` | |ROM| |BIOS|                                |
   +-----------------------------------+---------------------------------------------+
   | :addr:`2000H` |...| :addr:`27FFH` | |CCP|                                       |
   +-----------------------------------+---------------------------------------------+
   | :addr:`2800H` |...| :addr:`37FFH` | |BDOS|                                      |
   +-----------------------------------+---------------------------------------------+
   | :addr:`3800H` |...| :addr:`3FFFH` | reserviert für Systemerweiterungen (z.B.:   |
   |                                   | Zeichensatz für Grafikerweiterung, |...|).  |
   +-----------------------------------+---------------------------------------------+

.. Local variables:
   coding: utf-8
   mode: text
   mode: rst
   End:
   vim: fileencoding=utf-8 filetype=rst :
