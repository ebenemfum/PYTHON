##Conditional Operators
##Do not forget to typecast user input!!!!
#if (condition):
#execute
#else:
#execute
# print("Welcome to the rollercoaster")
# height = int(input("what is your height in cm? "))
# if height >= 120:
#     print(" You can ride the rollercoaster")
# else:
#     print("Sorry you have to grow taller before you can ride. ")


# Modulo 
# print("Welcome to the even number checker")
# num = int(input("what number do you want to check? "))
# if(num%2==0):
#     print(f"The number {num} is an even number")
# else:
#     print(f"The number {num} is an odd number")


##Nested if and Elif Statement

#if (condition):

    #if (another condition):
    
        #do this:
        
    #else:
    
    #do this
    
#else:
    #do this:  

##Elif
#if condition1:
    #do A
#elif condition2:
    #do B
#elif condition3:
    #do C
#elif condition4:
    #do D
#else:
#do this:
# print("Welcome to the rollercoaster")
# height = int(input("What is your height in cm? "))
# bill=0

# if (height >= 120):
#     print("You can ride the rollercoaster.")
#     age = int(input("What is your age? "))
    
#     if age < 12:
#         bill=5
#         print("You have to pay $5.")
#     elif age <= 18:
#         bill=7
#         print("You have to pay $7.")
#     else:
#         bill=12
#         print("You have to pay $12.")
#     photo=input("Do you want a photo taken? Type Y for Yes and N for No. ").upper()
#     if(photo == "Y"):
#         bill +=3
#     print(f"Your final bill is ${bill}")
# else:
#     print("Sorry, you have to grow taller before you can ride.")

# Logical Operators
# and 
# or 
# not
# 


# print("Welcome to the Python Pizza Deliveries")
# size = input("What size do you want? S, M or L: ").upper()
# pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").upper()
# extra_cheese = input ( "Do you want extra cheese? Y or N").upper()
# bill=0

# ## todo: work out how much they need pay based on their size choice.
# if(size=="S"):
#     bill += 15
    
# elif(size=="M"):
#     bill += 20

# elif(size=="L"):
#     bill += 25
# else:
#     print("Check your input!")
    
# ## todo: work out how much to add to their bill based on their pepperoni choice.
# if(size =="S" and pepperoni=="Y"):
#     bill += 2
# elif((size =="M" or size =="L") and pepperoni=="Y"):
#     bill += 3

# if(extra_cheese=="Y"):
#     bill += 1


# ## todo: workout their final amount based on whether if they want extra cheese.
# print(f"Your total bill is ${bill} because size = {size} pepperoni = {pepperoni} and extra cheese = {extra_cheese} ")



##TREASURE ISLAND GAME
print('''88888888888888888888888888888888888888888888888888888888888888888888888
88.._|      | `-.  | `.  -_-_ _-_  _-  _- -_ -  .'|   |.'|     |  _..88
88   `-.._  |    |`!  |`.  -_ -__ -_ _- _-_-  .'  |.;'   |   _.!-'|  88
88      | `-!._  |  `;!  ;. _______________ ,'| .-' |   _!.i'     |  88
88..__  |     |`-!._ | `.| |_______________||."'|  _!.;'   |     _|..88
88   |``"..__ |    |`";.| i|_|MMMMMMMMMMM|_|'| _!-|   |   _|..-|'    88
88   |      |``--..|_ | `;!|l|MMoMMMMoMMM|1|.'j   |_..!-'|     |     88
88   |      |    |   |`-,!_|_|MMMMP'YMMMM|_||.!-;'  |    |     |     88
88___|______|____!.,.!,.!,!|d|MMMo * loMM|p|,!,.!.,.!..__|_____|_____88
88      |     |    |  |  | |_|MMMMb,dMMMM|_|| |   |   |    |      |  88
88      |     |    |..!-;'i|r|MPYMoMMMMoM|r| |`-..|   |    |      |  88
88      |    _!.-j'  | _!,"|_|M<>MMMMoMMM|_||!._|  `i-!.._ |      |  88
88     _!.-'|    | _."|  !;|1|MbdMMoMMMMM|l|`.| `-._|    |``-.._  |  88
88..-i'     |  _.''|  !-| !|_|MMMoMMMMoMM|_|.|`-. | ``._ |     |``"..88
88   |      |.|    |.|  !| |u|MoMMMMoMMMM|n||`. |`!   | `".    |     88
88   |  _.-'  |  .'  |.' |/|_|MMMMoMMMMoM|_|! |`!  `,.|    |-._|     88
88  _!"'|     !.'|  .'| .'|[@]MMMMMMMMMMM[@] \|  `. | `._  |   `-._  88
88-'    |   .'   |.|  |/| /                 \|`.  |`!    |.|      |`-88
88      |_.'|   .' | .' |/                   \  \ |  `.  | `._    |  88
88     .'   | .'   |/|  /                     \ |`!   |`.|    `.  |  88
88  _.'     !'|   .' | /                       \|  `  |  `.    |`.|  88

Welcome to Treasure Island 
Your mission is to find the treasure.
''')

choice1=input("Left or Right? ").upper()


if(choice1=="LEFT"):
    
    
    choice2=input("Swim or Wait? ").upper()
    
    
    if(choice2=="WAIT"):
        
        
        choice3=input("Which door ? Red or Blue or Yellow ").upper()
        
        
        if(choice3=="YELLOW"):
            
            print('''

   ||====================================================================||
   ||//$\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\//$\\||
   ||(100)==================| FEDERAL RESERVE NOTE |================(100)||
   ||\\$//        ~         '------========--------'                \\$//||
   ||<< /        /$\              // ____ \\                         \ >>||
   ||>>|  12    //L\\            // ///..) \\         L38036133B   12 |<<||
   ||<<|        \\ //           || <||  >\  ||                        |>>||
   ||>>|         \$/            ||  $$ --/  ||        One Hundred     |<<||
||====================================================================||>||
||//$\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\//$\\||<||
||(100)==================| FEDERAL RESERVE NOTE |================(100)||>||
||\\$//        ~         '------========--------'                \\$//||\||
||<< /        /$\              // ____ \\                         \ >>||)||
||>>|  12    //L\\            // ///..) \\         L38036133B   12 |<<||/||
||<<|        \\ //           || <||  >\  ||                        |>>||=||
||>>|         \$/            ||  $$ --/  ||        One Hundred     |<<||
||<<|      L38036133B        *\\  |\_/  //* series                 |>>||
||>>|  12                     *\\/___\_//*   1989                  |<<||
||<<\      Treasurer     ______/Franklin\________     Secretary 12 />>||
||//$\                 ~|UNITED STATES OF AMERICA|~               /$\\||
||(100)===================  ONE HUNDRED DOLLARS =================(100)||
||\\$//\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\$//||
||====================================================================||
You Won!!!!!!! Congratulations!!!!!
''')
        elif(choice3=="RED"):
            print('''
         88                               88           
         88                         ,d    88           
         88                         88    88           
 ,adPPYb,88  ,adPPYba, ,adPPYYba, MM88MMM 88,dPPYba,   
a8"    `Y88 a8P_____88 ""     `Y8   88    88P'    "8a  
8b       88 8PP""""""" ,adPPPPP88   88    88       88  
"8a,   ,d88 "8b,   ,aa 88,    ,88   88,   88       88  
 `"8bbdP"Y8  `"Ybbd8"' `"8bbdP"Y8   "Y888 88       88
 Game Over!
 ''')
        elif(choice3=="BLUE"):
            print('''
         88                               88           
         88                         ,d    88           
         88                         88    88           
 ,adPPYb,88  ,adPPYba, ,adPPYYba, MM88MMM 88,dPPYba,   
a8"    `Y88 a8P_____88 ""     `Y8   88    88P'    "8a  
8b       88 8PP""""""" ,adPPPPP88   88    88       88  
"8a,   ,d88 "8b,   ,aa 88,    ,88   88,   88       88  
 `"8bbdP"Y8  `"Ybbd8"' `"8bbdP"Y8   "Y888 88       88
 Game Over
 ''')
            
            
    else:
        print('''
         88                               88           
         88                         ,d    88           
         88                         88    88           
 ,adPPYb,88  ,adPPYba, ,adPPYYba, MM88MMM 88,dPPYba,   
a8"    `Y88 a8P_____88 ""     `Y8   88    88P'    "8a  
8b       88 8PP""""""" ,adPPPPP88   88    88       88  
"8a,   ,d88 "8b,   ,aa 88,    ,88   88,   88       88  
 `"8bbdP"Y8  `"Ybbd8"' `"8bbdP"Y8   "Y888 88       88
Game Over
 ''')
        
        
        
        
        
        
else:
    print('''
               ...
             ;::::;
           ;::::; :;
         ;:::::'   :;
        ;:::::;     ;.
       ,:::::'       ;           OOO\
       ::::::;       ;          OOOOO\
       ;:::::;       ;         OOOOOOOO
      ,;::::::;     ;'         / OOOOOOO
    ;:::::::::`. ,,,;.        /  / DOOOOOO
  .';:::::::::::::::::;,     /  /     DOOOO
 ,::::::;::::::;;;;::::;,   /  /        DOOO
;`::::::`'::::::;;;::::: ,#/  /          DOOO
:`:::::::`;::::::;;::: ;::#  /            DOOO
::`:::::::`;:::::::: ;::::# /              DOO
`:`:::::::`;:::::: ;::::::#/               DOO
 :::`:::::::`;; ;:::::::::##                OO
 ::::`:::::::`;::::::::;:::#                OO
 `:::::`::::::::::::;'`:;::#                O
  `:::::`::::::::;' /  / `:#
   ::::::`:::::;'  /  /   `#
   Wrong Turn!
   Game Over!
   ''')