import random
from PlayerClasses import *
from Race import *
def lookUpRace(race):
    races={"Human": Human(),
           "Elf": Elf(),
           "Dragonborn": Dragonborn(),
           "Gnome": Gnome(),
           "Dworf": Dworf(),
           "Tiefling": Tiefling(),
           "Halfling": Halfling()}
    if race in races:
        return races[race]
    else:
        return "Nope"
def languages(race,human="h"):
    r=lookUpRace(race)
    pRace=r.getRace()
    if pRace!="Human":
        if pRace != "Human" and pRace != "Tiefling":
            if pRace != "Halfling":
                return ["Common",pRace[:-1]+"vish"]
            return ["Common",pRace]
        else:
            if pRace == "Tiefling":
                return ["Common","Infernal"]
    elif pRace == "Human" and human!="h":
        return ["Common",human]
        
class Player:
    def __init__(self,name,race):
        self.name=name
        self.hp=10
        self.maxHP=10
        self.tempHP=0
        self.strength=random.randint(0,20)
        self.dextarity=random.randint(0,20)
        self.intelligence=random.randint(0,20)
        self.wisdom=random.randint(0,20)
        self.constitution=random.randint(0,20)
        self.ac=10
        self.pp=0
        self.gp=0
        self.sp=0
        self.cp=0
        self.exp=0
        self.race=lookUpRace(race)
        self.languages=languages(race)
        self.speed=self.race.getSpeed()
        self.availableLvls=0
        self.expNeeded=1000
        self.playerClass=[]
        self.items=[]

    def addItems(self,item):
        self.items.append(item)
    def getName(self):
        return self.name
    def addClass(self,charClass):
        #have switch case for the classes
        switcher={"Barbarian":Barbarian(),"Monk": Monk(),"Bard": Bard(),"Cleric": Cleric(),
                  "Druid": Druid(),"Fighter": Fighter(),"Sorcerer": Sorcerer, "Worlock": Worlock(),"Wizard": Wizard()}
        self.playerClass.append(switcher.get(charClass))
    
    def addExp(self,amount):
        self.exp+=amount
        if(self.exp>=self.expNeeded):
            self.exp-=self.expNeeded
            self.expNeeded+=int(self.expNeeded*0.5)
            self.availableLvls+=1
    def getClasses(self):
        return self.playerClass
    
    def useLvlUP(self,Class):
        if(self.availableLvls>=1):
            for i in getClasses():
                if(Class == i.getName()):
                    self.playerClass[i].addLevel()
                    self.availablelvl-=1
            self.addClass(Class)#basically adding a new playerClass object to the array
            
    def getLanguages(self):
        return self.languages
    def addMoney(self,moneyType,amount):
        if(moneyType=="Platinum"):
            self.pp+=amount
        elif(moneyType=="Gold"):
            self.gp+=amount
        elif(moneyType=="Silver"):
            self.sp+=amount
        elif(moneyType=="Copper"):
            self.cp+=amount
    def RemoveMoney(self,moneyType,amount):
        if(moneyType=="Platinum"):
            if(amount>=self.pp):
                self.pp=0
            else:
                self.pp-=amount
        elif(moneyType=="Gold"):
            if(amount>=self.gp):
                self.gp=0
            else:
                self.gp-=amount
        elif(moneyType=="Silver"):
            if(amount>=self.sp):
                self.sp=0
            else:
                self.sp-=amount
        elif(moneyType=="Copper"):
            if(amount>=self.cp):
                self.cp=0
            else:
                self.cp-=amount
    def hasEnoughPlatinum(self,amount):
        if(self.pp>=amount):
            return True
        return False
    def hasEnoughGold(self,amount):
        if(self.gp>=amount):
            return True
        return False
    def hasEnoughSilver(self,amount):
        if(self.sp>=amount):
            return True
        return False
    def hasEnoughCopper(self,amount):
        if(self.cp>=amount):
            return True
        return False


class Item:
    def __init__(self,name,description,weight,worth,amount):
        self.name=name
        self.desc=description
        self.weight=weight
        self.value=worth
        self.amount=amount
class Weapon:
    def __init__(self,name,Type,damage,damageType,magical,prop,weight):
        self.name=name
        self.type=Type
        self.damage=damage #damage is max damage
        self.damageType=damageType
        self.magical=magical #true or false
        self.prop=prop #this is for if the weapon is heavy or
        self.weight=weight
    def attack():
        roll= random.randint(1,20)
        damage=random.randint(1,self.damage)
        return [roll,damage]
    def getDamageType():
        return self.damageType
    def isMagical():
        return self.magical

class Armor:
    def __init__(self,name,minStrength,stealthDis,weight,Class):
        self.name=name
        self.minStrength=minStrength
        self.stealth=stealthDis
        self.weight=weight
        self.set=Class
    def getSet(self):
        return self.set
    def getName(self):
        return self.name
    def getMinStr(self):
        return self.minStrength
    def hasStealthDis(self):
        #should return true or false
        return self.stealth
    def addAbility(self,desc):
        self.ability=desc
    
def main():
    print(languages("Elf"))
    
main()
