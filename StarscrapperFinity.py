import time
import random
def next_engine():
    input("...")
def skip_engine(x):
    while x>0:
        x-=1
        time.sleep(0.5)
class Characters:
    def __init__(self, name, stats, skills, lvlsystem):
        self._name=name
        self._health=stats[0]
        self._maxhealth=stats[0]
        self._attack=stats[1]
        self._ogattack=stats[1]
        self._hitratio=stats[2]
        self._oghitratio=stats[2]
        self._defence=stats[3]
        self._ogdefence=stats[3]
        self._magic=stats[4]
        self._maxmagic=stats[4]
        self._skillist=skills
        self._level=lvlsystem[0]
        self._exp=lvlsystem[1]
        self._party = 0
        self._partymp = 0
        self._ogpartymp = 0
        self._partyskills1 = ["range mode", "full blast", "self strike"]
        self._partyskills2 = ["regen wave", "artist block", "call of the dead"]
        self._partyskills3 = ["sprint", "sharpen", "blitz"]
        self._gold = 0
        self._speedlv = 0
        self._hitratiolv = 4
        self._defencelv = 5
        self._speed = stats[5]
        self._ogspeed = stats[5]
    def replace_skills(self, skills):
        self._skillist = skills
    def new_party(self, num):
        self._party+=num
    def spend(self, num):
        self._gold+=num
    def get_health(self):
        return self._health
    def get_party(self):
        return self._party
    def get_gold(self):
        return self._gold
    def get_skills(self):
        return self._skillist
    def get_hitratio(self):
        return self._hitratio
    def get_attack(self):
        return self._attack
    def get_defence(self):
        return self._defence
    def get_magic(self):
        return self._magic
    def get_name(self):
        return self._name
    def get_level(self):
        return self._level
    def get_speed(self):
        return self._speed
    def get_exp(self):
        return self._exp
    def get_test(self):
        print(self._level)
        print("Attack ",self._attack,"Hitratio ", self._hitratio,"Defence ", self._defence)
    def reset(self):
        self._health = self._maxhealth
        self._magic = self._maxmagic
        self._hitratio = self._oghitratio
        self._defence = self._ogdefence
        self._attack = self._ogattack
        self._partymp = self._ogpartymp
        self._speed = self._ogspeed
    def damage(self, damage, hitratio):
        roll = random.randint(0, hitratio)
        if roll == hitratio:
            self._health-=damage * 1.5
            print("CRIT")
        elif roll >= self._defence or self._defence > hitratio:
            self._health-=damage
            print("Hit")
        else:
            print("Miss")
    def levelup(self, exp):
        self._exp += exp
        if self._exp > self._level*10:
            print("level up")
            self._exp -= self._level*10
            self._level += 1
            self._maxhealth+=20
            self._maxmagic+=10
            self._ogpartymp+=5*self._party
            self._speedlv += 1
            self._hitratiolv += 1
            self._defencelv += 1
            if self._speedlv == 10:
                self._ogspeed += 1
                self._speedlv = 0
            if self._hitratiolv == 5:
                self._oghitratio += 2
                self._hitratiolv = 0
            if self._defencelv == 6:
                self._ogdefence += 2
                self._defencelv = 0
    def slevelup(self, exp):
        self._exp += exp
        if self._exp > self._level*10:
            self._exp -= self._level*10
            self._level += 1
            self._maxhealth+=20
            self._maxmagic+=10
            self._ogpartymp+=5*self._party
            self._speedlv += 1
            self._hitratiolv += 1
            self._defencelv += 1
            if self._speedlv == 10:
                self._ogspeed += 1
                self._speedlv = 0
            if self._hitratiolv == 5:
                self._oghitratio += 2
                self._hitratiolv = 0
            if self._defencelv == 6:
                self._ogdefence += 2
                self._defencelv = 0
    def battle(self, enemy):
        skillet = 0
        while self._health>0 and enemy.get_health()>0:
            if self._magic < 0:
                    self._magic = 0
            if self._magic > 99:
                self._magic = 99
            if self._health > 999:
                self._health = 999
            time.sleep(0.8)
            if skillet == 0:
                skillet = 1
            else:
                skillet = 0
            roll = random.randint(1, 10)
            if roll == 5:
                skillet = 2
            enemyskillet = random.randint(0, 2)
            skillskillet = random.randint(0, 2)
            skillskillet2 = random.randint(0, 2)
            skillskillet3 = random.randint(0, 2)
            if self._speed >= enemy.get_speed():
                time.sleep(0.9)
                print("["+self._name+"]", "HP:", self._health, "MP:", self._magic, "skill:", self._skillist[skillet])
                if enemy.get_health() >= 0:
                    print("Enemy: "+ enemy.get_name() + " Enemy HP: "+ str(enemy.get_health()))
                else:
                    print("Enemy: "+ enemy.get_name() + " Enemy HP: "+ "0")
                print("Option 1: Attack")
                print("Option 2: Skill")
                print("Option 3: Search")
                print("Option 4: Escape")
                action = input("Number of action you would like to take: ")
                while action!="1" and action!="2" and action!="3" and action!="4" and action!="7":
                    print("try again")
                    print("["+self._name+"]", "HP:", self._health, "MP:", self._magic, "skill:", self._skillist[skillet])
                    if enemy.get_health() >= 0:
                        print("Enemy: "+ enemy.get_name() + " Enemy HP: "+ str(enemy.get_health()))
                    else:
                        print("Enemy: "+ enemy.get_name() + " Enemy HP: "+ "0")
                    print("Option 1: Attack")
                    print("Option 2: Skill")
                    print("Option 3: Search")
                    print("Option 4: Escape")
                    action = input("Number of action you would like to take: ")
                if action == "1":
                    enemy.damage(self._attack, self._hitratio)
                elif action == "2":
                    if skillet == 0:
                        self._health -= 2
                    elif skillet == 1:
                        if self._magic > 0:
                            self._magic -= 2
                        else:
                            self._health -= 4
                elif action == "4":
                    print("[???] you are a silly fool")
                    time.sleep(0.9)
                    print("[???] there is no escape")
                    time.sleep(0.9)
                    print("[???] don't even try")
                    time.sleep(0.9)
                elif action == "7":
                    enemy.damage(999999, 999999)
                else:
                    print("ThErE iS nO eScApE sIlLy MoRtAl")
                    print("Attack:", self._attack, "Hit Chance:", self._hitratio, "Defence:", self._defence)
                    print("Enemy HP:", enemy.get_health())
                time.sleep(0.8)
                if enemy.get_skills()[enemyskillet] == "void":
                    print("[Enemy]: Attack")
                    roll = random.randint(0, enemy.get_hitratio())
                    if roll>self._defence:
                        print("Hit")
                        self._health-=enemy.get_attack()
                    else:
                        print("Miss")
            if self._speed < enemy.get_speed() and enemy.get_health() > 0 and self._health > 0:
                if enemy.get_skills()[enemyskillet] == "void":
                    print("[Enemy]: Attack")
                    roll = random.randint(0, enemy.get_hitratio())
                    if roll>self._defence:
                        print("Hit")
                        self._health-=enemy.get_attack()
                    else:
                        print("Miss")
                time.sleep(0.9)
                print("["+self._name+"]", "HP:", self._health, "MP:", self._magic, "skill:", self._skillist[skillet])
                if enemy.get_health() >= 0:
                    print("Enemy: "+ enemy.get_name() + " Enemy HP: "+ str(enemy.get_health()))
                else:
                    print("Enemy: "+ enemy.get_name() + " Enemy HP: "+ "0")
                print("Option 1: Attack")
                print("Option 2: Skill")
                print("Option 3: Search")
                print("Option 4: Escape")
                action = input("Number of action you would like to take: ")
                while action!="1" and action!="2" and action!="3" and action!="4" and action!="7":
                    print("try again")
                    print("["+self._name+"]", "HP:", self._health, "MP:", self._magic, "skill:", self._skillist[skillet])
                    if enemy.get_health() >= 0:
                        print("Enemy: "+ enemy.get_name() + " Enemy HP: "+ str(enemy.get_health()))
                    else:
                        print("Enemy: "+ enemy.get_name() + " Enemy HP: "+ "0")
                    print("Option 1: Attack")
                    print("Option 2: Skill")
                    print("Option 3: Search")
                    print("Option 4: Escape")
                    action = input("Number of action you would like to take: ")
                if action == "1":
                    enemy.damage(self._attack, self._hitratio)
                elif action == "2":
                    if skillet == 0:
                        self._health -= 2
                    elif skillet == 1:
                        if self._magic > 0:
                            self._magic -= 2
                        else:
                            self._health -= 4
                time.sleep(0.9)
            if self._party > 0 and enemy.get_health() >= enemy.get_magic():
                roll = random.randint(1, 8-self._party)
                if roll == 1:
                    print("[Party]: FULL ASSAULT!")
                    enemy.damage(self._attack*self._party, self._hitratio*self._party)
                elif roll == 2:
                    print("[Party]: Magic Break!")
                    self._partymp += self._party
                elif roll == 3:
                    print("[Shelly]: cheering!")
                    self._magic += 3
            if self._magic < 0:
                self._magic = 0
            if self._magic > 9999:
                self._magic = 9999
            if self._health > 9999:
                self._health = 9999
        print("Battle End")
        self._attack = self._ogattack
        self._hitratio = self._oghitratio
        self._defence = self._ogdefence
        self._partymp = self._ogpartymp
        self._speed = self._ogspeed
def voice(person, speach):
    print("["+person+"] "+speach)
def pa(text):
    print("<"+text+">")
def re_burst(mc, enemy):
    mc.reset()
    enemy.reset()
def saver(chapter):
    output_file = open("AhoySave.txt", "w")
    output_file.write(str(chapter))
    output_file.close()
    output_file = open("Name.txt", "w")
    output_file.write(str(name))
    output_file.close()
    output_file = open("AhoyLV.txt", "w")
    output_file.write(str(mc.get_level()))
    output_file.close()
    output_file = open("AhoyParty.txt", "w")
    output_file.write(str(mc.get_party()))
    output_file.close()
def ship(enemies):
    action = "0"
    while action != "3":
        print("Infront of you are the great seas")
        print("Option 1: Set sail")
        print("Option 2: Take a rest")
        print("Option 3: head towards land")
        action = input("What now? ")
        if action == "1":
            roll = random.randint(1, 70)
            if roll == 1:
                enemy = enemies[2]
            elif roll >= 30:
                enemy = enemies[1]
            else:
                enemy = enemies[0]
            mc.battle(enemy)
            if mc.get_health() > 0:
                mc.levelup(enemy.get_exp())
                mc.spend(5)
                if enemy.get_name == enemies[0].get_name:
                    mc.levelup(enemy.get_exp())
                    mc.spend(5)
            re_burst(mc, enemy)
        elif action == "2":
            voice("Shelly", "Wait, you still sleep?")
            next_engine()
            pa("You decided to rest")
            mc.get_test()
            next_engine()
        if action != "3":
            action == "0"
def saved():
    print("The Game Has Been Saved")
"""/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////"""
"""HP ATK HR DEF MP SP"""
wolf=Characters("Wolf", [10,5,15,1,5,2], ["void", "void", "void"], (1,2))
shark=Characters("Shark", [15,3,10,1,5,1], ["void", "void", "void"], (1,2))
drake=Characters("Drake", [30,7,15,4,5,5], ["void", "void", "void"], (1,6))
drakek=Characters("Drake King", [140,20,20,10,70,10], ["void", "void", "void"], (1,7))
beast=Characters("Berserker", [500,2,30,10,20,5], ["void", "Slow", "Purify"], (1,2))
narator1=Characters("Beast?", [300,2,2,2,200,7], ["void", "Slow", "Tears"], (1,14))
kraken=Characters("Kraken", [300,35,15,10,150,100], ["Slow", "Purify", "Wrap"], (1,6))
"""/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////"""
