import random
import time
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
        self._gold = 0
    def increase_attack(self):
        self._ogattack += 2
    def increase_hitratio(self):
        self._oghitratio += 1
    def increase_health(self):
        self._maxhealth += 5
    def spend_gold(self, cost):
        self._gold -= cost
    def get_health(self):
        return self._health
    def get_gold(self):
        return self._gold
    def add_party(self, amount, partyskills):
        self._party == amount
        self._partyskills = partyskills
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
    def get_test(self):
        print("Attack ",self._attack,"Hitratio ", self._hitratio,"Defence ", self._defence)
    def damage(self, damage, hitratio):
        roll = random.randint(0, hitratio)
        if roll == hitratio:
            self._health-=damage * 1.5
            print("CRIT")
        elif roll >= self._defence:
            self._health-=damage
            print("Hit")
        else:
            print("Miss")
    def reset(self):
        self._health = self._maxhealth
        self._magic = self._maxmagic
        #nice
        self._hitratio = self._oghitratio
        self._defence = self._ogdefence
        self._attack = self._ogattack
    def slevelup(self):
        self._exp+=76-self._level
        if self._exp >= 100:
            self._level += 1
            self._exp = 0
            x = 0
            while x < 3:
                x += 1
                roll = random.randint(1, 5)
                if roll == 1:
                    self._ogattack += 3
                elif roll == 2:
                    self._oghitratio += 1
                elif roll == 3:
                    self._ogdefence += 1
                elif roll == 4:
                    self._maxhealth += 10
                else:
                    self._maxmagic += 5
        if self._name!="Knight":
            output_file = open("Starscrapper.txt", "w")
            output_file.write(str(self._level))
            output_file.close()
        else:
            output_file = open("Knightlv.txt", "w")
            output_file.write(str(self._level))
            output_file.close()
    def levelup(self):
        self._exp+=76-self._level
        if self._exp >= 100:
            print("LVL UP")
            time.sleep(0.3)
            self._level += 1
            self._exp = 0
            x = 0
            while x < 3:
                x += 1
                roll = random.randint(1, 5)
                if roll == 1:
                    self._ogattack += 3
                    print("<attack up>")
                    time.sleep(0.3)
                elif roll == 2:
                    self._oghitratio += 1
                    print("<hit ratio up>")
                    time.sleep(0.3)
                elif roll == 3:
                    self._ogdefence += 1
                    print("<defence up>")
                    time.sleep(0.3)
                elif roll == 4:
                    self._maxhealth += 10
                    print("<health up>")
                    time.sleep(0.3)
                else:
                    self._maxmagic += 5
                    print("<magic up>")
                    time.sleep(0.3)
        if self._name!="Knight":
            output_file = open("Starscrapper.txt", "w")
            output_file.write(str(self._level))
            output_file.close()
        else:
            output_file = open("Knightlv.txt", "w")
            output_file.write(str(self._level))
            output_file.close()
    def battle(self, enemy):
        skillet = 0
        while self._health>0 and enemy.get_health()>0:
            time.sleep(0.8)
            if skillet == 0:
                skillet = 1
            else:
                skillet = 0
            roll = random.randint(1, 10)
            if roll == 5:
                skillet = 2
            enemyskillet = random.randint(0, 2)
            skillskillet = random.randint(0, 4)
            if skillskillet == 0 or skillskillet == 1:
                skillskillet = 0
            elif skillskillet == 2 or skillskillet == 3:
                skillskillet = 1
            else:
                skillskillet = 2
            print("["+self._name+"]", "HP:", self._health, "MP:", self._magic, "skill:", self._skillist[skillet])
            print("Option 1: Attack")
            print("Option 2: Skill")
            print("Option 3: Search")
            print("Option 4: Escape")
            action = input("Number of action you would like to take: ")
            while action!="1" and action!="2" and action!="3" and action!="4" and action!="7":
                print("try again")
                print("["+self._name+"]", "HP:", self._health, "MP:", self._magic, "skill:", self._skillist[skillet])
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
                if self._skillist[skillet] == "Hit Policy":
                    self._health += self._maxhealth//2
                    if self._health > self._maxhealth:
                        self._health = self._maxhealth
                elif self._skillist[skillet] == "Mystic Point":
                    enemy.damage(self._attack*2, self._hitratio)
                elif self._skillist[skillet] == "Transform":
                    useThis = self._defence
                    self._defence = self._hitratio
                    self._hitratio = useThis
                    print("HENSHIN")
                elif self._skillist[skillet] == "Point Blank":
                    enemy.damage(self._hitratio, 100000000)
                elif self._skillist[skillet] == "Timed Illusion":
                    self._health += enemy.get_attack()
                    self._hitratio += 3
                elif self._skillist[skillet] == "Pain Remover":
                    self._health += self._magic
                    if self._health > self._maxhealth:
                        self._health = self._maxhealth
                elif self._skillist[skillet] == "Over Joyed Trick":
                    self._health = self._maxhealth//2
                    self._hitratio += 100
                    self._defence = 0
                elif self._skillist[skillet] == "Monster Form":
                    self._hitratio += 10
                    self._defence += 1
                if self._skillist[skillet] == "Fruit of God":
                    self._health += self._magic*2
                    if self._health > self._maxhealth:
                        self._health = self._maxhealth
                elif self._skillist[skillet] == "Deathless Trick":
                    self._health += self._hitratio
                    self._hitratio += self._defence
                elif self._skillist[skillet] == "Star Scrapper":
                    self._hitratio += 10
                    self._defence += 3
                    self._magic -= 2
                    self._health -= 2
                elif self._skillist[skillet] == "Star Blaster":
                    self._attack += 10
                    self._hitratio += 10
                    enemy.damage(self._attack*2, self._hitratio*10)
                    self._hitratio -= 10
                    self._attack += 10
                    self._magic -= 2
                elif self._skillist[skillet] == "Great Regen":
                    self._magic += 4
                    self._health += self._magic
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
            elif enemy.get_skills()[enemyskillet] == "Aura Force":
                print("[Enemy]: Aura Force")
                print("<enemy gains health>")
                enemy.damage(-3, 100000000)
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
                enemy.damage(self._attack*-1, 100000000)
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
                enemy.damage(-20, 100000000)
            elif enemy.get_skills()[enemyskillet] == "Time Roar2":
                print("[Enemy]: #%&$#$^%")
                self._health -= 777
                enemy.damage(-777, 100000000)
            elif enemy.get_skills()[enemyskillet] == "Vamp Bite":
                print("[Enemy]: Bite")
                self._health -= 25
                enemy.damage(-50, 100000000)
            time.sleep(0.6)
            if self._party > 0:
                if self._partyskills[skillskillet] == "Regen":
                    print("[Effect]: Regen")
                    self._health += 2
                elif self._partyskills[skillskillet] == "Hit Boost":
                    print("[Effect]: Hit Chance Up")
                    self._hitratio += 3
                elif self._partyskills[skillskillet] == "Petrify":
                    print("[Effect]: Don's Stone Face")
                    print("<your opponent slows down>")
                    print("<your magic raises>")
                    self._defence += 1
                    self._hitratio += 1
                    self._magic += 2
                elif self._partyskills[skillskillet] == "Dark Mode":
                    print("[Effect]: Fafnir's Dragon Mode")
                    print("<your stats raise sharply>")
                    self._defence += 1
                    self._hitratio += 2
                    self._attack += 2
                elif self._partyskills[skillskillet] == "The Hunt":
                    print("[Effect]: Narator?'s Cursed Skin?")
                    self._attack += 3
                    self._hitratio += 5
                    self._partyskills[skillskillet] = "Big Bang"
                elif self._partyskills[skillskillet] == "Big Bang":
                    print("[Effect]: Narator?'s Cursed Skin?")
                    self._attack += 6
                    self._hitratio += 10
                    self._partyskills[skillskillet] = "The Hunt"
                elif self._partyskills[skillskillet] == "Explosion":
                    print("[Effect]: EXPLOSION???")
                    self._attack += 10
                    self._hitratio += 10
                elif self._partyskills[skillskillet] == "Team Attack":
                    print("[Effect]: Bonus Round")
                    print("[Type]: Team Attack")
                    enemy.damage(self._attack*4, self._hitratio*4)
                elif self._partyskills[skillskillet] == "Break":
                    print("[Effect]: Bonus Round")
                    roll = random.randint(1, 4)
                    if roll == 1:
                        print("[Type]: Limit Break")
                        self._attack += 5
                        self._hitratio += 5
                    elif roll == 2:
                        print("[Type]: Bonus Strike")
                        enemy.damage(self._attack*2, self._hitratio*2)
                    elif roll == 3:
                        print("[Type]: Brave")
                        self._attack += 5
                        enemy.damage(self._attack, self._hitratio)
                    else:
                        print("[Type]: Over Throw")
                        self._defence += 2
                        self._hitratio += 5
                time.sleep(0.3)
            if self._party > 0 and enemy.get_health() < enemy.get_magic():
                roll = random.randint(1, 10)
                if roll == 5:
                    print("[Party Assault]: Active")
                    time.sleep(0.3)
                    enemy.damage(self._attack*10, self._hitratio*10)
            if self._magic < 0:
                    self._magic = 0
            if self._magic > 999:
                self._magic = 999
            if self._health > 99999:
                self._health = 99999
        print("Battle End")
        self._attack = self._ogattack
        self._hitratio = self._oghitratio
        self._defence = self._ogdefence