def rock_paper_scissor(player,player1):
    if(player=="rock" and player1=="paper") or (player=="paper" and player1=="scissor")or(player=="scissor"and player1=="rock"):
        return player1
    elif(player=="paper" and player1=="rock") or (player=="scissor" and player1=="paper") or(player=="rock" and player1=="scissor"):
        return player
    else:
        return "nothing wins,match was tie"
player=input("player enter you'r choice 1.rock 2.paper 3.scissor:")
player1=input("player1 enter you'r choice 1.rock 2.paper 3.scissor:")
result=rock_paper_scissor(player,player1)
print(result,"wins")