import Game, Knight, Wizard

print("Welcome to Wonderland" + '\n' + "Where Dreams and Nightmares Thrive")
playGame = input("Dare to enter? (Type yes or no) ")
if playGame == "yes":
    print('\n' + "Nightmares and Dream are thought to be the product of the mortal minds imagination" + '\n' + "However, a finite mind cannot comprehend the infinite" + '\n'+ "Dreams exsist as a gateway to another world where creatures roam and thrive" + '\n' + "There are no limits but one crucial rule: Balance, for every Nightmare there must be a Dream" + '\n' + "Something is disrupting the balance, Nightmares are plauging the Human kind"+ '\n' + "YOU ARE THE ONLY ONE WHO CAN HELP")
    name = input("What is your name (Type in your name) ")           #this code is used to get information from the user
    print('\n',"Hello great hero", name, sep=" ")         #instead of using plus and adding spacing sep helped make it concise
else:
    exit()

