class Barbarian:
    def __init__(self):
        self.name="Barbarian"
        self.abilities=["Rage"]
        self.level=1
        self.attackAbilities=[]
        self.feature=["Unarmourd Defence"]
        self.spellCaster=False
        self.spells=0
        self.rages=2
        self.maxRage=2
        self.hitPoints=12
        self.abilityChange=0
        self.brutalCrit=0
    def getHitPoints(self):
        if self.level==1:
            return 12
        else:
            return random.randint(self.level,self.level*12)
    def addAbility(self,ability):
        self.abilities.append(ability)
    def addFeature(self,feature):
        self.feature.append(feature)
    def addAbilityChange(self):
        self.abilityChange+=1
    def getAbilityChange(self):
        return self.abilityChange
    def getLevel(self):
        return self.level
    def addBrutalCrit(self):
        self.brutalCrit+=1
    def getBrutalCritDice(self):
        return self.brutalCrit
    def getLevel(self):
        return self.level
    def addLevel(self):
        self.level+=1
        allAbilities={2:[self.addAttackAbility("Reckless Attack"),self.addFeature("Danger Sense")],
                      3: [self.addPath(),self.pathFeatures()],
                      4: self.addAbilityChange(),
                      5:[self.addAttackAbility("Extra Attack"),self.addFeature("Fast Movement")],
                      6: self.pathFeatures(),
                      7: self.addFeature("Feral Instinct"),
                      8: self.addAbilityChange(),
                      9: [self.addFeature("Brutal Critical"),self.addBrutalCrit()],
                      10: self.pathFeatures(),
                      11: self.addAbility("Relentless Rage"),
                      12: self.addAbilityChange(),
                      13: self.addBrutalCrit(),
                      14: self.pathFeatures(),
                      15: self.addAbility("Persistent Rage"),
                      16: self.addAbilityChange(),
                      17: self.addBrutalCrit(),
                      18: self.addFeature("Indomitable Might"),
                      19: self.addAbilityChange(),
                      20: self.addFeature("Primal Champion")}
        self.addChange(allAbilities.get(self.level))
    def addChange(self,lst):#need testing
        for i in lst:
            if(i!=0):
                i
    def addPath(self):
        lst = ["Beast","Berserker","Wild Soul"]
        path=input("which path would you like? Beast, Berserker, Wild Soul ")
        while path not in lst:
            path=input("which path would you like? Beast, Berserker, Wild Soul ")

        self.path=[path]
    def addAttackAbility(self,ability):
        self.attackAbility.append(ability)
    def pathFeatures(self):
        lvl=self.getLevel()
        path=self.path[0]
        paths.get(path)
        if path == "Beast":
            if lvl == 3:
                self.addAttackAbility("Bite")
                self.addAttackAbility("Claws")
                self.addAttackAbility("Tail")
            elif lvl == 6:
                self.addFeature("Climbing")
                self.addFeature("Jumping")
                self.addFeature("Swimming")
                self.addFeature("Breathe Underwater")
            elif lvl == 10:
                self.addAttackAbility("Infectious Fury")
            elif lvl == 14:
                self.addAttackAbility("Call the Hunt")
        elif path == "Berserker":
            if lvl == 3:
                self.addAbility("Frenzy Rage")
            elif lvl == 6:
                self.addAbility("Mindless Rage")
            elif lvl == 10:
                self.addAttackAbility("Indimidating Presence")
            elif lvl == 14:
                self.addAttackAbility("Retaliation")
        elif path == "Wild Soul":
            if lvl == 3:
                self.spells=["Detect Magic"]
                self.spellCaster=True
            elif lvl == 6:
                self.addFeature("Wild Surge")
                self.addAttackAbility("Magic Reserves")
            elif lvl == 10:
                self.addFeature("Arcane Rebuke")
            elif lvl == 14:
                self.addAttackAbility("Chaotic Fury")
        
    def getAbilityScore(self):
        return self.abilityChange
    def removeAbilityScore(self):
        if(self.abilityChange<=0):
            self.abilityChange=0
        else:
            self.abilityChange-=1
        
    def getAbilities(self):
        return self.abilites
    def getFeatures(self):
        return self.features
    def getRages(self):
        return self.rages
    def rest(self):
        self.rages=self.maxRage
        if self.isSpellCaster:
            self.spell=self.level
    def isSpellCaster():
        return self.spellCaseter
    def getName(self):
        return self.name

class Monk:
    def __init__(self):
        self.name="Monk"
        self.abilities=[]
        self.level=1
        self.attackAbilities=[]
        self.feature=["Unarmourd Defence","Martial Arts"]
        self.spellcaster=False
        self.spells=0
        self.hitPoints=8
        self.abilityChange=0
    def addAbility(self,ability):
        self.abilities.append(ability)
    def addFeature(self,feature):
        self.feature.append(feature)
    def addChange(self,lst):#need testing
        for i in lst:
            if(i!=0):
                i
    def addUnArmMove(self,move):
        self.unArmMove=move
    def getUnArmMove(self):
        return self.unArmMove
    def addLevel(self):
        self.level+=1
        allAbilities={2: [self.addKi(),self.addAttackAbility("Flurry of Blows"),
                          self.addAttackAbility("Patient Defense"),
                          self.addAttackAbility("Step of the Wind"),
                          self.addFeature("Unarmored Movement"),
                          self.addUnArmedMove(10)],
                      3: [self.addAttackAbility("Deflect Missles"),self.addAttackAbility("Open Hand Technique")],
                      4: [self.addAbilityChange(),self.addFeature("Slow Fall")],
                      5: [self.addAttackAbility("Extra Attack"),self.addAttackAbility("Stunning Strike")],
                      6: [self.addAttackAbility("Ki-Empowered Strikes"),self.addUnArmedMove(15),self.addAbility("Wholeness of Body")],
                      7: [self.addFeature("Evasion"),self.addFeature("Stillness of Mind")],
                      8: self.addAbilityChange(),
                      9: self.addAbility("Unarmored Movement Improvement"),
                      10: [self.addFeature("Immune to Poison"),self.addFeature("Immune to Disease")],
                      11: self.addAbility("Sanctuary"),
                      12: self.addAbilityChange(),
                      13: self.addFeature("Speak to Everything"),
                      14: self.addUnArmedMove(25),
                      15: self.addFeature("Timeless Body"),
                      16: self.addAbilityChange(),
                      17: self.addAttackAbility("Quivering Palm"),
                      18: [self.addAbility("Invisibility"),self.addUnArmedMove(30)],
                      19: 0,
                      20: self.addFeature("Perfect Self")}
        self.addChange(allAbilities.get(self.level))
    def addAbilityChange(self):
        self.abilityChange+=2
    def getAbilityChange(self):
        return self.abilityChange
    def getAbilities(self):
        return self.abilites
    def getUnArmmedMovement(self):
        return self.unArmedMove
    def getFeatures(self):
        return self.features
    def getKi(self):
        return self.ki
    def addKi():
        self.ki= self.level
    def getLevel(self):
        return self.level
    def rest(self):
        self.ki=self.level
    def isSpellCaster():
        return self.spellcaseter
    def getName(self):
        return self.name
