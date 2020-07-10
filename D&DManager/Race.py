def lookUpRace(race):
    racelst={"Human": Human(),"Elf": Elf(),"Dworf": Dworf()}
    return racelst.get(race)
class Human:
    def __init__(self):
        self.name="Human"
        self.speed=30
        self.size="Medium"
        self.scoreChange=[1]
        self.abilityScores=["All"]
        self.abilities=[]
    def getSpeed(self):
        return self.speed
    def getRace(self):
        return self.name
    def getAbilities(self):
        return self.abilites
    def getSize(self):
        return self.size
    
class Elf:
    def __init__(self):
        self.name="Elf"
        self.speed = 30
        self.size="Medium"
        self.scoreChange=[2]
        self.abilityScores=["DEX"]
        self.abilities=["Darkvision","Keen Senses","Trance"]
    def getSpeed(self):
        return self.speed
    def getRace(self):
        return self.name
    def getAbilities(self):
        return self.abilites
    def getSize(self):
        return self.size
class Dworf:
    def __init__(self):
        self.name="Dworf"
        self.speed=25
        self.size="Medium"
        self.scoreChange=[2]
        self.abilityScores=["CON"]
        self.abilities=["Darkvision","Dwarven Resilience","Tool Proficiency","Stonecunning"]
    def ToolProf(self,tool):
        self.abilities[self.abilities.index("Tool Proficiency")]==tool
    def getSpeed(self):
        return self.speed
    def getRace(self):
        return self.name
    def getAbilities(self):
        return self.abilites
    def getSize(self):
        return self.size
class Dragonborn:
    def __init__(self):
        self.name="Dragonborn"
        self.speed=30
        self.size="Medium"
        self.scoreChange=[2,1]
        self.abilityScores=["STR","CHR"]
        self.abilities=["Breath Weapon","Draconic Ancestory"]
    def DragonRace(self,color):
        self.abilities[self.abilities.index("Draconic Ancestory")]=color
    def getSpeed(self):
        return self.speed
    def getRace(self):
        return self.name
    def getAbilities(self):
        return self.abilites
    def getSize(self):
        return self.size

class Gnome:
    def __init__(self):
        self.name="Gnome"
        self.speed=30
        self.size="Small"
        self.scoreChange=[2]
        self.abilityScores=["INT"]
        self.abilities=["Darkvision","Gnome Cumming"]
    def getSpeed(self):
        return self.speed
    def getRace(self):
        return self.name
    def getAbilities(self):
        return self.abilites
    def getSize(self):
        return self.size
    
class Tiefling:
    def __init__(self):
        self.name="Tiefling"
        self.speed=30
        self.scoreChange=[2,1]
        self.abilityScores=["CHR","INT"]
        self.abilities=["Darkvision","Fire Resistance","Hellish Rebuke","Thaumaturgy"]
    def getSpeed(self):
        return self.speed
    def getRace(self):
        return self.name
    def getAbilities(self):
        return self.abilites
    def getSize(self):
        return self.size
class Halfling:
    def __init__(self):
        self.name="Halfling"
        self.speed=30
        self.size="Small"
        self.scoreChange=[2]
        self.abilityScores=["DEX"]
        self.abilities=["Lucky","Brave","Nimbleness"]
        
    def getSpeed(self):
        return self.speed
    def getRace(self):
        return self.name
    def getAbilities(self):
        return self.abilites
    def getSize(self):
        return self.size
