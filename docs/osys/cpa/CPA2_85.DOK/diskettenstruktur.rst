.. index:: pair: CP/A, Version 2; Diskettenstruktur

Diskettenstruktur
#################

.. index:: triple: CP/A, Version 2; Diskettenstruktur; Standardformat

Standardformat
**************

Es werden sowohl 5\ |oneq|" als auch 8" Disketten mit 128 Bytes je Sektor, d.h. 26 Sektoren je Spur unterstützt.

|CP/A| gestattet auf Nicht-Kaltstartdisketten die Nutzung der Systemspuren, mit Systemspuren beginnen sie erst ab Spur 2 (allgemeiner |CP/M| Standard) bzw. Spur 3 (allgemeiner |SCP| Standard) und haben damit eine geringere Kapazität.

.. index:: triple: CP/A, Version 2; Diskettenstruktur; Diskettenformate

Sonstige Diskettenformate
*************************

Sowohl international als auch national haben sich verschiedene Diskettenformate als sogenannte "Hausformate" einzelner |CP/M| kompatibler Betriebssysteme herausgebildet. |CP/A| unterstützt folgende Diskettenformate, die im |BIOS| automatisch bei der erstmaligen Benutzung einer Diskette (LOGIN Bit in Reg. :reg:`E`, Bit 0 bei |BIOS| Entry :z80:`SELDSK`\ =0) erkannt werden:

.. tabularcolumns:: l|CCCCC
.. table:: |CP/A| V2(1985) - Unterstützte Diskettenformate
   :widths: 25, 75
   :width: 80%

   +---------+----------+--------+-------+--------+-----------+
   |         | Sektoren | Sektor | Block | System |           |
   | Typ     | / Spur   | Länge  | Länge | Spuren | Kapazität |
   +=========+==========+========+=======+========+===========+
   | 5"      | 26       |  128   | 1 |kB|| 2      | 123 |kB|  |
   |         +----------+--------+-------+--------+-----------+
   |         | 26       |  128   | 1 |kB|| 0      | 130 |kB|  |
   |         +----------+--------+-------+--------+-----------+
   |         | 16       |  256   | 2 |kB|| 3      | 146 |kB|  |
   |         +----------+--------+-------+--------+-----------+
   |         | 16       |  256   | 2 |kB|| 0      | 158 |kB|  |
   |         +----------+--------+-------+--------+-----------+
   |         |  5       | 1024   | 1 |kB|| 2      | 193 |kB|  |
   |         +----------+--------+-------+--------+-----------+
   |         |  5       | 1024   | 1 |kB|| 0      | 200 |kB|  |
   +---------+----------+--------+-------+--------+-----------+
   | 8"      | 26       |  128   | 1 |kB|| 2      | 243 |kB|  |
   |         +----------+--------+-------+--------+-----------+
   |         | 26       |  128   | 1 |kB|| 0      | 250 |kB|  |
   |         +----------+--------+-------+--------+-----------+
   |         | 16       |  256   | 2 |kB|| 3      | 296 |kB|  |
   |         +----------+--------+-------+--------+-----------+
   |         | 16       |  256   | 2 |kB|| 0      | 308 |kB|  |
   |         +----------+--------+-------+--------+-----------+
   |         |  4       | 1024   | 2 |kB|| 3      | 296 |kB|  |
   |         +----------+--------+-------+--------+-----------+
   |         |  4       | 1024   | 2 |kB|| 0      | 308 |kB|  |
   +---------+----------+--------+-------+--------+-----------+

Die Angabe der Kapazität erfolgt einschließlich von jeweils 2 |kB| Verzeichnis.

Es können u.a. damit direkt Disketten bearbeitet werden, die unter dem Robotron Betriebssystem |SCP| erzeugt wurden bzw. weiterverarbeitet werden sollen. Unter |CP/A| haben dabei Systemspuren (erkannt an 'S'(YL) in Spur 0, Sektor 1) keine weitere Bedeutung und dienen nur zum Erkennen des Formates. Werden sie explizit gelesen oder geschrieben (nur durch spezielle Dienstprogramme für physischen Transfer möglich), so wird ein Spurformat von 26 |*| 128 für die Systemspuren angenommen.

Die angegebenen Diskettenformate werden durch das |CP/A| Dienstprogramm :program:`FORMAT` erzeugt. Defekte Spuren können übergangen werden, indem mit dem Formatieren bei der nachfolgenden Spur neu begonnen wird. Mit Hilfe des |CP/M| Dienstprogramms :program:`POWER` kann dann eine Dummydatei erzeugt werden, in der alle fehlerhaften Sektoren zu einer Pseudodatei zusammengefasst werden, womit diese für die weitere Nutzung ausgeschlossen sind.

Eine neu formatierte Diskette besitzt zunächst keine Systemspuren. Mit Hilfe des |CP/M| Dienstprogramms :program:`SYSGEN` können diese von einer bereits vorhandenen Kaltstartdiskette kopiert und danach mit :program:`PIP` weitere Programme kopiert werden (z.B. :program:`FORMAT`, :program:`ZSID`, :program:`POWER`, ...).

Neben dem Neuformatieren von Disketten gestattet :program:`FORMAT` auch das (u.U. teilweise) physische Kopieren von Disketten.

.. index:: triple: CP/A, Version 2; Diskettenstruktur; Fehlermeldungen

Bei aufgetretenen Fehlern bei der Arbeit mit Disketten werden vom |BIOS| nach erfolgloser Fehlerkorrektur unabhängig von einer evtl. folgenden |BDOS| Meldung folgende Fehler detailliert ausgewiesen, um einen Laufwerks- oder Datenträgerdefekt frühzeitig und genau zu lokalisieren:

.. tabularcolumns:: cL
.. table:: |CP/A| V2(1985) - Kurzkennzeichen von Disketten-Fehlermeldungen
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
   | W               | Write protected (schreibgeschützt)           |
   +-----------------+----------------------------------------------+

.. Local variables:
   coding: utf-8
   mode: text
   mode: rst
   End:
   vim: fileencoding=utf-8 filetype=rst :
