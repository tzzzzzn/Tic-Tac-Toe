from random import *
play='s'
while(play!='n'):
    us=input("Welcome to play Tic Tac Toe with computer\n Select 1.    X\n             2.   O\n")
    if us=='1':
        us="    X    "
        cs="    O    "
    else:
        us="    O    "
        cs="    X    "
    board={}
    for i in range(1,10):
        board[i]="    _    "
    def pb():
        for i in range(1,10):
            print(board[i],end="   ")
            if(i==3 or i==6):
                print()
        return
    pb()
    filled=[]
    counter=0
    def checkwin(boardx):
        if(boardx[1]==boardx[2]==boardx[3]==us or boardx[1]==boardx[2]==boardx[3]==cs):
            if boardx[1]==us:
                return 1
            else:
                return 2
        elif(boardx[4]==boardx[5]==boardx[6]==us or boardx[4]==boardx[5]==boardx[6]==cs):
            if boardx[4]==us:
                return 1
            else:
                return 2
        elif(boardx[7]==boardx[8]==boardx[9]==us or boardx[7]==boardx[8]==boardx[9]==cs):
            if boardx[7]==us:
                return 1
            else:
                return 2
        elif(boardx[1]==boardx[4]==boardx[7]==us or boardx[1]==boardx[4]==boardx[7]==cs):
            if boardx[1]==us:
                return 1
            else:
                return 2
        elif(boardx[2]==boardx[5]==boardx[8]==us or boardx[2]==boardx[5]==boardx[8]==cs):
            if boardx[2]==us:
                return 1
            else:
                return 2
        elif(boardx[3]==boardx[6]==boardx[9]==us or boardx[3]==boardx[6]==boardx[9]==cs):
            if boardx[3]==us:
                return 1
            else:
                return 2
        elif(boardx[1]==boardx[5]==boardx[9]==us or boardx[1]==boardx[5]==boardx[9]==cs):
            if boardx[1]==us:
                return 1
            else:
                return 2
        elif(boardx[7]==boardx[5]==boardx[3]==us or boardx[7]==boardx[5]==boardx[3]==cs):
            if boardx[7]==us:
                return 1
            else:
                return 2
        else:
            return 0
            
        
    while(counter<=9):
        counter+=1
        uv=int(input("\nEnter where you want to place").strip())
        if board[uv]=="    _    ":
            board[uv]=us
            filled.append(uv)
            pb()
            if(counter>4):
                if(1==checkwin(board)):
                    print("YOU WON ")
                    break;
        else:
            print("you selected the wrong value it gonna terminate\n")
            break;
        counter+=1
        def cg():
            k=0
            global board
            for i in range(1,10):
                if i not in filled:
                    dummyboard=board.copy()
                    dummyboard[i]=cs
                    if 2==checkwin(dummyboard):
                        board[i]=cs
                        k=1
                        filled.append(i)
                        break
            if(k==1):
                return 1
            for i in range(1,10):
                if i not in filled:
                    dboard=board.copy()
                    dboard[i]=us
                    if 1==checkwin(dboard):
                        board[i]=cs
                        filled.append(i)
                        k=2
                        break
            if(k==2):
                return 2
            for i in range(1,10):
                if i not in filled:
                    board[i]=cs
                    filled.append(i)
                    return 0
        if(counter>3):
            print("\ncomputer1 thinking")
            c=cg()
            pb()
            if(c==1):
                print("\ncomputer WON")
                break
        else:
            print("\ncomputer thinking")
            cv=randint(1,9)
            while(cv in filled):
                cv=randint(1,9)
            board[cv]=cs
            filled.append(cv)
            pb()
        if(counter>=9):
            print("match draw")
            play=input("\nDo yoouuuuuuu... want to play again")

















            
        
            
    
        
    
