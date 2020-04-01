.. highlight:: none

.. index:: pair: PC/M; Umgang mit den Dateien (V3.XX)

Information zum Umgang mit den Dateien (V3.XX)
##############################################

Dr. Albrecht Mugler: 2.3.1990

Die auf der Diskette befindlichen Betriebssystemversionen oder Ihre spezielle Anpassung sind wie folgt zu verwenden:

1. Die |ROM| Version ist auf Ihre |PC/M| |EPROM|'s der zentralen Platine zu programmieren. Zu beachten ist, dass bei Umrüstung auf |U2732| eine veränderte Adressaufteilung zur Anwendung kommt.
2. Die Diskettenversion wird wie folgt auf die Systemspuren Ihrer Diskette geschrieben (bitte selbst vornehmen). Dazu verwenden Sie z.B. das Programm :program:`POWER` (nachfolgend sind die erforderlichen Eingaben als Beispiel aufgeführt):

   :program:`POWER` aufrufen::

      POWER

   Laufwerk mit :file:`SYSDISK.COM` anwählen (oder Ihre spezielle Version)::

      B:

   System in den Speicher schreiben::

      LOAD SYSDISK.COM 4000

   Umschalten auf das Laufwerk mit der zukünftigen Systemdiskette (wenn erforderlich)::

      C:

   Schreiben des Systems in die Systemspuren::

      WRITE 0 1 4000 96

   Verlassen von :program:`POWER`::

      EXIT

   Damit erhalten Sie eine Systemdiskette (Voraussetzung ist das Vorhandensein einer ausreichenden Anzahl von Systemspuren), die mit dem Kommando :command:`C` (|BIOS| wird vom |BIOS| |ROM| gelesen und |CCP| und |BDOS| bei Bedarf von Diskette) oder :command:`K` (|BIOS|, |CCP| und |BDOS| werden von den Systemspuren der Diskette gelesen) gestartet werden kann.

Aufgrund des Umfanges der Programme und Dokumentation ist es nicht mehr möglich, diese auf Kassette in 124 |kB| oder 118 |kB| unterzubringen. Aus diesem Grund befinden sich auf den Kassetten alle Programme und Dateien einzeln. Sie können sich selbst nach Bedarf Kassetten zusammenstellen. Dazu ist bei den **Versionen 1.XX** und **2.XX** wie folgt vorzugehen:

- Rücksetzen des |PC/M|::

     <RESET>

- RAM Floppy Laufwerk A löschen::

     F A

- Laden des |BDOS|::

     L BDOS.COM DE00

- das |V-Tape| Kopierprogramm wird auf Adresse :addr:`0100H` geladen (auch :file:`VTCP.COM`, :file:`PCMVTC.COM` o.ä.)::

     L VTCOP.COM 0100

- Einstieg ins |CP/M| System::

     C

- das leere Programm :program:`GO` wird erzeugt::

     SAVE 0 GO.COM

- :command:`GO` wird aufgerufen und damit :command:`VTCOP` (auf Adresse :addr:`0100H`) gestartet::

     GO

- ein beliebiges Programm :file:`NAME.TYP` wird von Kassette auf RAM Floppy geladen; so lange, bis alle gewünschten Programme im RAM Floppy sind::

     T NAME.TYP

- Verlassen des V-Tape Kopierprogramm::

     Q

- Kontrolle, ob alles im RAM Floppy gespeichert ist::

     DIR

- Rückkehr ins Grundsystem (:kbd:`CTRL-_`)::

     <1fh>

- Speichern des RAM Floppy Inhaltes auf Kassette::

     W MEINE.DSK A

In der **Diskettenversion 3.XX** erfolgt sinnvollerweise die Übernahme auf Diskette ebenfalls mit dem |V-Tape| Kopierprogramm.

.. Local variables:
   coding: utf-8
   mode: text
   mode: rst
   End:
   vim: fileencoding=utf-8 filetype=rst :
