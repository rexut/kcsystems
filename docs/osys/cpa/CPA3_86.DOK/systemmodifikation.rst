.. highlight:: none

.. index:: pair: CP/A, Version 3; Systemmodifikation

Systemmodifikation
##################

Eine Modifikation des Systems ist leicht mittels :program:`ZSID` oder gleichwertigen Debuggern möglich::

   ZSID @OS.COM
   ...
   ...
   ^C
   SAVE xx @OS.COM
   Kaltstart

Ist eine Neuübersetzung erforderlich, so läuft die Änderung wie folgt ab (:file:`s:` sei das Laufwerk mit Systemprogrammen):

a) für Bürocomputer

   - Modifikation des |BIOS| Quelltextes :file:`BIOS.MAC`
   - Assemblierung der |BIOS| Quellen::

      s:M80 BIOS.ERL=BIOS

   - Link |BIOS| mit BAS, |CCP| und |BDOS|::

      s:LINKMT @OS=CPABAS,CCP,BDOS,BIOS/P:xxxx

   - Kaltstart

b) für |PC1715|

   - Modifikation des |BIOS| Quelltextes :file:`BIOP.MAC`
   - Assemblierung der |BIOS| Quellen::

      s:M80 BIOP.ERL=BIOP

   - Link |BIOS| mit BAS, |CCP| und |BDOS|::

      s:LINKMT @OS=CPPBAS,CCP,BDOS,BIOP/P:xxxx

   - Kaltstart

.. option:: xxxx

   Die Basisadresse aller Teile, hexadezimal. Die Adresse wird vom
   Assembler ausgegeben!

:program:`LINKMT` ist der zum Pascal Paket gehörige Linker und erfordert den Filetyp :mimetype:`.ERL` für die Link-Eingaben. Dieser Linker wird hier benutzt, weil er er im Gegensatz zu :program:`L80` bei Programmadressen größer :addr:`100H` keine Füllbytes erzeugt.

Die Basisadresse :option:`xxxx` ist wegen des vorgelagerten Records CPxBAS um :addr:`80H` kleiner als die gewünschte Adresse vom |CCP|.

Das |CCP| wird beim Warmstart aus einem Hauptspeicherbereich (im |BIOS|) kopiert, das |BDOS| wird in der Regel nicht durch Anwendersoftware zerstört, da es die gesamte Logik für die Arbeit mit Disketten enthält. Dadurch entfällt beim Warmstart jegliche Notwendigkeit des Ladens, wodurch dieser beschleunigt wird und Systemspuren nur auf der Kaltstartdiskette erforderlich sind, auf allen anderen können sie mit zur Datenspeicherung benutzt werden (0 Systemspuren).

Für spezielle Anforderungen an einen großen |TPA| Bereich existieren auch Varianten zum Nachladen des |CCP| bei Warmstart ohne |CCP| Kopie im |BIOS|.

Hat ein Anwenderprogramm auch das |BDOS| zerstört (|TPA| dann um :addr:`0E00H` - d.h. 3,5 |kB| - größer), so muss es den Kaltstarteingang des |BIOS| benutzen. Hierdurch wird ein Kaltstartvorgang vom |BIOS| simuliert, d.h. es wird wie bei einem ersten Kaltstart eine Systemdiskette in den Laufwerken gesucht.

Die Länge des Gesamtsystems hängt sehr stark vom gewünschten Leistungsumfang ab, für Spezialzwecke können auch "Miniversionen" mit ca. 7 |kB| |BIOS| (ca. 53,5 |kB| |TPA|) generiert werden.

.. Local variables:
   coding: utf-8
   mode: text
   mode: rst
   End:
   vim: fileencoding=utf-8 filetype=rst :
