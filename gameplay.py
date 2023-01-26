import random

__author__ = "7535842, Seiffert, 8051657, Erdogan, 6872562, Hentschl"


def start():
    begruessung = "\nWilkommen in deinem neuem Ökosystem.\n" \
    "Bevor die Simulation startet, hier ein paar Informationen. Du kannst mit dem Betätigen der\n" \
    "ENTER taste die Runden starten. Am Ende jeder Runde hast du die Möglichkeit >>>Info einzugeben und zu bestätigen\n" \
    "Dann siehst du eine Übersicht aller Pflanzen und Tiere. Wenn du dann ENTER drückst fährst du mit der nächsten\n" \
    "runde fort. Andernfalls kannst du auch den Namen eines Tieres oder einer Pflanze eingeben und genauere Informationen erlangen.\n" \
    "\nNach einer Runde, oder nach dem Betrachten der Population, kannst du auch folgende Eingabe tätigen. >>>5\n" \
    "In diesem Fall würden 5 Runden simuliert werden.\n"
    
    
    print(begruessung)
    wait_to_start = input("Zum Starten bitte ENTER drücken\n>>>")

pflanzen = ["Laubbaum", "Nadelbaum", "Farn", "Gras", "Moos", "Baumflechte"]
herbivoren = ["Giraffe", "Hirsch", "Reh", "Schaf", "Ziege", "Maus"]
carnivoren = ["Fuchs", "Luchs", "Tieger", "Schlange", "Habicht", "Bussart"]
omnivoren = ["Ratte", "Schwein", "Baer"]


def main():
    # TODO erstellen des Habitats 

    # TODO aus den Listen wird eine Zufäüllige Zahl an Tieren/Pflanzen genommen, aber mindestens drei Pflanzen und insgesamt mindestens drei Tiere, wobei 
    #      bei den Tieren die Wahrscheilichkeit für eine höhere Zahl wahrscheinlicher sein sollte, damit die meisten Karnivoren auch etwas zu fressen haben.
    #      am einfachsten dürfte es sein, eine Anzahl X an Namen, aus den Listen zu entfernen. 

    # TODO für die ausgewählten Tiere und Pflanzen müssen eindeutige namen erstellt werden, indem man mit count += 1 eine Zahl mit dem Tiernamen kombiniert
    #      Diese Tiere bekommen dann ihre Self werte zugewiesen, die abhängig davon sind, in welcher der drei Listen sie stehen. Die Anzahl der Tiere sollte
    #      mindestens 2 sein, damit sie sich auch vermehren können.
    
    
    class create_animals():
        # Erstellung der Herbivoren
        random.shuffle(herbivoren)
        del herbivoren[0:random.randint(0, len(herbivoren)-1)]
        quantity_herbivoren = len(herbivoren)
        for animals in range (quantity_herbivoren):
            quantity = random.randint(1, random.randint(2, random.randint(2, 5)))
            for index in  range(quantity):
                name = herbivoren[animals] + str(index)
                herbivoren.append(name)
        del herbivoren[0:quantity_herbivoren]
        print(herbivoren)


        for animals in herbivoren:
            match animals:
                case s if s.startswith("Giraffe"):
                    pass
                    # TODO hier werden die Eigenschaften für die Giraffen festgelegt 
                case s if s.startswith("Hirsch"):
                    pass
                case s if s.startswith("Reh"):
                    pass
                case s if s.startswith("Schaf"):
                    pass
                case s if s.startswith("Ziege"):
                    pass
                case s if s.startswith("Maus"):
                    pass
        


start()
main()
