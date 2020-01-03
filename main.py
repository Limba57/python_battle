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
    elif index ==1:
        player.choose_magic()
        magic_choice = int(input("Choose magic : ")) - 1
        magic_damage = player.generate_spell_damage(magic_choice)
        spell = player.get_spell_name(magic_choice)
        cost = player.get_mp_cost(magic_choice)

        current_mp = player.get_mp()
        if cost > current_mp:
            print(bColors.in_red_bold("\nNot enought MP"))
            continue

        player.reduce_mp(cost)
        enemy.take_damage(magic_damage)
        print(bColors.in_blue("\n" + spell + " deals " + str(magic_damage) + " point of damage"))

    enemy_choice = 1
    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy attack for", bColors.in_red_bold(enemy_dmg), "point of damage")

    print("=======================")
    print("Enemy HP:", bColors.in_red_bold(enemy.get_hp()), "/" + bColors.in_red_bold(enemy.get_max_hp()))
    print("\nPlayer HP:", bColors.in_red_bold(player.get_hp()), "/" + bColors.in_red_bold(player.get_max_hp()))
    print("Player MP:", bColors.in_blue(player.get_mp()), "/" + bColors.in_blue(player.get_max_mp()))

    if enemy.get_hp() == 0:
        print("\n")
        print(bColors.in_green("*********"))
        print(bColors.in_green("*You win*"))
        print(bColors.in_green("*********"))
        running = False
    elif player.get_hp() == 0:
        print("\n")
        print(bColors.in_red_bold("*************"))
        print(bColors.in_red_bold("*You LOSE !!*"))
        print(bColors.in_red_bold("*************"))
        running = False


