.. highlight:: none

.. index:: pair: CP/A, Version 2; Systemmodifikation

Systemmodifikation
##################

Eine Modifikation des Systems ist leicht mittels :program:`ZSID` möglich::

   ZSID @OS.COM
   ...
   ...
   ^C
   SAVE xx @OS.COM
   Kaltstart

Ist eine Neuübersetzung erforderlich, so läuft die Änderung wie folgt ab (:file:`s:` sei das Laufwerk mit Systemprogrammen):

- Modifikation des |BIOS| Quelltextes :file:`BIOS.MAC`
- Assemblierung der |BIOS| Quellen::

     s:M80 BIOS.ERL=BIOS

- Link |BIOS| mit BAS, |CCP| und |BDOS|::

     s:LINKMT @OS=CPABAS,BDOS,CCP,BIOS/P:xxxx

  .. option:: xxxx

     Die Basisadresse aller Teile, hexadezimal.

- Kaltstart

:program:`LINKMT` ist der zum Pascal Paket gehörige Linker und erfordert den Filetyp :mimetype:`.ERL` für die Link-Eingaben. Dieser Linker wird hier benutzt, weil er im Gegensatz zu :program:`L80` bei Programmadressen größer :addr:`100H` keine Füllbytes erzeugt.

Die Basisadresse :option:`xxxx` ist wegen des vorgelagerten Records CPABAS um :addr:`80H` kleiner als die gewünschte Adresse von |BDOS|. Für die Standardlänge des |BIOS| ist :option:`xxxx`\ =C680, :option:`xxxx` wird bei der Assemblierung protokolliert.

Längen der einzelnen Komponenten:

.. tabularcolumns:: lrL
.. table:: |CP/A| V2(1985) - Längen der einzelnen Komponenten
   :widths: 10, 15, 75
   :width: 80%

   +--------+--------------+-----------------------+
   | Name   | Länge (hex.) | Länge (|kB|)          |
   +========+==============+=======================+
   | CPABAS |           80 |                       |
   +--------+--------------+-----------------------+
   | |BDOS| |          E00 | 3,5                   |
   +--------+--------------+-----------------------+
   | |CCP|  |          800 | 2                     |
   +--------+--------------+-----------------------+
   | |BIOS| |     ca. 2300 | 8,75 (einschl. 2 |kB| |
   |        |              | Bildschirmpuffer und  |
   |        |              | 1K Diskpuffer)        |
   +--------+--------------+-----------------------+

Die Reihenfolge |BDOS| vor |CCP| wurde bewusst gewählt, da so das |CCP| nicht durch Anwendersoftware zerstört wird und daher bei einem Warmstart nicht neu geladen werden muss. Dadurch entfällt beim Warmstart jegliche Notwendigkeit des Ladens, wodurch dieser beschleunigt wird und Systemspuren nur auf der Kaltstartdiskette erforderlich sind, auf allen anderen können sie mit zur Datenspeicherung benutzt werden (0 Systemspuren).

.. Local variables:
   coding: utf-8
   mode: text
   mode: rst
   End:
   vim: fileencoding=utf-8 filetype=rst :
