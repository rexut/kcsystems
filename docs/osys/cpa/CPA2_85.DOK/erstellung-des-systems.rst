.. highlight:: none
   :linenothreshold: 1

.. index:: pair: CP/A, Version 2; Erstellung des Systems

Kurzbeschreibung der Erstellung des Systems CP/A
################################################

Das Übergabesystem besteht aus folgenden Files:

.. .. tabularcolumns:: |p{4cm}|p{11cm}|

.. table:: |CP/A| V2(1985) - Dateien des Übergabesystem (Werkzeuge und Quellen)
   :widths: 25, 75
   :width: 80%

   +------------------------+-----------------------------------------------+
   | :file:`FORMAT.COM`     | Formatieren / Kopieren Disketten              |
   +------------------------+-----------------------------------------------+
   | :file:`SYSTEM.TRK`     | Kaltstart Systemspuren 0,1                    |
   +------------------------+-----------------------------------------------+
   | :file:`PLO.COM`        | physikalisches Lesen / Schreiben Diskette     |
   +------------------------+-----------------------------------------------+
   | :file:`CPABAS.ERL`     | ERL Files zum Linken einer neuen              |
   +------------------------+-----------------------------------------------+
   | :file:`BDOS.ERL`       | Systemversion                                 |
   +------------------------+-----------------------------------------------+
   | :file:`CCP.ERL`        |                                               |
   +------------------------+-----------------------------------------------+
   | :file:`BIOS*.MAC`      | Quelltextmodule des |BIOS|                    |
   +------------------------+-----------------------------------------------+

Es wird ein bereits arbeitsfähiges |CP/M| kompatibles System vorausgesetzt.
Belegung der Diskettenlaufwerke als Beispiel:

:C: zukünftige Kaltstartdiskette
:B: Übergabesystem
:A: Systemprogramme :program:`ZSID`, :program:`WS`, :program:`PIP`,
    :program:`M80`, :program:`LINKMT`

Ablauf der Systemübernahme (Operatoreingaben klein):

0) Sicherheitskopie vom Übergabesystem anlegen::

      b:format

   - in Laufwerk C eine (leere) Diskette legen und als Source Laufwerk B angeben
   - Diskette aus Laufwerk C entnehmen und weit weg legen

1) Formatieren der zukünftigen Kaltstartdiskette::

      b:format

   - auf Laufwerk C, ohne Source Diskette, ohne Volume Angabe

2) Anlegen der Systemspuren::

      zsid b:plo.com
      g                       (( Verschieben PLO nach A000H ))
      ib:system.trk
      r
      s81
      2                       (( neue Disk. in Laufw. C ))
      0                       (( Spur 0 ))
      1                       (( Sector 1 ))
      #52                     (( 2 Spuren ))
      1                       (( ohne Sectorversatz ))
      0
      1                       (( ab 100H ))
      1                       (( schreiben ))
      ga000
      j                       (( Anfrage auf Schreiberlaubnis beantworten ))
      ^C

3) Modifizieren des Quelltextes von :file:`BIOS.MAC` entsprechend der aktuellen
   Gerätekonfiguration. Sämtliche Angaben dazu befinden sich am Anfang
   des Quelltextes.

4) Übersetzen der neuen |BIOS| Version::

      b:                      (( St.laufw. B, da INCLUDE in BIOS.MAC ))
      a:m80 bios.erl=bios

5) Linken der Systemversion::

      a:linkmt c:@os=cpabas,bdos,ccp,bios/p:c680

6) Ausprobieren der neuen Version

   - Laufwerksverriegelungen von A und B öffnen
   - Kaltstart

   Die Ausschrift :console:`ACCOUNT?` nach dem Kaltstart zeigt den
   fehlerfreien Ablauf. Das Abrechnungssystem (:program:`ACCOUNT`
   und weitere Programme) kann bei Bedarf vom |IIR| nachgefordert werden.

.. Local variables:
   coding: utf-8
   mode: text
   mode: rst
   End:
   vim: fileencoding=utf-8 filetype=rst :
