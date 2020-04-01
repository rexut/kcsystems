.. index:: pair: PC/M; Inbetriebnahme

Inbetriebnahme
##############

.. rubric:: Ein paar Hinweise.

Der Computer sollte in der folgenden Reihenfolge aufgebaut und in Betrieb genommen werden:

1. zentrale Platine:(Durchkontaktierungen), Brücken, Fassungen und Steckverbinder
2. Netzteil
3. Funktionsgruppenweise Bestückung und Inbetriebnahme der zentralen Platine
4. Tastatur
5. Fernsehinterface (|BSA|)
6. Kassetteninterface

Die Punkte 4. und 5. können dabei auch parallel und vor dem Aufbau der Zentralen Platine realisiert werden.

Bei der Inbetriebnahme der einzelnen Funktionsgruppen sollte als erstes immer die Spannung an den IC Pins und der Wert der Stromaufnahme der Baugruppe gemessen werden. Dann sind die einzelnen Signale und Pegel im Signalzweig zu kontrollieren. Um die einwandfreie Funktion aller Baugruppen zu gewährleisten, müssen alle vorgesehenen Stützkondensatoren (Bestückungsplan) bestückt werden.

.. index:: triple: PC/M; Inbetriebnahme; Zentrale Platine

.. rubric:: Zentrale Platine

Zuerst werden der Quarzoszillator (D1.1) einschließlich des 1:4 Teilers (D2), die Resetlogik (D3.2) und der |NMI| Generator (D4.1, D60.2, D3.1) eingelötet. Am Ausgang des Oszillators ist die Frequenz von 10,0 |MHz| zu kontrollieren und mit C1 eventuell abzugleichen. Am Lötauge für Pin 6 der |CPU| muss der 2,5 |MHz| Takt mit den geforderten Pegel- und Flankenverhältnissen (Pull Up) anliegen.

Beim Einschalten der Betriebsspannung 5P muss am Lötauge für Pin 26 der |CPU| ein Resetimpuls (power on) vorhanden sein. Dabei muss die Breite des Impulses unter 2 |ms| liegen, um den Refresh für die dynamischen Speicher zu garantieren. Die Kontrolle des |NMI| Generators wird zu einem späteren Zeitpunkt im Zusammenhang mit der Software (Betriebssystem) durchgeführt.

Nun können die Bustreiber D6 bis D8 eingelötet werden. Ihre Funktion kontrolliert man durch statisches Anlegen von Low bzw. High Pegel an den Bustreibereingängen und durch Nachmessen der Pegel an den Ausgängen. Wird Pin 11 des Gatters D1.2 auf Low gelegt, müssen sich die Ausgänge der Bustreiber D6 bis D8 im hochohmigen Zustand befinden. Nach dieser Prüfung kann die |CPU| eingelötet werden. Der Datenbus liegt auf High Pegel. Damit werden nach dem Resetimpuls von der |CPU| :z80:`RST 38` Befehle gelesen und der gesamte Speicherbereich würde mit 0039H beschrieben. Dieser Umstand hat ein zyklisches Durchlaufen des gesamten Adressbereiches zur Folge und ermöglicht die Kontrolle verschiedener Impulsfolgen. Es werden die Adressleitungen A0 bis A15 an den Ausgängen der Bustreiber D6 bis D8 kontrolliert. Die an A0 anliegende Pulsfolge muss die höchste Frequenz aufweisen, mit ansteigender Adressreihenfolge liegt an jeder Adressleitung je die halbe Frequenz der vorhergehenden Adresse. Auch an den Steuersignalausgängen /RD, /MREQ und /M1 müssen Impulsfolgen anstehen. Dieser Kontrolle schließt sich der Aufbau von Bootstraploader, Speicherblockselektport, Überblendlogik und Adressdekodierung für die |EPROM|\s an. Dazu werden die Bauelemente D9, D10, D11, D12 und D53 eingelötet. An den Ausgängen der Dekoder D10 (Ausgänge 0 bis 7) und D11 (Ausgänge 0 bis 3) müssen jeweils versetzt zueinander Pulsfolgen erkennbar sein. Die Ausgänge 0 bis 3 von D11 entsprechen den /OE Signalen der |EPROM|\s und können an Pin 20 der jeweiligen |EPROM| Fassungen überprüft werden . Dabei muss mit Aktivieren des entsprechenden /OE Signals auch das /CE Signal für die |EPROM|\s (Pin 18) Low einnehmen. Dazu muss das Speicherblockselektport (DS 8212) durch den Resetimpuls beim Einschalten zurückgesetzt sein (alle Ausgänge = Low Pegel). Die Signale /OE und /CE dürfen nur bei /RD = Low aktiv sein.

:raw-latex:`\begin{turn}{90}`
:raw-latex:`\begin{minipage}[c][\textwidth][c]{\textheight}`

.. index:: triple: PC/M; Zusatzdaten; FA 3/88-05 (ZD/3)
.. index:: triple: PC/M; Zusatzdaten; FA 3/88-05 (ZD/4)

.. list-table:: FA 3/88-05 (ZD/3) (ZD/4)
   :name: kcsystems-mach-pcm-fa038805-zd34
   :class: longtable
   :align: center
   :width: 80 %
   :header-rows: 1

   * - FA 3/88-05 (ZD/4)
     - FA 3/88-05 (ZD/3)

   * - :raw-latex:`\begin{minipage}[c][][c]{0.45\textwidth}`

       .. figure:: bild-28.png
          :name: kcsystems-mach-pcm-bild-28
          :figclass: align-center
          :align: center
          :width: 480 px
          :alt: Taktdiagramm "READ" und "EARLY-WRITE" Zyklus

          Taktdiagramm "READ" und "EARLY-WRITE" Zyklus

       :raw-latex:`\end{minipage}`

     - :raw-latex:`\begin{minipage}[c][][c]{0.45\textwidth}`

       .. figure:: bild-27.png
          :name: kcsystems-mach-pcm-bild-27
          :figclass: align-center
          :align: center
          :width: 480 px
          :alt: Blockschaltbild |U2164|

          Blockschaltbild |U2164|

       :raw-latex:`\end{minipage}`

:raw-latex:`\end{minipage}`
:raw-latex:`\end{turn}`
:raw-latex:`\FloatBarrier`

.. index:: triple: PC/M; Zusatzdaten; FA 3/88-05 (ZD/5)

.. list-table:: FA 3/88-05 (ZD/5)
   :name: kcsystems-mach-pcm-fa038805-zd5
   :class: longtable
   :align: center
   :width: 80 %
   :header-rows: 1

   * - FA 3/88-05 (ZD/5)

   * - .. figure:: bild-29.png
          :name: kcsystems-mach-pcm-bild-29
          :figclass: align-center
          :align: center
          :width: 320 px
          :alt: Taktdiagramm "RAS-ONLY-REFRESH" Zyklus

          Taktdiagramm "RAS-ONLY-REFRESH" Zyklus

Nun können die restlichen Bauelemente der Systemseite außer den |DRAM|\s bestückt werden. Anhand der Impulsdiagramme (|PC_M_B28_N| und |PC_M_B29_N|) wird das Zeitverhalten der Signale /RAS, /CAS0, /CAS1, /CAS2, /WR (Pin 3 von D 52.4) und SEL (Multiplexer Pin 1) kontrolliert. Nach dieser Kontrolle werden die ICs des ersten |DRAM| Blockes bestückt. Sollten sich beim späteren Test des kompletten |PC/M| Computers Speicherzellen nicht beschreiben lassen oder verlieren diese ihre Information, müssen noch einmal die Impulsbilder geprüft und eventuell C2 verändert werden.

Beim Aufbau weiterer Exemplare des |PC/M| Computers wurde festgestellt, dass die Bestückung mit |DRAM| unterschiedlicher Hersteller zu Schwierigkeiten mit der /RAS /CAS Signalbildung und damit zu Schreib- oder Lesefehlern führen kann. Innerhalb einer Speicherbank sollten keinesfalls unterschiedliche Typen eingesetzt werden. Bei einigen |U2164| war es erforderlich die /RAS Leitung an den Speichern mit einem Pull Up Widerstand von 560 |Omega| zu versehen bzw. D52 (DL000) durch einen D100 oder D200 zu ersetzen. Unterschiede bei der Bestückung mit verschiedenen Typen in den 3 Bänken lassen sich durch separate Verzögerungskapazitäten (100 |pF| bis ca. 1 |nF|) direkt an den /CAS Leitungen ausgleichen. Bei Verwendung von K565RU5 bewährte sich die im Stromlaufplan angegebene Dimensionierung.

Mit dem eventuellen Bestücken und Testen des zweiten und dritten |DRAM| Blockes ist der systemseitige Aufbau der Zentralen Platine abgeschlossen.

Nun werden der I/O Adressdekoder (D54), die Bauelemente der Tonausgabe (D60.1, VT1) sowie die Bauelemente der |IFSS| Schnittstellen (D61, A2 bis A5, VT2 bis VT5, passive BE) eingelötet. Am Adressdekoder D54 (DS 8205) sind die 8 zeitlich zueinander versetzten /CE Signale (Pin 7, 9 bis 15) zu kontrollieren. Diese Signale liegen unabhängig von /IORQ an, da die peripheren Bausteine (|PIO|, |CTC|, |SIO|) das Signal /IORQ direkt zu ihrer Aktivierung verwenden. Werden andere als oben genannte Systembausteine eingesetzt, müssen deren Aktivierungssignale mit /IORQ verknüpft werden. Die Tonausgabe kann durch Anlegen einer Impulsfolge an Pin 11 von D60.1 (DL 074) überprüft werden. Bei höherohmigen Schallwandlern (z.B. Kopfhörer mit Z größer 200 |Omega|) kann der 100 |Omega| Widerstand im Kollektorzweig des VT1 entfallen oder verringert werden. Für die Inbetriebnahme der |IFSS| Schnittstellen werden über den Anwendersteckverbinder (Koppelbus) die Spannungen 12P und 12N zugeführt. Legt man High Pegel an die Pin 12/13 bzw. 9/10 von D61 (TxDA bzw. TxDB), müssen die zugehörigen LED leuchten, zwischen X2:B21 und X2:A21 bzw. X2:B22 und X2:A22 müssen 24V anliegen. Verbindet man X2:A24 und X2:B24 bzw. X2:A25 und X2:B25, muss an Pin 6 bzw. 3 von D61 (RxDA bzw. RxDB) High Pegel nachweisbar sein.

Nach dieser Kontrolle werden die |CTC|\s D55, D58, die |PIO|\s D56, D59 und die |SIO| D57 eingelötet. Mittels Prüfprogrammen (z.B. Emulator) können diese, wenn die Möglichkeit besteht, auf ordnungsgemäße Funktion kontrolliert werden. Abschließend wird das |KMBG| Interface (A1) bestückt. Dieses wird nach vollständigem Aufbau des |PC/M| Computers mit dem Betriebssystem (Monitor) in Betrieb genommen.

Damit ist die zentrale Platine vollständig bestückt und kann im Zusammenspiel mit Betriebssystem (programmierte |EPROM|\s D14 bis D16), Tastatur, |BSA| und einem |KMBG| als lauffähiges System auf den vollen Funktionsumfang getestet werden.

.. index:: triple: PC/M; Inbetriebnahme; Bildschirmansteuerung

.. rubric:: Bildschirmansteuerung

Die |BSA| wird direkt über den Systembus (X3 - X103) oder über eine Rückverdrahtung (Erweiterungsmöglichkeit anderer Baugruppen) an die zentrale Platine angekoppelt. Vor Beginn der Inbetriebnahme sind die Brücken 1 bis 4, 6-10, E3, R, D, Z0, Z1, Z2, 5P und GND, sowie bei |BAS| Signalauskopplung die Brücke A zu realisieren.

Zuerst sollte der Quarzgenerator (D101) bestückt werden. Mittels C101 wird am Pin 6 von D101 die Frequenz auf 10500 |kHz| abgeglichen. Anschließend werden alle Zähler ICs (D102, D123 bis D127) sowie D103 und D121 bestückt. D102 arbeitet als 1:7 Teiler. An dessen Ausgang QC (Pin 7) muss eine Pulsfolge mit der Frequenz von 1500 |kHz| anliegen. An den Zählerausgängen müssen Impulsfolgen sinkender Frequenz (von D123 - QA bis D127 - QB) nachweisbar sein. Am Ausgang der Impulsverkürzerschaltung (D103 - Pin 8) wird nun die Pulsfolge für die Übernahme jedes Bytes in den Parallel-Serien-Wandler kontrolliert, deren H-Impulse schmaler als die der Pulsfolge an D102 - QC sind. Nach dem Einlöten der ICs D117, D118, D121 und D122 sowie der passiven Bauelemente werden an den Eingängen des |BAS| Mischers das Bildsynchron- (D122 - Pin 4), das Zeilensynchron- (D122 - Pin 5) und das Austastsignal (D121 - Pin 11) sowie am Ausgang das |BAS| Signal (VT101) kontrolliert. Entsprechen die Verläufe den Bildern und , werden alle Bauelemente bis auf den |BWS| (U 214), den Zeichengenerator (U 2716) und den Modulator bestückt. Sind die Adressen A11 bis A15 und das Signal /RFSH gleich High (in den /RFSH Zyklen darf die |CPU| nicht auf die |BSA| zugreifen), besitzt Ausgang 7 des Dekoders D114 (Pin 7) Low Potential. Beim Aktivieren von /MREQ liegt am /OE Eingang des Datentreibers D111 (Pin 9) sowie am Multiplexer (Pin 1) Low Potential. Pin 8 von D116 wird Low, wenn /WR aktiv ist. Nach dieser Kontrolle wird der Zeichengenerator D113 in die Fassung gesteckt und die Multiplexerausgänge A0 bis A7 mit den Eingängen des Zeichenlatches D112 verbunden. Es werden die |BAS| Auskoppelstufe (VT101) und der Modulator bestückt. Das |BAS| Signal kann an den Punkten B bzw. phasenverschoben an /B abgegriffen werden. Mit dem Trimmer C102 wird eine Frequenz im Fernsehband I (47 |...| 68 |MHz|) eingestellt, wobei eine Umdimensionierung auf Band III ohne weiteres möglich ist. Auf dem Bildschirm erscheint nun der gesamte Zeichensatz des Zeichengenerators. Der Kontrast kann mit R101 des Modulators korrigiert werden. Die Verbindungen zwischen Zeichenlatch und Multiplexer werden wieder aufgetrennt. Der |BWS| wird mit den 4 ICs U 214 bestückt. Die sonst kompatiblen CMOS |RAM|\s U 224 können wegen ihrer dynamischen Übernahme nicht eingesetzt werden! Nun muss nach dem Einschalten des Computers ein feststehendes Zufallsmuster, bestehend aus dem Zeichenvorrat, symmetrisch auf dem Bildschirm erscheinen. Jede Speicherzelle der U 214 nimmt beim Zuschalten der Betriebsspannung eine Vorzugsstellung ein, woraus sich das dargestellte Zeichen ergibt.

Abschließend kann die |BSA| über den Systembus bzw. direkt mit der bereits fertiggestellten Zentralen Platine verbunden werden.

.. index:: triple: PC/M; Zusatzdaten; FA 5/88-04 (ZD/3)

.. list-table:: FA 5/88-04 (ZD/3)
   :name: kcsystems-mach-pcm-fa058804-zd3
   :class: longtable
   :align: center
   :width: 80 %
   :header-rows: 1

   * - FA 5/88-04 (ZD/3)

   * - .. figure:: bild-25.png
          :name: kcsystems-mach-pcm-bild-25
          :figclass: align-center
          :align: center
          :width: 480 px
          :alt: Taktdiagramm Zeilenerzeugung

          Taktdiagramm Zeilenerzeugung

.. index:: triple: PC/M; Zusatzdaten; FA 5/88-04 (ZD/4)

.. list-table:: FA 5/88-04 (ZD/4)
   :name: kcsystems-mach-pcm-fa058804-zd4
   :class: longtable
   :align: center
   :width: 80 %
   :header-rows: 1

   * - FA 5/88-04 (ZD/4)

   * - .. figure:: bild-26.png
          :name: kcsystems-mach-pcm-bild-26
          :figclass: align-center
          :align: center
          :width: 480 px
          :alt: Taktdiagramm Bilderzeugung

          Taktdiagramm Bilderzeugung

.. index:: triple: PC/M; Inbetriebnahme; Tastatur

.. rubric:: Tastatur

Die Tastaturelektronik findet auf einer Leiterplatte der Größe 105 |mm| x 75 |mm| Platz. Sie kann ohne Zwischenprüfungen vollständig aufgebaut werden. Die LED Treiber werden statisch durch Anlegen von High bzw. Low Potential an den Anschlüssen X201:C4 bis X201:C9 bei an LED0 bis LED5 angeschlossenen LED (VQA 13, 23, 33 o.a.) getestet. Die Tasten sollten auf eine Leiterplatte entsprechend |PC_M_B18_N| angeordnet und nach ihrer Anordnung in der Matrix verdrahtet werden. Die Tastaturmatrix wird über die Anschlüsse S1 bis S8, Z1 bis Z8, Z1A, Z2A, SP, SHIFT, CTRL und GND an die Tastaturelektronik angeschlossen. Eine folgende Prüfung bezieht sich auf die ordnungsgemäße Erzeugung des ASCII Kodes bei Tastenbetätigung und die richtige Einbindung der Shift- und Controlfunktion (Mehrfachbelegung der Tasten). Dazu können an die Ausgänge TD0 bis TD6 und TAST über Vorwiderstände (ca. 470 |Omega|) LED gegen Masse angeschlossen werden. Das Signal TAST muss mit jeder Betätigung einer sich in der Matrix befindenden Taste High Signal aufweisen. Die an TD0 bis TD6 angeschlossenen LEDs zeigen binär den ASCII Kode der gedrückten Taste an.

.. index:: triple: PC/M; Stromlaufplan; FA 6/88-03 (ZD/1)

.. list-table:: FA 6/88-03 (ZD/1)
   :name: kcsystems-mach-pcm-fa068803-zd1
   :class: longtable
   :align: center
   :width: 80 %
   :header-rows: 1

   * - FA 6/88-03 (ZD/1)

   * - .. figure:: bild-18.png
          :name: kcsystems-mach-pcm-bild-18
          :figclass: align-center
          :align: center
          :width: 480 px
          :alt: Realisierte Tastenanordnung

          Realisierte Tastenanordnung

.. index:: triple: PC/M; Inbetriebnahme; Stromversorgung

.. rubric:: Stromversorgung

Die Leiterplatte kann bis auf den Überspannungsschutz des 5P Reglers (VT302, VT304) vollständig bestückt werden. Danach wird Wicklung 4 des Trafos an den Eingang der Graetzbrücke des 12N Regler angeschlossen. Nach dem Einschalten muss LED VD304 leuchten und am Ausgang +12V GS anliegen. Desgleichen wird mit dem 5N Regler und Wicklung 3 verfahren. Liegen die -5 V GS an (LED VD303 leuchtet), muss Relais K301 anziehen, dessen Kontakt K301/1 im 12P Regler schließen und K301/2 öffnen und somit den Regler freigeben. Nun kann der 12P Regler über seine Brückeneingänge an Wicklung 2 des Trafos angeschlossen werden. Stehen am Ausgang +12 V GS an (LED VD302 leuchtet), kann der 5P Regler in Betrieb genommen werden. Der Längstransistor VT303 (KU 607) wurde auf einem Aluminiumkühlblech der Größe 200 |mm| x 100 |mm| x 2,5 |mm| montiert. Nach Anschluss der Trafowicklung 1 und Einschalten der Netzspannung müssen am Ausgang +5 V GS anstehen. Die LED VD301 muss das Vorhandensein der Spannung signalisieren. Mittels des Einstellreglers R301 wird die Strombegrenzung auf ca. 3 A eingestellt. Abschließend werden der 5P Überspannungsschutz bestückt und alle Spannungen noch einmal nachgemessen und auf Stabilität bei Belastung kontrolliert. Bei Verwendung von auf Funktion geprüften Bauelementen stellt der Aufbau der Stromversorgung keine Schwierigkeit dar.

.. index:: triple: PC/M; Inbetriebnahme; Computer

.. rubric:: Der komplette PC/M Computer

Wurde der Aufbau und die Inbetriebnahme der einzelnen Baugruppen entsprechend Punkt 3.5. erfolgreich durchgeführt, können alle Baugruppen miteinander verschaltet und der |PC/M| Computer als Einheit getestet werden. Als erstes werden die Anschlüsse 5P, 5N und GND der Stromversorgung auf die Zentrale Platine geführt. Nach dem Einschalten müssen die LED der |IFSS| Schnittstellen leuchten, die Spannung 5P muss an allen Punkten der Zentralen Platine stabil (minimal 4,75 V) anliegen, die Stromaufnahme darf 1,5 A nicht übersteigen. Nun wird die Tastatur angeschlossen. Dabei darf die Stromaufnahme maximal um 90 |mA| ansteigen. Nachdem die |BSA| mit der Zentralen Platine verbunden wurde, muss die Stromaufnahme bei ca. 2,5 A liegen. Jetzt können, bei abgeschalteter Betriebsspannung, die programmierten |EPROM|\s D14 bis D16 gesteckt werden. Bei ordnungsgemäßer Funktion aller Baugruppen und ihrer Verbindung muss nach dem Einschalten des Computers, beginnend auf der 1. Bildschirmzeile, die Systemausschrift zu sehen sein. In diesem Zustand kann die Tastatur überprüft werden, ob bei Betätigung der Tasten das entsprechende Zeichen auf dem Bildschirm dargestellt wird.

Nun bleiben noch die Kontrolle des Kassetteninterfaces, des |NMI| Generators sowie ein umfassender Test des |PC/M| Computers durch die Arbeit mit den einzelnen Kommandos und Funktionen der beschriebenen Software.

Bei der Arbeit mit dem |KMBG|, muss dessen Tonkopf auf beste Wiedergabe der hohen Frequenzen eingestellt sein. Geschwindigkeits-, Gleichlauf- und Pegelschwankungen haben auf das beim |PC/M| Computer zum Einsatz kommende Verfahren kaum einen Einfluss. Magnetische Fehlstellen, sogenannte Drop Outs, können dabei jedoch das beste Programm unbrauchbar machen. Aus diesem Grund wird empfohlen, jedes Programm aus Sicherheitsgründen zweimal nacheinander auf Kassette zu speichern. Das Überspielen einer 124 |kB| umfassenden "Diskette" von Band dauert ca. 5 Minuten. Es wird nun ein Programm von Kassette eingelesen und dabei der Einstellregler R1 auf der Zentralen Platine so lange verändert, bis der Computer fehlerfrei alle Blöcke des Programmes einliest. Anschließend erfolgt mit R2 bei Aufnahme eines Programmes der Abgleich, bis eine verzerrungs- und übersteuerungsfreie Aufnahme erreicht wird, die fehlerfrei wieder eingelesen werden kann. Eventuell muss C4 (4,7 |nF| - 100 |nF|) verändert werden.

.. spelling::

   Zeilensynchron
   Geschwindigkeits
   verzerrungs

.. Local variables:
   coding: utf-8
   mode: text
   mode: rst
   End:
   vim: fileencoding=utf-8 filetype=rst :
