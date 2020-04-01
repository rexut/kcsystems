.. highlight:: none

.. index:: pair: PC/M; Floppy Betriebssystem

Floppy Betriebssystem für den PC/M Computer
###########################################

Dr.Mugler: 15.04.1990

Beschreibung zum Floppy Betriebssystem ab Version 3.0 für den |PC/M| Computer.

Mit der vorliegenden Betriebssystemversion steht Ihnen ein modulares und erweiterbares Betriebssystem kompatibel zu |CP/M| 2.2 zur Verfügung.

Die vorliegende Diskette enthält die Dateien im Quellformat. Sie können also nach Wunsch eigene Treiber einbauen oder Anpassungen an Ihre Hardware vornehmen. Sollten Sie Treiber nachrüsten die von allgemeinem Interesse sind, oder Sie finden Fehler, bitte ich um Kennzeichnung dieser als Kommentar in folgender Form::

   ;!!!!! hier ist geaendert worden.

Senden Sie bitte eine Kopie der geänderten Quelle zur Einarbeitung in das Quellprogramm an mich zurück.

.. topic:: Geänderten Quellen bitte zurück senden

   +-----------------------------------------------------------+
   | | Albrecht Mugler                                         |
   +-----------------------------------------------------------+
   | **Anmerkung:** *Anschriften aus datenschutzrechtlichen*   |
   | *Gründen entfernt!*                                       |
   +-----------------------------------------------------------+

.. | | PSF 24                                                  |
.. | | 9273 Oberlungwitz                                       |
.. +-----------------------------------------------------------+

.. index:: triple: PC/M; Floppy Betriebssystem; Disketteninhalt

Inhalt der Diskette
*******************

Auf der vorliegenden Diskette sind folgende Programme bzw. Module enthalten:

:LESEDAS.PCM:

   Dieses File.

   Weitere Files mit der Endung :mimetype:`.PCM` enthalten Informationen
   zum |PC/M| Computer.

:M80.COM:

   |Makroassembler| für I8080 und Z80 (|U880|).

:LINKMT.COM:

   |Linker| dazu

:CCP.ERL:

   Verschieblicher Code des |CCP| (von |CP/A|).

:BDOS.ERL:

   Verschieblicher Code des |BDOS| (von |CP/A|).

:BAS.ERL:

   Verschieblicher Code des Diskettenurladers
   (Übersetzung von :file:`PCMBAS.MAC`).

:PCMDEF.MAC:

   Kommentierte Quelle des Definitionsteils für das Betriebssystem zur
   Generierung spezieller Betriebssystemversionen.

:PCMBAS.MAC:

   Quellen des Betriebssystems.

:PCMBOOT.MAC:

   --- " ---

:PCMBIOS.MAC:

   --- " ---

:PCMCOM.MAC:

   --- " ---

:PCMDISK.MAC:

   --- " ---

:PCMIO.MAC:

   --- " ---

:PCMSVDB.MAC:

   --- " ---

:PCMVTAPE.MAC:

   --- " ---

:PCMURLAD.MAC:

   --- " ---

:PCMVAR.MAC:

   --- " ---

:SYSROM.COM:

   Standardsystem mit folgender Konfiguration:

   - A: System RAM Floppy bis 118 |kB|
   - B: MFS 1.6 624 |kB| |SCP| DD/DS/80T (für |K5601|)
   - C: MFS 1.4 304 |kB| |SCP| DD/SS/80T (für |K5600.20|)
   - D: MFS 1.2 148 |kB| |SCP| DD/SS/40T (für |K5600.10|)
   - Original |PC/M| Tastatur
   - Bildschirm 64 |x| 16 Original |PC/M|
   - mit ESC Steuerzeichen
   - Diskettenurlader + Diskettentreiber
   - |V-Tape|

:SYSDISK.COM:

   System wie oben, aber für Disketten zum nachladen, z.B. mit
   :program:`POWER`::

      LOAD SYSDISK.COM 4000
      WRITE 0 1 4000 96

   Beachten Sie bitte, dass nur Disketten mit Formate einer entsprechenden
   Anzahl von Systemspuren als Systemdiskette eingesetzt werden können
   (z.B. 148 |kB| |SCP|, 624 |kB| |SCP| usw.).

:PCMVDB.COM:

   Debugger für den |PC/M| Computer.

:PCMFORM.COM:

   Programm zur Formatierung von Disketten.

:PCMDISK.COM:

   Programm zur Einstellung des Diskettenformates (für Laufwerke 40T/SS,
   40T/DS, 80T/SS, 80T/DS).

:PCMVTC.COM:

   |V-Tape| Kopierprogramm für den |PC/M| Computer.

.. index:: triple: PC/M; Floppy Betriebssystem; Einstellen und Übersetzen

Einstellen und Übersetzen einer Version
***************************************

Wünschen Sie ein spezielles System, können Sie das File :file:`PCMDEF.MAC` mit einem Editor bearbeiten und an den entsprechenden Stellen Ihre Werte eintragen. Danach Übersetzen Sie mit M80 die Quelle in folgender Form::

   M80 BIOS.ERL=PCMBIOS/M/Z

Wurde die Übersetzung erfolgreich durchgeführt (No Fatal Error), erfolgt das Binden der Dateien in der durch den Kommentar beim Übersetzen angezeigten Form.

Beachten Sie bitte, dass es sich bei vorliegendem System um eine Arbeitsversion handelt, die ständig weiterentwickelt wird. Aufgrund des Umfanges der Quellen ist es nicht möglich, Betriebssystemversionen in jeder Version zu erstellen und zu testen.

Die Möglichkeiten der Generierung entnehmen Sie bitte dem File :file:`PCMDEF.MAC`.

.. Local variables:
   coding: utf-8
   mode: text
   mode: rst
   End:
   vim: fileencoding=utf-8 filetype=rst :
