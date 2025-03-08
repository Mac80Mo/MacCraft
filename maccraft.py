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

# Globaler Modus: "box" für Boden, "stone" für Stein
current_mode = "box"

# Optional: Anzeige des aktuellen Modus als Text in der Ecke
mode_text = Text(text=f'Modus: {current_mode}', origin=(0,0), position=(0,0.45), scale=2)

# Erklärender Text unterhalb des Modus-Textes:
instruction_text = Text(text="1 für Box | 2 für Stein | 3 für Holz", origin=(0,0), position=(0,0.35), scale=1)

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

# Neue Funktion für Steine, die grau sind.
def add_wood(pos):
    boxes.append(
        Button(
            parent=scene,
            model="cube",
            origin=0.5,
            color=color.yellow,      
            position=pos
        )
    )

# Erstelle ein 20x20 Raster von Boxen als Boden
for x in range(20):
    for y in range(20):
        add_box((x, 0, y))

def input(key):
    global current_mode
    # Umschalten der Modi:
    if key == "1":
        current_mode = "box"
        mode_text.text = f"Modus: {current_mode}"
    elif key == "2":
        current_mode = "stone"
        mode_text.text = f"Modus: {current_mode}"
    elif key == "3":
        current_mode = "wood"
        mode_text.text = f"Modus: {current_mode}"
    
    # Eingabe zur Platzierung oder Entfernung von Blöcken:
    for box in boxes:
        if box.hovered:
            if key == "left mouse down":
                # Abhängig vom aktuellen Modus den entsprechenden Block hinzufügen
                if current_mode == "box":
                    add_box(box.position + mouse.normal)
                elif current_mode == "stone":
                    add_stone(box.position + mouse.normal)
                elif current_mode == "wood":
                    add_wood(box.position + mouse.normal)
            if key == "right mouse down":
                boxes.remove(box)
                destroy(box)

# Starte die Anwendung
app.run()
