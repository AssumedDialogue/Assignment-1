import random
import Knight
import Wizard
import App

class DiceOfFaith:
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        die3 = random.randint(1,6)


class KnightRole:
    def role(self):
        print("YOUR A KNIGHT")
        print("Your strength is", Knight.Kstrength, "Your Intelligeence is", Knight.KIntelligeence, "Your Experience is", Knight.KExperience)
        strength = Knight.Kstrength
        Intelligeence = Knight.KIntelligeence
        Experience = Knight.KExperience

        

class WizardRole:
    def role(self):
        print("YOUR A WIZARD HARRY")
        print("Your strength is", Wizard.Wstrength, "Your Intelligeence is", Wizard.WIntelligeence, "Your Experience is", Wizard.WExperience)
    

class challenges:
    def Challenge1(self,):
        print("Challenge 1:" + '\n' + "on your way to defeat the dragon, you get attacked by Direwolf" + '\n' + "This challenge will rely on your strength and how strong your attacks are" + '\n\n' + "To attack you must roll the die of faith, you will get three rolls." + '\n' + "The sum of all of those rolls plus your strength will determine if you have won the challege")
        YesOrNo1 = input('\n' +"ARE YOU READYYY (typr yes ot continue type no to quit game)")
        if YesOrNo1 == "yes":
            YN=input("Roll the die of faith (press enter)")
            if YN == "":
                num = DiceOfFaith()
                num.show()
                total1 = (DiceOfFaith.die1 + DiceOfFaith.die2 + DiceOfFaith.die3 + RoleFinalAtributes.Experience)
                print()
    def Challenge2(self):
        bleh
    def Challenge3(self):
        bleh
