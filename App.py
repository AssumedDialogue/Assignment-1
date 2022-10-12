import Game

print("Welcome to Wonderland" + '\n' + "Where Dreams and Nightmares Thrive")
playGame = input("Dare to enter? (Type yes or no) ")
if playGame == "yes":
    print('\n' + "Nightmares and Dream are thought to be the product of the mortal minds imagination" + '\n' + "However, a finite mind cannot comprehend the infinite" + '\n'+ "Dreams exsist as a gateway to another world where creatures roam and thrive" + '\n' + "There are no limits but one crucial rule: Balance, for every Nightmare there must be a Dream" + '\n' + "Something is disrupting the balance, Nightmares are plauging the Human kind"+ '\n' + "YOU ARE THE ONLY ONE WHO CAN HELP")
    
    name = input("What is your name (Type in your name) ")           #this code is used to get information from the user
    print('\n',"Hello great hero", name)         #instead of using plus and adding spacing sep helped make it concise

    Role = input("Choose your Charater" + '\n\n' + "1.Knight 2.Wizard") 
    
    if Role == "1":
        Rolemsg = Game.KnightRole()
        Rolemsg.role()
        chall = Game.Kchallenges()
        chall.Challenge1()
    if Role == "2":
        Rolestart = Game.WizardRole()
        Rolestart.role()
        chall = Game.challenges()
        chall.Challenge1
    else:
        exit()

