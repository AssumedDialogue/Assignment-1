###############
#Name of programmer: Areeba Minhaj
#Date: october 2022
#Programming principles
#program:adventure game
#Game: has all the logic and brains and execution code
##############
import random
import Knight
import Wizard  

class KnightRole:
    def role(self):
        print("YOUR A KNIGHT")
        print("Your strength is:", Knight.Kstrength,'\n',"Your Intelligeence is", Knight.KIntelligeence, '\n',"Your Experience is", Knight.KExperience) #these are reference codes to get the variables from other files


class WizardRole:
    def role(self):
        print("YOUR A WIZARD")
        print("Your strength is", Wizard.Wstrength,'\n',"Your Intelligeence is",Wizard.WIntelligeence,'\n',"Your Experience is", Wizard.WExperience) #these are reference codes to get the variables from other files


class Kchallenges: #the knights challenges
    def Challenge1(self,): #challenge 1 fight with direwolf relies on strength
        YesOrNo = input("Ready for challenge 1 (Press enter)") #just as an click next needed to use a variable tho
        if YesOrNo== "":
            YN=input("Challenge 1:"+'\n'+"On your way to defeat the dragon, you get attacked by Direwolf!!"+'\n'+"This challenge will rely on your strength and how strong your attacks are"+'\n\n'+"To attack you must roll the die of faith, you will get three rolls."+'\n'+"The sum of all of those rolls plus your strength will determine if you have won the challenge"+'\n'+"Roll the die of faith (Press enter)")
            if YN == "": #just as an click next needed to use a variable tho
                die1 = random.randint(1,6) #three different dices
                die2 = random.randint(1,6)
                die3 = random.randint(1,6)
                total= (die1 + die2 + die3 + Knight.Kstrength) # adding up all the points
                if (total <= 5) and (total >= 1) :
                    print("Roll 1:", die1,'\n',"Roll 2:", die2,'\n',"Roll 3:",die3,'\n\n',"Total score:",total)
                    print("Critcal loss: GAME OVER")
                    exit()
                if (total <= 15) and (total >= 6):
                    print("Roll 1:", die1,'\n',"Roll 2:", die2,'\n',"Roll 3:",die3,'\n\n',"Total score:",total)
                    print("You have passed")
                if (total <= 26) and (total >= 20):
                    print("YOU PASSED WITH FLYING COLOURS!")
    def Challenge2(self,):
        YesOrNo = input("Ready for challenge 2 (Press enter)")
        if YesOrNo== "":
            YN1=input("Challenge 2:"+'\n'+"After your encounter with the Direwolf, you get attacked by A Shapeshifter"+'\n'+"This challenge will rely on your Intelligence and how strong your attacks are"+'\n\n'+"To attack you must roll the die of faith, you will get three rolls."+'\n'+"The sum of all of those rolls plus your Intelligence will determine if you have won the challenge"+'\n'+"Roll the die of faith (Press enter)")
            if YN1 == "":
                die21 = random.randint(1,6)
                die22 = random.randint(1,6)
                die23 = random.randint(1,6)
                total2= (die21 + die22 + die23 + Knight.KIntelligeence)
                if (total2 <= 5) and (total2 >= 1) :
                    print("Roll 1:", die21,'\n',"Roll 2:", die22,'\n',"Roll 3:",die23,'\n\n',"Total score:",total2)
                    print("Critcal loss: GAME OVER")
                    exit()
                if (total2 <= 15) and (total2 >= 6):
                    print("Roll 1:", die21,'\n',"Roll 2:", die22,'\n',"Roll 3:",die23,'\n\n',"Total score:",total2)
                    print("You have passed")
                if (total2 <= 26) and (total2 >= 20):
                    print("YOU PASSED WITH FLYING COLOURS!")
    def Challenge3(self,):
        YesOrNo = input("Ready for challenge 3 (Press enter)")
        if YesOrNo== "":
            YN1=input("Challenge 3:"+'\n'+"After your encounter with the Direwolf, you arrived at the dragons cave"+'\n'+"The dragon realizes your in its territory and is about to attack you!!!"+"To complete the final challenge your Experience and your attacks are your last hope!!"+'\n\n'+"To attack you must roll the die of faith, you will get three rolls."+'\n'+"The sum of all of those rolls plus your Experience will determine if you have won the game"+'\n'+"Roll the die of faith (Press enter)")
            if YN1 == "":
                die31 = random.randint(1,6)
                die32 = random.randint(1,6)
                die33 = random.randint(1,6)
                total3= (die31 + die32 + die33 + Knight.KExperience)
                if (total3 <= 5) and (total3 >= 1) :
                    print("Roll 1:", die31,'\n',"Roll 2:", die32,'\n',"Roll 3:",die33,'\n\n',"Total score:",total3)
                    print("Critcal loss: GAME OVER")
                    exit()
                if (total3 <= 15) and (total3 >= 6):
                    print("Roll 1:", die31,'\n',"Roll 2:", die32,'\n',"Roll 3:",die33,'\n\n',"Total score:",total3)
                    print("You have completed the game!!!",'\n',"Thank you for your service great hero!")
                if (total3 <= 26) and (total3 >= 20):
                    print("YOU WON WITH FLYING COLOURS!",'\n',"Thank you for your service great hero!")

class Wchallenges: #challenges for the wizard
    def Challenge1(self,):
        YesOrNo = input("Ready for challenge 1 (Press enter)")
        if YesOrNo== "":
            YN=input("Challenge 1:"+'\n'+"on your way to defeat the dragon, you get attacked by Direwolf"+'\n'+"This challenge will rely on your strength and how strong your attacks are"+'\n\n'+"To attack you must roll the die of faith, you will get three rolls."+'\n'+"The sum of all of those rolls plus your strength will determine if you have won the challenge"+'\n'+"Roll the die of faith (Press enter)")
            if YN == "":
                die1 = random.randint(1,6)
                die2 = random.randint(1,6)
                die3 = random.randint(1,6)
                total= (die1 + die2 + die3 + Wizard.Wstrength)
                if (total <= 5) and (total >= 1) :
                    print("Roll 1:", die1,'\n',"Roll 2:", die2,'\n',"Roll 3:",die3,'\n\n',"Total score:",total)
                    print("Critcal loss: GAME OVER")
                    exit()
                if (total <= 15) and (total >= 6):
                    print("Roll 1:", die1,'\n',"Roll 2:", die2,'\n',"Roll 3:",die3,'\n\n',"Total score:",total)
                    print("You have passed")
                if (total <= 26) and (total >= 20):
                    print("YOU PASSED WITH FLYING COLOURS!")
    def Challenge2(self,):
        YesOrNo = input("Ready for challenge 2 (Press enter)")
        if YesOrNo== "":
            YN1=input("Challenge 2:"+'\n'+"After your encounter with the Direwolf, you get attacked by A Shapeshifter"+'\n'+"This challenge will rely on your Intelligence and how strong your attacks are"+'\n\n'+"To attack you must roll the die of faith, you will get three rolls."+'\n'+"The sum of all of those rolls plus your Intelligence will determine if you have won the challenge"+'\n'+"Roll the die of faith (Press enter)")
            if YN1 == "":
                die21 = random.randint(1,6)
                die22 = random.randint(1,6)
                die23 = random.randint(1,6)
                total2= (die21 + die22 + die23 + Wizard.WIntelligeence)
                if (total2 <= 5) and (total2 >= 1) :
                    print("Roll 1:", die21,'\n',"Roll 2:", die22,'\n',"Roll 3:",die23,'\n\n',"Total score:",total2)
                    print("Critcal loss: GAME OVER")
                    exit()
                if (total2 <= 15) and (total2 >= 6):
                    print("Roll 1:", die21,'\n',"Roll 2:", die22,'\n',"Roll 3:",die23,'\n\n',"Total score:",total2)
                    print("You have passed")
                if (total2 <= 26) and (total2 >= 20):
                    print("YOU PASSED WITH FLYING COLOURS!")
    def Challenge3(self,):
        YesOrNo = input("Ready for challenge 3 (Press enter)")
        if YesOrNo== "":
            YN1=input("Challenge 3:"+'\n'+"After your encounter with the Direwolf, you arrived at the dragons cave"+'\n'+"The dragon realizes your in its territory and is about to attack you!!!"+"To complete the final challenge your Experience and your attacks are your last hope!!"+'\n\n'+"To attack you must roll the die of faith, you will get three rolls."+'\n'+"The sum of all of those rolls plus your Experience will determine if you have won the game"+'\n'+"Roll the die of faith (Press enter)")
            if YN1 == "":
                die31 = random.randint(1,6)
                die32 = random.randint(1,6)
                die33 = random.randint(1,6)
                total3= (die31 + die32 + die33 + Wizard.WExperience)
                if (total3 <= 5) and (total3 >= 1) :
                    print("Roll 1:", die31,'\n',"Roll 2:", die32,'\n',"Roll 3:",die33,'\n\n',"Total score:",total3)
                    print("Critcal loss: GAME OVER")
                    exit()
                if (total3 <= 15) and (total3 >= 6):
                    print("Roll 1:", die31,'\n',"Roll 2:", die32,'\n',"Roll 3:",die33,'\n\n',"Total score:",total3)
                    print("You have completed the game!!!",'\n',"Thank you for your service great hero!")
                if (total3 <= 26) and (total3 >= 20):
                    print("YOU WON WITH FLYING COLOURS!",'\n',"Thank you for your service great hero!")

