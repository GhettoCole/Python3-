import random
import math


class Warrior:  # Create a class
    def __init__(self, name="Warrior", health=0, attkMax=0, blockMax=0):  # Initialize the class attributes
        self.name = name
        self.health = health
        self.attkMax = attkMax
        self.blockMax = blockMax

    def attack(self):  # def function 'attack'
        attkAmt = self.attkMax * (random.random() + .5)  # Set the attAmt to AttMax multiplied by
        #  a random number + a precision of .5

        return attkAmt  # Return the attkAmt

    def block(self):  # def function 'block'
        blockAmt = self.blockMax * (random.random() + 1.5)  # Set the block amount to blockAmt multiplied by
        #  a random number + a precision of .5
        # Return the blockAmt
        return blockAmt


class Battle:  # Create a class
    def startFight(self, warrior1, warrior2):  # Give the class two parameters
        while True:
            if self.getAttackResult(warrior1, warrior2) == "Game Over":
                print("Game Over")
                break

            if self.getAttackResult(warrior2, warrior1) == "Game Over":
                print("Game Over")
                break

    @staticmethod
    def getAttackResult(warriorA, warriorB):
        warriorAAttackAmt = warriorA.attack()

        warriorBBlockAmt = warriorB.block()

        damage2WarrorB = math.ceil(warriorAAttackAmt - warriorBBlockAmt)

        warriorB.health = warriorB.health - damage2WarrorB

        print("\n{} attacks {} and deals {} damage".format(warriorA.name, warriorB.name, damage2WarrorB))

        print("\n{} is down to {} health".format(warriorB.name, warriorB.health))

        if warriorB.health <= 0:
            print("\n{} has Died and {} is victorious".format(warriorB.name, warriorA.name))
            return "Game Over"
        else:
            return "Fighting Again"


def main():
    given = Warrior("GhettoCole", 50, 20, 10)
    goitse = Warrior("Goitse", 50, 20, 10)

    battle = Battle()

    battle.startFight(goitse, given)


main()
