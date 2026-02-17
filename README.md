# Metadata Extractor (ME) - System Analysis Tool (MVP)

**Metadata Extractor** ist ein in Python entwickelter **Prototyp (MVP)** für die automatisierte Suche und Überprüfung von Dateien. Das Hauptziel dieses Projekts war nicht, eine schicke Oberfläche zu bauen, sondern zu lernen, wie man mit Python stabil auf das Dateisystem zugreift und Datei-Informationen (Metadaten) zuverlässig ausliest.

---

## Kernfunktionen & Sicherheitsmerkmale

### 1. Daten-Fingerabdruck (SHA-256 Hashing)
Um sicherzugehen, dass digitale Spuren (Dateien) im Nachhinein nicht heimlich verändert wurden, erstellt das Skript für jede Datei einen eindeutigen Fingerabdruck.
* **Verfahren:** Hashing mit der **SHA-256** Methode.
* **Speicherschonend:** Das Skript liest Dateien stückchenweise ein (Stream-Processing). So stürzt das Programm nicht ab und der Arbeitsspeicher (RAM) läuft nicht voll, selbst wenn man riesige Dateien wie ganze Festplatten-Abbilder (Disk-Images) scannt.

### 2. Automatische Ordner-Suche
Das Tool kann Dateien auf dem Computer finden, auch wenn man den genauen Speicherort (Pfad) nicht kennt.
* **Technik:** Das Skript durchsucht mit dem Python-Befehl `os.walk` automatisch alle Haupt- und Unterordner.
* **Schlaue Suche:** Das Programm findet die gesuchte Datei auch dann, wenn man die Dateiendung weglässt.

### 3. Forensische Zeitstempel (Metadaten)
Das Programm liest wichtige Informationen direkt aus dem System aus, um den "Lebenslauf" einer Datei zu rekonstruieren.
* **MAC-Zeiten:** Das Skript liest aus, wann die Datei erstellt wurde (Created), wann sie zuletzt geändert wurde (Modified) und wann sie zuletzt geöffnet wurde (Accessed). 
* **Lesbarkeit:** Die vom Computer gelieferten, kryptischen "Unix-Zeitstempel" (Sekunden seit 1970) werden in ein normales, gut lesbares Datum umgewandelt.

---

## Installation & Setup

### Voraussetzungen
* Python 3.x
* Keine extra Installationen nötig (nutzt nur die in Python bereits eingebauten Standard-Bibliotheken).

### Schnellstart
1. Lade das Projekt herunter (Repository klonen).
2. Starte das Programm im Terminal mit dem Befehl: `python extractor.py`
3. Wähle im Hauptmenü, ob du Metadaten auslesen (1) oder Dateien vergleichen (2) möchtest.

> **Wichtiger Hinweis:** Die Suche durchforstet alle verfügbaren Laufwerke. Je nachdem, wie viele Dateien du auf dem PC hast, kann das ein paar Minuten dauern.

---

## Roadmap (Nächste Schritte)

- [ ] **Berichte speichern:** Das Programm soll die Ergebnisse am Ende automatisch in eine Textdatei (`.txt`) schreiben.
- [ ] **Magic Byte Analyse:** Das Skript soll Dateien nicht an ihrer Endung (z.B. `.pdf`), sondern an ihrem echten inneren Aufbau (Header-Signatur) erkennen.
- [ ] **Ladebalken:** Eine optische Anzeige für den Nutzer, damit er sieht, dass das Programm bei langen Suchen noch arbeitet und nicht eingefroren ist.

---

## Entwicklungsprozess (Meine Lernschritte)

1. **Phase 1 (Grundlagen):** Lernen, wie man mit Python SHA-256 Hashes berechnet und einfache Metadaten wie die Dateigröße ausliest.
2. **Phase 2 (Menü):** Einbau eines interaktiven Terminals, in dem der Nutzer Auswahlen treffen kann.
3. **Phase 3 (Ordner durchsuchen):** Verstehen und Einbauen von `os.walk`, damit Python sich selbstständig durch Ordnerstrukturen bewegt.
4. **Phase 4 (Stabilität):** Einbau von `try-except` Blöcken (Fehlerbehandlung). Wenn das Programm z.B. eine Datei nicht lesen darf (fehlende Rechte), soll es nicht abstürzen, sondern einfach bei der nächsten weitermachen.

---

## Über das Projekt
Mit diesem Projekt zeige ich, was ich in den ersten Monaten meiner Umschulung gelernt habe, besonders in den Bereichen:
* **Dateisysteme:** Wie man mit Python durch Ordner navigiert.
* **Datenintegrität:** Wie man mit Hashes prüft, ob eine Datei verändert wurde.
* **Fehlerbehandlung:** Wie man Programme stabil macht (`try-except`).
