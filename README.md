# MacCraft

Ein einfaches Minecraft-ähnliches Spiel, das mit der Ursina Engine entwickelt wurde. In diesem Spiel kannst du in einer 3D-Welt Blöcke platzieren und entfernen.

![Bild](./pics/Screenshot%202025-03-08%20145451.png)


## Features

- **Boden:**  
  Ein 20x20 Raster aus Grasblöcken mit zufälligen Farben.

- **Bau-Modus:**  
  Mit der linken Maustaste kannst du graue Steinblöcke (Bau-Blöcke) an den Rändern vorhandener Blöcke hinzufügen.

- **Entfernungs-Modus:**  
  Mit der rechten Maustaste kannst du bestehende Blöcke entfernen.

- **First-Person-Steuerung:**  
  Der Spieler bewegt sich in der 3D-Welt mithilfe der First-Person-Steuerung.

## Voraussetzungen

- Python 3.6 oder höher
- [Ursina Engine](https://github.com/pokepetter/ursina)  
  Installation via:
  ```bash
  pip install ursina
  ```

## Installation und Ausführung

1. Lade den Quellcode herunter oder klone das Repository.
2. Stelle sicher, dass Python und die Ursina-Bibliothek installiert sind.
3. Speichere den folgenden Code in einer Datei, z. B. `maccraft.py`.
4. Starte das Spiel über die Kommandozeile:
   ```bash
   python maccraft.py
   ```

## Steuerung während des Spiels

- **Bewegung und Kamera:**  
  Der Spieler wird durch das `FirstPersonController`-Prefab gesteuert.
  - **W, A, S, D:** Bewegen den Spieler vorwärts, rückwärts und seitlich.
  - **Mausbewegung:** Steuert die Blickrichtung (First-Person-Perspektive).
  - **Leertaste:** Springt (falls aktiviert).

- **Interaktion mit Blöcken:**  
  - **Linke Maustaste:**  
    Wenn der Mauszeiger über einem Block schwebt, fügt ein Linksklick einen neuen grauen Steinblock hinzu. Dabei wird der neue Block an der Kante des angeklickten Blocks positioniert (mittels `mouse.normal`).
  - **Rechte Maustaste:**  
    Entfernt den Block, über dem die Maus schwebt, aus der Szene.


## Weiterführende Informationen

Weitere Informationen zur Ursina Engine und deren Möglichkeiten findest du in der [Ursina Dokumentation](https://www.ursinaengine.org/).

```

