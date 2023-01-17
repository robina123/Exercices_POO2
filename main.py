import random as r


class Npc:
    def __init__(self):
        self.force = [r.randint(1, 6) for _ in range(4)]
        self.force.sort()
        self.force = self.force[:3]
        self.force = sum(self.force)

        self.agilite = [r.randint(1, 6) for _ in range(4)]
        self.agilite.sort()
        self.agilite = self.agilite[:3]
        self.agilite = sum(self.agilite)

        self.constitution = [r.randint(1, 6) for _ in range(4)]
        self.constitution.sort()
        self.constitution = self.constitution[:3]
        self.constitution = sum(self.constitution)

        self.intelligence = [r.randint(1, 6) for _ in range(4)]
        self.intelligence.sort()
        self.intelligence = self.intelligence[:3]
        self.intelligence = sum(self.intelligence)

        self.sagesse = [r.randint(1, 6) for _ in range(4)]
        self.sagesse.sort()
        self.sagesse = self.sagesse[:3]
        self.sagesse = sum(self.sagesse)

        self.charisme = [r.randint(1, 6) for _ in range(4)]
        self.charisme.sort()
        self.charisme = self.charisme[:3]
        self.charisme = sum(self.charisme)

        self.armure = r.randint(1, 12)
        self.nom = str
        self.race = str
        self.espece = str
        self.nombre_de_vie = r.randint(1, 20)
        self.profession = str

    def afficher_caracteristiques(self):
        print("Force: ", self.force)
        print("Agilité: ", self.agilite)
        print("Constitution: ", self.constitution)
        print("Intelligence: ", self.intelligence)
        print("Sagesse: ", self.sagesse)
        print("Charisme: ", self.charisme)
        print("Armure: ", self.armure)
        print("Nom: ", self.nom)
        print('Race: ', self.race)
        print('Espèce: ', self.espece)
        print('Nombre de vie: ', self.nombre_de_vie)
        print('Profession: ', self.profession)


class Kobold(Npc):
    def __init__(self):
        super().__init__()

    def attaque(self, cible):
        return

    def defense(self):
        return


class Hero(Npc):
    def __init__(self):
        super().__init__()

    def attaque(self, cible):
        return

    def subir_dommage(self, nombre_de_dommage):
        return
