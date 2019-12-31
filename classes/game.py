import random


class bColors:

    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    def in_red_bold(text):
        return str(bColors.FAIL + bColors.BOLD + str(text) + bColors.ENDC)


class Person:
    def __init__(self, hp, mp, atk, df, magic):
        self.max_hp = hp
        self.hp = hp
        self.max_mp = mp
        self.mp = mp
        self.atk_l = atk - 10
        self.atk_h = atk + 10
        self.df = df
        self.magic = magic
        self.actions = ["Attack", "Magic"]

    def generate_damage(self):
        return random.randrange(self.atk_l, self.atk_h)

    def generate_spell_damage(self, i):
        mgl = self.magic[i]["dmg"] - 5
        mgh = self.magic[i]["dmg"] + 5
        return random.randrange(mgl,mgh)

    def take_damage (self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.max_hp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.max_mp

    def reduce_mp(self, cost):
        self.mp -= cost
        '''
        if self.mp < 0:
            self.mp = 0
        '''
    def get_spell_name(self, i):
        return self.magic[i]["name"]

    def get_mp_cost(self, i):
        return self.magic[i]["cost"]

    def choose_action(self):
        i = 1
        print("")
        print("**********")
        print("* Action *")
        print("**********")
        for item in self.actions:
            print(str(i) +":", item)
            i += 1

    def choose_magic(self):
        i = 1
        print("")
        print("*********")
        print("* Magic *")
        print("*********")
        for spell in self.magic:
            print(str(i)+":", spell["name"], "(cost:", str(spell["cost"]) + ")")
            i += 1