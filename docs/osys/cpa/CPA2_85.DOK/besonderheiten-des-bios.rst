.. highlight:: none

.. index:: pair: CP/A, Version 2; BIOS

Besonderheiten des BIOS
#######################

Das |BIOS| kann entsprechend der Hardwarekonfiguration und der geplanten Betriebsweise in verschiedenen Varianten generiert werden. Sämtliche Angaben dazu befinden sich als kommentierte :z80:`EQU` Anweisungen am Anfang des |BIOS| Quelltextes. Es folgen daher nur Erläuterungen zu im |BIOS| enthaltenen Sonderfunktionen.

.. index:: triple: CP/A, Version 2; BIOS; Tastatur

Tastatur
********

Die Tastenbelegung wurde dem Textverarbeitungssystem :program:`WordStar` und einer bequemen Systembedienung angepasst. Bis zu 48 Zeichen (Länge modifizierbar) werden vom |BIOS| gepuffert.

Belegung der Kursor- und der darüberliegenden Tasten
====================================================

.. tikz:: CP/A V2(1985) |BIOS| - Belegung der Kursortasten
   :include: tastatur-belegung-kursor.tikz
   :libs: matrix

:HC: Hardcopy (:kbd:`INS MODE` Taste) schaltet den Drucker direkt parallel zur
     Bildschirmausgabe. Zur Kontrolle dieses Zustands wird die neben der Taste
     liegende Lampe angesteuert. Erneutes Drücken der Taste hebt den Zustand
     wieder auf. Die :kbd:`^P` Funktion des |BDOS| ist weiterhin
     verfügbar, jedoch sollten nicht beide Funktionen zugleich aktiv sein.

:DEL: Delete (:code:`7FH`)

:DS: Mit dieser Taste werden Druckertreiber und Drucker synchronisiert. Sie
     sollte nach jeder Neueinstellung des Blattanfangs betätigt werden
     (:kbd:`SYN` Taste am Drucker nicht benutzen!).

:ESC: Escape (:code:`1BH`)

Belegung der Starttasten
========================

.. tikz:: CP/A V2(1985) |BIOS| - Belegung der Starttasten
   :include: tastatur-belegung-start.tikz
   :libs: matrix

Belegung von Sondertasten
=========================

.. rubric:: CI - Stop/Start

Beim Betätigen der Taste wird das gesamte System bis zu ihrer erneuten Betätigung bzw. bis zum Abbruch des laufenden Programms durch Warmstart (:kbd:`^C`) gestoppt (Warteschleife in Tastatureingabe) und die Fehlerlampe eingeschaltet. Diese Reaktionen werden ggf. bis zur Beendigung zeitkritischer Diskettentransfers oder des Bildneuaufbaus verzögert.

Die Taste enthält die :kbd:`^S` Funktion des |BDOS| in verallgemeinerter Form und erlaubt durch die ständige Tastaturabfrage auch dann das Stoppen der Anlage, wenn vom Programm keine Tastatureingabe oder Bildschirmausgabe gefordert wird.

.. rubric:: M - MONITOR-Taste

Wurde die Monitorvariante des |BIOS| generiert, so wird beim Betätigen dieser Taste der |BIOS| Monitor aufgerufen (siehe :ref:`osys/cpa/CPA2_85.DOK/besonderheiten-des-bios:BIOS Monitor`; ggf. ebenfalls verzögert); in der Variante ohne Monitor wirkt die Taste wie :kbd:`ET1`.

.. index:: triple: CP/A, Version 2; BIOS; Drucker

Drucker
*******

Im |BIOS| wurde ein Druckertreiber integriert, der neben der normalen Betriebsart den Drucker *DIABLO 1610/1620* simuliert. Dadurch konnten alle :program:`WordStar` Druckfunktionen auf der Basis von Microspaceschritten des Druckwerks (1\ |oneh| zeiliger Druck, Schattendruck zur Hervorhebung von Textteilen) sowie eine Farbbandumschaltung (bessere Ausnutzung einfarbiger Bänder) nutzbar gemacht werden. Hinweise zur Ansteuerung sind dem |BIOS| Quelltext bzw. entsprechenden :program:`WordStar` Unterlagen zu entnehmen.

Folgende Besonderheiten bei der Nutzung von :program:`WordStar` ergeben sich aus der Tatsache, dass der obige Druckertyp eine Schrittweite von 1/120" für den Zeichenabstand besitzt, Drucker vom Typ |SD1152| aber nur 1/60", d.h. im Druckertreiber gerundet werden muss:

:.CW n: n ungerade arbeitet nicht exakt

:.UJ 1: Bei Microspace können durch Rundungen Zeichenabstandsänderungen
        auftreten, die das Druckbild negativ beeinflussen.

Weiterhin ergibt sich als Einschränkung:

:^P<CR>: nicht erlaubt (Überdrucken von Zeilen arbeitet nur bei zufälliger
         Druckrichtung vorwärts exakt, da kein Vor- und Rückwärtsdruck in
         diesem Fall).

Nach 120 Zeichen erfolgt eine automatische Zeilenschaltung, nach 67 Zeilen ein automatischer Seitenvorschub (beide Werte sind im |BIOS| Quelltext modifizierbar). Bei Ausgabe von TAB Steuerzeichen realisiert der Druckertreiber die TAB Funktion in Schritten von 8 Zeichen.

Bei Simulation des Druckertyps *DIABLO 1610/1620* werden alle automatischen Funktionen (Zeilenvorschub, Seitenvorschub, TAB Expansion) unterdrückt, d.h. :program:`WordStar` bestimmt allein die Seitenaufteilung. Die *DIABLO* Simulation wird durch die Steuerzeichenfolge ':code:`1B 34`' aktiviert ,alle anderen Steuerzeichenfolgen vor dieser Aktivierung werden normal an den Drucker gesendet, es sind also auch entsprechende Programme zur direkten Druckerbedienung nutzbar.

Sämtliche Funktionen sind für Drucker |SD1152|/|SD1157| mit |PIO|\ 1/|PIO|\ 2 und |IFSS| Anschluss durch entsprechende Quelltextvarianten im |BIOS| verfügbar.

.. index:: triple: CP/A, Version 2; BIOS; Zeitgeber

Zeitgeberdienste
****************

Überblick der Zeitgeberdienste
==============================

Unter Ausnutzung der kaskadierten |CTC| Kanäle 2 und 3 wurden Zeittakte von 5 |ms| und 1 s bereitgestellt.

Der Zeittakt von 5 |ms| ist für Zeitmessungen vorgesehen. Die Einheit von 5 |ms| ist ein Kompromiss zwischen der zusätzlichen Interruptbelastung und dem maximal möglichen Faktor von 256 zur Erreichung des kaskadierten 1 s Taktes. Bei jedem Interrupt im Abstand von 5 |ms| wird ein 2 Byte Zähler auf dem Hauptspeicherplatz :z80:`TIM5CN` (siehe :ref:`osys/cpa/CPA2_85.DOK/besonderheiten-des-bios:Arbeitszellen`) zyklisch um 1 erhöht. Der Anfangswert ist beliebig, d.h. es sind durch ständiges Aktivieren / Deaktivieren auch kumulative Zeitmessungen möglich. Die maximale Messdauer beträgt für eine Periode ca. 327 s bei einer Genauigkeit von 5 |ms|.

Der 5 |ms| Zeittakt ist standardmäßig aktiviert. Nach Rückkehr aus der Interruptreaktionsroutine des Taktes wird :z80:`CONST` aufgerufen und damit eine möglicherweise gedrückte Taste gelesen.

Der Zeittakt von 1 s ist zur Realisierung eines Timeout Apparats vorgesehen. Bei jedem Interrupt wird ein 2 Byte Zähler auf Hauptspeicherplatz :z80:`TIM1CN` (siehe :ref:`osys/cpa/CPA2_85.DOK/besonderheiten-des-bios:Arbeitszellen`) um 1 vermindert. Der Nulldurchgang stellt i.a. das Timeout Ereignis dar, muss jedoch explizit abgefragt werden (keine Unterbrechung des gerade aktiven Programms!). Die maximale Timeout Größe beträgt hierbei ca. 9.1 Std. Außerdem wird jede Sekunde zu der durch :z80:`TIM1RT` (siehe :ref:`osys/cpa/CPA2_85.DOK/besonderheiten-des-bios:Arbeitszellen`) definierten Routine gesprungen, wodurch beliebige Nutzerroutinen aktivierbar sind (alle Register frei, Rückkehr mit :z80:`RET`, Interruptverbot muss erhalten bleiben!). Standardmäßig wird bei jedem Warmstart die Adresse einer leeren Routine (nur :z80:`RET` Befehl) auf :z80:`TIM1RT` hinterlegt. Auch der 1 s Zeittakt ist standardmäßig aktiviert.

Routinen zur Realisierung der Zeitgeberdienste
==============================================

.. rubric:: :z80:`TIMINI`

Initialisierung der |CTC| Kanäle 2,3 bei Kaltstart ohne Interrupt; Initialisierung eines Eintrags im Interruptvektor des |BIOS| für |CTC| Kanal 0 (Interruptroutinen :z80:`TIM5MS`, :z80:`TIM1SC`).

.. rubric:: :z80:`TIM5ON` / :z80:`TIM5OFF`

Zulassen / Verbieten Interrupt 5 |ms|.

.. rubric:: :z80:`TIM1ON` / :z80:`TIM1OFF`

Zulassen / Verbieten Interrupt 1 s.

.. index:: triple: CP/A, Version 2; BIOS; Speicherschutz

Speicherschutzdienste
*********************

Überblick der Speicherschutzdienste
===================================

Die Speicherschutzeinrichtung basiert auf einer Einteilung des verfügbaren Hauptspeichers von 64 |kB| in 64 Byte lange Abschnitte, die unabhängig voneinander als geschützt gekennzeichnet werden können. Schreibbefehle in diese Bereiche sind nur aus geschützten Bereichen selbst erlaubt, anderenfalls erfolgt eine Unterbrechung. Gekoppelt mit dem Speicherschutz ist ein Schutz gegen Ausführung von E/A Befehlen außerhalb von geschützten Bereichen (führt zu NMI Interrupt), d.h. geschützte Bereiche werden als privilegierte Systemprogramme betrachtet.

Bei Nutzung der Speicherschutzeinrichtung muss daher der |BIOS|/|BDOS| Bereich grundsätzlich mit geschützt werden (vom |BDOS| aus wird in Diskettentabellen geschrieben, die im |BIOS| liegen). Alle sonstigen Programmbereiche, in denen E/A Befehle abgearbeitet werden können, müssen ebenfalls unabhängig von dem eigentlich gegen Überschreiben zu sichernden Bereich geschützt werden.

Routinen zur Realisierung der Speicherschutzdienste
===================================================

.. rubric:: :z80:`MPINIT`

Initialisierung der Speicherschutzeinrichtung und Definition des standardmäßig zu schützenden Bereichs.

.. rubric:: :z80:`MPSET` (Integer Register :reg:`BC`: Anfangsadresse, Integer Register :reg:`DE`: Endadresse)

Definition eines zusätzlich zu schützenden Bereichs. Sind die Adressen nicht durch 64 teilbar, so wird die Anfangsadresse ab- und die Endadresse aufgerundet.

.. rubric:: :z80:`MPOFF`

Der gesamte Speicherschutz wird außer Kraft gesetzt. :z80:`MPOFF` wird bei jedem Warmstart aufgerufen, d.h. der normale |CP/A| Betrieb erfolgt ohne Speicherschutz.

Reaktion bei Verletzen des Speicherschutzes
===========================================

Der Schreibversuch wird unterdrückt. Auf dem Bildschirm erfolgt eine Ausschrift mit Angabe der Adresse des dem betreffenden Schreibbefehl folgenden Befehls. Das laufende Programm wird nicht gestoppt.

Reaktion bei Verletzen des E/A Schutzes
=======================================

Der E/A Befehl im ungeschützten Bereich wird ausgeführt. Anschließend erfolgt eine NMI Unterbrechung, d.h. es wird zur Adresse :addr:`66H` verzweigt. Da diese Zelle evtl. vom auszutestenden Programm benutzt wird (Standard :z80:`FCB` von :addr:`5CH` bis :addr:`7FH`), kann hier nicht standardmäßig ein Sprung zur entsprechenden Reaktionsroutine hinterlegt werden. Deshalb wurde innerhalb des |BIOS| Monitor die Möglichkeit geschaffen, auf Adresse :addr:`66H` wahlweise

1) einen Sprungbefehl zur Reaktionsroutine (Reaktion dann analog zu Speicherschutz), oder
2) einen Befehl :z80:`RETN` zum Ignorieren des Schutzes

zu hinterlegen (siehe :ref:`osys/cpa/CPA2_85.DOK/besonderheiten-des-bios:\:command:\`PROTECT\` Kommando`). Der Befehl muss bis nach dem Aufruf von :z80:`MPOFF` dort stehen bleiben!

.. index:: triple: CP/A, Version 2; BIOS; Console

Konsoleneingabe und Konsolenausgabe
***********************************

Das Lesen der physischen Tastencodes und die Übergabe der gegebenenfalls umkodierten Zeichen an den Nutzer sind entkoppelt. :z80:`CONST` liest bei gedrückter Taste deren Code. Die den Tasten :kbd:`INS MODE` (Hardcopy), :kbd:`INS LINE` (Drucker synchronisieren), :kbd:`CI` (Stop/Start), :kbd:`M` (Monitoraufruf), :kbd:`SEL0` |...| :kbd:`SEL3` (Lampenanzeige ein/aus und Setzen/Rücksetzen der entsprechenden Bits im Pufferspeicher für die Tastaturlampen) zugeordneten Steuerfunktionen werden sofort ausgeführt. Die Betätigung der Taste :kbd:`ET2` (:kbd:`CTRL`) führt zur Umrechnung des Tastencodes der nächsten alphanumerischen Taste modulo 20H. Zweimal :kbd:`CTRL` unmittelbar nacheinander hat keine Wirkung.

Die den alphanumerischen Tasten und den anderen Funktionstasten entsprechenden logischen Codes gelangen in einen Zeichenpuffer. Die Mehrfacheingaben "00" und "000" werden vorher aufgelöst. :z80:`CONST` meldet zurück, ob der Puffer wenigstens ein Zeichen enthält.

:z80:`CONIN` übergibt - wenn vorhanden - das erste Zeichen aus dem Puffer. Anderenfalls wird auf die nächste Eingabe gewartet. Des Weiteren realisiert :z80:`CONIN` die Dauerfunktion für alle alphanumerischen Tasten der Tastatur |K7604/06|.

In :z80:`CONOUT` wird die Ausgabe des Zeichens :code:`07H` (BELL) durch einmaliges Blinken der Fehlerlampen realisiert.

.. index:: triple: CP/A, Version 2; BIOS; Monitor

BIOS Monitor
************

Der |BIOS| Monitor stellt - seine Generierung vorausgesetzt - einen Satz von residenten Funktionen bereit, die somit ohne Veränderung der Speicherplatzbelegung ständig, d.h. auch während der Arbeit eines Nutzerprogramms zur Verfügung stehen.

Die Aktivierung dieser Funktionen ist im Dialog durch Drücken der MONITOR Taste (:kbd:`M` rechts oben) oder direkten Aufruf der Prozedur :z80:`MONCAL` möglich.

Der |BIOS| Monitor schützt sich gegen rekursiven Aufruf durch Setzen eines Sperrbits.

MONITOR Taste
=============

Die MONITOR Taste ist gegenüber anderen Tasten der Tastatur nicht ausgezeichnet. Insbesondere erzeugt auch sie bei ihrer Betätigung keinen Interrupt, d.h. sie muss abgefragt werden. Folgende zwei Methoden wurden implementiert:

1) Abfrage bei Eingabe eines Zeichens durch das |BIOS|, d.h. nur zu Zeitpunkten, wo auch eine Eingabe vom Programm gefordert wird und die Steuerung ohnehin im |BIOS| liegt;
2) Abfrage im 5 |ms| Zeitinterrupt, falls dieser aktiv ist.

Nach Drücken der MONITOR Taste erfolgt eine Ausschrift mit Angabe der Rückkehradresse (d.h. der Unterbrechungsstelle beim 5 |ms| Interrupt bzw. der Aufrufstelle bei normaler Zeicheneingabe). Danach können nacheinander beliebig viele Monitorfunktionen durch Eingabe ihres Anfangsbuchstabens (groß oder klein) aufgerufen werden.

Eine leere Eingabe (:kbd:`ET1`) oder die erneute Betätigung der MONITOR Taste führen zum Verlassen des |BIOS| Monitors.

Übersicht über die Monitorkommandos
===================================

Die Monitorkommandos sind:

.. tabularcolumns:: cL
.. table:: |CP/A| V2(1985) |BIOS| - Monitorkommandos
   :widths: 25, 75
   :width: 80%

   +----------+-----------------------------------------------------+
   | Zeichen  | Funktion                                            |
   +==========+=====================================================+
   | :kbd:`M` | Lesen/Modifizieren Speicher                         |
   +----------+-----------------------------------------------------+
   | :kbd:`C` | Aufruf Unterprogramm                                |
   +----------+-----------------------------------------------------+
   | :kbd:`P` | Ein-/Ausschalten Speicherschutz                     |
   +----------+-----------------------------------------------------+
   | :kbd:`R` | Anzeige der Registerstände beim Aufruf des Monitors |
   +----------+-----------------------------------------------------+
   | :kbd:`T` | Ein-/Ausschalten Zeittakt                           |
   +----------+-----------------------------------------------------+

:command:`MEM` Kommando
=======================

Nach Eingabe von :kbd:`M` wird eine 2 Byte Adresse in hexadezimaler Form erwartet. Sie gibt die Anfangsadresse eines Speicherbereichs an.

Jeweils ein Byte wird aufsteigend in hexadezimaler Form angezeigt und eine Eingabe erwartet:

:keine Eing.:   keine Veränderung; nächstes Byte
:2 Hex-Ziffern: Überschreiben des Bytes; nächstes Byte
:"-" (Minus):   keine Veränderung; vorheriges Byte
:4 Hex-Ziffern: keine Veränderung; neuer Speicherbereich
:"." (Punkt):   Ende des :command:`MEM` Kommandos

:command:`CALL` Kommando
========================

Nach Eingabe von :kbd:`C` wird eine 2 Byte Adresse in hexadezimaler Form erwartet. Sie gibt die Startadresse eines Unterprogramms an. Als Rückkehradresse wird vor dem Ansprung dieses Programms eine Rückkehr zum |BIOS| Monitor in das Stack gebracht.

:command:`PROTECT` Kommando
===========================

Nach Eingabe von :kbd:`P` (Aufruf :z80:`MPINIT`: Definition des standardmäßig zu schützenden Bereichs) wird eine der folgenden Eingaben erwartet:

:"." (Punkt):   keine weitere Aktion
:2 Hex-Ziffern: ein Adresspaar: bezeichnet einen zu schützenden Bereich
:"-" (Minus):   Aufruf MPOFF: Aufhebung des gesamten Speicherschutzes
:"I":           Einstellung des Regimes "Ignorieren von E/A Schutzverletzungen", d.h. Hinterlegen von :z80:`RETN` auf :addr:`66H` (vgl. :ref:`osys/cpa/CPA2_85.DOK/besonderheiten-des-bios:Reaktion bei Verletzen des E/A Schutzes`)
:"L":           Einstellung des Regimes "Protokollieren von E/A Schutzverletzungen", d.h. Hinterlegen eines Sprungbefehls auf :addr:`66H` (vgl. :ref:`osys/cpa/CPA2_85.DOK/besonderheiten-des-bios:Reaktion bei Verletzen des E/A Schutzes`)

Wird keine Regimeeinstellung ("I" oder "L") vorgenommen, so bleibt die Zelle :addr:`66H` unverändert (Standard :z80:`FCB` von :addr:`5CH` bis :addr:`7FH`).

:command:`REG` Kommando
=======================

Nach Eingabe von :kbd:`R` werden die Stände der Registerpaare :reg:`AF`, :reg:`BC`, :reg:`DE`, :reg:`HL`, :reg:`IX`, :reg:`IY`, :reg:`SP` an der Aufrufstelle des Monitors sowie die Leitadresse des Rettungsbereich dieser Register (für eventuelle Modifizierung mittels :command:`MEM` Kommando) angezeigt.

:command:`TIME` Kommando
========================

Nach Eingabe von :kbd:`T` wird eine :kbd:`5` zur Aktivierung / Deaktivierung des 5 |ms| Zeittakts oder eine :kbd:`1` zur Aktivierung / Deaktivierung des 1 s Zeittakts erwartet. Eingabeabschluss mit :kbd:`ET1` aktiviert den Takt, :kbd:`-` deaktiviert ihn.

.. index:: triple: CP/A, Version 2; BIOS; Erweiterungen

Einbindung der Erweiterungen in CP/A
************************************

Sprungvektor
============

Sämtliche angeführten Routinen sind Bestandteile des |BIOS| Codes. Ihr Aufruf von normalen Programmen aus ist über einen Sprungvektor möglich. Dieser besteht aus je 3 Byte langen Sprungbefehlen. Die Anfangsadresse des Sprungvektors befindet sich auf Hauptspeicherplatz :addr:`4EH` (beim Warmstart hinterlegt).

Folgende Entries sind vergeben:

.. tabularcolumns:: clL
.. table:: |CP/A| V2(1985) |BIOS| - Sprungvektoren
   :widths: 10, 15, 75
   :width: 80%

   +------------+------------------+---------------------------+
   | Nummer     | Entry            | Parameter                 |
   +============+==================+===========================+
   | :code:`00` | :z80:`JP MONCAL` | \-                        |
   +------------+------------------+---------------------------+
   | :code:`03` | :z80:`JP TIM5ON` | \-                        |
   +------------+------------------+---------------------------+
   | :code:`06` | :z80:`JP TIM5OF` | \-                        |
   +------------+------------------+---------------------------+
   | :code:`09` | :z80:`JP TIM1ON` | \-                        |
   +------------+------------------+---------------------------+
   | :code:`0C` | :z80:`JP TIM1OF` | \-                        |
   +------------+------------------+---------------------------+
   | :code:`0F` | :z80:`JP MPINIT` | \-                        |
   +------------+------------------+---------------------------+
   | :code:`12` | :z80:`JP MPSET`  | Reg. :reg:`BC`, :reg:`DE` |
   +------------+------------------+---------------------------+
   | :code:`15` | :z80:`JP MPOFF`  | \-                        |
   +------------+------------------+---------------------------+

Der Aufruf ist z.B. über folgende Befehlsfolge möglich:

.. code-block:: nasm
   :linenos:

   	ld	a,<entry>
   	ld	hl,(4eh)
   	add	a,l
   	ld	l,a
   	ld	a,0		;kein XOR!
   	adc	a,h
   	ld	h,a
   	jp	(hl)

Arbeitszellen
=============

Als Scratch Bereich des |BIOS| sind in |CP/M| die Zellen :addr:`40H` bis :addr:`4FH` freigehalten. Sie werden von |CP/A| wie folgt benutzt:

.. tabularcolumns:: p{2cm}p{2cm}L
.. table:: |CP/A| V2(1985) |BIOS| - Arbeitszellen
   :widths: 15, 15, 70
   :width: 80%

   +-----------------+------------------------------------------------------------+
   | Bereich         | Inhalt                                                     |
   +=================+============================================================+
   | *Pufferspeicher für Tastaturlampen*                                          |
   +-----------------+------------------------------------------------------------+
   | :addr:`40H`     | (0 bei aus, 1 bei ein)                                     |
   |                 +---------------+--------------------------------------------+
   |                 |         Bit 7 | Hardcopylampe                              |
   |                 +---------------+--------------------------------------------+
   |                 |             6 | Fehlerlampe                                |
   |                 +---------------+--------------------------------------------+
   |                 |     5 |...| 4 | reserviert (=0)                            |
   |                 +---------------+--------------------------------------------+
   |                 |     3 |...| 0 | Selektor 3-0                               |
   +-----------------+---------------+--------------------------------------------+
   | *Zeitgeberdienste*                                                           |
   +-----------------+---------------+--------------------------------------------+
   | :addr:`41H`     | :z80:`TIM5CN` | Zähler 5 |ms| Zeittakt                     |
   | |...|           |               |                                            |
   | :addr:`42H`     |               |                                            |
   +-----------------+---------------+--------------------------------------------+
   | :addr:`43H`     | :z80:`TIM1CN` | Zähler 1 s Zeittakt                        |
   | |...|           |               |                                            |
   | :addr:`44H`     |               |                                            |
   +-----------------+---------------+--------------------------------------------+
   | :addr:`45H`     | :z80:`TIM1RT` | Adresse der 1 s Nutzerroutine              |
   | |...|           |               |                                            |
   | :addr:`46H`     |               |                                            |
   +-----------------+---------------+--------------------------------------------+
   | :addr:`49H`     |               | reserviert                                 |
   | |...|           |               |                                            |
   | :addr:`4DH`     |               |                                            |
   +-----------------+---------------+--------------------------------------------+
   | :addr:`4EH`     | :z80:`CPMEXT` | Sprungvektoradresse für |CP/A| Erweiterung |
   | |...|           |               |                                            |
   | :addr:`4FH`     |               |                                            |
   +-----------------+---------------+--------------------------------------------+

.. Local variables:
   coding: utf-8
   mode: text
   mode: rst
   End:
   vim: fileencoding=utf-8 filetype=rst :
