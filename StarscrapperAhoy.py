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
                if self._party >= 1 and self._party != 4:
                    if self._partyskills1[skillskillet] == "range mode" and self._partymp>=10:
                        print("[Shelly] ranged mode")
                        enemy.damage(self._attack+20 , self._hitratio)
                        enemy.damage(self._attack, self._hitratio+10)
                        enemy.damage(self._attack-10, self._hitratio+20)
                        self._partymp -= 10
                    elif self._partyskills1[skillskillet] == "full blast" and self._partymp>=10:
                        print("[Shelly] full blast")
                        enemy.damage(self._attack*self._hitratio, 9223372036854775807)
                        self._partymp -= 10
                    elif self._partyskills1[skillskillet] == "self strike" and self._health>=self._speed+enemy.get_attack():
                        print("[Shelly] self strike")
                        self._health -= self._speed
                        self._partymp += 30
                        self._magic += 20
                    else:
                        print("[Shelly] attack")
                        enemy.damage(self._attack, self._hitratio)
                if self._party >= 2:
                    if self._partyskills2[skillskillet2] == "regen wave" and self._partymp>=5:
                        print("[Drake] regen wave")
                        self._health += 40
                        self._partymp -= 5
                    elif self._partyskills2[skillskillet2] == "artist block" and self._partymp>=5:
                        print("[Drake] artist block")
                        self._speed += 1
                        self._hitratio += 2
                        self._partymp -= 5
                    elif self._partyskills2[skillskillet2] == "call of the dead" and self._partymp>=5:
                        print("[Drake] call of the dead")
                        self._hitratio += 4
                        enemy.damage(self._attack, self._hitratio)
                        self._partymp -= 5
                    else:
                        print("[Drake] attack")
                        enemy.damage(self._attack, self._hitratio)
                if self._party >= 3:
                    if self._partyskills3[skillskillet3] == "sprint" and self._partymp>=10:
                        print("[Neo] sprint")
                        self._speed += 2
                        self._partymp -= 10
                    elif self._partyskills3[skillskillet3] == "sharpen" and self._partymp>=5:
                        print("[Neo] sharpen")
                        self._attack += 3
                        self._hitratio += 1
                        self._partymp -= 5
                    elif self._partyskills3[skillskillet3] == "blitz" and self._partymp>=5:
                        print("[Neo] blitz")
                        self._attack += 2
                        enemy.damage(self._attack, self._hitratio)
                        self._partymp -= 5
                    else:
                        print("[Neo] attack")
                        enemy.damage(self._attack, self._hitratio)
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
                    if self._skillist[skillet] == "Ahoy!":
                        self._attack += 3
                        self._defence -= 1
                        self._health += self._magic
                        if self._defence < 1:
                            self._defence = 1
                        if self._health >self._maxhealth:
                            self._health = self._maxhealth
                    elif self._skillist[skillet] == "Cannon Fire":
                        self._attack += 10
                        enemy.damage(self._attack, self._hitratio*10)
                    elif self._skillist[skillet] == "Pain Killer":
                        self._attack -= 1
                        self._health += 10
                        if self._attack < 1:
                            self._attack = 1
                    elif self._skillist[skillet] == "Charge Strike":
                        self._attack += 5
                        self._hitratio += 5
                    elif self._skillist[skillet] == "Revol Shot":
                        self._attack += 10
                        enemy.damage(self._attack, self._hitratio)
                        self._attack -= 10
                    elif self._skillist[skillet] == "Big Bang Punch":
                        self._partymp += 20
                        self._magic += 10
                        enemy.damage(self._attack*5, self._hitratio*10)
                    elif self._skillist[skillet] == "Revolt Beam":
                        self._speed = 1
                        enemy.damage(self._attack, 999999)
                        enemy.damage(self._attack, 999999)
                        enemy.damage(self._attack, 999999)
                    elif self._skillist[skillet] == "Rebel Wishes":
                        self._attack += 5
                        self._speed -= 2
                        self._health += self._magic + self._attack
                        if self._health >self._maxhealth:
                            self._health = self._maxhealth
                    elif self._skillist[skillet] == "Soul Liberate":
                        self._attack += 10
                        self._hitratio += 10
                        self._partymp += 10
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
                elif enemy.get_skills()[enemyskillet] == "Slow":
                    print("[Enemy]: Slow")
                    self._speed -= 2
                elif enemy.get_skills()[enemyskillet] == "Aura Force":
                    print("[Enemy]: Aura Force")
                    print("<enemy gains health>")
                    enemy.damage(-3, 999999)
                elif enemy.get_skills()[enemyskillet] == "God Scape":
                    print("[Enemy]: God Scape")
                    print("<the ground distorts bellow you>")
                    self._defence = 1
                    if self._magic > 10:
                        self._magic -= 10
                    else:
                        self._health -= 5
                elif enemy.get_skills()[enemyskillet] == "Starscrapper":
                    print("[Enemy]: Starscrapper")
                    print("<time seems to speed up>")
                    self._defence = 1
                    self._hitratio = 1
                    enemy.damage(self._attack*-1, 999999)
                elif enemy.get_skills()[enemyskillet] == "Purify":
                    print("[Enemy]: Attack")
                    print("<your stats reset>")
                    roll = random.randint(0, enemy.get_hitratio())
                    if roll>self._defence:
                        print("Hit")
                        self._health-=enemy.get_attack()
                    else:
                        print("Miss")
                    self._defence = self._ogdefence
                    self._hitratio = self._oghitratio
                elif enemy.get_skills()[enemyskillet] == "Time Roar":
                    print("[Enemy]: Time Roar")
                    self._health -= 20
                    enemy.damage(-20, 999999)
                elif enemy.get_skills()[enemyskillet] == "Time Roar2":
                    print("[Enemy]: #%&$#$^%")
                    self._health -= 777
                    enemy.damage(-777, 999999)
                elif enemy.get_skills()[enemyskillet] == "Vamp Bite":
                    print("[Enemy]: Bite")
                    self._health -= 25
                    enemy.damage(-50, 999999)
                elif enemy.get_skills()[enemyskillet] == "Wrap":
                    print("[Enemy]: Wrap")
                    self._health -= 5
                    enemy.damage(-10, 999999)
                    self._magic -= 5
                    self._speed -= 1
                    if self._magic < 0:
                        self._magic = 0
                elif enemy.get_skills()[enemyskillet] == "Tears":
                    print("[Enemy]: Heavy Tears")
                    self._health -= 5
                    self._attack -= 1
                    self._speed -= 1
                    if self._attack <= 1:
                        self._attack = 2
                time.sleep(0.9)
            if self._speed < enemy.get_speed() and enemy.get_health() > 0 and self._health > 0:
                if enemy.get_skills()[enemyskillet] == "void":
                    print("[Enemy]: Attack")
                    roll = random.randint(0, enemy.get_hitratio())
                    if roll>self._defence:
                        print("Hit")
                        self._health-=enemy.get_attack()
                    else:
                        print("Miss")
                elif enemy.get_skills()[enemyskillet] == "Slow":
                    print("[Enemy]: Slow")
                    self._speed -= 1
                elif enemy.get_skills()[enemyskillet] == "Aura Force":
                    print("[Enemy]: Aura Force")
                    print("<enemy gains health>")
                    enemy.damage(-3, 999999)
                elif enemy.get_skills()[enemyskillet] == "God Scape":
                    print("[Enemy]: God Scape")
                    print("<the ground distorts bellow you>")
                    self._defence = 1
                    if self._magic > 10:
                        self._magic -= 10
                    else:
                        self._health -= 5
                elif enemy.get_skills()[enemyskillet] == "Starscrapper":
                    print("[Enemy]: Starscrapper")
                    print("<time seems to speed up>")
                    self._defence = 1
                    self._hitratio = 1
                    enemy.damage(self._attack*-1, 999999)
                elif enemy.get_skills()[enemyskillet] == "Purify":
                    print("[Enemy]: Attack")
                    print("<your stats reset>")
                    roll = random.randint(0, enemy.get_hitratio())
                    if roll>self._defence:
                        print("Hit")
                        self._health-=enemy.get_attack()
                    else:
                        print("Miss")
                    self._defence = self._ogdefence
                    self._hitratio = self._oghitratio
                elif enemy.get_skills()[enemyskillet] == "Time Roar":
                    print("[Enemy]: Time Roar")
                    self._health -= 20
                    enemy.damage(-20, 999999)
                elif enemy.get_skills()[enemyskillet] == "Wrap":
                    print("[Enemy]: Wrap")
                    self._health -= 10
                    enemy.damage(-10, 999999)
                    self._magic -= 10
                    if self._magic < 0:
                        self._magic = 0
                elif enemy.get_skills()[enemyskillet] == "Time Roar2":
                    print("[Enemy]: #%&$#$^%")
                    self._health -= 777
                    enemy.damage(-777, 999999)
                elif enemy.get_skills()[enemyskillet] == "Vamp Bite":
                    print("[Enemy]: Bite")
                    self._health -= 25
                    enemy.damage(-50, 999999)
                elif enemy.get_skills()[enemyskillet] == "Tears":
                    print("[Enemy]: Heavy Tears")
                    self._health -= 1
                    self._defence -= 1
                    self._speed += 3
                    if self._defence <= 0:
                        self._defence = 1
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
                    if self._skillist[skillet] == "Ahoy!":
                        self._attack += 3
                        self._defence -= 1
                        self._health += self._magic
                        if self._defence < 1:
                            self._defence = 1
                        if self._health >self._maxhealth:
                            self._health = self._maxhealth
                    elif self._skillist[skillet] == "Cannon Fire":
                        self._attack += 5
                        enemy.damage(self._attack, self._hitratio*5)
                    elif self._skillist[skillet] == "Pain Killer":
                        self._attack -= 2
                        self._speed += 1
                        self._health += 10
                        if self._attack < 1:
                            self._attack = 1
                    elif self._skillist[skillet] == "Charge Strike":
                        self._attack += 5
                        self._speed += 2
                    elif self._skillist[skillet] == "Revol Shot":
                        self._attack += 10
                        enemy.damage(self._attack, self._hitratio)
                        self._attack -= 10
                    elif self._skillist[skillet] == "Big Bang Punch":
                        self._partymp += 10
                        self._magic += 5
                        self._speed += 2
                        enemy.damage(self._attack, self._hitratio*5)
                    elif self._skillist[skillet] == "Revolt Beam":
                        self._speed += 20
                        self._attack += 5
                        self._hitratio += 5
                        self._defence += 1
                    elif self._skillist[skillet] == "Rebel Wishes":
                        self._attack += 2
                        self._speed += 3
                        self._health += self._attack
                        if self._health >self._maxhealth:
                            self._health = self._maxhealth
                    elif self._skillist[skillet] == "Soul Liberate":
                        self._attack += 5
                        self._hitratio += 5
                        self._speed += 2
                if self._party >= 1 and self._party != 4:
                    if self._partyskills1[skillskillet] == "range mode" and self._partymp>=10:
                        print("[Shelly] ranged mode")
                        enemy.damage(self._attack+10 , self._hitratio-10)
                        enemy.damage(self._attack, self._hitratio-10)
                        enemy.damage(self._attack-10, self._hitratio-10)
                        self._partymp -= 10
                    elif self._partyskills1[skillskillet] == "full blast" and self._partymp>=10:
                        print("[Shelly] full blast")
                        enemy.damage(self._attack*self._speed, 9223372036854775807)
                        self._speed += 1
                        self._partymp -= 10
                    elif self._partyskills1[skillskillet] == "self strike" and self._health>=self._speed+enemy.get_attack():
                        print("[Shelly] self strike")
                        self._health -= self._speed
                        self._partymp += 15
                        self._magic += 15
                    else:
                        print("[Shelly] attack")
                        enemy.damage(self._attack, self._hitratio)
                if self._party >= 2:
                    if self._partyskills2[skillskillet2] == "regen wave" and self._partymp>=10:
                        print("[Drake] regen wave")
                        self._health += 30
                        self._partymp -= 10
                    elif self._partyskills2[skillskillet2] == "artist block" and self._partymp>=5:
                        print("[Drake] artist block")
                        self._speed += 3
                        self._partymp -= 5
                    elif self._partyskills2[skillskillet2] == "call of the dead" and self._partymp>=5:
                        print("[Drake] call of the dead")
                        self._hitratio += 1
                        self._speed += 1
                        enemy.damage(self._attack, self._hitratio)
                        self._partymp -= 5
                    else:
                        print("[Drake] attack")
                        enemy.damage(self._attack, self._hitratio)
                if self._party >= 3:
                    if self._partyskills3[skillskillet3] == "sprint" and self._partymp>=5:
                        print("[Neo] sprint")
                        self._speed += 3
                        self._partymp -= 5
                    elif self._partyskills3[skillskillet3] == "sharpen" and self._partymp>=5:
                        print("[Neo] sharpen")
                        self._attack += 7
                        self._partymp -= 5
                    elif self._partyskills3[skillskillet3] == "blitz" and self._partymp>=5:
                        print("[Neo] blitz")
                        self._attack += 5
                        self._speed += 2
                        self._partymp -= 5
                    else:
                        print("[Neo] attack")
                        enemy.damage(self._attack, self._hitratio)
                time.sleep(0.9)
            if self._party > 0 and self._party != 4 and enemy.get_health() >= enemy.get_magic():
                roll = random.randint(1, 9-self._party)
                if roll == 5:
                    print("[Party]: FULL ASSAULT!")
                    enemy.damage(self._attack*self._party, self._hitratio*self._party)
                elif roll == 1:
                    print("[Party]: Magic Break!")
                    self._partymp += self._party
                elif roll == 2 and self._party == 1:
                    print("[Shelly]: cheering!")
                    self._magic += 3
            elif self._party == 4:
                roll = random.randint(1, 5)
                if roll == 1:
                    print("[Party]: Party Assault?")
                    enemy.damage(self._attack, self._hitratio)
                elif roll == 2:
                    print("[Party]: Magic Break?")
                    self._partymp += self._party
                elif roll == 3:
                    print("[Shelly]: Shelly's tears")
                    self._magic += 3
                    self._partymp += 6
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
chapter = 0
with open("AhoySave.txt", "r") as read_file:
    chapter=int(read_file.read())
with open("difficulty.txt", "r") as read_file:
    action=int(read_file.read())
with open("name.txt", "r") as read_file:
    name=str(read_file.read())
if action=="1":
    mc=Characters(name, [30,5,20,3,15,4], ["Charge Strike", "Pain Killer", "Revol Shot"], (1,2))
elif action=="2":
    mc=Characters(name, [20,3,10,2,5,1], ["Charge Strike", "Pain Killer", "Revol Shot"], (1,2))
else:
    mc=Characters(name, [15,2,8,2,5,0], ["Charge Strike", "Pain Killer", "Revol Shot"], (1,2))
with open("AhoyLV.txt", "r") as read_file:
    x=int(read_file.read())
    while(mc.get_level() < x):
        mc.slevelup()
with open("AhoyParty.txt", "r") as read_file:
    trys=int(read_file.read())
    mc.new_party(trys)
if chapter == 0:
    pa("You look around and see some weird building")
    next_engine()
    pa("How did you get here?")
    next_engine()
    voice("???", "Go! Quick! Run for the exit")
    skip_engine(5)
    pa("You start to run in a random direction")
    next_engine()
    pa("You see an exit but see some beast in the way")
    next_engine()
    pa("What is this feeling?")
    next_engine()
    pa("Your body feels warm...")
    next_engine()
    pa("Is this the truth?")
    next_engine()
    mc=Characters("???", [999,10,50,15,0,5], ["Cannon Fire", "Ahoy!", "Big Bang Punch"], (1,2))
    mc.new_party(3)
    enemy = beast
    mc.battle(enemy)
    pa("You blacked out")
    next_engine()
    #main story start
    pa("you wake up in a weird space")
    voice("???", "Welcome hero to a new world")
    skip_engine(4)
    print("Press Enter")
    next_engine()
    voice("???", "I am the narator to your story")
    next_engine()
    voice("Narator", "I will help you on your quest")
    next_engine()
    voice("Narator", "So, what is your name?")
    name=input("Name: ")
    if name=="your mom" or name=="jayden" or name=="Your Mom" or name=="Your mom":
        voice("Narator", "You are not funny")
        next_engine()
        name="loser"
    elif name=="jesus" or name=="Jesus" or name=="God":
        voice("Narator", "Those people don't exist here")
        next_engine()
        name="false prophet"
    elif name=="Narator" or name=="narator":
        voice("Narator", "No it isn't")
        next_engine()
        name="Copy Cat"
    elif name=="Bill" or name=="bill":
        voice("Bill", "May I borrow that?")
        next_engine()
        name="Bill?"
    voice("Narator", "What a nice name")
    next_engine()
    print("from now on you will only need the number pad and enter")
    mc=Characters(name, [20,5,10,2,10,1], ["Charge Strike", "Pain Killer", "Revol Shot"], (1,2))
    next_engine()
    voice("Narator", "Is this your first time hero?")
    next_engine()
    voice("Narator", "Do I need to teach you how to fight?")
    print("1=Yes")
    print("2=No")
    action=input("What will you do? ")
    if action=="1":
        print("Tutorial battle 1")
        enemy=Characters("Small Beast", [30,2,10,1,5,0], ["void", "void", "void"], (1,2))
        mc.battle(enemy)
        print("Tutorial battle 2")
        enemy=Characters("Small Beast", [20,2,10,1,5,1], ["void", "void", "void"], (1,2))
        mc.battle(enemy)
        re_burst(mc, enemy)
        print("Tutorial battle 3")
        enemy=Characters("Small Beast", [10,2,10,1,5,2], ["void", "void", "void"], (1,2))
        mc.battle(enemy)
    else:
        voice("Narator", "So, we have met before?")
        next_engine()
    voice("Narator", "Now to choose dificulty")
    print("1=easy")
    print("2=normal")
    print("3=hard")
    action=input("what mode will you play? ")
    if action=="1":
        mc=Characters(name, [30,5,20,3,15,4], ["Charge Strike", "Pain Killer", "Revol Shot"], (1,2))
    elif action=="2":
        mc=Characters(name, [20,3,10,2,5,1], ["Charge Strike", "Pain Killer", "Revol Shot"], (1,2))
    else:
        mc=Characters(name, [15,2,8,2,5,0], ["Charge Strike", "Pain Killer", "Revol Shot"], (1,2))
    output_file = open("difficulty.txt", "w")
    output_file.write(str(action))
    output_file.close()
    chapter += 1
saver(chapter)
if chapter == 1:
    x=0
    while x<=4:
        x+=1
        pa("You wake up somewhere")
        next_engine()
        pa("Looking around you see the ocean")
        next_engine()
        pa("Water goes on for miles")
        next_engine()
        print("1=walk across beach")
        print("2=try to swim")
        action=input("What will you do? ")
        b=0
        while action=="1" and b==0:
            pa("You walk across the beach")
            next_engine()
            pa("You come across a small cave")
            next_engine()
            pa("something comes out and looks at you")
            next_engine()
            pa("It looks like a wolf")
            next_engine()
            pa("It suddenly bolts at you")
            enemy=wolf
            mc.battle(enemy)
            if mc.get_health()>0:
                mc.levelup(enemy.get_exp())
                b=1
                next_engine()
            re_burst(mc, enemy)
        if action=="1":
            pa("You walk into the cave")
            next_engine()
            pa("It is too dark to see")
            next_engine()
            pa("Soemthing feels off")
            next_engine()
        i=0
        while action=="2" and i==0:
            pa("You jump into the water")
            next_engine()
            pa("You keep going")
            next_engine()
            pa("Looking back you already made it pretty far")
            next_engine()
            pa("You might actual make it")
            next_engine()
            pa("You see a boat in the distance")
            next_engine()
            pa("Something bites your leg")
            skip_engine(3)
            pa("You get dragged under the water")
            skip_engine(4)
            pa("A shark attacks you")
            next_engine()
            enemy=shark
            mc.battle(enemy)
            if mc.get_health()>0:
                mc.levelup(enemy.get_exp())
                i=1
                pa("You climb onto the boat")
                next_engine()
            re_burst(mc, enemy)
        if action=="2":
            pa("The ship is old an rotted")
            next_engine()
            pa("You still see no land in the distance")
            next_engine()
            pa("Just a small island which you came")
            next_engine()
            pa("Something feels off")
            next_engine()
    pa("You wake up on the beach again")
    next_engine()
    pa("You see a box of matches in the sand")
    next_engine()
    pa("You go to explore the beach")
    next_engine()
    pa("You come across a cave")
    next_engine()
    pa("Nothing stands infront of it")
    next_engine()
    pa("You light a match and enter the cave")
    next_engine()
    pa("Some kind of scaled beast appears")
    next_engine()
    pa("It roars at you then walks away")
    next_engine()
    pa("You walk farther into the cave")
    next_engine()
    pa("A box sits in the middle of the floor")
    next_engine()
    pa("The box is covered in vines")
    next_engine()
    pa("You walk upto the box")
    next_engine()
    pa("It seems to be locked")
    skip_engine(4)
    voice("???", "OPEN THE BOX!!!")
    skip_engine(4)
    voice("???", "OPEN IT ALREADY!!!")
    skip_engine(4)
    pa("Something compells you to open the box")
    next_engine()
    pa("You bang on the lock and it opens")
    next_engine()
    pa("A girl in all white steps out")
    skip_engine(5)
    voice("???", "Thank you loser!")
    mc.new_party(1)
    skip_engine(5)
    pa("You feel breathing on your back")
    next_engine()
    pa("Shelly joins the party!")
    skip_engine(4)
    pa("The beast attacks you")
    next_engine()
    enemy=drake
    mc.battle(enemy)
    mc.levelup(enemy.get_exp())
    re_burst(mc, enemy)
    pa("You feel tired and pass out")
    next_engine()
    chapter += 1
    saved()
saver(chapter)
if chapter == 2:
    next_engine()
    pa("You slowly start to wake up")
    next_engine()
    voice("???", "WAKE UP!!!")
    next_engine()
    pa("You quickly bolt awake")
    skip_engine(3)
    pa("you look around a bit")
    skip_engine(3)
    pa("You seem to be on a boat")
    next_engine()
    voice("???", "Finally, you are so annoying")
    skip_engine(5)
    voice("???", "I'm Shelly, thanks for saving me")
    next_engine()
    voice("Shelly", "Welcome aboard my ship")
    next_engine()
    voice("Shelly", "We call it the hour glass")
    next_engine()
    voice("Shelly", "You might be wondering why")
    skip_engine(5)
    voice("Shelly", "Well that's a secret")
    next_engine()
    pa("You decide to explore the ship")
    next_engine()
    ship([drake, drake, drakek])
    pa("You finally reached land")
    saved()
saver(chapter)
if chapter == 3:
    next_engine()
    voice("Shelly", "Well, we made it")
    skip_engine(3)
    pa("You head onto the land")
    next_engine()
    pa("Heading towards the inn")
    next_engine()
    pa("You hear a few men talking")
    next_engine()
    voice("man1", "Did you hear about the mission?")
    skip_engine(4)
    voice("man2", "Yeah, when do they leave?")
    skip_engine(4)
    voice("man1", "The first crew leaves in 4 days")
    skip_engine(4)
    voice("man3", "You think they can finally find it?")
    skip_engine(5)
    voice("man2", "No way, it's been lost for years")
    skip_engine(4)
    voice("man1", "Yeah, the old man's chest")
    skip_engine(4)
    voice("man2", "They say it holds a powerful secret")
    next_engine()
    pa("You wonder what could be in that chest")
    next_engine()
    pa("You continue on to the inn")
    skip_engine(3)
    pa("Arriving at the inn you decide to stay the night")
    next_engine()
    pa("In your dream you see a beast in white clothing")
    next_engine()
    pa("Tears are rolling down it's eyes, is it crying?")
    skip_engine(5)
    pa("The beast roars and attacks you")
    next_engine()
    enemy = narator1
    mc.battle(enemy)
    if mc.get_health() > 0:
        mc.levelup(enemy.get_exp())
    re_burst(mc, enemy)
    mc.levelup(enemy.get_exp())
    saved()
    chapter += 1
saver(chapter)