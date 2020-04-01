.. index:: pair: CP/A, Version 3; Kaltstart

Kaltstart des Systems
#####################

Vom Kaltstartloader des jeweiligen Rechnersystems wird auf allen
Diskettenlaufwerken nach einer bestimmten Kennung gesucht. Die erste passenden
Diskette wird als Kaltstartdiskette benutzt und die sogenannten Systemspuren
von dort geladen. Die Kaltstartdisketten für |A51xx| und |PC1715| sind nicht
kompatibel. Das Betriebssystem |CP/A| befindet sich auf der Kaltstartdiskette
als File mit dem (festen) Namen :file:`@OS.COM`. Beim Bürocomputer besitzt die
Kaltstartdiskette neben zwei speziellen Systemspuren auf Spur 0 und 1 ein
Bibliotheksverzeichnis ab Spur 2. Beim |PC1715| ist der Systemloader im
Verzeichnis versteckt, so dass auch Kaltstartdisketten keine Systemspuren
haben (Verzeichnis ab Spur 0). Die Kaltstartdiskette kann nach dem Kaltstart
wie andere Disketten benutzt werden. In der Regel enthält sie
Standardprogramme und das Abrechnungssystem.

Die Systemdatei :file:`@OS.COM` kann mit :program:`PIP` (o.ä. Software)
kopiert, mittels :program:`ZSID` und :program:`SAVE` modifiziert worden sein
oder auch direkt eine Link-Ausgabe darstellen. Sie wird wie eine normale Datei
behandelt und kann beim Bürocomputer auf der Diskette ab einer beliebigen
Stelle (u.U. auch gestreut) gespeichert sein, beim |PC1715| muss sie die erste
Datei nach dem Verzeichnis und dicht gespeichert sein.

Beim Bürocomputer steht in den Systemspuren lediglich ein Bootsystem, dass
zum Laden des eigentlichen Systems aus dem File :file:`@OS.COM` dient.

Beim |PC1715| erfolgt nach dem Starten des Systems eine automatische Erkennung
vorhandener Diskettenlaufwerke. Dazu wird der Kopf jedes Laufwerks auf Spur 0
positioniert, was bei weit innen stehendem Kopf zu entsprechenden (normalen!)
Geräuschen führen kann.

Nach dem Kaltstart wird i.a. das Programm :program:`ACCOUNT`
(Abrechnungssystem) von der Kaltstartdiskette geladen und ausgeführt. Bei der
Systemgenerierung kann jedoch auch ein anderes Kommando (auch ein leeres oder
der Aufruf von :program:`SUBMIT` für eine ganze Kommandofolge) als
Standardprogramm vereinbart werden. Die Ausführung dieses Programms kann nach
einem Kaltstart infolge eines Systemzusammenbruchs, wo eine Neuanmeldung durch
:program:`ACCOUNT` nicht sinnvoll ist, durch Betätigen der :kbd:`STOP` und
:kbd:`^C` Taste (siehe
:ref:`osys/cpa/CPA3_86.DOK/besonderheiten-des-bios:Tastatur`) während des
Ladevorgangs unterdrückt werden.

.. Local variables:
   coding: utf-8
   mode: text
   mode: rst
   End:
   vim: fileencoding=utf-8 filetype=rst :
