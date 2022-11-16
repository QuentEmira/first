# Creating a 3x3 TicTacToe game

def display():
    for i in a:
        for j in i:
            print("_",end=" ") if (j == 0) else (print("X",end=" ") if (j == 1) else print("O",end=" "))
        print()

def check(j):
    if (sum(a[j[0]]) == 3) or (sum(a[x][j[1]] for x in range(0,3)) == 3):
        print("The Winner is Player 1")
        return 1
    elif sum(a[j[0]]) == -3 or (sum(a[x][j[1]] for x in range(0,3)) == -3):
        print("The Winner is Player 2")
        return 2
    elif max(j) - min(j) in [0,2] and ( (sum(a[x][x] for x in range(0,3)) == 3) or (sum(a[x][2-x] for x in range(0,3)) == 3)):
        print("The Winner is Player 1")
        return 1
    elif max(j) - min(j) in [0,2] and ( (sum(a[x][x] for x in range(0,3)) == -3) or (sum(a[x][2-x] for x in range(0,3)) == -3)):
        print("The Winner is Player 2")
        return 2
    return 0
    
        

a = [[0,0,0],[0,0,0],[0,0,0]]
d = 0

l = 1

game = 0
while True:
    print("Options : 1) New Game 2) Exit")
    game = int(input())
    
    if game == 1:
        while True:
            print("\n")
            if l == 1:
                print("Player 1: ",end = "")
            else:
                print("Player 2: ",end = "")
            j = list(map(int,input().split()))
            if a[j[0]][j[1]] != 0 or not(-1<j[0]<3) or not(-1<j[1]<3):
                print("\n !!Move Invalid, Please Enter valid move!! \n")
                continue
            a[j[0]][j[1]] = l
            l *= -1
            d += 1
            r = check(j)

            display()

            if r in [1,2]:
                break
            if d == 9:
                print("\nIt is a Tie")
                break

    elif game == 2:
        print("\n Thank you for playing \n")
        break

    else:
        print("Choice is invalid.")
