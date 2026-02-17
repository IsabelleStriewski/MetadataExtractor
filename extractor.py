import os
import hashlib
from datetime import datetime

import time
import string

def get_file_hashes (filepath):
    sha256_hash = hashlib.sha256()                              # berechnet SHA Hash zur Sicherstellung der Datenintegrität
    with open (filepath, "rb") as f:
        for byte_block in iter (lambda: f.read(4096), b""):      # Datei in Blöcken lesen, da besser bei großen Dateien        
            sha256_hash.update (byte_block)
    return sha256_hash.hexdigest()

def get_metadata (filepath):                                     # extrahiert grundlegende Dateisystem-Metadaten
    stats = os.stat (filepath)
    
    return {
        "filename": os.path.basename (filepath),
        "size_bytes": stats.st_size,
        "created": datetime.fromtimestamp (stats.st_ctime).strftime ('%Y-%m-%d %H:%M:%S'),
        "last_modified": datetime.fromtimestamp (stats.st_mtime).strftime ('%Y-%m-%d %H:%M:%S'),
        "last_accessed": datetime.fromtimestamp (stats.st_atime).strftime ('%Y-%m-%d %H:%M:%S'),
        "sha256": get_file_hashes (filepath)
    }

def finde_datei (suchbegriff):
    treffer = []
    laufwerke = []                                               # Liste aller Laufwerke (Buchstaben, wie Windows)
    import string
    for buchstabe in string.ascii_uppercase:
        laufwerk = f"{buchstabe}:\\"
        if os.path.exists(laufwerk):
            laufwerke.append(laufwerk)
    
    print(f"\nSuche auf folgenden Laufwerken: {laufwerke} ... das kann einen Moment dauern.")

    # 2. Jedes Laufwerk einzeln durchgehen
    for lw in laufwerke:
        # 'onerror=None' sorgt dafür, dass das Programm bei gesperrten 
        # Systemordnern (wie 'System Volume Information') nicht einfach abstürzt.
        for root, dirs, files in os.walk(lw):
            for name in files:
                dateiname_rein, endung = os.path.splitext(name)
                
                if dateiname_rein.lower() == suchbegriff.lower() or name.lower() == suchbegriff.lower():
                    voller_pfad = os.path.join(root, name)
                    treffer.append(voller_pfad)
                    # Kleines Feedback für den User, damit man sieht, dass er arbeitet
                    print(f"  -> Gefunden: {voller_pfad}")          
    return treffer
    
def main():

    print ("\n\n=== Metadata Extractor ===\n\n")

    while True:                                         
        time.sleep(1)
        print ("\n=== Metadata Extractor Menü ===\n")
        print ("1. Datei analysieren")
        print ("2. Datei-Integrität prüfen")
        print ("3. Programm beenden")
     
        wahl = input ("\nWas möchtest du tun? (1,2 oder 3): ")   # Auswahl durch Nutzer

        if wahl == "1":
            name_eingabe = input("\nWelche Datei soll geprüft werden? (ohne oder mit Endung): ")
            ergebnisse = finde_datei(name_eingabe)

            ziel_datei = None                           # Datei soll erst am Ende analysiert werden

            if len(ergebnisse) == 0:                    # keine Datei gefunden
                time.sleep (1)
                print("Es konnte keine Datei mit diesem Namen gefunden werden.")
            elif len(ergebnisse) == 1:                  # genau eine Datei gefunden
                ziel_datei = ergebnisse[0]        
                time.sleep (1)
                print (f"\nEindeutiger Fund: {ziel_datei}")
            else:                                       # mehrere Dateien mit gleichen Namen gefunden
                print("\nEs wurden mehrere Dateien gefunden:")
                for i, datei in enumerate (ergebnisse, 1):
                    print(f"\n{i}. {datei}")

                auswahl = input (f"\nWelche Datei soll analysiert werden, bitte die Nummer angeben: ")
                try:
                    wahl_index = int (auswahl)
                    if 1 <= wahl_index <= len(ergebnisse):
                        ziel_datei = ergebnisse[wahl_index - 1]
                #        print(f"\nDiese Datei wird überprüft: {ziel_datei}")
                    else:
                        print(f"\nUngültige Nummer. Bitte wähle, Sie eine Nummer zwischen 1 und {len(ergebnisse)}.")
                
                except ValueError:                      # falls der User keine Zahl eingibt 
                    print("Fehler: Bitte geben Sie eine Zahl ein.")

            if ziel_datei:
                print(f"\nExtrahiere Metadaten für {ziel_datei}...\n")
                time.sleep(1)
                data = get_metadata(ziel_datei)
                
                print(f"=== Forensischer Bericht für {data['filename']} ===\n")
                for key, value in data.items():
                    print(f"{key.replace('_', ' ').capitalize()}: {value}")  

        elif wahl == "2":
            dateipfad = input ("\nWie lautet der Dateipfad? ")
            if os.path.exists (dateipfad):
                user_hash = input ("Bitte geben sie den Original Hash-Wert der Datei ein: ")
                print ("\nDatei wird analysiert...\n")
                time.sleep (1)
                aktueller_hash = get_file_hashes (dateipfad)
                if aktueller_hash == user_hash.strip().lower():
                    print ("Datei ist integer, der Hash-Wert stimmt überein.")
                else:
                    print ("\nWarnung! Der Hash-Wert stimmt nicht überein. Die Datei wurde manipuliert.")
                    print (f"\nErwarteter Hash: {user_hash.strip().lower()}")
                    print (f"Gefundener Hash: {aktueller_hash}\n")
            else:
                print ("\n Datei nicht gefunden.\n")            

        elif wahl == "3":
            time.sleep(2)
            print ("\nMetadata Extractor wird beendet...\n\n")
            break
        else:
            print ("\nUngültige Eingabe, bitte wähle 1, 2 oder 3!\n")

if __name__ == "__main__":
    main()

