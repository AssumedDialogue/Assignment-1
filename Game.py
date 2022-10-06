import random
from Knight import *
from Wizard import *
class DiceOfFaith:
    def show(self):
        die1= random.randint(1,6)


class KnightRole:
    def role(self):
        print("YOUR A KNIGHT")
        print("Your strength is", Kstrength, "Your Intelligeence is", KIntelligeence, "Your Experience is", KExperience)

class WizardRole:
    def role(self):
        print("YOUR A WIZARD HARRY")
        print("Your strength is", strength, "Your Intelligeence is", Intelligeence, "Your Experience is", Experience)