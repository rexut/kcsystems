.. index:: pair: CP/A, Version 3; Änderungen

Kurzübersicht zu letzten Änderungen an CP/A
###########################################

:CCP:

   - Prompt :console:`du>` bei :envvar:`USER` > 0
   - Kommandofiles werden bei :envvar:`USER` > 0 auch unter :envvar:`USER` 0
     und wenn dort erfolglos auf der Systemdiskette (im Kaltstart Laufwerk)
     unter :envvar:`USER` 0 gesucht (gilt nicht für nachgeladene Files!)
   - neue residente Kommandos: :command:`CLK`, :command:`GO`, :command:`EXT`,
     :command:`RES`, :command:`HELP`


:BDOS:

   - Um eine Arbeit ohne Laufwerk :file:`A` zu erlauben, wird das erste
     Default Laufwerk nach Kaltstart bei jedem "Disk Reset" selektiert.

:Floppy:

   - Beschleunigung der Arbeit mit 8" Disketten am Bürocomputer, vor allem
     beim Kopieren zwischen 2 Laufwerken

:Bildschirm:

   - 00h wird als :z80:`NOP` Steuerzeichen interpretiert
   - Bit7 wird immer gelöscht (kein Kursor mehr)
   - wahlweise Unterstützung |ADM-3A| Steuerzeichenfolgen

:Tastatur:

   - Vereinfachung der Einbindung weiterer Tastaturen
   - Integration Spezialtastatur IH Mittweida
   - Möglichkeit der nutzereigenen Stringdefinition durch
     Bildschirmsteuerzeichenfolge oder im Stoppzustand
   - :kbd:`^Q` Prefix (:program:`WordStar` Positionsfuktionen) beim Betätigen
     der Cursortaste mit vorherigem :kbd:`ET2` (nicht bei K76x4 und |PC1715|
     Tastatur) bzw. gleichzeitigem :kbd:`CTRL`
   - Änderung der Standardbelegung für Tasten :kbd:`PF6` und :kbd:`PF7`:

     :PF6: :kbd:`^OD` :program:`WordStar`: Anzeige Steuerzeichen ein/aus (zuvor
           :kbd:`^Q`  :program:`WordStar`: Positionsmenü)
     :PF7: :kbd:`^OG` :program:`WordStar`: Absatz einrücken um jeweils einen
           Tabulator (zuvor :kbd:`^P` :program:`WordStar`: Druckmenü, wenig
           benutzt)

   - Unterstützung der Tasten :kbd:`PF10`, :kbd:`PF11`, :kbd:`PF12`

     :PF10: :kbd:`^KS` :kbd:`^QP` :program:`WordStar`: Speichern und
            Weiterarbeit mit der Datei an Position vor letztem Kommando
     :PF11: :kbd:`^KB` :program:`WordStar`: Blockanfangsmarke setzen/löschen
     :PF12: :kbd:`^KK` :program:`WordStar`: Blockendemarke setzen/löschen

   - Unterstützung der Taste  :kbd:`F13` (nur |PC1715| Tastatur):

     :F13: :kbd:`^KV` :program:`WordStar`: Blocktransport (einfügen mit löschen)

:Drucker:

:Stopfunktion:

   - Gepufferte Tastaturzeichen werden wie bei Monitoraufruf gelöscht
   - Möglichkeit der Definition von Nutzerstringtasten

.. Local variables:
   coding: utf-8
   mode: text
   mode: rst
   End:
   vim: fileencoding=utf-8 filetype=rst :
