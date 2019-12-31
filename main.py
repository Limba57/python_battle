from classes.game import Person, bColors

magic = [{"name": "fire", "cost": 10, "dmg": 60},
         {"name": "thunder", "cost": 20, "dmg": 80},
         {"name": "blizzard", "cost": 30, "dmg": 100}]

player = Person(460, 65, 60, 34, magic)
enemy = Person(1200, 65, 45, 25, magic)

running = True
i = 0

print(bColors.in_red_bold("An Enemy ATTACKS !!"))

while running:
    print("=======================")
    player.choose_action()
    choice = input("Choose action : ")
    index = int(choice) - 1

    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("You attack for", bColors.in_red_bold(dmg), "point of damage")
        print("Enemy Hp:", bColors.in_red_bold(enemy.get_hp()))

    enemy_choice = 1
    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy attack for", bColors.in_red_bold(enemy_dmg), "point of damage")
    print("Your's Hp:", bColors.in_red_bold(player.get_hp()))

    #running = False


