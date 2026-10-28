# VL Robotik – Kamerabasierte Zeichenerkennung mit KUKA KR6


## 1. Projektübersicht

**Projekttitel:**  
Kamerabasierte Erkennung und Reproduktion von Zeichen mittels eines KUKA KR6

**Programmiersprachen:**
- Python  
- KUKA Robot Language (KRL), sofern eine KSS-Steuerung verwendet wird

**Haupttechnologien:**
- Industrielle Robotik
- Bildverarbeitung
- Computer Vision
- Koordinatentransformation
- Roboterprogrammierung
- Bahnplanung

---


## 2. Projektbeschreibung

Im Rahmen dieses Projekts soll ein KUKA-Industrieroboter mithilfe einer Kamera verschiedene Zeichen erkennen und anschließend selbstständig reproduzieren.

Dazu wird ein Zeichen auf einem Blatt Papier platziert und durch eine Kamera aufgenommen.

Die Bilddaten werden mithilfe von Python und OpenCV verarbeitet. Dabei werden die Linien des Zeichens erkannt und in Koordinaten umgewandelt.

Anschließend wird aus diesen Koordinaten eine geeignete Zeichenbahn erstellt.

Diese Zeichenbahn wird an die KUKA-Robotersteuerung übertragen beziehungsweise als Roboterprogramm bereitgestellt.

Der Roboter reproduziert das erkannte Zeichen mithilfe eines am Roboterflansch befestigten Stiftes auf einer Zeichenfläche.


### Projektziel

Entwicklung eines Systems, das:

1. Ein Zeichen mit einer Kamera erfasst.
2. Das Zeichen automatisch erkennt.
3. Die Zeichenkontur beziehungsweise Mittellinie extrahiert.
4. Die erkannten Punkte in reale Koordinaten umrechnet.
5. Eine geeignete Roboterbahn erstellt.
6. Die Bahn an die Robotersteuerung übergibt.
7. Das Zeichen mit dem KUKA KR6 nachzeichnet.
8. Die Genauigkeit des Ergebnisses überprüft.

---

## 3. Benötigte Hardware

### 3.1 Roboter und Steuerung

- [ ] KUKA KR6 Industrieroboter
- [ ] Passende KUKA-Steuerung, z. B. KR C4
- [ ] KUKA smartPAD
- [ ] Freigegebene und abgesicherte Roboterzelle
- [ ] Geeignete Kommunikationsschnittstelle
- [ ] Optional: federnder Stifthalter

### 3.2 Kamerasystem

- [ ] USB-Webcam oder Industriekamera
- [ ] Kamerahalterung oder Stativ
- [ ] Geeignete Beleuchtung
- [ ] Kalibriermuster oder Referenzmarkierungen

### 3.3 Zeichenwerkzeug

- [ ] Stifthalter für den KUKA-Roboter
- [ ] Filzstift oder Whiteboardmarker
- [ ] Papier oder Whiteboard
- [ ] Stabile Zeichenunterlage
- [ ] Befestigung für das Papier


---

## 4. Benötigte Software

| Software | Verwendung |
|---|---|
| Python 3 | Bildverarbeitung und Datenverarbeitung |
| OpenCV | Erkennung von Zeichen und Linien |
| NumPy | Mathematische Berechnungen |
| Matplotlib | Visualisierung der erkannten Zeichen |
| Visual Studio Code | Python-Entwicklung |

---

## Systemarchitektur

```text
        +----------------------+
        |        Kamera        |
        |  Aufnahme des Bildes |
        +----------+-----------+
                   |
                   v
        +----------------------+
        |    PC mit Python     |
        |       OpenCV         |
        +----------+-----------+
                   |
                   v
        +----------------------+
        |  Bildverarbeitung    |
        |  Zeichenerkennung    |
        +----------+-----------+
                   |
                   v
        +----------------------+
        | Koordinatenumrechnung|
        |    und Bahnplanung   |
        +----------+-----------+
                   |
                   v
        +----------------------+
        |   KUKA-Steuerung     |
        |  Roboterprogramm     |
        +----------+-----------+
                   |
                   v
        +----------------------+
        |       KUKA KR6       |
        |  Zeichnet das Symbol |
        +----------------------+
```

Die Kamera wird vorzugsweise fest oberhalb der Vorlage montiert.

Der Roboter erhält einen Stifthalter, mit dem er das erkannte Zeichen auf einer zweiten Zeichenfläche reproduziert.