
import random
def prob():
    roll = random.randint(1,101)
    return roll

class Character:
    def __init__(self, name, health, power, gold ,armor, inventory,equiped, evade):
        self.name = name
        self.equiped = equiped
        self.health = health
        self.power = power
        self.gold = gold
        self.armor= armor + equiped
        self.maxhealth = health
        self.maxarmor = self.armor + self.equiped
        self.inventory = inventory
        self.startpower = power
        self.evade = evade

    def add_item_inv(self,name):
        self.inventory.append(name)

    def update_armor(self):
        self.armor = self.armor + self.equiped
        self.maxarmor = self.armor + self.equiped

    def remove_item_inv(self,item):
        itemindex = self.inventory.index(item)
        if itemindex >= 0:
            del self.inventory[itemindex]

    def print_item_info(self):
        print(f"{self.name} : adds {self.power_bonus} power, fits: {self.slot_type} ")    

    def print_status(self):
        print(f"\n{self.name} has:\n{self.health} Health\n{self.armor} Armor\n{self.power} Power\n")

    def print_status_player(self):
        print(f"\n{self.name} has {self.health} health, {self.power} power, {self.armor} armor and {self.gold} gold.\n")

    def print_inventory(self):
        print("*** INVENTORY ***")
        print(f"Gold: {hero.gold}")
        for item in self.inventory:
            print(f"\n{self.inventory.index(item) + 1}: {item}")

    def resurrect(self):
        if self.health <= 0:
            self.health = self.maxhealth * .5
            print("\nIt is not yet your time traveller! ARISE!\n")
            print(f"{self.name} has been resurrected!\n")
            print("Your death has damaged your armor!")
            self.armor =0

    def respawn(self):
        if self.health <= 0:
            self.health = self.maxhealth

    def isDead(self):
        if self.health <= 0:
            dead_input = input(dead_menu)
            if dead_input == '1':
                self.resurrect()
            elif dead_input == '2':
                raise SystemExit
    def print_evade(self,opponent):
        print(f'{opponent.name} evades {self.name}\'s attack!')

    def alive(self):
        alive = True
        if self.health <= 0:
            alive = False
        else: 
            return alive
    def calc_evade(self,opponent):
        if opponent.evade <= 2:
            if prob() > 90:
                self.print_evade(opponent)
            else:
                self.swing(opponent)
        elif opponent.evade <= 4:
            if prob() > 85:
                self.print_evade(opponent)
            else:
                self.swing(opponent)
        elif opponent.evade <= 6:
            if prob() > 82:
                self.print_evade(opponent)
            else:
                self.swing(opponent)

        elif opponent.evade <= 8:
            if prob() > 80:
                return True
        else:
            return False

    def swing(self,opponent):
        if opponent.armor == 0:
            opponent.health -= self.power
            print(f"{self.name} strikes {opponent.name} for {self.power} damage.\n")

        elif opponent.armor >= self.power:
            print(f"{opponent.name}'s armor blocked {self.name}'s strike!\n")
            print(f"{opponent.name}'s armor blocks {self.power} damage!\n")
            print(f"{opponent.name}'s armor suffers minor damage! -1 armor durability!\n")
            opponent.armor -= 1

        elif opponent.armor < self.power:
            damage = self.power - opponent.armor
            opponent.health -= damage
            print(f"{self.name} strikes {opponent.name} for {self.power} damage.\n")
            print(f"{opponent.name}'s armor blocks {opponent.armor} damage!\n")
            print(f"{opponent.name}'s armor suffers minor damage! -1 armor durability!\n")
            opponent.armor -= 1


    def attack(self, opponent):
        self.calc_evade(opponent)
        # self.swing(opponent)
        if opponent.armor <= 0:
            opponent.armor = 0

        if opponent.health <= 0:
            print(f"{opponent.name} has died!\n")

        if hero.health > hero.maxhealth:
                hero.health = hero.maxhealth
        hero.isDead()

    def high_ground(self):
        print('You feel the spirit of Obi-Wan Kenobi. You know that you now hold the High Ground!\n')
        print
        self.power = self.power * 10

class Fighter(Character):
    def __init__(self,name, health , power, gold, armor,inventory, equiped,evade):
        self.name = name
        self.equiped = equiped
        self.health = health
        self.power = power
        self.gold = gold
        self.armor = armor + self.equiped
        self.maxhealth = health
        self.maxarmor = armor + equiped
        self.inventory = inventory
        self.startpower = power
        self.evade = evade

    def passive(self,opponent):
        if prob() < 10:
            self.power = self.power * 2
            self.armor = 0
            print('Enrage!')
            print("Your damage output is doubled but your armor has been destroyed by your increased size!")
            print('Wait, are you turning.....green?')
        else:
            self.power = self.startpower

class Medic(Character):
    def __init__(self,name, health, power, gold, armor,inventory, equiped,evade):
        self.name = name
        self.equiped = equiped
        self.health = health
        self.power = power
        self.gold = gold
        self.armor= armor + equiped
        self.maxhealth = health
        self.maxarmor = self.armor + self.equiped
        self.inventory = inventory
        self.startpower = power
        self.evade = evade

    def passive(self,opponent):
        if prob() <= 20:
            self.health = self.health + 2
            if self.health > self.maxhealth:
                self.health = self.maxhealth
            print(f"You feel Rejuvenated! You have {self.health} health!")

class Shadow(Character):
    def __init__(self,name, health, power, gold, armor,inventory,equiped, evade):
        self.name = name
        self.equiped = equiped
        self.health = health
        self.power = power
        self.gold = gold
        self.armor= armor + equiped
        self.maxhealth = health
        self.maxarmor = self.armor + self.equiped
        self.inventory = inventory
        self.startpower = power
        self.evade = evade

    def passive(self, opponent): 
            if prob() > 10: 
                self.health += opponent.power 
                print("You cannot strike the Cloak of Shadows!\n")
            elif prob() < 10:
                opponent.power = opponent.power

class Mage(Character):
    def __init__(self,name, health, power, gold, armor,inventory,equiped, evade):
        self.name = name
        self.equiped = equiped
        self.health = health
        self.power = power
        self.gold = gold
        self.armor= armor + equiped
        self.maxhealth = health
        self.maxarmor = self.armor + self.equiped
        self.inventory = inventory
        self.startpower = power
        self.evade = evade

    def passive(self,opponent):
        if prob() > 60: 
            opponent.power = opponent.startpower *.5
            print("\n You are surrounded by a barrier of arcane energy! You take half damage! \n")
        else:
            opponent.power = opponent.startpower

class Bard(Character):
    def __init__(self,name, health, power,gold, armor,inventory, equiped,evade):
        self.name = name
        self.equiped = equiped
        self.health = health
        self.power = power
        self.gold = gold
        self.armor= armor + equiped
        self.maxhealth = health
        self.maxarmor = self.armor + self.equiped
        self.inventory = inventory
        self.startpower = power
        self.evade = evade

    def passive(self, opponent):
        if prob() > 80:
            self.power = opponent.health
            print(f"{opponent.name} is Star Struck! Perhaps a stiff breeze will topple {opponent.name} now!" )
        else:
            self.power = self.startpower

class Goblin(Character):
    def __init__(self,name, health, power, gold, armor,inventory, equiped,evade):
        self.name = name
        self.equiped = equiped
        self.health = health
        self.power = power
        self.gold = gold
        self.armor= armor + equiped
        self.maxhealth = health
        self.maxarmor = self.armor + self.equiped
        self.inventory = inventory
        self.startpower = power
        self.evade = evade

    def passive(self,opponent):
        if prob() > 50:
            self.power = self.power + 2
            print(f"{self.name} has a sharp stick! + 2 power!")
        else:
            self.power = self.startpower

class Wizard(Character):
    def __init__(self,name, health, power, gold, armor,inventory, equiped,evade):
        self.name = name
        self.equiped = equiped
        self.health = health
        self.power = power
        self.gold = gold
        self.armor= armor + equiped
        self.maxhealth = health
        self.maxarmor = self.armor + self.equiped
        self.inventory = inventory
        self.startpower = power
        self.evade = evade


    def passive(self,opponent):
        if prob() > 90:
            self.armor = self.armor + 10
            print(f"{self.name} conjured a suit of magical armor! + 10 armor!")

class Zombie(Character):
    def __init__(self,name,health,power, gold, armor,inventory,equiped, evade):
        self.name = name
        self.equiped = equiped
        self.health = health
        self.power = power
        self.gold = gold
        self.armor= armor + equiped
        self.maxhealth = health
        self.maxarmor = self.armor + self.equiped
        self.inventory = inventory
        self.startpower = power
        self.evade = evade

    def passive(self,opponent):
        opponent = opponent
        if self.health < self.maxhealth:
            self.health = self.maxhealth
            print(f"{self.name} regenerates!")

class Item:
    def __init__(self,name, health, power, armor, evade):
        self.name = name
        self.power = power
        self.armor = armor
        self.health = health
        self.evade = evade

    def use_super_tonic(self,hero):
        hero.health += self.health

    def use_potpill(self,hero):
        hero.power += self.power

    def use_scaly(self,hero):
        hero.armor += self.armor

    def use_dodge(self,hero):
        hero.evade += self.evade

    def use_app_armor(self,hero):
        hero.equiped += self.armor
        hero.update_armor()

    def use_journ_armor(self,hero):
        hero.equiped += self.armor
        hero.update_armor()
        
    def use_mast_armor(self,hero):
        hero.equiped += self.armor
        hero.update_armor()

    def use_infinite(self,hero):
        hero.equiped += self.armor
        hero.health += self.health
        hero.power += self.power
        hero.armor += self.armor
        hero.update_armor()


    def print_item_info(self,name, hero):
        print(f"{self.name} : adds {self.power_bonus} power, fits: {self.slot_type} ")    

# class Store: 
#     def __init__self(self):
#         self.items = []

#     def add_item(self,name, power_bonus, slot_type):
#         itemObj = Item(name, power_bonus, slot_type)
#         self.items.append(itemObj)


def choose_item():
    hero.print_inventory()
    useitemchoice = int(input('Which item would you like to use?'))
    useitemindex = useitemchoice - 1
    SuperTonic = Item('Super Tonic',10,0,0,0)
    PotPill = Item("Potencey Pill",0,10,0,0)
    scaly = Item("Draught of the Dragon",0,0,100,0)
    dodge= Item("Dodge Bottle",0,0,0,4)

    if hero.inventory[useitemindex] == 'Super Tonic':
        SuperTonic.use_super_tonic(hero)
        print('You drink Super Tonic! +10 health!')
        del hero.inventory[useitemindex]

    elif hero.inventory[useitemindex] == 'Potencey Pill':
        PotPill.use_potpill(hero)
        print('You take a Potencey Pill! +10 power!')
        del hero.inventory[useitemindex]

    elif hero.inventory[useitemindex] == "Draught of the Dragon":
        scaly.use_scaly(hero)
        print('You drink the Draught of the Dragon! Your skin is now covered in dragon scales! +100 Armor')
        del hero.inventory[useitemindex]

    elif hero.inventory[useitemindex] == 'Dodge Bottle':
        PotPill.use_dodge(hero)
        print('You catch the Dodge Bottle! +4 Evade!')
        del hero.inventory[useitemindex]

def choose_enemy():
    choice = input(enemy_menu)
    goblin = Goblin("The goblin",25,3,15,0,[],0,4)
    zombie = Zombie("Rob the Zombie",100,1,50,0,[],0,0)
    wizard = Wizard("Sarumon of Many Colours",200,15,1000,5,[],0,0)


    for choice in choice:
        if choice == '1':
            enemy = goblin
            print("\n********** A goblin leaps out of the bushes! **********\n")
            
        elif choice == '2':
            enemy = zombie
            print("\nYou hear a soft groaning... whats that smell?   Its Rob the Zombie!\n")

        elif choice == '3':
            enemy = wizard
            print('\n Your demise is closer than you think, if you believe you are welcome here!')

        elif choice == '4':
            pass
        else:
            print("That isnt a valid selection.")
    return enemy

def combat():
    while enemy.alive() and hero.alive():
        enemy.print_status()
        hero.print_status()
        hero.passive(enemy)
        enemy.passive(hero)
        raw_input = input(combat_menu)
        if raw_input == "1":
            print("\n********** You chose combat! **********\n")
            hero.attack(enemy)

        elif raw_input == "2":
            print("\nWhat are you doing!? Dont just stand there!\n")
            print('*'* 60 + '\n')

        elif raw_input == "3":
            print("\nYou run from the fight!\n")
            break

        elif raw_input == "4":
            choose_item()
            
        elif raw_input == "obiwan":
            print("Help me Obi-Wan Kenobi! You're my only hope!\n")
            hero.high_ground()

        else:
            print(f"Invalid input {raw_input}")

        if enemy.alive():
            if raw_input != 'obiwan' or raw_input != '4':
                enemy.attack(hero)
            else: 
                pass

    if not enemy.alive():
        hero.gold += enemy.gold
        print(f"You loot {enemy.gold} gold!")

    enemy.respawn()

def town():
    while True: 
        town_input = input(town_menu)
        if town_input == '1':
            blacksmith(hero)
            pass
        elif town_input == '2':
            apothecary(hero)
            pass
        elif town_input == '3':
            deckard()
            pass
        elif town_input == '4':
            break
        elif town_input == 'gooddeals':
            black_market(hero)
            pass
        else:
            print("Invalid Input")

def deckard():
    print(" My name is Deckard Cain. Stay awhile and listen!")
    choice = input('''
    Would you like to hear a story?
            1. Yes 
            2. No
    ''')
    for choice in choice:
        if choice == '1':
            story_time()
        elif choice == '2':
            print('Goodbye')
            break

def blacksmith(hero):
    while True: 
        bs_input = input(blacksmith_menu)
        if bs_input == '1':
            dmg = int(input("How much damage would you like repaired?"))

            if hero.gold < dmg:
                print("You dont have enough money!")

            elif hero.gold >= dmg:
                hero.armor +=dmg
                hero.gold -= dmg
                print(f"Your armor has been repaired")

            elif hero.armor == hero.maxarmor:
                print('Your armor is not in need of repair.')

        elif bs_input == '2':
            app_armor = Item("Apprentice Armor Set",0,0,10,0)
            journ_armor = Item('Journeyman Armor Set',0,0,20,0)
            master_armor = Item('Mastercraft Armor Set',0,0,30,0)
            infinite = Item('Infinity Gloves',100,100,100,0)
            bschoice = input(bsitem_menu)
            if bschoice == '1':
                if hero.gold<20:
                    print("You dont have enough money!")

                elif hero.gold>20:
                    hero.equip = 0
                    app_armor.use_app_armor(hero)
                    print('You have equiped Apprentice Armor Set')
                    hero.gold -= 20

            elif bschoice == '2':
                if hero.gold < 40:
                    print("You dont have enough money!")

                elif hero.gold>=40:
                    hero.equip = 0
                    journ_armor.use_journ_armor(hero)
                    print('You have equiped Journeyman Armor Set')
                    hero.gold -= 40

            elif bschoice == '3':
                if hero.gold < 80:
                    print("You dont have enough money!")

                elif hero.gold >= 80:
                    hero.equip = 0
                    master_armor.use_mast_armor(hero)
                    print('You have equiped Mastercraft Armor Set')
                hero.gold -= 80

            elif bschoice == '4':
                if hero.gold < 5000:
                        print("You dont have enough money!")

                elif hero.gold >= 5000:
                    hero.equip = 0
                    infinite.use_infinite()
                    print('You have equiped the Infinity Gloves!')
                    hero.gold -= 5000

        elif bs_input == 'E' or 'e':
            break

        hero.update_armor()

        if hero.armor > hero.maxarmor:
            hero.armor = hero.maxarmor
            print('Thanks for the extra!')

def apothecary(hero):
    while True: 
        ap_input = input(apothecary_menu)
        if ap_input == '1':
            dmg = hero.maxhealth - hero.health
            if hero.gold < dmg:
                print("You dont have enough money!")
            elif hero.gold >= dmg:
                hero.health +=dmg
                hero.gold -= dmg
                print(f"Your health has been replenished")
            elif hero.health == hero.maxhealth:
                print('Your health is not in need of attention.')

        elif ap_input == '2':
            ap_item_choice = input(ap_item_menu)
            if ap_item_choice == "1":
                if hero.gold < 15:
                    print("You dont have enough money!")

                elif hero.gold>=15:
                    hero.add_item_inv('Super Tonic')
                    hero.print_inventory()
                    hero.gold -=15

            elif ap_item_choice == "2":
                if hero.gold < 15:
                    print("You dont have enough money!")

                elif hero.gold >=15:
                    hero.add_item_inv('Potencey Pill')
                    hero.print_inventory()
                    hero.gold -= 15

            elif ap_item_choice == '3':
                if hero.gold < 1000:
                    print("You dont have enough money!")

                elif hero.gold >= 1000:
                    hero.add_item_inv('Draught of the Dragon')
                    hero.print_inventory()
                    hero.gold -= 1000

            elif ap_item_choice == "4":
                if hero.gold < 30:
                    print("You dont have enough money!")

                elif hero.gold >=30:
                    hero.add_item_inv('Dodge Bottle')
                    hero.print_inventory()
                    hero.gold -= 30

        elif ap_input == 'E' or 'e':
            break

        if hero.health > hero.maxhealth:
            hero.health = hero.maxhealth
            print('Thanks for the extra!')

def black_market(hero):
    while True:
        bm_input = input(bm_menu)
        if bm_input == '1':
            hero.health = hero.maxhealth
            
        elif bm_input == '2':
            hero.armor = hero.maxarmor

        elif bm_input == '3':
            hero.health = 0
            print(f'{hero.name} has died')
            print("Its called a DEATH STICK! What did you think would happen?")
            hero.isDead()
            break

        elif bm_input == '4':
                bm_choice = input(bm_items)
                if bm_choice == '1':
                    hero.add_item_inv('Super Tonic')
                    hero.print_inventory()

                elif bm_choice == '2':
                    hero.add_item_inv('Potencey Pill')
                    hero.print_inventory()

                elif bm_choice =='3':
                    hero.add_item_inv('Draught of the Dragon')
                    hero.print_inventory()

                elif bm_choice == '3':
                    hero.add_item_inv('Dodge Bottle')
                    hero.print_inventory()
                    
        elif bm_input == '5':

            break


        else:
            break

def story_time():
    story = random.choice(stories)
    print(story)

bsitem_menu = '''
Select an item to purchase:
        1.Apprentice Armor Set : 20 gold
            +10 Armor
            An apprentice armorer crafted this.

        2.Journeyman Armor Set : 40 gold
            +20 Armor
            A journeyman armorer crafted this.

        3.Mastercraft Armor Set : 80 gold
            +30 Armor
            A master armorer crafted this.

        4.Infinity Gloves : 5,000 gold
            +100 armor| +100 power |+100 health
            Some angry purple dude returned these awhile ago. Complained that they didn't 
            offer any head protection. Dude, they're GLOVES!
'''

bm_items = ('''
****** Black Market Items ******
1. Super Tonic

2. Potency Pill

3. Draught of the Dragon

4. Dodge Bottle

''')
stories =[
''' 
    It is a period of civil war.

    Rebel spaceships, striking from a hidden base, 

    have won their first victory against the evil Galactic Empire. 


    During the battle, Rebel spies managed to steal secret plans to the Empire’s ultimate weapon, 

    the DEATH STAR,

    an armoured space station with enough power to destroy an entire planet. 


    Pursued by the Empire’s sinister agents, Princess Leia races home aboard her starship,

    custodian of the stolen plans that can save her people and restore freedom to the galaxy. . .
''',
'''

            The world is changed: I feel it in the
            water, I feel it in the earth, I smell it
            in the air...Much that once was is lost,
            for none now live who remember it.

            It began with the forging of the Great
            Rings...

            Three were given to the Elves, immortal,
            wisest...fairest of all beings.

            Seven to the Dwarf Lords, great miners
            and craftsmen of the mountain halls.

            And Nine...nine rings were gifted to the
            race of Men who, above all else, desire
            power.

            For within these rings was bound the
            strength and will to govern each race.

            But they were all of them deceived.

            ...for another ring was made.



            In the land of Mordor, in the fires of
            Mount Doom, the Dark Lord Sauron forged
            in secret a Master Ring to control all
            others.

            ...and into this Ring he poured his
            cruelty, his malice and his will to
            dominate all life.


            One Ring to rule them all...


            One by one the Free lands of Middle earth
            fell to the power of the ring.


            But there were some.....who resisted.



            A last alliance of Men and Elves marched
            against the armies of Mordor.

            On the slopes of Mount Doom they fought
            for the freedom of Middle- Earth.

            Victory was near!

            But the power of the Ring could not be
            undone.

            It was in this moment..when all hope had
            faded, that Isildur, son of the king,
            took up his father's sword.

            Sauron, the enemy of the Free Peoples of
            Middle Earth, was defeated.

            The Ring passed to Isildur...who had this
            one chance to destroy evil forever.

            But the hearts of Men are easily
            corrupted. And the Ring of Power has a
            will of its own.

            It betrayed Isildur to his death.

            And some things that should not have been
            forgotten...were lost.

            History became legend...


            
            Legend became myth...



            And for two and a half thousand years the
            Ring passed out of all knowledge.

            Until, when chance came, it ensnared a
            new bearer!

            The Ring came to the creature Gollum, who
            took it deep into the tunnels of the
            Misty Mountains.

            And there, it consumed him.

            The Ring brought to Gollum unnatural long
            life. For five hundred years it poisoned
            his mind. And in the gloom of Gollum's
            cave...

            It waited.

            Darkness crept back into the forests of
            the world. Rumor grew of a Shadow in the
            East...whispers of a nameless fear. And
            the Ring of Power perceived...its time
            had now come. It abandoned Gollum.

            But something happened then the Ring did
            not intend...

            It was picked up by the most unlikely
            creature imaginable...


''',
'''
.==============================================.
|                                              |
|                           .'\                |
|                          //  ;               |
|                         /'   |               |
|        .----..._    _../ |   \               |
|         \'---._ `.-'      `  .'              |
|          `.    '              `.             |
|            :            _,.    '.            |
|            |     ,_    (() '    |            |
|            ;   .'(().  '      _/__..-        |
|            \ _ '       __  _.-'--._          |
|            ,'.'...____'::-'  \     `'        |
|           / |   /         .---.              |
|     .-.  '  '  / ,---.   (     )             |
|    / /       ,' (     )---`-`-`-.._          |
|   : '       /  '-`-`-`..........--'\         |
|   ' :      /  /                     '.       |
|   :  \    |  .'         o             \      |
|    \  '  .' /          o       .       '     |
|     \  `.|  :      ,    : _o--'.\      |     |
|      `. /  '       ))    (   )  \>     |     |
|        ;   |      ((      \ /    \___  |     |
|        ;   |      _))      `'.-'. ,-'` '     |
|        |    `.   ((`            |/    /      |
|        \     ).  .))            '    .       |
|     ----`-'-'  `''.::.________:::mx'' ---    |
|                                              |
|                                              |
|                                              |
'=============================================='
*** You know how This ends... 
'''
]

ap_item_menu = ('''
Pick an Item to purchase:
        1. Super Tonic : 15 gold
            A powerful health tonic! +10 Health!

        2. Potencey Pill : 15 gold
        A little blue pill with a powerful potencey boost! +10 Power!
            (If effect last longer than 4 hours contact your Healer.)

        3. Draught of the Dragon : 1000 gold
            This unassuming bottle contains the essence of a creature 
                far more powerful than you can imagine.
        
        4. Dodge Bottle : 30 gold 
            Masterclass in evasive techniques. Provided you can catch the damn thing. +4 Evade

''')
dead_menu = ('''
                                         .""--..__
                     _                     []       ``-.._
                  .'` `'.                  ||__           `-._
                 /    ,-.\                 ||_ ```---..__     `-.
                /    /:::\\               /|//}          ``--._  `.
                |    |:::||              |////}                `-.\\
                |    |:::||             //'///                    `.\\
                |    |:::||            //  ||'                      `|
                /    |:::|/        _,-//\  ||
               /`    |:::|`-,__,-'`  |/  \ ||
             /`  |   |'' ||           \   |||
           /`    \   |   ||            |  /||
         |`       |  |   |)            \ | ||
        |          \ |   /      ,.__    \| ||
        /           `         /`    `\   | ||
       |                     /        \  / ||
       |                     |        | /  ||
       /         /           |        `(   ||
      /          .           /          )  ||
     |            \          |             ||
    /             |          /             ||
   |\            /          |              ||
   \/`-._       |           /              ||
    //   `.    /`           |              ||
   //`.    `. |             \              ||
  ///\ `-._  )/             |              ||
 //// )   .(/               |              ||
 ||||   ,'` )               /              //
 ||||  /                    /             || 
 `\\` /`                    |             // 
     |`                     \            ||  
    /                        |           //  
  /`                          \         //   
/`                            |        ||    
`-.___,-.      .-.        ___,'        (/    
         `---'`   `'----'`
******** You Have Died! ********
    Would you like to continue?
            1. Yes
            2. No
''')
bm_menu =('''
******* Black Market *******
    1. Be Healed by Witch Doctor. Are those eyeballs? Entrails? Yuck!

    2. Repair Armor. Is that rust?

    3. Wanna buy a Death Stick?

    4. Buy Items. 

    5. Return to the fairer parts of Tristram.
''')

blacksmith_menu = ('''
***** Welcome to the Blacksmith! *****
    1. Repair armor:
        One gold per armor point.

    2. Buy items

    3. Go back to Town
''')
apothecary_menu = ('''
***** Welcome to the Apothecary! *****
    1. Heal me! 
        One gold per Health Point

    2. Buy Items

    3. Go back to Town
''')
char_create_menu = ('''
*** Select a Class ***
    1. Fighter - A close in combat specialist who can take a hit and favors a good, gritty brawl. 

    2. Medic - A balanced medical professional who has a chance to passively heal themselves
    
    3. Shadow- A nimble acrobat who flits through combat dodging blows and dealing absurd damage, but cannot take a hit. 

    4. Mage - A glass cannon who has a chance to conjure a damage reducing shield. 

    5. Bard - A "renowned" musical afficianado who has "regailed royalty and commoner alike" with dashing songs of daring adventures!
            Surely you've heard of them? 'Toss a Coin in my Pitcher'?  No?
''')
Main_Menu = ('''
****** Main Menu ******
What would you like to do? 
    1. Fight a Monster
    2. Go to Town
    3. See Player Status
    
    Press E to Exit Game
''')
town_menu = ('''
****** Welcome to Tristram! ******
Where would you like to go?
    1. Blacksmith
    2. Apothecary
    3. Speak to Town Elder
    4. Leave Town

''')

enemy_menu =('''
Who would you like to fight? Select an option number:
        1. Goblin
        2. Zombie
        3. Wizard
''')

combat_menu=(f'''
What do you want to do?

1. Fight! 
2. Hesitate?
3. Flee! Flee for your life!
4. Use Item
''')

def character_creation():
    name = input('What is your characters name?\n')
    char_input = input(char_create_menu)
    fighter = Fighter(name,20,10,100,10,[],0,0)
    medic = Medic(name,20,5,100,5,[],0,0)
    shadow = Shadow(name,1,20,100,0,[],0,4)
    mage = Mage(name,20,10,100,5,[],0,0)
    bard = Bard(name,20,5,150,0,[],0,0)
    for char_input in char_input:
        if char_input == '1':
            hero = fighter
            
        elif char_input == '2':
            hero = medic
            
        elif char_input == '3':
            hero = shadow
            
        elif char_input == '4':
            hero = mage
            
        elif char_input == '5':
            hero = bard
        break
    return hero

#Game Engine starts here
# need to create a hero variable. 
hero = character_creation()
print(f'Welcome {hero.name}!')
while True:
    mm_input = input(Main_Menu)

    if mm_input == '1':
        enemy = choose_enemy() 
        combat()

    elif mm_input == '2':
        town()

    elif mm_input == '3':
        hero.print_status_player()
        print(hero.armor)

    elif mm_input == "E" or 'e':
        break

    else:
        print("Invaild Input")
