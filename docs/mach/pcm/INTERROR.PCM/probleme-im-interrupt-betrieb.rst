.. index:: pair: PC/M; Probleme im Interrupt Betrieb

.. _kcsystems-mach-pcm-fa038805-k1:

Probleme im Interrupt Betrieb des PC/M
######################################

Im Falle der Nutzung von Interrupts im |PC/M| kann es zu Fehlern bei
der Abarbeitung kommen. Diese treten z.B. bei Installation der Uhr
(:file:`PCMDEF.MAC`) in der **Version 3.XX** auf.

Dieser Effekt kann behoben werden, wenn folgende Änderungen vorgenommen
werden:

- trennen der Verbindung :comp:`D9` (DS8212) Pin :pin:`13` von Pin :pin:`10`
  des davor liegenden Negators
- Einfügen eines Gatters eines DL008 an dieser Stelle; Ausgang des DL008 auf
  Pin :pin:`13` von :comp:`D9` und ein Eingang auf Pin :pin:`10` des Negators
- der verbleibende Eingang wird auf :signal:`/M1` gelegt; z.B. an D8 (DS8282)
  Pin :pin:`13`
- Der benötigte DL008 wird entweder "Huckepack" z.B. auf den auf der Platte
  vorhandenen DL008 aufgelötet, oder es wird die Schrittbetriebslogik außer
  Betrieb genommen und damit der freiwerdende DL008 verwendet.
