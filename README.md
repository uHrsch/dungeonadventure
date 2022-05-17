# dungeonadventure

## Ziel
Ein Text Dungeonadventure bei dem Kämpfe über einen Zufall entschieden werden. Die spielende Person gibt eine Ziffer ein welche mit einer zufäligen Zahl des Gegners verglichen wird. Bei Gleichheit trifft die spielende Person den Gegner, sonst trifft der Gegner. 
Es soll verschiedene Ausrüstungen geben die sich in Attributswerten unterschieden und verschiedene Gegnerkategorien. 
Nach jedem Kampf soll anhand einer Zufallszahl ein Heiltrank genutzt werden und die spielende Person um 5 Lebenspunkte heilen.
Die spielende Person soll die Möglichkeit haben ein zwischen Pfaden zu wählen um Einfluss auf die benötigte Zeit zu haben, die benötigt wird um den Dungeon abzuschließen.

Das Spiel soll als Skript in der Kommandozeile verwendet werden.

## Ausrüstung
### Schwere Ausrüstung
- Lebenspunkte: 40
- Schaden: 2
- Ausweichchance: 5%

### Mittlere Ausrüstung
- Lebenspunkte: 30
- Schaden: 2
- Ausweichchance: 10%

### Leichte Ausrüstung
- Lebenspunkte: 20
- Schaden: 3
- Ausweichchance: 15%

## Gegnerklassen
### Schwache Gegner
- Lebenspunkte: 3
- Schaden: 1
- Ausweichchance: 5%
- Auftrittschance: 45%
- Trefferchance: 50%

### Mittlere Gegner
- Lebenspunkte: 6
- Schaden: 2
- Ausweichchance: 7%
- Auftrittschance: 30%
- Trefferchance: 33,33%

### Starke Gegner
- Lebenspunkte: 9
- Schaden: 3
- Ausweichchance: 10%
- Auftrittschance: 20%
- Trefferchance: 10%

### Boss Gegner (evtl)
- Lebenspunkte: 15
- Schaden: 3
- Ausweichchance: 15%
- Auftrittschance: 5%
- Trefferchance: 5%

## Trefferberechnung
enemyValue = zufällige Zahl

hitValue = enemyValue % Trefferchance

Ausgabe(Wertebereich für Eingabe)

userValue = userInput 

    wenn (userValue == hitValue){
        wenn (zufällige Zahl % 10 < Ausweichchance)
            Angriff ausgewichen
        sonst
            user hit enemy
    }
    sonst{   
        wenn (zufällige Zahl % 10 < Ausweichchance)
                Angriff ausgewichen
        sonst
            enemy hit user
    }