print("""
     _______               ___.                    ________                            .__                   ________                       
     \      \  __ __  _____\_ |__   ___________   /  _____/ __ __   ____   ______ _____|__| ____    ____    /  _____/_____    _____   ____  
     /   |   \|  |  \/     \| __ \_/ __ \_  __ \ /   \  ___|  |  \_/ __ \ /  ___//  ___/  |/    \  / ___\  /   \  ___\__  \  /     \_/ __ \ 
     /    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/ \    \_\  \  |  /\  ___/ \___ \ \___ \|  |   |  \/ /_/  > \    \_\  \/ __ \|  Y Y  \  ___/ 
     \____|__  /____/|__|_|  /___  /\___  >__|     \______  /____/  \___  >____  >____  >__|___|  /\___  /   \______  (____  /__|_|  /\___  >
     \/            \/    \/     \/                \/            \/     \/     \/        \//_____/           \/     \/      \/     \/ 
     """)


play_again = "yes"
while(play_again == "yes"):
    import random
    print("welcome to the number guessing game !")
    print("What number range would you be willing to guess")
    num1=int(input("Enter the lowest number : "))
    num2 = int(input("Enter the highest number : "))
    difficulty = input("Enter you difficulty, TYPE \n 1.easy  2.hard \n")
    #
    guess_number = random.randint(num1,num2)
    def easy():
        n=10

        while (n >= 1):
            number = int ( input ( f"You have {n} attempts remaining  to guess the number \n make a guess :" ) )
            if number < guess_number:
                print("Too Low \n guess again")
                n -= 1
            elif number > guess_number:
                print("Too High \n guess again")
                n -= 1
            else:
                print(f" You got it, the right number is {guess_number}  ")
                break


    def hard():
        n = 5
        while (n >= 1) :
            number = int ( input ( f"You have {n} attempts remaining  to guess the number \n make a guess" ) )
            if number < guess_number :
                print ( "Too Low \n guess again" )
                n -= 1
            elif number > guess_number :
                print ( "Too High \n guess again" )
                n -= 1
            else :
                print ( f" You got it, the right number is {guess_number}  " )
                break


    if (difficulty == "easy"):
        easy()
    else:
        hard()
    play_again = input ( "You gave it a good try \n Do you wanna play again \n 1.yes   2.no :" )
    if(play_again == "no"):
        print()
        print("Thank You for playing this game")