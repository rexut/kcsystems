.. index:: pair: CP/A, Version 2; Kaltstart

Kaltstart des Systems
#####################

Das Betriebssystem befindet sich auf einer Kaltstartdiskette als File mit dem
(festen) Namen :file:`@OS.COM`. Die Kaltstartdiskette besitzt neben zwei
speziellen Systemspuren auf Spur 0 und 1 ein Bibliotheksverzeichnis ab Spur 2.
Sie kann nach dem Kaltstart wie andere Disketten benutzt werden. In der Regel
enthält sie Standardprogramme und das Abrechnungssystem.

Die Systemdatei :file:`@OS.COM` kann mit :program:`PIP` kopiert, mittels
:program:`ZSID` und :program:`SAVE` modifiziert worden sein oder auch direkt
eine Link-Ausgabe darstellen. Sie wird wie eine normale Datei behandelt und
kann auf der Diskette ab einer beliebigen Stelle (u.U. auch gestreut)
gespeichert sein.

Der Kaltstart läuft in folgenden Etappen ab:

1) Suchen eines Laufwerks mit Kaltstartdiskette (beginnend bei
   Laufwerk :file:`A`),
2) Laden eines Minisystems (ab :addr:`400H`) von den Systemspuren,
3) Laden des Files :file:`@OS.COM` entsprechend seiner Länge, wobei im Wort
   :addr:`7EH` des ersten Records (immer ab :addr:`100H` geladen) die
   Ladeadresse des restlichen Teils vermerkt ist,
4) Ansprung des geladenen Systems auf :addr:`100H`.

Damit ist auf einfache Art auch der Kaltstart anderer Anwendersysteme möglich,
wenn diese unter dem Namen :file:`@OS.COM` abgespeichert sind!

Nach dem Kaltstart wird automatisch das Programm :program:`ACCOUNT`
(Abrechnungssystem) von der Kaltstartdiskette geladen und ausgeführt. Bei der
Systemgenerierung kann jedoch auch ein anderes Kommando (auch ein leeres) als
Standardprogramm vereinbart werden. Das Laden dieses Programms kann nach einem
Kaltstart infolge eines Systemzusammenbruchs, wo eine Neuanmeldung durch
:program:`ACCOUNT` nicht sinnvoll ist, durch Betätigen der :kbd:`STOP` und
der :kbd:`^C` Taste (siehe
:ref:`osys/cpa/CPA2_85.DOK/besonderheiten-des-bios:Belegung von Sondertasten`)
unterdrückt werden.

.. Local variables:
   coding: utf-8
   mode: text
   mode: rst
   End:
   vim: fileencoding=utf-8 filetype=rst :
