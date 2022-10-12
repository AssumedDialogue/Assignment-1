###############
#Name of programmer: Areeba Minhaj
#Date: october 2022
#Programming principles
#program:adventure game
#app: handles the calls and interacts with the user
##############
import Game

print("Welcome to Wonderland" + '\n' + "Where Dreams and Nightmares Thrive")
playGame = input("Dare to enter? (Type yes or no) ")
if playGame == "yes": #this variable helps us know if the user wants to play or not
    print('\n' + "Nightmares and Dream are thought to be the product of imagination" + '\n' + "in reality however,dreams exsist as a gateway to another world where creatures roam and thrive" + '\n' + "There are no limits but one crucial rule: Balance, for every Nightmare there must be a Dream" + '\n' + "A dragon is disrupting the balance, Nightmares are plauging the Wonderland"+ '\n' + "YOU ARE THE ONLY ONE WHO CAN HELP")
    
    name = input("What is your name (Type in your name) ")           #this code is used to get information from the user
    print('\n',"Hello great hero", name, sep=" ")         #instead of using plus and adding spacing sep helped make it concise

    Role = input("Choose your Charater" + '\n\n' + "1.Knight 2.Wizard (Type 1 for Knight, Type 2 for Wizard)")  #this variable helped users choose which role and helps the code discern between the two
    
    if Role == "1":
        Rolemsg = Game.KnightRole() #calling class from file
        Rolemsg.role() #calling methods
        chall = Game.Kchallenges() #calling class from file
        chall.Challenge1() #calling methods
        chall.Challenge2() #calling methods
        chall.Challenge3()#calling methods

    if Role == "2":
        Rolestart = Game.WizardRole() #calling class from file
        Rolestart.role()
        chall = Game.Wchallenges() #calling class from file
        chall.Challenge1() #calling methods
        chall.Challenge2() #calling methods
        chall.Challenge3() #calling methods
    else:
        exit()

