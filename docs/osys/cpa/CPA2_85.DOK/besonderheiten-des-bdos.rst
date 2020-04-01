.. index:: pair: CP/A, Version 2; BDOS

Besonderheiten des BDOS
#######################

|CP/A| unterscheidet sich durch folgende inhaltlichen Veränderungen im |BDOS|
vom Betriebssystem |CP/M|, Version 2.2:

- Beschleunigung der Arbeit mit Nicht-Default Laufwerken. Ist im :z80:`FCB`
  ein anderes als das Default Laufwerk angegeben (:z80:`FCB[0]<>0`) und dies
  ist nicht ausgewählt, so wird vom |BDOS| auf dieses umgeschaltet
  (:z80:`SELDSK`) und beim Verlassen nicht zurückgeschaltet, sondern nur
  eine hängende Umschaltung vermerkt. Dadurch wird eine ständige Übernahme
  der Disk Parameter durch das |BDOS| vermieden, so dass auch in diesem Fall
  die gleiche Geschwindigkeit wie bei der Arbeit mit Default Disketten
  erreicht wird.

- Wegfall der :kbd:`^S` Funktion. Das Stoppen von Konsolenausgaben kann als
  Spezialfall der allgemeinen Stop Funktion im |BIOS| (siehe
  :ref:`osys/cpa/CPA2_85.DOK/besonderheiten-des-bios:Belegung von Sondertasten`)
  erreicht werden. Verbunden mit dem Wegfall der :kbd:`^S` Funktion konnte
  auf die Pufferung von Konsoleneingaben im |BDOS| völlig verzichtet werden,
  d.h. es werden keine Zeichen vertauscht, wenn zwischen |BDOS| und direkter
  |BIOS| Tastatureingabe gewechselt wird.

.. Local variables:
   coding: utf-8
   mode: text
   mode: rst
   End:
   vim: fileencoding=utf-8 filetype=rst :
