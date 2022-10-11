import random
import Knight
import Wizard

class DiceOfFaith:
    def show(self):
        die1= random.randint(1,6)
        print(die1)


class KnightRole:
    def role(self):
        print("YOUR A KNIGHT")
        print("Your strength is", Knight.Kstrength, "Your Intelligeence is", Knight.KIntelligeence, "Your Experience is", Knight.KExperience)

class WizardRole:
    def role(self):
        print("YOUR A WIZARD HARRY")
        print("Your strength is", Wizard.strength, "Your Intelligeence is", Wizard.Intelligeence, "Your Experience is", Wizard.Experience)

class challenges:
    def Challenge1(self):
        print("Challenge 1:" + '\n' + "on your way to defeat the dragon, you get attacked by Direwolf" + '\n' + "This challenge will rely on your strength and how strong your attacks are" + '\n\n' + "To attack you must roll the die of faith, you will get three rolls." + '\n' + "The sum of all of those rolls plus your strength will determine if you have won the challege")
        YesOrNo1 = input('\n' +"ARE YOU READYYY (typr yes ot continue type no to quit game)")
        if YesOrNo1 == "yes":
            print("Roll the die of faith")
    def Challenge2(self):
        bleh
    def Challenge3(self):
        bleh
