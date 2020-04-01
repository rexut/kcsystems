.. highlight:: none

.. index:: pair: CP/A, Version 3; Diskettenstruktur

Diskettenstruktur
#################

.. index:: triple: CP/A, Version 3; Diskettenstruktur; Standardformat

Standardformat
**************

Es werden sowohl 5\ |oneq|" als auch 8" Disketten mit 128 Bytes je Sektor und 26 Sektoren je Spur unterstützt.

|CP/A| gestattet auf Nicht-Kaltstartdisketten die Nutzung der Systemspuren, mit Systemspuren beginnen sie beim Bürocomputer erst ab Spur 2 (allgemeiner |CP/M| Standard) bzw. Spur 3 (allgemeiner |SCP| Standard) und haben damit eine geringere Kapazität.

.. index:: triple: CP/A, Version 3; Diskettenstruktur; Diskettenformate

Sonstige Diskettenformate
*************************

Sowohl international als auch national haben sich verschiedene Diskettenformate als sogenannte "Hausformate" einzelner |CP/M| kompatibler Betriebssysteme herausgebildet. |CP/A| unterstützt folgende Diskettenformate, die im |BIOS| automatisch bei der erstmaligen Benutzung einer Diskette (LOGIN Bit in Reg. :reg:`E`, Bit 0 bei |BIOS| Entry :z80:`SELDSK`\ =0) erkannt werden (entsprechende Laufwerke vorausgesetzt):

.. tabularcolumns:: l|CCCCC
.. table:: |CP/A| V3(1986) - Unterstützte Diskettenformate
   :widths: 25, 75
   :width: 80%

   +---------+----------+--------+------------+----------------+--------------+
   |         | Sektoren | Sektor | |BDOS|     | Systemspuren   | Kapazität    |
   | Disktyp | pro Spur | Länge  | Blocklänge | / DIR Einträge | (gesamt)     |
   +=========+==========+========+============+================+==============+
   | 5"      | 26       |  128   | 1 |kB|     | 2 / 64         | 123 |kB|     |
   | DD,SS   +----------+--------+------------+----------------+--------------+
   | 40 Sp.  | 26       |  128   | 1 |kB|     | 0 / 64         | 130 |kB|     |
   |         +----------+--------+------------+----------------+--------------+
   |         | 16       |  256   | 2 |kB|     | 3 / 64         | 148 |kB|     |
   |         +----------+--------+------------+----------------+--------------+
   |         |  9       |  512   | 1 |kB|     | 2 / 64         | 171 |kB|     |
   |         +----------+--------+------------+----------------+--------------+
   |         |  9       |  512   | 1 |kB|     | 0 / 64         | 180 |kB|     |
   |         +----------+--------+------------+----------------+--------------+
   |         |  5       | 1024   | 1 |kB|     | 2 / 64         | 190 |kB|     |
   |         +----------+--------+------------+----------------+--------------+
   |         |  5       | 1024   | 1 |kB|     | 0 / 64         | 200 |kB|     |
   +---------+----------+--------+------------+----------------+--------------+
   | 5"      | 26       |  128   | 2 |kB|     | 2 / 128        | 252 |kB| (K) |
   | DD,SS   +----------+--------+------------+----------------+--------------+
   | 80 Sp.  | 26       |  128   | 2 |kB|     | 0 / 128        | 260 |kB|     |
   |         +----------+--------+------------+----------------+--------------+
   |         | 16       |  256   | 2 |kB|     | 3 / 128        | 308 |kB| (K) |
   |         +----------+--------+------------+----------------+--------------+
   |         |  9       |  512   | 2 |kB|     | 2 / 128        | 350 |kB| (*) |
   |         +----------+--------+------------+----------------+--------------+
   |         |  9       |  512   | 2 |kB|     | 0 / 128        | 360 |kB|     |
   |         +----------+--------+------------+----------------+--------------+
   |         |  5       | 1024   | 2 |kB|     | 2 / 128        | 390 |kB| (*) |
   |         +----------+--------+------------+----------------+--------------+
   |         |  5       | 1024   | 2 |kB|     | 0 / 128        | 400 |kB|     |
   +---------+----------+--------+------------+----------------+--------------+
   | 5"      | 26       |  128   | 2 |kB|     | 0 / 128        | 260 |kB| (*) |
   | DD,DS   +----------+--------+------------+----------------+--------------+
   | 40 Sp.  | 16       |  256   | 2 |kB|     | 4 / 128        | 304 |kB| (*) |
   |         +----------+--------+------------+----------------+--------------+
   |         |  9       |  512   | 2 |kB|     | 0 / 128        | 360 |kB| (*) |
   |         +----------+--------+------------+----------------+--------------+
   |         |  5       | 1024   | 2 |kB|     | 0 / 128        | 400 |kB| (*) |
   +---------+----------+--------+------------+----------------+--------------+
   | 5"      | 26       |  128   | 2 |kB|     | 0 / 128        | 520 |kB| (*) |
   | DD,DS   +----------+--------+------------+----------------+--------------+
   | 80 Sp.  | 16       |  256   | 2 |kB|     | 4 / 128        | 624 |kB| (*) |
   |         +----------+--------+------------+----------------+--------------+
   |         |  9       |  512   | 2 |kB|     | 0 / 128        | 720 |kB| (*) |
   |         +----------+--------+------------+----------------+--------------+
   |         |  5       | 1024   | 2 |kB|     | 0 / 192        | 800 |kB| (*) |
   +---------+----------+--------+------------+----------------+--------------+
   | 8"      | 26       |  128   | 1 |kB|     | 2 / 64         | 243 |kB|     |
   | SD,SS   +----------+--------+------------+----------------+--------------+
   |         | 26       |  128   | 1 |kB|     | 0 / 64         | 250 |kB|     |
   |         +----------+--------+------------+----------------+--------------+
   |         | 16       |  256   | 2 |kB|     | 3 / 64         | 296 |kB|     |
   |         +----------+--------+------------+----------------+--------------+
   |         |  9       |  512   | 2 |kB|     | 2 / 128        | 336 |kB|     |
   |         +----------+--------+------------+----------------+--------------+
   |         |  9       |  512   | 2 |kB|     | 0 / 128        | 346 |kB|     |
   |         +----------+--------+------------+----------------+--------------+
   |         |  4       | 1024   | 2 |kB|     | 3 / 64         | 296 |kB|     |
   |         +----------+--------+------------+----------------+--------------+
   |         |  4       | 1024   | 2 |kB|     | 0 / 64         | 308 |kB|     |
   +---------+----------+--------+------------+----------------+--------------+

(*) Diese Variante wird vom |CP/A| Kaltstartsystem für den Bürocomputer in den Systemspuren nicht unterstützt, da es vom Anwender nicht konfiguriert werden kann und ein eindeutiges (automatisches) Unterscheiden von 40 und 80 Track Laufwerken für die Bestimmung der |BDOS| Blockgröße (1 |kB| bei 40, 2 |kB| bei 80 Track Laufwerken) nur mit größerem Aufwand möglich wäre. Daher müssen Kaltstartdisketten für 80 Track Laufwerke ein mit (K) gekennzeichnetes Format verwenden.

Die Angabe der Kapazität erfolgt einschließlich der Verzeichnisgröße von 2 |kB| (64 Directory Einträge) bzw. 4 |kB| (128 Directory Einträge) bzw. 6 |kB| (192 Directory Einträge). Haben die Disketten weniger Directory Einträge, so ist Lesen ohne Einschränkung und auch Schreiben möglich, jedoch wird i.a. nicht die volle Diskettenkapazität nutzbar, da das erste File auf der Diskette als Directory interpretiert wird.

Bei Nutzung von DS Formaten wird die Rückseite in den Steuerblöcken des |BIOS| als extra Spur behandelt, daher haben diese Disketten beim Protokollieren des Formates doppelt soviel logische Spuren wie physische.

Unter |CP/A| haben Systemspuren (daran erkannt, dass der dezimale Wert des Bytes 0 in Spur 0, Sektor 1 nicht :code:`E5H`, aber größer als :code:`31H` ist - der größte mögliche Nutzer in einem evtl. dort befindlichen |CP/M| Directory Eintrag ist :code:`31H`!) keine weitere Bedeutung und dienen nur zum Erkennen des Formates. |CP/A| legt seine Systemspuren für den Bürocomputer grundsätzlich im Format 26 |*| 128 an (leider notwendig wegen der Kaltstart Version 0.6 auf einigen älteren |A51xx| Geräten), auch wenn die restlichen Spuren ein anderes Format haben (i.a. wird man für 40 Track, SS das 190 |kB| Format benutzen).

Bei |SCP| Disketten (Sektorlänge 256) werden unabhängig vom Inhalt der 0. Spur immer Systemspuren angenommen. Es können u.a. damit direkt Disketten bearbeitet werden, die unter dem Robotron Betriebssystem |SCP| erzeugt wurden bzw. weiterverarbeitet werden sollen.

Die angegebenen Diskettenformate werden durch das |CP/A| Dienstprogramm :program:`FORMAT` erzeugt. Defekte Spuren werden übergangen. Mit Hilfe des |CP/M| Dienstprogramms :program:`POWER` kann dann eine Dummydatei erzeugt werden, in der alle fehlerhaften Sektoren zu einer Pseudodatei zusammengefasst werden, womit diese für die weitere Nutzung ausgeschlossen sind.

Eine neu formatierte Diskette, zukünftige Systemdiskette besitzt zunächst keine Systemspuren.

Beim Bürocomputer können diese mit Hilfe des |CP/M| Dienstprogramms :program:`SYSGEN` oder des |CP/A| Dienstprogramms :program:`FORMAT` von einer bereits vorhandenen Kaltstartdiskette übertragen werden.

Beim |PC1715| geschieht das Anlegen einer neuen Systemdiskette auf eine formatierte und leere Diskette durch Kopieren von :file:`@OS.COM` von Laufwerk :file:`A` nach :file:`B` durch das Kommando::

   CPA1715G B:

Die allgemeine Aufrufform von :program:`CPA1715G` ist

   :samp:`CPA1715G z: quellfile`
   
wobei:

   .. option:: z:

      das Ziellaufwerk und
   
   .. option:: quellfile

      der Name des Quellsystemfiles ist
   
z.B.:

   :samp:`CPA1715G B: C:@OS54K.COM`.
   
Auf der neuen Systemdiskette ist der Filename des Systems unabhängig vom Quellnamen immer :file:`@OS.COM`. Bei einer späteren Modifizierung des Files :file:`@OS.COM` darf sich beim |PC1715| die Länge nicht ändern, andernfalls muss die gesamte Systemdiskette neu angelegt werden!

Danach können sowohl beim Bürocomputer als auch beim |PC1715| auf die angelegte Kaltstartdiskette weitere Programme kopiert werden (z.B. :program:`FORMAT`, :program:`ZSID`, :program:`POWER`, ...).

Einige Formate benutzen einen nichtkonstanten physischen Sektorabstand, der der Standardpuffergröße von 1 |kB| (es werden ja bei Sektorlängen <1 |kB| i.a. mehrere aufeinanderfolgende Sektoren gepuffert) sowie der Laufwerks- und Verarbeitungsgeschwindigkeit angepasst ist und das Lesen bzw. Schreiben einer Spur mit weniger Umdrehungen erlaubt. Bei Formaten mit 26 Sektoren zu 128 Bytes wird der in |CP/M| übliche logische Sektorversatz von 6 angewendet.

Neben dem Formatieren von Disketten erlaubt das |CP/A| Dienstprogramm :program:`FORMAT[P]` auch das Kopieren von Disketten. Die Quelldisketten können dabei einen beliebigen physischen (auch nichtkonstanten) Sektorabstand haben, der sich insbesondere von dem der Zieldiskette unterscheiden kann. Damit ist z.B. durch Kopieren bereits vorhandener Disketten mit konstantem physischen Sektorabstand nachträglich eine Beschleunigung des Zugriffs zu erreichen.

Für spezielle Untersuchungen kann mit Hilfe von :program:`FORMAT` das Diskettenformat unabhängig von den standardmäßig vorhandenen definiert werden.

Ein Übertragen von Files zwischen Disketten unterschiedlichen Formats geschieht unter |CP/A| i.a. problemlos durch die automatische Formaterkennung des beim Formatieren festgelegten Diskettenformates. Dies trifft auch für 80 Track, DS Laufwerke des |PC1715| zu; es können hiermit auch 40 Track, SS Disketten vom Bürocomputer gelesen und geschrieben werden (indem nur jede zweite Spur benutzt wird). Treten dabei Diskettenfehler auf, so sollte man den Vorgang auf einem anderen Laufwerk wiederholen, da sich auf Grund der engen Toleranzen bei einer 80 spurigen Benutzung einer Diskette geringe Justierfehler der Laufwerke störend bemerkbar machen können. Im Extremfall sind auch die Disketten zu wechseln, wenn sie schon auf sehr vielen unterschiedlichen Laufwerken beschrieben wurden.

.. index:: triple: CP/A, Version 3; Diskettenstruktur; Fehlermeldungen

Fehlermeldungen
***************

Bei aufgetretenen Fehlern bei der Arbeit mit Disketten werden vom |BIOS| nach erfolgloser Fehlerkorrektur unabhängig von einer evtl. folgenden |BDOS| Meldung folgende Fehler detailliert ausgewiesen, um einen Laufwerks- oder Datenträgerdefekt frühzeitig und genauer zu lokalisieren:

.. tabularcolumns:: cL
.. table:: |CP/A| V3(1986) - Kurzkennzeichen von Disketten-Fehlermeldungen
   :widths: 25, 75
   :width: 80%

   +-----------------+----------------------------------------------+
   | Kurzkennzeichen | Bedeutung                                    |
   +=================+==============================================+
   | C               | CRC Error (Daten nicht lesbar)               |
   +-----------------+----------------------------------------------+
   | D               | Device Error (Gerät existiert nicht)         |
   +-----------------+----------------------------------------------+
   | F               | Fault Adapter (zu langsame Datenübertragung) |
   +-----------------+----------------------------------------------+
   | L               | Length Error (unzulässiges Spurformat)       |
   +-----------------+----------------------------------------------+
   | S               | Sector not found (meist falsches Format)     |
   +-----------------+----------------------------------------------+
   | T               | Track not found (Spur nicht auffindbar)      |
   +-----------------+----------------------------------------------+
   | U               | Undefined (keine Adressmarken auffindbar)    |
   +-----------------+----------------------------------------------+
   | W               | Write protected (schreibgeschützt)           |
   +-----------------+----------------------------------------------+

Die Fehlermeldung lautet beim Bürocomputer::

   x BIOS Disk x-Error "y", track (hex):zz

wobei :console:`x` = R für Read (Lesen) und :console:`x` = W für Write (Schreiben), :console:`y` das oben angegebene Kurzkennzeichen und :console:`zz` die hexadezimale physikalische Spurnummer, bei der der Fehler auftrat, angeben.

Beim |PC1715| lautet die Fehlermeldung (stark verkürzt, da nicht mehr Platz in der Statuszeile)::

   x xy;T,S,Se=zz,d,ss

wobei :console:`x`, :console:`y`, :console:`zz` die gleiche Bedeutung wie beim Bürocomputer haben, :console:`d` gibt die Diskettenseite (0 o. 1) und :console:`ss` den physischen Sektor an.

.. Local variables:
   coding: utf-8
   mode: text
   mode: rst
   End:
   vim: fileencoding=utf-8 filetype=rst :
