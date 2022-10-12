import random
import Knight
import Wizard  

class KnightRole:
    def role(self):
        print("YOUR A KNIGHT")
        Kstrength = Knight.Kstrength
        KIntelligeence = Knight.KIntelligeence
        KExperience = Knight.KExperience
        print("Your strength is", Kstrength, "Your Intelligeence is", KIntelligeence, "Your Experience is", KExperience)


class WizardRole:
    def role(self):
        print("YOUR A WIZARD HARRY")
        Wstrength =  Wizard.Wstrength
        WIntelligeence = Wizard.WIntelligeence
        WExperience = Wizard.WExperience
        print("Your strength is", Wstrength, "Your Intelligeence is",WIntelligeence , "Your Experience is", WExperience)


class Kchallenges:
    def Challenge1(self,):
        YesOrNo = input("Ready for challenge 1")
        if YesOrNo== "":
            print("Challenge 1:" + '\n' + "on your way to defeat the dragon, you get attacked by Direwolf" + '\n' + "This challenge will rely on your strength and how strong0 your attacks are" + '\n\n' + "To attack you must roll the die of faith, you will get three rolls." + '\n' + "The sum of all of those rolls plus your strength will determine if you have won the challege")
            YN=input('\n',"Roll the die of faith (Press enter)")
            if YN == "":
                die1 = random.randint(1,6)
                die2 = random.randint(1,6)
                die3 = random.randint(1,6)
                total= (die1 + die2 + die3 + Wizard.Wstrength)
                print("Roll 1:", die1,"Roll 2:", die2, "Roll 3:",die3,'\n\n',"Total score:",total)
                if total == (1,5)
                    print("Critcal loss: GAME OVER")
                    exit()
                if total == (6,15)
                    print("YOU PASSED")
                if total == (16,20)
                    print("YOU PASSED WITH FLYING COLOURS!")

    def Challenge2(self):
        bleh
    def Challenge3(self):
        bleh
