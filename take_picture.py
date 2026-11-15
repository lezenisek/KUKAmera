
import cv2

# erst installieren: pip install opencv-python
from pathlib import Path

from datetime import datetime

# Ordner für die Bilder erstellen
ordner = Path("bilder")
ordner.mkdir(exist_ok=True)

# Kamera öffnen (0 = Standardkamera, 1 = die von Logitech))
kamera = cv2.VideoCapture(1, cv2.CAP_DSHOW)

if not kamera.isOpened():
    print("Fehler: Kamera konnte nicht geöffnet werden.")
    exit()

# Hohe Auflösung anfordern
kamera.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
kamera.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

print("Kamera bereit!")
print("Enter = Foto aufnehmen")
print("q + Enter = Programm beenden")

while True:
    eingabe = input("\nEingabe: ")

    if eingabe.lower() == "q":
        break

    if eingabe == "":
        # Einige Frames lesen, damit das Bild aktuell ist
        for _ in range(5):
            erfolg, bild = kamera.read()

        if erfolg:
            # Eindeutigen Dateinamen erstellen
            zeit = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
            dateiname = f"bild_{zeit}.png"
            pfad = ordner / dateiname

            # Bild verlustfrei speichern
            gespeichert = cv2.imwrite(
                str(pfad),
                bild,
                [cv2.IMWRITE_PNG_COMPRESSION, 0]
            )

            if gespeichert:
                print("Bild erfolgreich aufgenommen!")
                print(f"Dateiname: {dateiname}")
                print(f"Speicherort: {pfad.resolve()}")
            else:
                print("Fehler beim Speichern!")
        else:
            print("Fehler bei der Bildaufnahme!")

kamera.release()
print("Kamera geschlossen.")
