.. index:: pair: CP/A, Version 3; BDOS

Besonderheiten des BDOS
#######################

|CP/A| unterscheidet sich durch folgende inhaltlichen Veränderungen im |BDOS|
vom Betriebssystem |CP/M|, Version 2.2 (bei gleichem Hauptspeicherbedarf von
:addr:`E00H` Bytes):

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
  :ref:`osys/cpa/CPA3_86.DOK/besonderheiten-des-bios:Tastatur`) erreicht
  werden. Verbunden mit dem Wegfall der :kbd:`^S` Funktion konnte auf die
  Pufferung von Konsoleneingaben im |BDOS| völlig verzichtet werden, d.h. es
  werden keine Zeichen vertauscht, wenn zwischen |BDOS| und direkter |BIOS|
  Tastatureingabe gewechselt wird.

- :kbd:`^S` und :kbd:`DEL` wirken bei der Stringeingabe über das |BDOS|
  wie :kbd:`^H`.

- Um eine Arbeit ohne Laufwerk :file:`A` (weil es gerade defekt ist und die
  Laufwerke nicht umgesteckt werden können) zu erlauben, wird statt Laufwerk
  :file:`A:` dasjenige Laufwerk, von dem aus der Kaltstart erfolgte bei der
  |BDOS| Funktion "Disk Reset" selektiert. Da mit dieser |BDOS| Funktion auch
  die Abarbeitung von :program:`SUBMIT` Strömen verbunden ist, muss daher beim
  Aufruf von :program:`SUBMIT` das Kaltstart Laufwerk als Standardlaufwerk
  zugewiesen sein, damit der Kommandostrom dort abgelegt wird! Erfolgte der
  Kaltstart von Laufwerk :file:`A`, so hat diese |BDOS| Änderung keine
  Auswirkungen.

- :reg:`IX` und :reg:`IY` werden durch das |BDOS| (und daraus resultierende
  |BIOS| Aufrufe) nicht zerstört.

- Es wurde ein Kopierschutz integriert, das Kopieren geschützter Dateien
  führt zu der Fehlermeldung :console:`File R/O` (unabhängig vom evtl.
  R/O Status der Dateien). Wie dieser Schutz funktioniert, wird hier nicht
  verraten.

.. Local variables:
   coding: utf-8
   mode: text
   mode: rst
   End:
   vim: fileencoding=utf-8 filetype=rst :
