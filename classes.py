'''Die Klasse der Habitate und Organismen und specifische Formen von organismen'''
import basic_functions as bf
import numpy as np              #hab ich schin erwähnt das ich numpy liebe? und das es für diese Aufgabe wahrscheinlich vollkommen überflüssig ist?
import numpy.random as rnd

__author__ = ""

class habitat:
    '''Klasse für alle spieler um die Basic funktionen festzulegen, darin sind hauptächlich Karten und Punkte gespeichert'''
    def __init__(self, size):
        self.size = size
    def fill_with_organisms(self):
        self.no_plants = rnd.randint(1, 10, size = 1)
        self.plants = []
        for i in range(plants):
            self.plants.append(plant())
        print(no_plants)
        # todo analoges für Tiere, vllt. bias mit arten anteile für vrsch. habitate einführen, spezifische tier und pflanzenarten implementieren
    def time_step():
        print('ToDo')
        #does it happen here? idk, gotta think 'bout this
    def no_space(self):
        '''hungriest plant dies first'''
        while self.filled_space > self.size:
            hunger = np.full(self.no_plants, 0)
            for i in range(self.no_plants):
                hunger[i] = plants[i].hunger
            hungriest = np.whereis(np.max(hunger))[0]
            self.delete_plant(hungriest)
            
    def delete_plant(self, index):
        plants_new = []
        for k in range(index-1):
            plants_new.append(plants[k])
        for k in range(index + 1, no_plants):
            plants_new.append(plants[k])
            
    def calculate_need():
        print('yea, auch ToDo')
        
                
class organism:
    '''Klasse für alle Spieler um die Basic funktionen festzulegen, darin sind hauptächlich Karten und Punkte gespeichert'''
    def __init__(self, size):
        self.size = size

        

    def time_step():
        print('vllt sollte das Zeug altern und so')
        print('und verbauchen Energie')
        print('und reproduzieren sich')
        print('Wie wärs wenn weibchen einen reproduktionszyklus haben?')
        
        #does it happen here? idk, gotta think 'bout this


class plant(organism):
    # Init für Pflanzen
    def __init__(self, water_bedarf, size, max_size, habitat, alter, min_energie, energie, motivation, flucht, jagd, vorteil, einschraenkung, foodsource):
        self.size = size
        self.size_per_time = 2
        self.hunger = 0
        self.water_bedarf
        self.max_size = max_size
        self.habitat = habitat
        self.alter = alter
        self.min_energie = min_energie
        self.energie = energie
        self.einschraenkung = einschraenkung
        self.vorteil = vorteil  # Hier können Eigenschaften für Pflanzen wie "giftig", "stachelig", "bitter", stehen, die beim Fressen abgefragt werden 
        self.foodsource = foodsource

    def be_eaten(self, size):
        if size < self.size:
            self.size -= size
            return True
        else:
            return False
    def regenerate(self):
        self.mass += self.mass_per_time

class animal(organism):
    def __init__(self, size, size_per_time, max_size, durst, habitat, alter, min_energie, energie, motivation, flucht, jagd, foodsource):
        self.size = size
        self.size_per_time = 2
        self.max_size = max_size
        self.durst = durst
        self.habitat = habitat
        self.alter = alter
        self.min_energie = min_energie
        self.energie = energie  # eventuell gedoppelt mit motivation
        self.motivation = motivation
        self.flucht = flucht
        self.jagd = jagd
        self.foodsource = foodsource
    def eat(self, kcal):
        self.energy += kcal

# TODO wenn sich Tiere vermehren sollen, muss überprüft werden, wie viele ihrer Gattung übrig sind: m/w einfach mal ignoriert    
class herbivor(animal):
    def die(self, size, alter, durst, energie, min_energie, motivation):
        if size > alter or energie > min_energie or motivation <= 0:
            #TODO aus Liste entfernen
            pass
        else:
            #Tier Lebt weiter
            pass

      

class carnivor(animal):
    def jagd(self, habitat):
        print('Did I mention that this is to do?')
    

class omnivor(carnivor, herbivor):
    def check_footsource(self):
        print('ToDo')
        if habitat.plant_mass > habitat.animal_plant_need:
            print('Pflanzen fressen')
        else:
            print('Tiere fressen')
        
    

if __name__ == 'main':
    '''Sehr kurze wenige einzel Testfälle'''
    habititi=habitat(100)
    for i in range(100):
        habititi.time_step()
