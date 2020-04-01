.. kcsystems documentation master file, created by
   sphinx-quickstart on Tue Oct  7 11:43:41 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. index:: single: PC/M
   :name: kcsystems-mach-pcm-home
.. index:: pair: PC/M; Machine
.. index:: pair: PC/M; Computer

##################
|mach_pcm_project|
##################

.. only:: html

   .. sectionauthor:: |dm_mach_pcm_contact_obfuscated|

.. only:: latex or man or texinfo or text

   .. sectionauthor:: |dm_mach_pcm_contact_plain_text|

.. ...........................................................................

.. include:: docsummary.rsti

.. only:: latex

   .. include:: doclegal.rsti
   .. include:: docversions.rsti

.. raw:: latex

   \cleardoublepage\phantomsection

.. ...........................................................................

This is a collection of the original manuscripts written in German by
|amu|, |hma| and |ube| with working state of August 30, 1988 until 1990.
They were taken without any changes but some formal corrections,
enhancements and merges with the series of articles as published
by the German journal |Funkamateur| :cite:`mugler8891pcm`.

The original manuscripts [#f1]_ [#f2]_ in a historical WordStar 4 format were
published on September 29, 2008 by the German social club `KC-Club`_
in download archive `Rubrik 26: Dokumentationen für CP/M und MicroDOS`_.
Additional information, improvements and modification instructions [#f3]_
were distributed on July 13, 2014 by the German web page
`Lagerplatz von Li-Pro.Net`_ with the system disks for |PC/M| **Version 3.0**,
archived on April 15, 1990 by |slz| as `PC/M Floppy Disk Images`_.

.. .. tabularcolumns:: p{0.25\linewidth}p{0.17\linewidth}p{0.23\linewidth}p{0.35\linewidth}
.. tabularcolumns:: p{0.17\linewidth}p{0.13\linewidth}p{0.19\linewidth}p{0.39\linewidth}
.. table:: |PC/M| - Original manuscripts and documents about the base system
   :name: kcsystems-mach-pcm-origins
   :widths: 25, 20, 20, 35
   :class: longtable
   :align: center
   :width: 100%

   +------------------+-------------+---------+-------------------------------------+
   | File             | Date        | Authors | Document Title                      |
   +==================+=============+=========+=====================================+
   | `PC_M1.DOC`_     | 16-Dec-1986 | |amu|,  | Der PC/M Computer, Hardware         |
   |                  |             | |hma|   | Bearbeitungsstand: 30-Aug-1988      |
   +------------------+-------------+---------+-------------------------------------+
   | `PC_M2.DOC`_     | 16-Dec-1986 | |amu|,  | Der PC/M Computer, Software         |
   |                  |             | |hma|   | Bearbeitungsstand: 30-Aug-1988      |
   +------------------+-------------+---------+-------------------------------------+
   | `PC_M3.DOC`_     | 16-Dec-1986 | |amu|,  | Der PC/M Computer, Tabellen, Listen |
   |                  |             | |hma|   | Bearbeitungsstand: 30-Aug-1988      |
   +------------------+-------------+---------+-------------------------------------+
   | `PC_M4.DOC`_     | 16-Dec-1986 | |amu|,  | Der PC/M Computer, Hinweise         |
   |                  |             | |hma|   | Bearbeitungsstand: 30-Aug-1988      |
   +------------------+-------------+---------+-------------------------------------+
   | `PC_MBUSK.DOC`_  |             | |amu|,  | K1520-Adapter für den PC/M-Computer |
   |                  |             | |hma|   |                                     |
   +------------------+-------------+---------+-------------------------------------+
   | `PC_MEPT.DOC`_   | 17-Sep-1988 | |amu|,  | Intelligente Tastatur am PC/M       |
   |                  |             | |hma|   |                                     |
   +------------------+-------------+---------+-------------------------------------+
   | `PC_M7659.DOC`_  | 09-Jan-1989 | |amu|,  | K7659 - Tastaturanschluss für den   |
   |                  |             | |hma|   | PC/M-Computer                       |
   +------------------+-------------+---------+-------------------------------------+
   | `IFSSV24.DOC`_   | 20-Jul-1989 | |ube|   | Beschreibung Wandlerbaustein        |
   |                  |             |         | IFSS auf V.24                       |
   +------------------+-------------+---------+-------------------------------------+
   | `INTERROR.PCM`_  |             | |dramu| | Probleme im Interrupt-Betrieb des   |
   |                  |             |         | PC/M                                |
   +------------------+-------------+---------+-------------------------------------+
   | `UMBA2732.PCM`_  |             | |dramu| | Umbau und Einsatz von U2732 im      |
   |                  |             |         | PC/M-Computer                       |
   +------------------+-------------+---------+-------------------------------------+
   | `SYSINFO.PCM`_   | 02-Mar-1990 | |dramu| | Information zum Umgang mit den      |
   |                  |             |         | Dateien (V3.XX)                     |
   +------------------+-------------+---------+-------------------------------------+
   | `BESTLPL.PCM`_   | 05-Apr-1990 | |dramu| | Bestellung Leiterplatten für den    |
   |                  |             |         | PC/M-Computer                       |
   +------------------+-------------+---------+-------------------------------------+
   | `BESTSOFT.PCM`_  | 15-Apr-1990 | |dramu| | Bestellung Software für den         |
   |                  |             |         | PC/M-Computer                       |
   +------------------+-------------+---------+-------------------------------------+
   | `LESEDAS.PCM`_   | 15-Apr-1990 | |dramu| | Floppy-Betriebssystem für den       |
   |                  |             |         | PC/M-Computer                       |
   +------------------+-------------+---------+-------------------------------------+

.. ...........................................................................

.. index:: pair: PC/M; Baugruppenverzeichnis
.. index:: pair: PC/M; Hardware Assemblies
.. index:: pair: PC/M; Hardware Components

.. rubric:: Hardware Assemblies and Components

.. tabs::

   .. tab:: |FA 3/88-05|

      |FA038805|

      .. tabs::

         .. tab:: Block Diagram

            * |FA038805_BG|

         .. tab:: Schematic

            * |FA038805_SP1|
            * |FA038805_SP2|

         .. tab:: Layout

            * |FA038805_LS|
            * |FA038805_BS|

         .. tab:: Assembly

            * |FA038805_BP|
            * |FA038805_SL|
            * |FA038805_KP|

              * |PC_M_T3_N|: |PC_M_T3_T|
              * |PC_M_T4_N|: |PC_M_T4_T|

                * |PC_M_TA2_N|: |PC_M_TA2_T|

              * |PC_M_T5_N|: |PC_M_T5_T|

                * |PC_M_TA3_N|: |PC_M_TA3_T|

         .. tab:: Software

            * |FA038805_SW1|
            * |FA038805_SW2|
            * |FA038805_SW3|
            * |FA038805_SW4|
            * |FA038805_SW5|
            * |FA038805_SW6|

         .. tab:: Supplementaries

            * |FA038805_ZD1|

              * |PC_M_T1_N|: |PC_M_T1_T|

            * |FA038805_ZD2|

              * |PC_M_T2_N|: |PC_M_T2_T|

            * |FA038805_ZD3|
            * |FA038805_ZD4|
            * |FA038805_ZD5|
            * |FA038805_K1|
            * |FA038805_K2|

              * |PC_M_T1K2_N|: |PC_M_T1K2_T|
              * |PC_M_T2K2_N|: |PC_M_T2K2_T|

            * |FA038805_K3|

              * |PC_M_B251K3_N|: |PC_M_B251K3_T|
              * |PC_M_T1K3_N|: |PC_M_T1K3_T|


   .. tab:: |FA 4/88-04|

      |FA048804|

      .. tabs::

         .. tab:: Layout

            * |FA048804_LS|
            * |FA048804_BS|

   .. tab:: |FA 5/88-04|

      |FA058804|

      .. tabs::

         .. tab:: Block Diagram

            * |FA058804_BG|

         .. tab:: Schematic

            * |FA058804_SP|
            * |FA058804_SPK1|

         .. tab:: Layout

            * |FA058804_LS|
            * |FA058804_BS|

         .. tab:: Assembly

            * |FA058804_BP|
            * |FA058804_SL|

         .. tab:: Software

            * |FA058804_SW|

         .. tab:: Supplementaries

            * |FA058804_ZD1|
            * |FA058804_ZD2|
            * |FA058804_ZD3|
            * |FA058804_ZD4|
            * |FA058804_K1|

   .. tab:: |FA 6/88-03|

      |FA068803|

      .. tabs::

         .. tab:: Block Diagram

            * |FA068803_TM|
            * |FA068803_BG|

         .. tab:: Schematic

            * |FA068803_SP|

         .. tab:: Layout

            * |FA068803_LS|
            * |FA068803_BS|

         .. tab:: Assembly

            * |FA068803_BP|
            * |FA068803_SL|

         .. tab:: Supplementaries

            * |FA068803_ZD1|

   .. tab:: |FA 7/88-05|

      |FA078805|

      .. tabs::

         .. tab:: Schematic

            * |FA078805_SP|

         .. tab:: Layout

            * |FA078805_LS|

         .. tab:: Assembly

            * |FA078805_BP|
            * |FA078805_SL|

   .. tab:: |KMBG Anett IS2|

      |KMBGANETTIS2|

      .. tabs::

         .. tab:: Schematic

            * |KMBGANETTIS2_SP|

   .. tab:: |FA 11/88-K1520VTCP|

      |FA1188K1520VTCP|

      .. tabs::

         .. tab:: Schematic

            * |FA1188K1520VTCP_SP|

         .. tab:: Software

            * |FA1188K1520VTCP_SW|

   .. tab:: |FA 11/88-V24IO|

      |FA1188V24IO|

      .. tabs::

         .. tab:: Schematic

            * |FA1188V24IO_SP|

   .. tab:: |FA 10/89-01|

      |FA108901|

      .. tabs::

         .. tab:: Schematic

            * |FA108901_BG|
            * |FA108901_SP|

         .. tab:: Layout

            * |FA108901_LS|
            * |FA108901_BS|

         .. tab:: Assembly

            * |FA108901_BP|

   .. tab:: |EPT/EPR2TUK|

      |EPTEPR2TUK|

      .. tabs::

         .. tab:: Schematic

            * |EPTEPR2TUK_SP|

         .. tab:: Layout

            * |EPTEPR2TUK_LS|
            * |EPTEPR2TUK_BS|

         .. tab:: Assembly

            * |EPTEPR2TUK_BP|

   .. tab:: |FA 5/90-01|

      |FA059001|

      .. tabs::

         .. tab:: Schematic

            * |FA059001_TM|
            * |FA059001_SP|

         .. tab:: Layout

            * |FA059001_LS|
            * |FA059001_BS|

         .. tab:: Assembly

            * |FA059001_BP|

         .. tab:: Software

            * |FA059001_SW|

.. ...........................................................................

.. toctree::
   :caption: Hardware und Software
   :maxdepth: 3

   PC_M1.DOC/der-pcm-computer
   PC_M1.DOC/die-zentrale-platine
   PC_M1.DOC/die-peripherie
   PC_M1.DOC/inbetriebnahme
   PC_M2.DOC/das-betriebssystem
   PC_M2.DOC/zusammenfassung

.. toctree::
   :caption: Tabellen und Listen
   :maxdepth: 3

   PC_M3.DOC/systemzellen-und-sprungvektoren
   PC_M3.DOC/io-adressen
   PC_M3.DOC/stuecklisten
   PC_M3.DOC/steckverbinder
   PC_M3.DOC/abbildungsverzeichnis
   PC_M3.DOC/literaturverzeichnis

.. toctree::
   :caption: Hinweise
   :maxdepth: 3

   PC_M4.DOC/hinweise-und-ergaenzungen
   PC_M4.DOC/hinweise-und-korrekturen
   PC_M4.DOC/abbildungsverzeichnis
   INTERROR.PCM/probleme-im-interrupt-betrieb
   UMBA2732.PCM/einsatz-von-u2732
   IFSSV24.DOC/ifss-auf-v24

.. toctree::
   :caption: Erweiterungen
   :maxdepth: 3

   PC_MBUSK.DOC/k1520-adapter
   PC_MEPT.DOC/intelligente-tastatur
   PC_M7659.DOC/k7659-tastaturanschluss
   LESEDAS.PCM/floppy-betriebssystem
   SYSINFO.PCM/information-zum-umgang-mit-den-dateien

.. ...........................................................................

.. rubric:: Footnotes

.. [#f1] Local copy of the original manuscript:
   |PC_M1.DOC|, |PC_M2.DOC|, |PC_M3.DOC|, |PC_M4.DOC|

.. [#f2] Local copy of all original manuscripts:
   |PC_MBUSK.DOC|, |PC_MEPT.DOC|, |PC_M7659.DOC|

.. [#f3] Local copy of additional information and instructions:
   |IFSSV24.DOC|, |INTERROR.PCM|, |UMBA2732.PCM|,
   |LESEDAS.PCM|, |SYSINFO.PCM|, |BESTLPL.PCM|, |BESTSOFT.PCM|

.. ...........................................................................

.. only:: man or texinfo or text

   .. include:: doclegal.rsti

.. only:: html or man or texinfo or text

   .. include:: docversions.rsti

.. Local variables:
   coding: utf-8
   mode: text
   mode: rst
   End:
   vim: fileencoding=utf-8 filetype=rst :
