.. index:: pair: CP/A, Version 3; CCP

Besonderheiten des CCP
######################

Das |CCP| enthält gegenüber der Version |CP/M| 2.2 einige Erweiterungen (bei gleichem Hauptspeicherbedarf von :addr:`800H` Bytes). Sie betreffen vor allem die Arbeit mit verschiedenen Nutzerbereichen, wie sie sich bei 800 |kB| Disketten als sinnvoll erweisen kann.

Bei einem eingestellten Nutzerbereich größer als 0 lautet die Promtmeldung :console:`du>` statt nur :console:`d>` (:console:`d` für Default Laufwerk, :console:`u` für dezimale Nutzerbereichsnummer). Hierdurch hat der Anwender bei der Aufteilung einer Diskette in mehrere Nutzerbereiche einen leichteren Überblick, in welchem Bereich er sich zur Zeit bewegt.

Kommandofiles werden bei :envvar:`USER` > 0 auch unter :envvar:`USER` 0 und wenn dort erfolglos auf der Systemdiskette (im Kaltstart Laufwerk) unter :envvar:`USER` 0 gesucht (gilt nicht für nachgeladene Files!).

.. index:: single: Resident CCP commandos in CP/A

Weiterhin existieren zusätzliche residente Kommandos:

.. index:: single: CLK
.. index:: pair: CLK; Resident CCP commandos in CP/A

.. rubric:: :command:`CLK hh:mm:ss [tt.mm.jj]`

Im angegebenen Parameterformat bedeutet (jeweils dezimal, auch einstellig erlaubt):

.. program:: CLK

.. option:: hh:mm:ss

   Stunden:Minuten:Sekunden

.. option:: tt.mm.jj

   Tag.Monat.Jahr

Alle Angaben nach :option:`hh:mm:ss` können fehlen, in diesem Fall werden diese Werte nicht verändert.

Durch dieses Kommando können Uhrzeit und Datum (beide Angaben ab :code:`50H` in BCD Form vom Kaltstart bzw. von :program:`ACCOUNT` hinterlegt) neu gestellt werden. Dies kann sich z.B. nach Programmen, die diesen Bereich zerstört oder wegen zu langer geschlossener Interrupts eine falsche Uhrzeit verursacht haben, als notwendig erweisen.

.. index:: single: GO
.. index:: pair: GO; Resident CCP commandos in CP/A

.. rubric:: :command:`GO [<beliebige Parameter>]`

Im angegebenen Parameterformat bedeutet:

.. program:: GO

.. option:: <beliebige Parameter>

   Parameter wie beim Direktaufruf des Programms.

Das letzte geladene Programm wird ohne Neuladen aktiviert, Parameter können wie beim Direktaufruf angegeben werden, Nutzerbereich beliebig (d.h. das Programm kann zuvor über einen anderen Nutzerbereich in den Hauptspeicher gebracht worden sein).

.. index:: single: EXT
.. index:: pair: EXT; Resident CCP commandos in CP/A

.. rubric:: :command:`EXT [d:]<filename>`

Im angegebenen Parameterformat bedeutet:

.. program:: EXT

.. option:: [d:]

   Das optional anzugebende Diskettenlaufwerk.

.. option:: <filename>

   Das zu einem residenten Kommando erklärte :mimetype:`COM` File mit nur
   maximal 4 Zeichen Länge.

Das angegeben :mimetype:`COM` File wird zu einem residenten Kommando erklärt, indem es vor |BDOS|, |CCP| und vor evtl. schon residenten zusätzlichen Kommandos im Hauptspeicher abgelegt wird, um bei Aufruf statt von Diskette von dort nach :addr:`100H` geladen zu werden. Hierdurch verringert sich jedoch der |TPA| entsprechend. Da residente Kommandos nur maximal 4 Zeichen lang sein dürfen, trifft dies auch auf :option:`<filename>` zu.

.. index:: single: RES
.. index:: pair: RES; Resident CCP commandos in CP/A

.. rubric:: :command:`RES`

Streichen aller zusätzlich residenten Kommandos.

.. index:: single: HELP
.. index:: pair: HELP; Resident CCP commandos in CP/A

.. rubric:: :command:`HELP`

Ausgabe einer Liste aller zur Zeit residenten Kommandos

Bei jedem Warmstart prüft das |BIOS|, ob das über das |CCP| definierte Standard Laufwerk im System definiert ist. Im negativen Fall (z.B. Tippfehler) wird auf das Kaltstart Laufwerk umgeschaltet, der Nutzerbereich bleibt erhalten.

.. Local variables:
   coding: utf-8
   mode: text
   mode: rst
   End:
   vim: fileencoding=utf-8 filetype=rst :
