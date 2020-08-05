v = ['-', '-', '-', '-', '-', '-', '-', '-', '-']


def display():
    print('1', '2', '3')
    print('4', '5', '6')
    print('7', '8', '9')
    print("enter from 1 to 9")
    print(v[0], v[1], v[2])
    print(v[3], v[4], v[5])
    print(v[6], v[7], v[8])


display()
win_combination = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
player1 = []
player2 = []


def p1():# for player 1
    cnt = 0
    while len(player1) >= 3 and cnt == 0:
        for i in win_combination:
            count = 0
            for j in i:
                for k in player1:
                    if k == j:
                        count = count+1
                    else:
                        cnt = cnt+1
                if count >= 3:
                    print("player 1 win")
                    return 7


def p2():# for player 2
    y = 0
    while len(player2) >= 3 and y == 0:
        for p in win_combination:
            cout = 0
            for n in p:
                for z in player2:
                    if z == n:
                        cout = cout+1
                    else:
                        y = y+1
                if cout >= 3:
                    print("player 2 win")
                    return 8


played_position = []


def p1_p2(): # main function
    for q in range(1, 10):
        if (q%2!=0):
            c = int(input("player 1 turn(x)"))
            while c in played_position:
                print('this position is already taken, Please enter ')
                c = int(input("player 1 turn(x)"))
            played_position.append(c)
            v[c-1] = 'X'
            display()
            player1.append(c-1)
            u = p1()
            if u == 7:
                break
        else:
            d = int(input("player 2 turn(0)"))
            while d in played_position:
                print('this position is already taken, Please enter new position')
                d = int(input("player 2 turn(0)"))
            played_position.append(d)
            v[d-1] = 0
            display()
            player2.append(d-1)
            s=p2()
            if s == 8:
                break
    if u != 7 and s != 8:
        print('Match is tied')


p1_p2()
