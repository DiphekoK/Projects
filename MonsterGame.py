import random

class Character:
    def _init_(self,name,hp):
        self.name = name
        self.hp = hp

        def is_alive(self):
            return self.hp > 0
            def attack(self, target):
                damage = random.randint(1, 10)
                target.hp -= damage
                print(f"{self.name} attacks {target.name} for {damage} damage.")

class Monster(Character):
    pass

class Player(Character):
    pass

def main():
    player = Player("Player", 50)
    monster = Monster("Monster", 50)

    while player.is_alive() and monster.is_alive():
        print(f"{player.name}'s HP: {player.hp}")
        print(f"{monster.name}'s HP: {monster.hp}")

        player.attack(monster)
        if not monster.is_alive:
            break

        monster.attack(player)
        if not player.is_alive():
            break

        if player.is_alive():
            print("You win!")
        else:
            print("You lose!")

if __name__ == "_main_":
    main()