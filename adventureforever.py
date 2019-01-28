#sets position in farmhouse
x=0
y=0
#empties inventory
inventory=[]
class commands:
    def __init__(self, command):
        self.command = command
#a command
def win():
        print("Congratulations! You won in the simplest way possible. Try to gather every item next time!")
        input("would you like to restart? y/n: ")
        print("Doesn't matter. You're restarting anyway.")
        x=0
        y=0
#a command
def why():
        print("cause I said so.")
#a command that moves the character around, changing the look() description for the surroundings selected
def go():
        global x
        global y
        answer=input("Go which way?")
        if answer == "south" or answer == "s" or answer == "South" or answer == "S":
          if y==0:
            print("you are at the edge of the map and cannot go that way.")
          elif x==0 and y==1:
            print("You cannot enter the barn because there is no door on this side.")
          else:
            y-=1
        elif answer == "north" or answer == "n" or answer == "North" or answer == "N":
          if y==4:
            print("you are at the edge of the map and cannot go that way.")
          elif x==0 and y==0:
            print("There is no door in the north of the barn.")
          else:
            y+=1
        elif answer == "east" or answer == "e" or answer == "East" or answer == "E":
          if x==4:
            print("you are at the edge of the map and cannot go that way.")
          elif x==1 and y==3:
            print("There is a large wall of stone in your way. The treetops block your view of the top of the wall.")
          elif x==1 and y==4:
            print("There is a large wall of stone in your way. The treetops block your view of the top of the wall.")
          elif x==3 and y==3:
            print("The wall is blocking your path. Maybe you should try going through the giant cave entrance.")
          elif x==3 and y==4:
            print("The wall is blocking your path. Maybe you should try going through the giant cave entrance.")
          else:
            x+=1
        elif answer == "west" or answer == "w" or answer == "West" or answer == "W":
          if x==0:
            print("you are at the edge of the map and cannot go that way.")
          elif x==4 and y==3:
            print("There is a large wall of stone in your way. The treetops block your view of the top of the wall.")
          elif x==4 and y==4:
            print("There is a large wall of stone in your way. The treetops block your view of the top of the wall.")
          elif x==2 and y==3:
            print("The cave wall is blocking you from walking west.")
          elif x==2 and y==4:
            print("The cave wall is blocking you from walking west.")
          else:
            x-=1
        else:
          print("That's not a valid direction. Compound cardinal directions are not acceptable (NE, NW, SE, SW).")
#adds items to your inventory
def get():
        answer=input("what would you like to get?")
        if answer == "shiny" or answer == "shiny thing":
            print("Whatever put those skulls outside wasn't joking around. You don't even know what hit you.")
            die()
        elif answer == "farmer":
            if "cow" in inventory:
                print("The farmer asks for the cow that you are riding on. You agree to let him ride it if he comes with you. He looks totally badass on the back of the cow.")
                inventory.append(answer)
                print("The farmer has joined your party!")
            else:
                print("You ask the farmer for help, but he refuses. He says, and I quote,'My stupid ass legs don' work, pardner. Get me a ride and I'll join you.' You realize he is a very crude language style.")
        elif answer in inventory:
            print("You already have this item")
        elif answer in items:
          inventory.append(answer)
          print(f"You have gotten a(n) {answer}")
        else:
            print("You cannot get an item that isn't there.")
#a command
def help_me():
            print("Available non-hidden commands are inventory, get, go, why, look, and help. I cannot share hidden commands.")
def die():
        print("you have died! Congrats, your starting over.")
        x=0
        y=0
#shows inventory
def get_inventory():
          print(f"You have {inventory} in your inventory")
#leaves the barn
def leave():
        if x==0 and y==0:
          print("you have left the house. You are now at (1, 0).")
        else:
          print("there is nothing to leave.")
#a trio of fun commands. Just for fun!
def abracadabra():
        print("you have just said abracadabra very quietly to yourself. Maybe if you say it louder, It will actually do something!")
def Abracadabra():
        print("You have just spoken the word abracadabra at an audible level. Any monsters within a few feet heared you but nothing happened yet. Maybe if you yell it?")
def ABRACADABRA():
        print("You have just yelled abracadabra at the top of your lungs. Every monster in a 100 yd radius heard you and came running. What would you like to do?")
        answer=input("would you like to fight, flee, or negotiate?")
        if answer == "fight":
          print("you have attempted to fight off 100 monsters at once, instantly being surrounded and cut down.")
          input("")
          print("Why are you still trying to do things? omae wa mou shindeiru.")
          input("")
          print("just shut up and accept your death")
          input("would you like to restart? y/n: ")
          print("Doesn't matter. You quit when your finished!")
        elif answer == "flee":
          print("are you stupid? I said a radius. You were instantly surrounded and killed.")
          input("")
          print("Why are you still trying to do things? omae wa mou shindeiru.")
          input("")
          print("just shut up and accept your death")
          input("would you like to restart? y/n: ")
          print("Doesn't matter. You quit when your finished!")
        elif answer == "negotiate":
          print("You calmly speak to the monsters and they actually listen. You form a conference between the leaders of the monsters and yourself to create a permanant peace treaty. Suddenly, a radical goblin intrudes on the conference with a magic blast rune blazing on his chest. He yells 'We don't negotiate with terrorists!' The peace conference comes to an unsuccessful end. In your final moments, you relaize the goblin was referring to you as a terrorist. You die feeling confused and offended more than anything else.")
          input("")
          print("Why are you still trying to do things? omae wa mou shindeiru.")
          input("")
          print("just shut up and accept your death")
          input("would you like to restart? y/n: ")
          print("Doesn't matter. You quit when your finished!")
        else:
          print("Your inability to form a coherent thought causes you to stumble and hit your head on a rock. As the monsters arrive, they appear confused as to the source of the yell. All they see is a soiled dead body on the ground and assume a faster monster had killed you first. As you enter the afterlife, you hear someone from beyond yell 'abracadbra' and hysterical laughter ensue. You die in shame and wonder why you ever left your house.")
          input("")
          print("Why are you still trying to do things? omae wa mou shindeiru.")
          input("")
          print("just shut up and accept your death")
          input("would you like to restart? y/n: ")
          print("Doesn't matter. You quit when your finished!")
#actual game that plays through
def game():
    print(f"You are at {x}, {y}")
    answer=input("what would you like to do?")
    while items != []:
        if answer == "win":
          win()
          answer=input("What would you like to do?")
        elif answer == "why":
          why()
          answer=input("What would you like to do?")
        elif answer == "go":
          go()
          print(f"You are at {x}, {y}")
          answer=input("What would you like to do?")
        elif answer == "abracadabra":
          abracadabra()
          answer=input("What would you like to do?")
        elif answer == "Abracadabra":
          Abracadabra()
          answer=input("What would you like to do?")
        elif answer == "ABRACADABRA":
          ABRACADABRA()
          answer=input("What would you like to do?")
        elif answer == "help":
          help_me()
          answer=input("What would you like to do?")
        elif answer == "leave":
          leave()
          answer=input("What would you like to do?")
        elif answer == "look":
          look()
          answer=input("What would you like to do?")
        elif answer == "get":
          get()
          answer=input("What would you like to do?")
        elif answer == "die":
          die()
        elif answer == "inventory":
            get_inventory()
            answer=input("What would you like to do?")
        elif answer == "bye" or answer == "goodbye":
            print("What you sayun' bye for? You ain't done yet! Just for tryin' to quit, you startin' over. How bout dat?")
            game()
        else:
            answer=input("That is not a valid command. What would you like to do?")
    input("You have gotten everything in the game! Want to face the dragon?")
    if answer == "yes" or answer == "y":
        print("Too bad. You think having a boat is going to help you beat a dragon? I think not. Let's end the game here, shall we? The final command is 'goodbye'.")
        input("say goodbye")
        while answer != "goodbye":
            answer=input("The game's over. I won't let you continue the game. Say goodbye.")
        else:
            print("Yea, it's a sucky game. I did warn you. What can I say? The pay is low and the developers don't give a damn. Have a nice day!")
#displays the description for the tile
def look():
        if x==0 and y==0:
            print("you are in a house with a high roof and red walls. There appear to be lanterns and a couple of matches on a table. One wall has a dresser with a couple planks of wood and axes for chopping wood. The floor is covered in hay with a pile of hay in the corner. There is a door to leave to the east.")
        elif x==1 and y==0:
            print("You are in front of a farmhouse. There are pitchforks leaning against a fence. A meadow with cows to the north. You see a farmer sitting in front of a chicken coop to the east. He is holding what appears to be a shiny wooden stick, but you cannot tell what it is from here.")
        elif x==2 and y==0:
            print("As you go closer to the farmer, you realize he is holding a rifle. He looks up and asks you,'Whatchu want pardner?' Directly behind him is the door to the chicken coop. To the west is a farmhouse and to the north is a forest. To the east is a large cave. The soil here looks very nutritious.")
        elif x==3 and y==0:
            print("You are at the entrance of the cave 20 ft high. Red mushrooms grow around the entrance of the cave. to the north is a forest. What first appeared to be rocks on the ground are actually discarded bones. You hear a foreboding silence coming from the cave to the east. It seems dangerous to enter.")
        elif x==4 and y==0:
          print("You have entered the cave. It is very dark. You see something shiny in the corner but cannot tell what it is. There are exits to the west and north.")
        elif x==0 and y==1:
          print("You are in a valley with a river running through it. It curves off to the west and is to wide to cross. You see a few fish in the water. There is a very large smooth stone in the water. You see a farmhouse to the south, but you do not see a door. To the east is a meadow full of cows. To the north is upriver. It appears to get stronger from the north.")
        elif x==1 and y==1:
          print("You are in a meadow with a lot of cows, but there do not appear o be any bulls. There is a lot of manure here. To the south is the center of a farm. To the east is a forest. To the north is also forest. To the west is a valley.")
        elif x==2 and y==1:
          print("You have entered the forest. The branches are just out of reach. You cannot tell what is beyond the forest through the trees. You see a very strange looking tree to the east.")
        elif x==3 and y==1:
          print("You are in the forest. What appeared to be a weird tree turned out to be a witch house. No one appears to be home but you see steam coming out of the window. The door is closed. You cannot see beyond the forest because of the trees.")
        elif x==4 and y==1:
          print("You have found mirrormere. There is an abandoned boat on the shore. Across Mirrormere to the south is a crack in the wall of a cave. It looks like you can squeeze through if you do not carry anything. To the west is a forest. To the north is an ancient forest with trees hundreds of furlongs tall.")
        elif x==0 and y==2:
          print("You are upstream of the river's end. The river is to wide to cross. There is an abandoned fishing line with a hook still attached tied to a rock. to the south is downriver. To the north is upriver. To the east is an ancient forest.")
        elif x==1 and y==2:
          print("You are in an ancient forest. The trees are too tall to climb without proper equipment. However, you see an ancient network of treehouses hundreds of feet up. The forest continues to the north and east. You cannot see out of the forest.")
        elif x==2 and y==2:
          print("You are in an ancient forest. The trees are too tall to climb without proper equipment. However, you see an ancient network of treehouses hundreds of feet up. The forest continues to the west and east. To the north, an ominous darkness looms. You cannot see out of the forest.")
        elif x==3 and y==2:
          print("You are in an ancient forest. The trees are too tall to climb without proper equipment. However, you see an ancient network of treehouses hundreds of feet up. The forest continues to the west and east. To the north, an ominous darkness looms. You cannot see out of the forest.")
        elif x==4 and y==2:
          print("You are in an ancient forest. The trees are too tall to climb without proper equipment. However, you see an ancient network of treehouses hundreds of feet up. The forest continues to the north and west. You cannot see out of the forest.")
        elif x==0 and y==3:
          print("You are nearing a waterfall to the north. There are many rocks in the water and the water is moving quickly. There is a large rock standing in and above the water, steady in the middle. You cannot see the top. To the south is downriver. To the east is an ancient forest.")
        elif x==1 and y==3:
          print("You are in an ancient forest. The trees are too tall to climb without proper equipment. However, you see an ancient network of treehouses hundreds of feet up. There is an ominous darkness to the east. The forest continues north and south. You cannot see out of the forest.")
        elif x==2 and y==3:
          print("You have entered a large cave. A hole in the ceiling 1,000 ft up allows light to fill the cave for the most part. The hole is hundreds of feet wide. The cave is 1000's of times wider than the hole. You see valuables of all shapes and sizes everywhere. The pile nearly reaches the ceiling further back in the cave. It is incredibly warm.")
        elif x==3 and y==3:
          print("You have entered a large cave. A hole in the ceiling 1,000 ft up allows light to fill the cave for the most part. The hole is hundreds of feet wide. The cave is 1000's of times wider than the hole. You see valuables of all shapes and sizes everywhere. The pile nearly reaches the ceiling further back in the cave. It is incredibly warm.")
        elif x==4 and y==3:
          print("You are in an ancient forest. The trees are too tall to climb without proper equipment. However, you see an ancient network of treehouses hundreds of feet up. A tree has the word 'abracadabra' carved into it. There is an ominous darkness to the west. The forest continues north and south. You cannot see out of the forest.")
        elif x==0 and y==4:
          print("You are at a waterfall. There is a lot of mist shrouding the base of the waterfall. A rock appears to be underneath it. There is a large, turbulent river here. To the south is downriver. To the east is an ancient forest.")
        elif x==1 and y==4:
          print("You are in an ancient forest. The trees are too tall to climb without proper equipment. However, you see an ancient network of treehouses hundreds of feet up. There appears to be a stronghold above you. There is an ominous darkness to the east. The forest continues south. You cannot see out of the forest.")
        elif x==2 and y==4:
          print("As you near the pile of valuables, a dragon rises up from the depths of the pile. You drop to the floor, hoping that he does not see you.")
        elif x==3 and y==4:
          print("As you near the pile of valuables, a dragon rises up from the depths of the pile. You drop to the floor, hoping that he does not see you.")
        elif x==4 and y==4:
          print("You are in an ancient forest. The trees are too tall to climb without proper equipment. However, you see an ancient network of treehouses hundreds of feet up. There is a particularly large tree with a check engraved on it. There is an ominous darkness to the west. The forest continues south. You cannot see out of the forest.")
#introduction
items=["lantern", "matches", "axe", "plank", "hay", "pitchfork", "soil", "rifle", "farmer", "mushrooms", "bones", "fish", "stone", "cow", "manure", "boat", "line", "hook"]
print("Welcome to the world of Adventure Forever! By travelling through this world, you will gather items and encounter (2 unbeatable) monsters and will win eventually! Be smart and you will win. Be stupid and you will most likely die. Don't be stupid! Just a heads up, yhis game is pretty boring. Blame the developers.")
print("you type in commands like 'why', 'get', 'go' and 'look' to do things in the game. Some other commands work as well, but you must find them out. Be creative! Gather all the items! The monsters won't go anywhere, so you're best bet is to avoid them. If you have any questions, use command 'help' during the game.")
playing=input("Would you like to play? y/n: ")
if playing is "n":
  print("so sad, too bad, you're playing anyway.")
elif playing is "y":
  print("Glad to have you along willingly on this never ending adventure!")
else:
  print("Its not like it mattered what you answered. You're playing anyway.")
#runs game
game()