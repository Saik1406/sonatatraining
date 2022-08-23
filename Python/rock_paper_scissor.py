n=0

while(n<100):

    choice = input("do you want to continue press yes or no:")

    if(choice=="yes"):
        player = input("player enter your choice:")
        player1 = input("player1 enter your choice:")
        if (player == "rock" and player1 == "paper") or (player == "paper" and player1 == "scissor") or (
                player == "scissor" and player1 == "rock"):
            print (player1)
        elif (player == "paper" and player1 == "rock") or (player == "scissor" and player1 == "paper") or (
                player == "rock" and player1 == "scissor"):
            print (player)
        else:
            print("nothing wins,match was tie")

    print("thankyou for visiting!")
