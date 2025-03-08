# Importiere alle Module aus der Ursina-Bibliothek sowie den FirstPersonController
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

# Initialisiere die Ursina-App
app = Ursina()

# Erstelle einen Spieler mit First-Person-Steuerung
player = FirstPersonController()

# Füge einen Himmel zur Szene hinzu
Sky()

# Erstelle eine leere Liste zur Speicherung aller Boxen
boxes = []

# Funktion, die eine zufällige Farbe generiert
def random_color():
    # Erzeuge zufällige Werte für Rot, Grün und Blau (Skalierung auf 255)
    red = random.Random().random() * 255
    green = random.Random().random() * 255
    blue = random.Random().random() * 255
    # Rückgabe der RGB-Farbe
    return color.rgb(red, green, blue)

# Funktion zum Hinzufügen einer Box an einer gegebenen Position
def add_box(pos):
    boxes.append(
        Button(
            parent=scene,           # Füge die Box zur aktuellen Szene hinzu
            model="cube",           # Verwende ein Würfelmodell
            origin=0.5,             # Setze den Ursprung in die Mitte
            color=random_color(),   # Weise der Box eine zufällige Farbe zu
            position=pos,           # Positioniere die Box
            texture="grass"         # Verwende die Gras-Textur
        )
    )

# Neue Funktion für Steine, die grau sind.
def add_stone(pos):
    boxes.append(
        Button(
            parent=scene,
            model="cube",
            origin=0.5,
            color=color.gray,      # Fester Grauton
            position=pos
        )
    )

# Erstelle ein 20x20 Raster von Boxen als Boden
for x in range(20):
    for y in range(20):
        add_box((x, 0, y))

# Funktion zur Eingabeverarbeitung
def input(key):
    # Gehe alle Boxen durch
    for box in boxes:
        # Prüfe, ob die Maus über der Box schwebt
        if box.hovered:
            if key == "left mouse down":
                # Füge eine neue Box hinzu, angrenzend an die aktuell angeklickte Box
                add_stone(box.position + mouse.normal)
            if key == "right mouse down":
                # Entferne die angeklickte Box aus der Liste und zerstöre sie in der Szene
                boxes.remove(box)
                destroy(box)

# Starte die Anwendung
app.run()
