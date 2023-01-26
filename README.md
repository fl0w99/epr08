oekosystem_EPR
# Ökosystem - der Lauf der Natur 


## classes.py 


### ---------- STYLE ----------
+   Leerzeichen zweischen Operatoren und nach Kommas hinzugefügt


### ---------- class plant ----------
+   __init__ um Attribute außer size erweitert
+   in be_eaten mass in size geändert



### ========== Info ==========
+   Da es nicht ausreicht die Eigenschaften der Tiere in der Klasse Organismus zu speichern, da dann für jedes Tier der selben Art
+   auch der selbe Hunger, oder das selbe Alter definiert wäre, müssen die Attribute jeweils pro Tierart im __init__ Teil stehen.



### ---------- class animal ----------
+   Klasse um __init__ Funktion erweitert 
+   __init__ um Attribute erweitert



### ---------- class herbivor ----------
+   Funktion die mit Argumenten und if Abfrage asgefüllt
+   Diese Funktion sollte in jeder Runde jedes Tier aus der Liste abfragen, ob es stirbt




### ---------- Pflanzen ----------

	VARIABLE	=	BESCHREIBUNG
	__init__ 	=	Name
	size		=	Min und max Größe
	size_per_time	=	Wachstum pro Runde
	hunger 		=	Hunger
	water_bedarf 	=	
	max_size	=	Maximal erreichbare Größe
	habitat 	=	Habitat
	alter		=	Alter
	min_energie 	=	Minimal benötigte Energie
	energie		= 	aktuelle Energie
	einschraenkung	=	Einschränkung wie z.B. benötigt Licht, welches durch zu viel Bäume genommen werden könnte, oder kann nur auf Bäumem wachsen
	vorteil		=	Vorteile die die Pflanze hat, z.B. giftig, stachelig, bitter
	foodsource	=	Nahrungsquelle

>fehlt noch:	Evtl. weitere Eigenschaften Wahrscheinlichkeit zu sterben



### ---------- Tiere ----------

	VARIABLE	=	BESCHREIBUNG
	__init__ 	=	Name
	size		=	Min und max Größe
	size_per_time	=	Wachstum pro Runde
	durst 		=	Durst
	habitat 	=	Habitat
	alter		=	Alter
	min_energie 	=	Minimal benötigte Energie
	energie		= 	aktuelle Energie
	motivation	=	Aktuelle Motivation
	flucht		=	Fluchtkönnen 
	jagd		=	Jagdkönnen des Tieres
	foodsource	=	Nahrungsquelle




## gameplay.py 



### ---------- IMPORTS ----------
+   Ich musste Numpy und die Basic Functions aus den Imports entfernen, da es bei mir nicht funktioniert.


### ---------- Funktion start ----------
+   Soll den Spieler Begrüßen
+   Eventuell kann ein Teil des Textes auch in eine Readme, oder Anleitung verschoben werden.


### ---------- VARIABLEN ----------
+   Listen mit Möglichen Pflanzen und Tieren definiert


### ---------- Class create_animals ----------
+   Alles ist beispielhaft für die Herbivoren ausgeführt
+   Zuerst werden die Tiere gemischt und eine zufällige Anzahl entfernt. Dann werden von jeder Art zufällig viele Tiere mit einem Index versehen
+   Die Tiere werden in einer Liste gespeichert, die dann in match case iteriert wird und den Tieren dann ihre self werte zugefügt werden.
+   An der Stelle wo die self Werte definiert werden sollen, steht aktuell jeweils pass
