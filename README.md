# KUKAmera 🤖

**Kamerabasierte Zeichenerkennung und Reproduktion mit einem KUKA-Industrieroboter**

## 1. Projektbeschreibung

KUKAmera ist ein Semesterprojekt im Bereich Robotik.

Ziel ist es, Zeichnungen mithilfe einer Kamera zu erfassen, mit Python zu verarbeiten und anschließend durch einen KUKA-Industrieroboter nachzeichnen zu lassen.

Das Projekt befindet sich derzeit in der Einrichtungs- und Entwicklungsphase.

## 2. Verwendete Technologien

| Technologie | Verwendung |
|---|---|
| Python 3.11 | Programmiersprache |
| Conda | Verwaltung der Python-Umgebung |
| NumPy | Numerische Berechnungen |
| OpenCV | Bildverarbeitung |
| Matplotlib | Visualisierung |
| scikit-image | Bildverarbeitung |
| NetworkX | Graphverarbeitung |
| CoppeliaSim Edu 4.7.0 | Robotersimulation |
| ZeroMQ Remote API | Kommunikation zwischen Python und CoppeliaSim |

## 3. Entwicklungsumgebung

Die bisherige Entwicklung erfolgt unter macOS mit Conda.

Die Python-Umgebung heißt `kuka-robotik`.

### Conda-Umgebung erstellen

```bash
conda env create -f environment.yml
```

### Conda-Umgebung aktivieren

```bash
conda activate kuka-robotik
```

Die benötigten Python-Abhängigkeiten werden über `environment.yml` verwaltet.

## 4. Installation überprüfen

Mit folgendem Befehl kann überprüft werden, ob die benötigten Python-Bibliotheken installiert sind:

```bash
python -c "import cv2, numpy, matplotlib, skimage, networkx; from coppeliasim_zmqremoteapi_client import RemoteAPIClient; print('Installation erfolgreich!')"
```

Der Importtest wurde erfolgreich durchgeführt.

## 5. Verbindung mit CoppeliaSim

Die Kommunikation zwischen Python und CoppeliaSim erfolgt über die ZeroMQ Remote API.

Die Verbindung wurde erfolgreich getestet.

### Python-Verbindungstest

```python
from coppeliasim_zmqremoteapi_client import RemoteAPIClient

client = RemoteAPIClient()
sim = client.require("sim")

print("Verbindung erfolgreich!")
print(
    "CoppeliaSim-Version:",
    sim.getInt32Param(sim.intparam_program_version)
)
```

### Testergebnis

```text
Verbindung erfolgreich!
CoppeliaSim-Version: 40700
```

Damit wurde bestätigt, dass Python erfolgreich mit CoppeliaSim Edu 4.7.0 kommunizieren kann.

## 6. Aktueller Projektstand

Folgende Schritte wurden bisher erfolgreich abgeschlossen:

- [x] Conda-Umgebung `kuka-robotik` eingerichtet
- [x] Benötigte Python-Bibliotheken installiert
- [x] Python-Importtest erfolgreich durchgeführt
- [x] CoppeliaSim Edu 4.7.0 gestartet
- [x] ZeroMQ Remote API eingerichtet
- [x] Verbindung zwischen Python und CoppeliaSim erfolgreich getestet

Weitere Funktionen, insbesondere die Roboterbewegung und die automatische Zeichenerkennung, wurden bisher noch nicht als erfolgreich getestet bestätigt.
