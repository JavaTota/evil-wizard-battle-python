import random


class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health

    def attack(self, opponent):
        damage = random.randint(self.attack_power - 5, self.attack_power + 5)
        opponent.health -= damage
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")

    def heal(self):
        heal_amount = random.randint(10, 20)
        self.health = min(self.health + heal_amount, self.max_health)
        print(f"{self.name} heals for {heal_amount}. Current health: {self.health}")

    def display_stats(self):
        print(f"{self.name} - HP: {self.health}/{self.max_health}")


class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, 140, 25)

    def ability(self, opponent):
        damage = self.attack_power * 2
        opponent.health -= damage
        print(f"{self.name} uses Power Strike for {damage} damage!")


class Mage(Character):
    def __init__(self, name):
        super().__init__(name, 100, 35)

    def ability(self, opponent):
        damage = random.randint(30, 60)
        opponent.health -= damage
        print(f"{self.name} casts Fireball for {damage} damage!")


class Archer(Character):
    def __init__(self, name):
        super().__init__(name, 110, 30)
        self.evade_next = False

    def ability(self, opponent):
        print(f"{self.name} uses Quick Shot!")
        for _ in range(2):
            self.attack(opponent)

    def evade(self):
        self.evade_next = True
        print(f"{self.name} will evade the next attack!")


class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, 130, 20)
        self.shield = False

    def ability(self, opponent):
        damage = self.attack_power + 20
        opponent.health -= damage
        print(f"{self.name} uses Holy Strike for {damage} damage!")

    def divine_shield(self):
        self.shield = True
        print(f"{self.name} activates Divine Shield!")


class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, 150, 15)

    def regenerate(self):
        self.health = min(self.health + 5, self.max_health)
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")


def create_character():
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer")
    print("4. Paladin")

    choice = input("Choose class: ")
    name = input("Enter name: ")

    if choice == "1":
        return Warrior(name)
    elif choice == "2":
        return Mage(name)
    elif choice == "3":
        return Archer(name)
    elif choice == "4":
        return Paladin(name)
    else:
        return Warrior(name)


def battle(player, wizard):
    while player.health > 0 and wizard.health > 0:
        print("\n1. Attack\n2. Ability\n3. Heal\n4. Stats")
        choice = input("Action: ")

        if choice == "1":
            player.attack(wizard)

        elif choice == "2":
            if isinstance(player, Archer):
                print("1. Quick Shot\n2. Evade")
                sub = input("Choose: ")
                if sub == "1":
                    player.ability(wizard)
                elif sub == "2":
                    player.evade()

            elif isinstance(player, Paladin):
                print("1. Holy Strike\n2. Divine Shield")
                sub = input("Choose: ")
                if sub == "1":
                    player.ability(wizard)
                elif sub == "2":
                    player.divine_shield()

            else:
                player.ability(wizard)

        elif choice == "3":
            player.heal()

        elif choice == "4":
            player.display_stats()

        else:
            print("Invalid choice")

        if wizard.health > 0:
            print("\n--- Wizard Turn ---")

            if isinstance(player, Archer) and player.evade_next:
                print(f"{player.name} evaded the attack!")
                player.evade_next = False
            elif isinstance(player, Paladin) and player.shield:
                print(f"{player.name}'s shield blocked the attack!")
                player.shield = False
            else:
                wizard.attack(player)

            wizard.regenerate()

    if player.health > 0:
        print(f"\n{player.name} defeated the Evil Wizard!")
    else:
        print(f"\n{player.name} was defeated...")


def main():
    player = create_character()
    wizard = EvilWizard("Dark Wizard")
    battle(player, wizard)


if __name__ == "__main__":
    main()